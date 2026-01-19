# CHALLENGE 1

**January 18, 2026**

---

## Challenge:

Before I write my experience with this que (IT WAS VERY EXHAUSTING FOR A NEWBIE LIKE
ME), I must say this was a very good que. I spent a lot of time on this and finally found the ans in
my second attempt. I think I spent around 6+ hours, maybe even 8 hours, idk now... but here’s what
actually happened.

To get a basic idea of how I should approach these kinds of CTF, I used ChatGPT to understand
how to start and to generate some fuzzing scripts, because as a beginner it is not obvious what the
first step should be or how to write complex python fuzzers from scratch.

---

## 1 Initial Enumeration - Understanding the System

The first thing I did was basic enumeration, which means understanding what kind of linux system I
was working on.

I checked the linux version and kernel info using:

```bash
uname -a
cat /etc/os-release
```

From this, I learned that it was an older linux version. Older systems usually have misconfigurations,
which is common in CTF.

---

## 2 Process Enumeration - Finding Something Sus

After that, I moved to one of the most basic steps in CTF:

```bash
ps aux
```

This command lists all running processes, and this is very important because it helps identify
custom services that don’t belong to the system. Here I found two python (py) files running:

1. server.py (Port 5000)

2. control.py (Port 9000)

These were very sus, because:

• They were not default linux processes.

• They were custom py scripts located in /opt/helios.

• They were clearly related to the challenge.

At this point, I knew these files would somehow be related to the flag.

1

---

## 3 File Permissions - What I Can and Cannot Access

Next, I checked the permissions of these files:

```bash
ls -l /opt/helios/
ls -l /opt/helios/worker
ls -l /opt/helios/web
```

Here I found:

• control.py could not be read (Permission Denied).

• server.py was readable.

This made control.py even more sus, because unreadable files in CTF usually hide important logic
or the main vulnerability. Since I could not read control.py, I decided to fully analyze server.py
first to find a “blueprint” for how the dev writes code.

---

## 4 Reading server.py - Understanding How the System Works

I read the code using cat /opt/helios/web/server.py. By analyzing the Python code, I identified
two critical endpoints and the logic behind them:

### 1. The Root Endpoint (/)

The code contained the following logic:

```python
if self.path == "/":
self.wfile.write("Helios Internal Dashboard")
```

When I opened the website on localhost (http://127.0.0.1:5000/), I saw the text “Helios Internal
Dashboard”. This confirmed that the server was active and using the / endpoint exactly as written in
the code.

### 2. The Hidden Endpoint (/internal/export)

I also found a restricted endpoint in the code:

```python
if self.path == "/internal/export":
token = self.headers.get("X-Internal -Token")
if token != INTERNAL_TOKEN:

return 403
self.wfile.write("SERVICE_TOKEN ={}".format(SERVICE_TOKEN))
```

This code block revealed the entire attack path:

1. To get the Service Token (needed for the worker), I must access /internal/export.

2. To access /internal/export, I must provide a valid X-Internal-Token.

3. The code loads this INTERNAL_TOKEN from a file: /etc/helios/web.env.

### Executing the Logic

Following the logic I found in the code, I first read the environment file to get the Internal Token:

```bash
cat /etc/helios/web.env
```

Inside, I found the INTERNAL_TOKEN. I then used this token to authenticate against the /internal/export
endpoint:

2

```bash
curl -H "X-Internal -Token: [TOKEN_FROM_FILE]" http ://127.0.0.1:5000/ internal
/export
```

The response gave me the Service Token:

```text
313 b96f83a85fb32b31ec70d86d5e40c
```

The output explicitly said “Used by helios-worker” , which confirmed that this token was the
key to accessing the suspicious process on Port 9000.

---

## 5 Discovering the Worker Process (Very Important)

From further enumeration, I checked init scripts, which are used to start services at boot:

```bash
cat /etc/init/helios -worker.conf
cat /etc/init/helios -runner.conf
```

Here I found:

• helios-worker runs control.py.

• helios-runner.sh runs as root.

This was very important and very sus, because a root-level script was connecting to the worker
every 2 seconds. This confirmed that if I can talk to the worker correctly, I can execute commands as
root.

---

## 6 The Hardest Part - Endless 400 Errors

This was the hardest and most frustrating part of the que. I authenticated using the X-Service-Token
header, but then I hit a wall.

I tried everything to get the server to accept a command:

• Keys: Fuzzed 200+ JSON keys (cmd, job, action, exec).

• Formats: Tried JSON, XML, YAML, and even compressed GZIP payloads.

• Traffic Analysis: I noticed the “Runner” was sending huge packets (1460 bytes), so I thought
I needed a complex schema. I wasted hours trying to build big JSON objects.

Almost everything resulted in: HTTP/1.0 400 Bad Request.

---

## 7 Final Breakthrough - Getting 200 OK

Each 400 error told me something: The server was receiving my request, but the logic was rejecting it
before processing the body.

After a lot of hit and trials and guidance from ChatGPT, I finally tried sending the command as
a header instead of body, which worked and gave me 200 OK.

The first command that gave me 200 OK was:

```bash
printf "POST / HTTP /1.1\r\nHost: 127.0.0.1\r\nX-Service -Token: 313
b96f83a85fb32b31ec70d86d5e40c\r\nX-Cmd: id\r\n\r\n" | nc 127.0.0.1 9000
```

3

### Why This Worked

• The request format was exact.

• The service token was valid.

• The command was passed in a custom header: X-Cmd.

• The server only checked headers! That’s why all my complex JSON body fuzzing gave 400s - it
was ignoring the body entirely.

---

## 8 Confirming Privileges and Finding the Flag

The exploit was “Blind” (it returned 200 OK but didn’t show the output). I verified RCE by redirecting
output to tmp:

```bash
# Payload sent in X-Cmd header
id > /tmp/pwned
```

Checking the file showed uid=0(root), which means I had root privileges from the very start
through the worker.

Flags are usually stored in /root, so I ran:

```bash
cat /root/flag.txt > /tmp/flag
cat /tmp/flag
```

And finally got the flag:

```text
SAIC{C0ngr4ts_d0_y0u_l0v3_ST4C?}
```

---

## 9 Final Thoughts

Even though I didn’t know all the commands or the correct approach initially (and relied on ChatGPT
for the scripting parts), this que helped me learn a lot.

This was my favorite que from the test because:

• It taught me enumeration.

• It showed how errors (like 400 Bad Request) are actually hints.

• It improved my understanding of HTTP headers vs body.

• It felt like solving a mystery.

In the end, this mental workout became very fun, especially when I finally found the flag. VERY
GOOD QUE.

4

---

### Contents

- Initial Enumeration - Understanding the System
- Process Enumeration - Finding Something Sus
- File Permissions - What I Can and Cannot Access
- Reading server.py - Understanding How the System Works
- Discovering the Worker Process (Very Important)
- The Hardest Part - Endless 400 Errors
- Final Breakthrough - Getting 200 OK
- Confirming Privileges and Finding the Flag
- Final Thoughts

