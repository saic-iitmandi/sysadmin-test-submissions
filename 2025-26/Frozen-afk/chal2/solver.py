import subprocess
import re
import socket
import time

def get_container_logs(id):
    
    result=subprocess.run(['docker','logs',id],capture_output=True,text=True)
    return result.stdout+result.stderr

def analyze_logs():
    print("---Starting Log Analysis ---")
    
    # Check running containers
    result=subprocess.run(['docker','ps','-q'],capture_output=True,text=True)
    ids=result.stdout.splitlines()
    
    print(f"---Found {len(ids)} running containers.")
    
    for id in ids:
        logs=get_container_logs(id)
        
        
        if re.search(r'(error|critical|exception|fatal|panic|traceback)',logs,re.IGNORECASE):
            print(f'Alert: Container {id} has errors')
        else:
            print(f"---No errors found in {id}")

def check_port_clash():
    print("\n---Starting Port Clash Check ---")
    
    
    result=subprocess.run(['docker','ps','-a','--filter','status=exited','-q'],capture_output=True,text=True)
    ids=result.stdout.splitlines()
    
    print(f"---Found {len(ids)} exited/stopped containers.")
    
    for id in ids:
        logs=get_container_logs(id)
        
       
        if re.search(r'(bind: address already in use|address already in use)',logs,re.IGNORECASE):
            print(f'Port clash detected for container {id}')
            
           
            insp=subprocess.run(['docker','inspect','--format={{.Config.Image}}',id],capture_output=True,text=True)
            image=insp.stdout.strip()
            
            print(f"---Clash confirmed. Image is: {image}")
            handle_recovery(image, 8080)
        else:
            print(f"---Container {id} stopped for a different reason.")

def handle_recovery(image, old_port):
    new_port=old_port+1
    
    print(f"---Finding free port starting from {new_port}...")
    
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex(('127.0.0.1',new_port))
        s.close()
        
        if result==0:
            print(f"---Port {new_port} is busy")
            new_port+=1
        else:
            print(f"---Port {new_port} is free")
            break
            
    print(f'we handled the port_clash, new_port={new_port}')
    
    
    subprocess.run(['docker','run','-d','-p',f'{new_port}:80',image])

if __name__=="__main__":
    analyze_logs()
    check_port_clash()