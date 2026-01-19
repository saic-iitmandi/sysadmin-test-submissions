# Challenge 2 - Docker Scripting & Log Analysis

## Project Overview
This project implements a Linux shell script that monitors Docker containers hosting websites, analyzes their logs to detect critical issues, and automatically handles port clash scenarios. The solution ensures service availability by detecting failures and restoring services on available ports without manual intervention.

The script is executed inside WSL (Windows Subsystem for Linux), which is used as the backend for Docker Desktop on Windows.

## Objectives

Analyze logs of running Docker containers

Identify critical and error-level log entries

Detect port clash issues

Automatically recover affected services

Generate a summary report of findings

## Tools & Technologies Used

Docker Desktop

WSL (Ubuntu)

Bash Shell Scripting

Linux utilities: grep, awk, curl

