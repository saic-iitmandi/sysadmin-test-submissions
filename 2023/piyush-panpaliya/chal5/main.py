import requests
from pyquery import PyQuery as pq
import json
import re
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
import resend

resend.api_key = 're_V93MJZDh_PCErxqTcGXUeAyqV71sGauMA'


def notify(a):
  html = html = f"<div><strong>Assignments are due! for 6 hours</strong></div>{
    '<div>' + a['course']['name'] + ' due at ' + a['due'].strftime('%Y-%m-%d %H:%M:%S') + '</div>'}"
  params = {
      "from": "Assignment Reminder <reminder@resend.dev>",
      "to": ["panpaliyapiyush0@gmail.com"],
      "subject": "ASSIGNMENT BHAIII",
      "html": html,
  }
  email = resend.Emails.send(params)
  print(email)


def fileExists(name, default):

  try:
    with open(name) as f:
      json.load(f)
  except:
    with open(name, 'w') as f:
      json.dump(default, f)


s = requests.Session()


def login():
  url = 'https://lms.iitmandi.ac.in/login/index.php'
  r = s.get(url)
  doc = pq(r.text)
  lt = doc('input[name="logintoken"]').attr('value')
  r2 = s.post(url, data={'username': 'b23279', 'password': 'PASSWORDBHAIIII',
                         'logintoken': lt})
  r2 = s.get(url)
  with open('login.json', 'w') as f:
    json.dump(s.cookies.get_dict(), f)


def getCourses():
  r = s.get('https://lms.iitmandi.ac.in/my/courses.php')
  t = r.text
  l = t.find('sesskey')
  r = s.post(
    f'https://lms.iitmandi.ac.in/lib/ajax/service.php?sesskey={t[l + 10:l + 20]}&info=core_course_get_enrolled_courses_by_timeline_classification', json=[{"index": 0, "methodname": "core_course_get_enrolled_courses_by_timeline_classification", "args": {"offset": 0, "limit": 0, "classification": "all", "sort": "fullname", "customfieldname": "", "customfieldvalue": ""}}])

  courses = [{'id': x.get('id'), 'name': x.get('fullname'), 'url': x.get('viewurl')}
             for x in r.json()[0].get('data').get('courses')]
  with open('courses.json', 'w') as f:
    json.dump({'courses': courses}, f)
  return courses


def getAssignments(c):
  u = c.get('url')
  r = s.get(u)
  l = r.text.find('sesskey')
  sesskey = r.text[l + 10:l + 20]
  doc = pq(r.text)
  assignments = doc('.modtype_assign.hasinfo')
  fa = []
  for a in assignments:
    due = pq(a).find('div > div.description > div > div > div:nth-child(2)').html(
    ).replace('<strong>Due:</strong>', '').replace(' ', '').replace('\n', '')
    dueO = datetime.datetime.strptime(due, '%A,%d%B%Y,%I:%M%p')
    # testing by adding due time since all assignments are over
    # dueO += datetime.timedelta(days=60, minutes=30)
    if dueO > datetime.datetime.now():
      fa.append({
          'id': a.attrib['data-id'],
          'link': 'https://lms.iitmandi.ac.in/mod/assign/view.php?id=' + a.attrib['data-id'],
          'due': dueO,
          'course': c
      })
  return fa


def checkAssignment(a):
  r = s.get(a.get('link'))
  doc = pq(r.text)
  status = doc(
    '#region-main > div:nth-child(4) > div.submissionstatustable > div > div > table > tbody > tr:nth-child(1) > td')
  due = status.text().find('No')
  print(status.text(), due)
  if due != -1:
    notify(a)


def main():
  login()
  print('logged in===============================================')
  selectedCourse = None

  fileExists('course.json', {'course': None})
  with open('course.json') as f:
    selectedCourse = json.load(f).get('course')

  if (selectedCourse == None):
    courses = getCourses()
    print('select no of course')
    for i in range(len(courses)):
      print(f'{i + 1}. {courses[i].get("name")}')
    n = int(input('enter no: '))
    selectedCourse = courses[n - 1]
    with open('course.json', 'w') as f:
      json.dump({'course': selectedCourse}, f)

  fileExists(
    f'finalassigns-cid-{selectedCourse["id"]}.json', {'assignments': []})
  oldA = []
  with open(f'finalassigns-cid-{selectedCourse["id"]}.json') as f:
    oldA = json.load(f).get('assignments')

  assigns = getAssignments(selectedCourse)
  assigns = [x for x in assigns if x['id'] not in [x['id'] for x in oldA]]

  if len(assigns) > 0:
    print('assignment scheduled', [x['id']for x in assigns])
    for a in assigns:
      #
      scheduler.add_job(
        checkAssignment, args=[a], trigger='date', run_date=a["due"] - datetime.timedelta(hours=6))

    with open(f'finalassigns-cid-{selectedCourse["id"]}.json', 'w') as f:
      json.dump({'assignments': oldA + [
          {**x, 'due': x['due'].strftime("%Y-%m-%d %H:%M:%S")} for x in assigns]}, f)


scheduler = BackgroundScheduler()
scheduler.add_job(main, 'date', run_date=datetime.datetime.now())
scheduler.add_job(main, 'interval', hours=10, id='main')
scheduler.start()

while True:
  time.sleep(2)
