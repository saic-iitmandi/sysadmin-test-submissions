# Bonus Challenge – Initial Attempt Documentation

## Objective

The bonus challenge involved setting up a basic reverse-shell–style client/server interaction between a Linux environment (WSL) and Windows PowerShell. Only the **initial setup and partial execution** were attempted.


---

## Environment

- **Host OS:** Windows  
- **Linux Environment:** WSL (Ubuntu)  
- **Python Version:** 3.12.3  
- **Shells Used:** Bash (WSL), Windows PowerShell  
---
## Step-by-Step Progress

### Step 1: Environment Verification (WSL)

```bash

python3 --version

```

Result: Python 3.12.3

---
### Step 2: Project Directory Setup

```bash

mkdir bonus_challenge

cd bonus_challenge

```

---
### Step 3: Listener Script Creation

A Python TCP listener was written in `listener.py` to listen on port `4444`.

Key points:

- Uses Python `socket` library
- Binds to `0.0.0.0`
- Waits for incoming connection

---
### Step 4: Running the Listener

```bash

python3 listener.py

```

Output:

```

[+] Listening on port 4444...

```

---
### Step 5: Network Configuration

```bash

ip a

```

Used to identify local IPv4 address for client connection.

---
### Step 6: PowerShell Client Script

A PowerShell script `client.ps1` was created to connect to the listener using `System.Net.Sockets.TCPClient`.

---
### Step 7: Execution Policy Change

```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

```

---
### Step 8: Client Execution Attempt

```powershell

powershell -ExecutionPolicy Bypass -File client.ps1

```

---

## Errors Encountered

Repeated PowerShell runtime errors:

```

You cannot call a method on a null-valued expression.

```

  
Affected lines:

- `$reader.ReadLine()`
- `$writer.WriteLine($output)`


The client failed to establish a stable interactive session.

---

## Status Summary

- Listener: ✅ Working  
- Client script: ✅ Created  
- Client-server interaction: ❌ Not functional  
---
## Conclusion

Only the **initial steps** of the bonus challenge were attempted. Due to persistent PowerShell errors and limited time, deeper debugging and exploitation were not performed. This documentation reflects an **early-stage attempt**, not a complete solution.