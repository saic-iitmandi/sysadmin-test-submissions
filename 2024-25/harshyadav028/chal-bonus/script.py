import os
import datetime
import requests

# function to enumerate in the test directory files
def enumerate_files_and_folders(test_directory, log_file):
    try: 
        timestamp = datetime.datetime.now()
        with open(log_file, "a") as log:
            log.write(f"log time: {timestamp} \n")

            for root, dirs, files in os.walk(test_directory):

                # folders extraction
                log.write(f"{root}:")
                for folder in dirs:
                    folder_path = os.path.join(root, folder) # ein dono ki path ko milake join karo
                    log.write(f"Folder: {folder_path}, ")

                # files extraction
                for file in files:
                    file_path = os.path.join(root, file) # ein dono ki path ko milake join karo
                    file_size = os.path.getsize(file_path)
                    log.write(f"file: {file_path}, ")

            log.write("enumeration completed\n")

    except Exception as e:
        print(f"an error occured: {e}")

def upload_to_gofile(file_path, server):
    # URL of the server chosen from the list (for example, store-eu-par-6)
    url = f'https://{server}.gofile.io/contents/uploadfile'  

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        files = {'file': file}

        # Send the POST request to upload the file
        response = requests.post(url, files=files)

    # Check if the upload was successful
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('status') == 'ok':
            return response_data['data']['downloadPage']  # Return the download page link
        else:
            return "Error: Upload failed. No valid response."
    else:
        return f"Error: Status code {response.status_code} received from the API."

target_directory = "./test_directory"
log_file = "basic_v_log_file.txt"
server = 'store-eu-par-6'

enumerate_files_and_folders(target_directory,log_file)

public_url = upload_to_gofile(log_file, server)
print(f"Public link to your uploaded log file: {public_url}")