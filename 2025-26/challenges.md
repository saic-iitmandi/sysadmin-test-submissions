# SysAdmin Test 2025-26 Challenges

## **Challenge 1 - Gain Access to a Remote**

Since you will be in charge of a public-facing server you need to know how to protect a server and to protect a server you must first learn how attacks generally work. A drive link containing a saic.ova file is provided to you. This file can be imported into a Virtual Box. When run as a guest, it will act as a remote server hosting a site on it's own local host which can be seen on your host's localhost. You have to get inside this server by exploiting any vulnerability that you find.

Report your findings and method. You will find the flag once you have gained root privileges. The flag is present in `root/flag.txt` once you obtain root privileges.

Use of tools like Metasploit is discouraged.

Drive link for the Virtual Machine: [Here](https://drive.google.com/file/d/1pN_jN7UCKShA6XbkrXWlnc1smIOONNB6/view?usp=sharing)

### **Deliverables**

In your git repository whose link you will be submitting, state your approach for finding the flag along with screenshots of the process.

### Login Details
- Username: `student`
- Password: `saic`

### **Restrictions**
- Accessing the mounted disk from outside the VM environment is strictly prohibited.
- You are not allowed to use Recovery Mode or Grub Terminal to gain root access. Everything must be performed from inside of the VM.

## **Challenge 2 - Docker Scripting & Log Analysis**

Create a script to analyze Docker container logs, detect critical issues, and automatically handle port clash scenarios for containerized websites.


### **Requirements**

The script should perform the following tasks.

### Log Analysis

- Parse logs from all running Docker containers hosting websites.
- Identify and extract critical and error-level log entries related to crashes or service failures.
- Generate a summary report.


### Port Clash Handling

- Detect and log when a port clash is seen in a Docker container.
- Ensure automatic recovery and proper service restoration.


### **Deliverables**

- The script file.
- Sample log output demonstrating:
  - Filtered and prioritized log entries
  - The summary report
  - Port clash detection warnings
- Clear instructions for:
  - Running the script
  - Simulating a port clash scenario
  - Verifying that automatic recovery and service restoration work properly

## **Challenge 3 - Docker Deployments**

You are provided with GitHub repositories for two different projects. Your task is to deploy both projects using Docker containers on your localhost in production grade. Each project uses a different technology stack, so you must configure and deploy them accordingly. Both the projects should run simultaneously on different containers.

### **Repositories**

1. **[RoyalChess](https://github.com/Sachitbansal/royalchess)** - A MERN project.
2. **[STAC Website](https://github.com/Sachitbansal/stac-clone)** - A Next.js + Django project.

### **Tasks**

1. **Deploy Both Projects Using Docker Compose**
   - Create Docker containers for both projects and configure them using a `docker-compose.yml` file.
   - Map each container to ports of your choice on your localhost.

2. **Network Configuration**
   - Suggest appropriate Docker network types (e.g., `bridge`, `host`, or `overlay`) for each container.
   - Justify your choice of network for each container.

### **Requirements**
1. Steps for containerizing the frontend and backend applications.
2. Configuration of a secure network for communication between containers.
3. Hosting details, including any necessary changes to the Docker Compose setup or infrastructure to achieve the stated security goals.
4. Any best practices for securing the database and preventing unauthorized access.
5. Document the process thoroughly, ensuring that the solution is both functional and adheres to modern security standards for web applications.
> As part of the hosting process, you are required to implement stringent security measures to protect the application and its database. Specifically, the database must not be accessible from outside the host environment under any circumstances. Additionally, even the host server itself should not have direct access to the database, ensuring it can only be accessed by the backend service.


### **Deliverables**

- A brief document explaining the setup process for hosting both projects.
- Dockerfiles for both projects.
- The `docker-compose.yml` script.
- Provide screenshots of:
  - Running containers (`docker ps`)
  - Accessing both websites in the browser

## **Challenge 4 - The Bakery’s Secret Recipe**
As the administrator of SAIC’s public-facing server, you are responsible for auditing exposed files and services. During a routine inspection, you discover a directory belonging to a small internal bakery project.

The folder appears harmless at first glance, but may reveal sensitive information if investigated properly.

Your task is to analyze and recover the hidden flag.


### **Objective**

- Investigate the provided folder.
- Use forensics techniques to analyze the directory and extract the hidden flag.


### **Flag Format**
```
SAIC{REDACTED_FLAG}
```

### **Files Provided**

- [`Folder`](https://drive.google.com/file/d/1DYS8GpT7W6qJwwsGOq88pi3Bn8GfwM7S/view?usp=sharing) – Contains the Git repository to be analyzed.


### **Deliverables**

- The recovered flag.
- A detailed writeup explaining:
  - The commands and techniques used.
  - How the process of how flag was discovered.
  
## **Challenge 5 - Proof of Parity**

As a member of SAIC, you are expected to represent the club by participating in Capture The Flag competitions throughout the year. These challenges test your ability to analyze data, recognize patterns, and extract hidden information. You are provided with a file containing some data. At first glance, the file may appear harmless or meaningless. Your task is to carefully analyze the contents and uncover the hidden flag encoded within it. The challenge requires identifying patterns and interpreting the data correctly to recover the flag in the required format.

### **Objective**

- Analyze the provided file.
- Identify hidden patterns or encodings within the data.
- Extract the flag from the file.

### **Flag Format**
```
SAIC{REDACTED_FLAG}
```

### **Files**
- [`File`](https://drive.google.com/drive/folders/1VPDCL_txR2q6U7ejr7W0GuFcmLxxuMXJ)

### **Deliverables**

- The recovered flag.
- A detailed writeup explaining:
  - The analysis process.
  - The techniques and tools used.
  - How the hidden data was decoded.

## **Bonus Challenge - Windows Remote Access (Proof of Concept)**

Design a remote access tunnel between two machines using direct network communication only.

This challenge evaluates your understanding of Windows internals, networking, and secure systems behavior under strict constraints.

### **Setup**

#### Client Machine (Target)
- Must run **Windows 11**, fully updated.
- Windows Defender and all default security features must remain enabled.
- No registry edits, group policy changes, exclusions, or security modifications are allowed.

#### Host Machine (Controller)
- May be a cloud VM (Azure, AWS) or a local Windows/Linux system.
- Must be reachable over the network.
- Acts as the command controller.

### **Requirements**

- The Windows 11 machine must initiate the connection to the host.
- Implement a **PowerShell script (Administrator)** that creates a reverse tunnel using raw TCP or UDP sockets only.
- Ensure that the script bypasses all the Defender's safety techniques. You are allowed to choose what methods you use to do so.
- Prohibited technologies:
  - SSH, WinRM, PowerShell Remoting, RDP, SMB, WMI, or similar tools.
- After connection, the host must be able to:
  - Send arbitrary shell commands.
  - Receive exact `stdout` and `stderr` output.
- Behavior should resemble a basic interactive shell implemented manually over sockets.
- The tunnel must remain stable across multiple command executions.

### **Stealth Constraints**

- The script must run without visible windows or prompts.
- No user-noticeable foreground activity is allowed.
- Background presence (e.g., Task Manager) is acceptable, but suspicion should be minimized.
- Script size should be as small as possible.

### **Bonus**

- Implement persistence so the tunnel survives a system reboot.

### **Security Constraints**

You must not:
- Disable or bypass Windows Defender.
- Modify Defender settings or exclusions.
- Patch system DLLs or inject into protected processes.

The solution must rely only on documented Windows APIs and work on a default Windows 11 installation without triggering Defender alerts.

### **Deliverables**

- The PowerShell script (`.ps1`).
- A detailed explanation covering:
  - Design choices.
  - Challenges encountered.
  - Assumptions and limitations.
- A video or images showing proof of the script being ran successfully and commands being issued from the host to the victim.

### **Evaluation Criteria**

- **Feasibility**: Soundness of approach, even if not fully implemented.
- **Problem-Solving**: Ability to reason within constraints.
- **Depth & Clarity**: Technical understanding and explanation quality.

> **Important:**
This is a simulated exercise for assessing problem-solving and scriptwriting skills. The solution will not be deployed for malicious purposes. Please provide explanations alongside your code to demonstrate your understanding of the task and constraints.