import docker
import json
import os
import resend
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

resend.api_key = 're_hQv8eniG_MiSGRJ8NupbNQiyy7xHeQ1BX'
def sendEmail(c,o):
  html=f"<div><strong>service(s) down! at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong></div>"
  lhtml = "<div><strong>Services that are still down</strong></div>"
  for x in o:
    lhtml += "<div>"+x['name']+" was down </div>"
  for x in c:
    html += "<strong>"+x['name']+" is down LOGS:</strong>"+"<div>"+str(x['logs'])+"</div>"+"<div>===============</div>"
  final=html
  if len(o)>0:
    final = lhtml+"<p>=====================================================<p>"+final
  params = {
      "from": "SAIC-monitoring <monitoring@resend.dev>",
      "to": ["panpaliyapiyush0@gmail.com"],
      "subject": "SERVICE DOWN",
      "html": final,
  }

  email = resend.Emails.send(params)
  print(email)

client = docker.from_env()

def save():
  with open('containers.json','+w') as f:
    json.dump({'services':[{'id':x.id,'name':x.name} for x in client.containers.list()]}, f, indent=2)


def checkStatus():

  oldServices=[]
  if not os.path.exists('containerStatus.json'):
    with open('containerStatus.json','w') as f:
      f.writelines('{"services":[]}')

  with open('containerStatus.json','r+') as f:
    if ( f.read() == ''):
      f.writelines('{"services":[]}')
    
  with open('containerStatus.json','r') as f:
      oldServices=json.load(f)['services']
  oldIDs = [x['id'] for x in oldServices]
  with open('containers.json','r') as f:
    data = json.load(f)
    down = []
    for container in data['services']:
      c=client.containers.get(container['id'])
      if c.status != 'running':
        down.append({**container,'logs':c.logs()})
        print(container['name'],'is down')
      else:
        if container['id'] in oldIDs:
          print(container['name'],'is up')
          oldServices = [x for x in oldServices if x['id'] != container['id']]

    print(oldServices)
    newServices = [x for x in down if x['id'] not in [x['id'] for x in oldServices]]
    print(newServices)
    if len(newServices)>0: 
      sendEmail(newServices,oldServices)
    with open('containerStatus.json','w') as f:
      json.dump({'services':oldServices+[{'id':x['id'],'name':x['name']} for x in newServices]}, f, indent=2)

save()


scheduler = BackgroundScheduler()
scheduler.add_job(checkStatus, 'date', run_date=datetime.datetime.now())
scheduler.add_job(checkStatus, 'interval', hours=1, id='main')

scheduler.start()

while True:
  time.sleep(2)
