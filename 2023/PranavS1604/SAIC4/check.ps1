# Send 10 requests to the Nginx load balancer
for ($i = 1; $i -le 20; $i++) {
    Invoke-WebRequest -Uri "http://localhost:8080"
}
