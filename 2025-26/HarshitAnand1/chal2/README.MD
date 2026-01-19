Q2.
Running containers after recovery

Port clash simulation

Running The script: 

The report:




Instructions:
How to run: (Have very less time to format the code 😢)
Start sample environment

docker run -d --name site1 -p 8080:80 nginx
docker run -d --name site2 -p 8081:80 nginx



Execute analyzer
./docker_log_analyzer.py

View Report
cat docker_log_report.txt

Simulating Port Clash
docker run -d --name badsite -p 8080:80 nginx

Result:
Bind for 0.0.0.0:8080 failed: port is already allocated


After this run the analyser again => service will be restored on port 8082

For verification just do
docker ps

It will show badsite running on new port 
And now websites are accessible on 
docker ps

http://localhost:8080/
http://localhost:8081/
http://localhost:8082/

also just for fun i added a feature to send telegram msgs whenever there is a crash 
learnt telegram bots along the way

**Note:** To use Telegram notifications, set these environment variables before running:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"
```
