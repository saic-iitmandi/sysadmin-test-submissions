## Challenge 5 - Scripting

first of all it was just surfing `lms.iitmandi.ac.in` to see how everything works

so found out there are two cookies that are required for every request and obviously we will get that through login

### Login

upon looking carefully formdata also contains a `logintoken input` that can be retrieved from the input field itself. So first a `GET` request then send a `POST` request with all the formdata.

### Flow

- used requests lib's session to store the 2 required auth cookies
- login takes place
- checks `course.json` if a preselected course is present
- if not get all the courses by scraping the webpage by a simple get request and then using `pyquery`(was planning to use beatifulsoup4 but it was giving issues with venv) to parse it.
- now get all the open assignments of that course with parse due date(had to add some days(a lot!) to the due since all assignments were post due date
- compare these with assignments already present in `finalassign-cid-courseID.json` and only keep that arent present
- now schedule each assignment on `checkAssignment` function 6 hours before the due date
- now when this scheduled function is called check if a submission has been made
- if not send email

- Email format

```
Assignments are due! for 6 hours
HS108_2 Basic English for Engineers due at 2024-01-29 17:30:00
```

now schedule this complete flow to run every 10 hours
and throw this script to some background worker

for scheduling I am using Apscheduler since I am using it in winter project
and resend to send email

for post requests there was also a query string named `sesskey` passed which I thought would be required but it wasnt necesaary for this use case.

### getAssignments(c)

```ps
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

```

- I get the course index page
- get all the assignment li using some js selector
- now similarly get the datetime string and parse it
- check if assignment is of future and return the assignmenta

### checkAssignment(a)

```py
def checkAssignment(a):
  r = s.get(a.get('link'))
  doc = pq(r.text)
  status = doc(
    '#region-main > div:nth-child(4) > div.submissionstatustable > div > div > table > tbody > tr:nth-child(1) > td')
  due = status.text().find('No')
  print(status.text(), due)
  if due != -1:
    notify(a)
```

- get the assignment page and check for submission status text if it has No send email
