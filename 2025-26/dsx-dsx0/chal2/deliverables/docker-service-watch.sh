#!/usr/bin/env bash

# ==========================================================
# Docker Service Watch
# Analyze logs of web-facing Docker containers, detect
# error/critical issues, identify port clashes, and
# optionally attempt automatic recovery.
# ==========================================================

# -------------------------
# Defaults
# -------------------------

LOG_TAIL_LINES=200
HISTORICAL_MODE=false
DRY_RUN=false

# -------------------------
# Help
# -------------------------

show_help() {
  cat <<EOF
Usage: ./docker-service-watch.sh [OPTIONS]

Options:
  --tail N         Number of recent log lines to scan (default: 200)
  --historical     Scan deeper logs for investigation (disables recovery)
  --dry-run        Show what actions would be taken without executing them
  --help           Show this help message

Examples:
  ./docker-service-watch.sh
  ./docker-service-watch.sh --tail 1000
  ./docker-service-watch.sh --historical
  ./docker-service-watch.sh --dry-run
EOF
}

# -------------------------
# Argument parsing
# -------------------------

while [ $# -gt 0 ]; do
  case "$1" in
    --tail)
      LOG_TAIL_LINES="$2"
      shift 2
      ;;
    --historical)
      HISTORICAL_MODE=true
      shift
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --help)
      show_help
      exit 0
      ;;
    *)
      echo "[ERROR] Unknown option: $1"
      show_help
      exit 1
      ;;
  esac
done

# Historical mode safety rule
if [ "$HISTORICAL_MODE" = true ]; then
  echo "[INFO] HISTORICAL SCAN MODE ENABLED"
  echo "[INFO] Automatic recovery is disabled in historical mode"
fi

if [ "$DRY_RUN" = true ]; then
  echo "[INFO] DRY-RUN MODE ENABLED (no actions will be performed)"
fi

echo "[INFO] Docker Service Watch starting..."

# -------------------------
# Pre-flight checks
# -------------------------

if ! command -v docker >/dev/null 2>&1; then
  echo "[ERROR] Docker CLI not found. Is Docker installed?"
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "[ERROR] Docker daemon not running or not accessible."
  exit 1
fi

# -------------------------
# Detect web-facing containers
# -------------------------

WEB_CONTAINERS=$(docker ps --format "{{.ID}} {{.Names}} {{.Ports}}" | grep -- "->" || true)

if [ -z "$WEB_CONTAINERS" ]; then
  echo "[INFO] No web-facing containers detected. Exiting."
  exit 0
fi

# -------------------------
# Summary data
# -------------------------

TOTAL_CONTAINERS=0
CRITICAL_COUNT=0
ERROR_COUNT=0
PORT_CLASH_COUNT=0
ANALYZED_CONTAINERS=()

# -------------------------
# Analyze containers
# -------------------------

while read -r CONTAINER_ID CONTAINER_NAME _; do
  TOTAL_CONTAINERS=$((TOTAL_CONTAINERS + 1))
  ANALYZED_CONTAINERS+=("$CONTAINER_NAME ($CONTAINER_ID)")

  echo "[INFO] Analyzing container: $CONTAINER_NAME ($CONTAINER_ID)"
  echo "[INFO] Scanning last $LOG_TAIL_LINES log lines"

  LOG_OUTPUT=$(docker logs --tail "$LOG_TAIL_LINES" "$CONTAINER_ID" 2>&1)

  if [ -z "$LOG_OUTPUT" ]; then
    echo "[INFO] No logs found for $CONTAINER_NAME ($CONTAINER_ID)"
    continue
  fi

  # Critical (infrastructure-impacting failures)
  CRITICAL_LOGS=$(echo "$LOG_OUTPUT" | grep -iE "panic|fatal|crash|segfault|bind failed|address already in use|EADDRINUSE")

  # Error-level (application-visible issues)
  ERROR_LOGS=$(echo "$LOG_OUTPUT" | grep -iE "error|exception|failed|unavailable")

  if [ -n "$CRITICAL_LOGS" ] || [ -n "$ERROR_LOGS" ]; then
    echo "[INFO] Displaying filtered and prioritized log entries"
  fi

  if [ -n "$CRITICAL_LOGS" ]; then
    CRITICAL_COUNT=$((CRITICAL_COUNT + 1))
    echo "[CRITICAL] Issues detected in $CONTAINER_NAME ($CONTAINER_ID)"
    echo "$CRITICAL_LOGS"
  fi

  if [ -n "$ERROR_LOGS" ]; then
    ERROR_COUNT=$((ERROR_COUNT + 1))
    echo "[ERROR] Error-level log entries detected in $CONTAINER_NAME ($CONTAINER_ID)"
    echo "$ERROR_LOGS"
  fi

  if [ -z "$CRITICAL_LOGS" ] && [ -z "$ERROR_LOGS" ]; then
    echo "[INFO] No issues detected in $CONTAINER_NAME ($CONTAINER_ID)"
  fi

  # ---------------------
  # Port clash handling
  # ---------------------

  if echo "$CRITICAL_LOGS" | grep -qiE "address already in use|bind failed"; then
    PORT_CLASH_COUNT=$((PORT_CLASH_COUNT + 1))
    echo "[WARN] Port clash detected in $CONTAINER_NAME ($CONTAINER_ID)"

    if [ "$HISTORICAL_MODE" = true ]; then
      echo "[INFO] Skipping recovery (historical mode)"
    elif [ "$DRY_RUN" = true ]; then
      echo "[DRY-RUN] Would restart container $CONTAINER_NAME ($CONTAINER_ID)"
    else
      echo "[ACTION] Restarting container $CONTAINER_NAME ($CONTAINER_ID)"
      docker restart "$CONTAINER_ID" >/dev/null
      echo "[INFO] Restart issued for $CONTAINER_NAME ($CONTAINER_ID)"
    fi
  fi

done <<< "$WEB_CONTAINERS"

# -------------------------
# Summary report
# -------------------------

echo "--------------------------------"
echo "[SUMMARY REPORT]"
echo "Containers analyzed        : $TOTAL_CONTAINERS"
echo "Error-level issues         : $ERROR_COUNT"
echo "Critical issues detected   : $CRITICAL_COUNT"
echo "Port clashes detected      : $PORT_CLASH_COUNT"

if [ "$TOTAL_CONTAINERS" -gt 0 ]; then
  echo "Analyzed container list:"
  for CONTAINER in "${ANALYZED_CONTAINERS[@]}"; do
    echo "  - $CONTAINER"
  done
fi

echo "[INFO] Docker Service Watch completed."
