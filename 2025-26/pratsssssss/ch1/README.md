**#Challenge-1 Writeup (My POV)**
So the first challenge looked scary and interesting at the same time and ngl it took most of my time but still it was really a great experience diving into this lol.

**What i did and what i got**

Booted the SAIC VM. Nothing showed up visually except a login and had no idea what ports were open so did some googling and also took help form GPT too.
Networking was annoying for like 10–15 mins.
but eventually after 40-50min setup was done.

- used `ip a` to find the ip address of the machine and then used `nmap` in kali but got no result 1000 ports but all closed, thought i did something wrong cause browser also didn't showed anything.
- after this again did some research took some help from internet and then came up with the command `ss -tulnp` and finally got the listening ports
  127.0.0.1:5000
  127.0.0.1:9000
- First Breakthrough (Internal Web Thing)
Did some curl action from saic vm and discovered:
localhost:5000
showed “Helios Internal Dashboard”.
At first thought i got something but then after some researching got that it was completely useless
Kali curl couldn’t see it (because loopback lol) so I used SAIC's vm browser which just said “internal dashboard”. 
- at this point kali wasn't helping so closed it and came back to this.
- used `curl` and got GET → 501 error complaining about unsupported method
Some POST attempts froze, some did nothing
One literally rebooted the entire VM.
This confused me because I thought VirtualBox crashed but after taking some help from internet found out it was intentional so got one thing that empty post rebooted the system but it didn't happened after that ever so maybe it was just a glitch.
- Again did some digging on processes:
/opt/helios/web/server.py  → user = websvc
/opt/helios/worker/control.py → user = ops
- Also discovered:
ops had sudo privileges (but no password)
/opt/helios/worker was locked (700 perms) gave some vibes that maybe i'll get something from here cause this was my only progress till now
- Then my brain was freezing cause i have no clue what to do next or where to move next so again some research some googling, asked gpt what to do next and after that got to know that it was an internal control plane running tasks on behalf of ops
- at this point my most time was going on researching about stuff which i think is the motive of this test
- well after some brainstorming with internet came up with it can be RCE + Sudo
and maybe PICKLE DESERIALIZATION RCE 
why ?? 
Python2
internal control API
BaseHTTP (501 GET error was a giveaway)
weird silent POST behavior
worker doing privileged actions
- So the path probably was:
student → POST → ops (pickle) → sudo → root → flag
that was my progress till now and after this i started some exploitation attempts.
- Actual Exploitation Attempts

**Generated malicious payload:**
ofcourse from help of gpt
import pickle, os
class R(object):
    def __reduce__(self):
        return (os.system, ('touch /tmp/pwned',))
and it worked for student user.
So my serialization was correct.
Then tried to send via:
curl -X POST --data-binary @p localhost:9000
and nothing happened no output, no error, just silence.i thought maybe did something wrong maybe the payload was wrog but checked it and it was fine cause it worked for student user perfectly too.
Which meant pickle itself is fine, but framing was wrong.
- again went google and get to know about different protocol framings.
got a list of tons of framings which made me go to gpt and ask which one is actually my case. 
- After that i tried different framings like 
EXEC prefix
RUN / CMD / TASK etc.
JSON base64
CRLF
- and came to know that worker never crashed again caus the PID never changed except on literal empty POST (which rebooted VM).
- after that my brain literally froze cause i wasn't getting anything even after doing googling or anything and it was taking too much of my time.
- I decided to stop here and move on to other challenges because, this was solvable (maybe) but was taking too much of time so decided to stop here. 

**conclusion**
it's 2nd day of the test and almost 7:00pm and am standing on an endpoint cause most of the sommands gave permission denied, didn't even have permission of sudo. no idea where to move next but am excited to see what's the solution of this challenge for sure.