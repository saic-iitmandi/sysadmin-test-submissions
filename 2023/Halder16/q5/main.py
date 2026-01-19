import lxml.html
import subprocess
import datetime
from bs4 import BeautifulSoup

#target_url = input("enter the web address of the page you want to read: ")

# Obtaining the page source
def write_content():
    content = '' # contains the page source code
    f = open('testing.html','r') # tested - works aight
    for i in list(f.readlines()):
        for j in i:
            content = content + j
    f.close()
    return content

# function to get the assignment info
def assn(content):
    wrk_txt = lxml.html.fromstring(content) # converting the cource code actually usable
    prnt_ele = wrk_txt.xpath(r"//li[@class='activity activity-wrapper assign modtype_assign  hasinfo ']") # reading only the 'topics' part of the web page source code

    # reads each part of every topic
    chld_ele = [element.text_content() for element in wrk_txt.xpath('./*')] # it is a list
    f = open('readit.txt','w')
    for i in chld_ele: # because too much content, just giving it more space so i can see it, it is cut off in the terminal otherwise
        f.write(i)
    f.close()
    f = open('readit.txt','r') # probably not the best approach but im too tired to be stuck here
    thing = []
    l = f.readlines()
    cnt = len(l)
    for i in range(0,cnt-1):
        thing.append([l[i]])
    f.close()
    return thing
    
# function to get the course name
def course():
    f = open('readit.txt','r') # probably not the best approach but im too tired to be stuck here
    thing = []
    l = f.readlines()
    cnt = len(l)
    for i in range(0,cnt-1):
        thing.append([l[i]])
    f.close()
    name = thing[1][0]
    n_name = ''
    for i in name:
        if i != '\n':
            n_name = n_name + i
    name = n_name
    return name
    

# leaving as -have nearly done it, next, maybe read the readit.txt and see that the assignment and teh due dates can be seen, somehow use that and you have what you need!
    
# funcion to get the course list
def course_list():
    course_list_url = 'https://lms.iitmandi.ac.in/my/courses.php'
    course_url = dict()
    # writing the page source into the html file using playwrite.py
    subprocess.run(['python','playwrite.py',course_list_url], stdout=subprocess.PIPE, text=True)
    content = write_content()
    soup = BeautifulSoup(content, 'html.parser')
    contents = [(str(egg)+',') for egg in soup.find_all('div',class_='col-md-9 d-flex flex-column')]
    
    f = open('readit_courselist.txt','w')
    for i in contents: # because too much content, just giving it more space so i can see it, it is cut off in the terminal otherwise
        f.write(i)
    f.close()
    f = open('readit_courselist.txt','r') # too tired
    thing = []
    l = f.readlines()
    cnt = len(l)
    for i in range(0,cnt-1):
        thing.append([l[i]])
    f.close()
    links = [] # will contain all the course links
    for i in thing:
        if '<a' in i[0]:
            things = i[0].split()[-1].split('"')[1] # is actual linl for the courses, one by one tho
            links.append(things)
    # links = links[7:] # for now
    for i in links:
        subprocess.run(['python','playwrite.py',i], stdout=subprocess.PIPE, text=True)
        that = write_content() #that html data is stored here
        ll = srch_time(assn(that)) #list of time of 'due' in that course page
        soup = BeautifulSoup(that, 'html.parser')
        prnt_ele = [ele for ele in soup.find('h1',class_='h2')]
        if prnt_ele == None:
            pass
        else:
            nm = prnt_ele[0]
            ll.append(i)
            course_url[nm] = ll # the dict data is entered
        
    return course_url # dict having the many course-name:[(),(),...,'link'], those being times of 'due'


# function to convert the date-time into something usable
def dt(sup): # sample input 'Thursday, 30 November 2023, 12:00 AM'
    words = sup.split()
    day,month,year = words[1],words[2],words[3].split(',')[0]
    tme = chng_time_format(words[-1])
    return [tme,day,month,year]

# function to return the month number in return for the month name
def mnth_name(word):
    months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
    word = word.lower()
    l = months.keys()
    if word in l:
        a = months[word]
    return a

# function to convert am/pm into 24 hr format, sample input - '12:00 AM'
def chng_time_format(tme):
    tme = tme.split()
    real = ''
    for i in tme[0]:
        if i != ':':
            real = real + i
    if tme[1] == 'AM' and real != '1200':
        return real
    elif tme[1] == 'PM' and real != '1200':
        return str(1200+int(real))
    elif real == '1200' and tme[1] == 'AM':
        return '0000'
    elif tme[1] == 'PM' and real == '1200':
        return str(1200)
        
# function to find the due time
def srch_time(lst): # (word to be found, lst to be searched in)
    due = [] # contains line number of each 'Due:' occurence
    tyme = [] # contains all the strings of due time
    wkdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for i in lst: # i being each line
        if 'assignment' in i[0] or 'ASSIGNMENT' in i[0] or 'Assignment' in i[0]:
            num = lst.index(i) # ie, if 'assignment' is in i of lst, store that index (of i in lst), in num'
        if 'Due' in i[0]:
            due.append(lst.index(i))
    for i in due:
        wurd = ''
        for j in wkdays:
            if j in lst[i][0]:
                ind_i = lst[i][0].index(j) + len(j) + 2 # index of the first number of the date-time we want
                if 'AM' in lst[i][0] :
                    ind_f = lst[i][0].index('AM') + 1
                elif 'PM' in lst[i][0] :
                    ind_f = lst[i][0].index('PM') + 1
        cont = ind_i
        aa = True
        while aa == True: # actually captures the required string
            if cont == ind_f:
                aa = False
            wurd = wurd + lst[i][0][cont]
            cont += 1
        tyme.append(wurd)
    return tyme # returns a list containing the time, date of submission

# function to compare time with today, now
def cmp_time(tm): # tm is of the form, [tme,day,month,year]
    today = datetime.datetime.now()
    tm_now = []

main_data = course_list() # contains, {coursename:['ass1','ass2',...,'courselink']}