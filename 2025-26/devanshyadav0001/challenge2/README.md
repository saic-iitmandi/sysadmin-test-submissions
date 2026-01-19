# Challenge 2 – Docker Scripting & Log Analysis

## 📌 Overview

This challenge focused on designing an **automated Docker monitoring and recovery system**, similar to real-world sysadmin infrastructure tooling.  
The system detects container crashes, identifies port conflicts, automatically restores failed services, and performs log-based health analysis.

---

## 🎯 Objectives

- Detect stopped / crashed containers  
- Detect port clash scenarios  
- Automatically restore blocked containers on free ports  
- Analyze container logs for critical errors  
- Generate structured diagnostic reports  

(Page 1 of the report outlines the objective and initial Docker validation.)

---

## 🖥️ Initial Setup

Docker was installed and verified on the host system:

- Docker daemon verified using basic commands  
- A test Nginx container deployed to confirm stable baseline service  

This ensured the environment was ready before scripting automation.

---

## ⚠️ Problem Encountered – Docker Port Clash Reality

Initial design attempted to detect port clashes by scanning **running containers**.

However, Docker does not allow two containers to bind to the same host port.  
If a port is already allocated, the second container fails to start immediately.

Therefore:

- A “running port clash” never exists inside `docker ps`
- The conflicting container is created but remains **non-running**

(Page 2 of the report demonstrates this Docker behavior.)

This required redesigning the detection logic.

---

## 🧠 Final Modular Design

To solve logical conflicts, the solution was split into two independent modules:

### 1️⃣ Port Clash & Critical Issue Handler
**File:** `clash_report.py`

### 2️⃣ Log Analysis Module
**File:** `log_analysis_report.py`

This modular architecture reflects realistic sysadmin monitoring separation of concerns.  
(Page 3 shows the modular design layout.)

---

## ⚙️ Revised Port Clash Handling Logic

The improved script performs:

- Inspection of **running containers** for real port ownership  
- Inspection of **stopped containers** for configured port bindings  
- Differentiation between:
  - Running container → legitimate port owner  
  - Non-running container → blocked due to port conflict  

### Automatic Recovery Flow

If a blocked container is detected:

- Detects port conflict  
- Finds a free port automatically  
- Removes blocked container  
- Recreates container on new free port  
- Logs recovery success  

(Page 4 illustrates this improved logic and recovery results.)

---

## 📊 Log Analysis Module

The second module performs:

- Infrastructure audit from `clash_report.txt`
- Runtime log scanning (last 300 lines per container)
- Detection of error / exception keywords
- Consolidation into `log_analysis_report.txt`
- Final health classification: **Healthy** or **Attention Required**

(Page 5 shows the unified diagnostic reporting workflow.)

---

## 📁 Generated Reports

| Report File | Purpose |
|-------------|---------|
| `clash_report.txt` | Port clashes + container crash recovery logs |
| `log_analysis_report.txt` | Log-based health diagnostics |

---

## ✅ Final Capabilities Achieved

✔ Detection of crashed containers  
✔ Real port ownership analysis  
✔ Correct identification of port clash conditions  
✔ Automatic rerouting of blocked services  
✔ Comprehensive log-based health analysis  

The final system successfully replicates a **production-grade Docker monitoring and auto-recovery workflow**.

---

## 🏁 Conclusion

This challenge demonstrated:

- Deep understanding of Docker networking behavior  
- Realistic sysadmin automation design  
- Automated service recovery logic  
- Structured diagnostic reporting  

All challenge requirements were successfully satisfied.

---

## 👤 Author

Devansh Yadav  
SAIC SysAdmin Challenge 2
