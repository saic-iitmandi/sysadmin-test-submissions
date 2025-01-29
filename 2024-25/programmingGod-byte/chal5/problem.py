from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio

busReservationUrl = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"


def splitDate(s):
    a = s.split('/')
    return [a[0], a[1], a[2]]

async def render_page(session, url, data):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": busReservationUrl,
    "Content-Type": "application/x-www-form-urlencoded",
    }
    response = await session.post(url, data=data,headers=headers)
    await response.html.arender(wait=20)  
    
    print("Cookies:", session.cookies.get_dict())
    print("Final URL:", response.url)
    
    return response

async def main():
    session = AsyncHTMLSession()
    
    routeDictionary = [
        {"value": "1", "text": "North Campus -To- Mandi (via South)"},
        {"value": "2", "text": "Mandi -To- North Campus (via South)"},
        {"value": "7", "text": "North Campus -To- Mandi (Direct)"}
    ]
    
    routeGivenValue = "1"
    travelDate = "03/02/2025"
    timeToTravel = "06:00 PM"

    postDate = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$txtFromDate"
    postClientState = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$M1_ClientState"
    postRoute = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlRoute"
    postTiming = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlTiming"
    postBus = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlBus"
    postMonth = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel3$MonthYear1$ddlMonth"
    postYear = "ctl00$ContentPlaceHolder1$TabContainer1$TabPanel3$MonthYear1$ddlYear"

    try:
        print("in try")
        
        loginURL = "https://oas.iitmandi.ac.in/instituteprocess/common/login.aspx"

        rollno = ""
        password = ""
        data = {}

     
        response = await session.get(loginURL)
        loginContent = response.html.html

        # Parse the login page HTML to get hidden input values
        soup = BeautifulSoup(loginContent, 'lxml')
        input_tags = soup.find_all('input')

        for input_tag in input_tags:
            name = input_tag.get('name')
            value = input_tag.get('value')
            data[name] = value if value else ''

      
        data["txtLoginId"] = rollno
        data["txtPassword"] = password
        data["btnLogin"] = "Log In"

        for item in data.keys():
            print(item)

        # Perform the login POST request
        loginPostRequest = await session.post(loginURL, data=data)
        print("login status code ",loginPostRequest.status_code)

       
        if loginPostRequest.status_code == 200 and 'ASP.NET_SessionId' in session.cookies:
            print('Login successful')
        else:
            print('Login failed')
            raise Exception("Login failed")

       
        busReservationGet = await session.get(busReservationUrl, allow_redirects=True)
        busReservationGetHtml = busReservationGet.html.html

      
       
       
        firstData = {}
        soup = BeautifulSoup(busReservationGetHtml, 'lxml')
        input_tags = soup.find_all('input')

        for input_tag in input_tags:
            name = input_tag.get('name')
            value = input_tag.get('value')
            if name[0:5] != 'ctl00' and name != "__EVENTTARGET":
                firstData[name] = value if value else ''

        firstData['__EVENTTARGET'] = postRoute
        firstData[postDate] = travelDate
        firstData[postClientState] = ""
        firstData[postRoute] = routeGivenValue
        firstData[postMonth] = '01'
        firstData["__EVENTARGUMENT"] = ""
        firstData["__LASTFOCUS"] = ""
        firstData[postYear] = splitDate(travelDate)[2]

        settingRoutePostRequest = await session.post(busReservationUrl, data=firstData)
        print("bus route slection status code ",settingRoutePostRequest.status_code)
        settingRoutePostRequestText = settingRoutePostRequest.html.html
      

        # Checking schedule 
        soup = BeautifulSoup(settingRoutePostRequestText, 'lxml')
        input_tags = soup.find_all('input')

        secondData = {}
        for input_tag in input_tags:
            name = input_tag.get('name')
            value = input_tag.get('value')
            if name[0:5] != 'ctl00' and name != "__EVENTTARGET":
                secondData[name] = value if value else ''

        select_bus_timing = soup.find('select', id='ddlTiming')
        options = select_bus_timing.find_all('option')
        optionsValue = ""
        optionsText = ""
        for option in options:
            value = option.get('value')
            text = option.text
            textSplit = text.split(" ")
            startingTime = textSplit[0]
            endingTime = textSplit[len(textSplit) - 1]
            timeToTravelSplit = timeToTravel.split(" ")
            timeToTravelfirst = timeToTravelSplit[0]
            timeToTravelsecond = timeToTravelSplit[len(timeToTravelSplit) - 1]
            if startingTime == timeToTravelfirst and endingTime == timeToTravelsecond:
                optionsValue = value
                optionsText = text
                break

        if optionsValue == "":
            raise Exception("Bus timing not found")

        globalPostTiming = optionsValue
        secondData["__EVENTTARGET"] = postTiming
        secondData[postClientState] = ""
        secondData[postRoute] = routeGivenValue
        secondData[postTiming] = optionsValue
        secondData[postMonth] = "01"
        secondData[postYear] = splitDate(travelDate)[2]
        secondData["__EVENTARGUMENT"] = ""
        secondData["__LASTFOCUS"] = ""

        scheduleBookResponse = await session.post(busReservationUrl, data=secondData)
        print("bus schedule response status code",scheduleBookResponse.status_code)
        scheduleBookResponseText = scheduleBookResponse.html.html

       
        ####### BUS SELECTION

        thirdData = {}
        

    
        soup = BeautifulSoup(scheduleBookResponseText, 'lxml')
        input_tags = soup.find_all('input')
        for input_tag in input_tags:
            name = input_tag.get('name')
            value = input_tag.get('value')
            if name[0:5] != 'ctl00' and name != "__EVENTTARGET":
                thirdData[name] = value if value else ''

        select_bus_name = soup.find('select', id='ddlBus')
        options = select_bus_name.find_all('option')
        if len(options) == 0:
            raise Exception("No buses found for this particular timing")
        optionsBusValue = ""

        for option in options:
            value = option.get('value')
            optionsBusValue = value
            break
        thirdData["__EVENTTARGET"] = postBus
        thirdData[postClientState] = ""
        thirdData[postRoute] = routeGivenValue
        thirdData[postTiming] = globalPostTiming
        thirdData[postBus] = optionsBusValue
        thirdData[postMonth] = "01"
        thirdData[postYear] = splitDate(travelDate)[2]
        thirdData["__EVENTARGUMENT"] = ""
        thirdData["__LASTFOCUS"] = ""

        
        session.cookies.update(loginPostRequest.cookies)

        busSelectionResponse = await render_page(session,busReservationUrl,thirdData)
        print("Redirect headers:", busSelectionResponse.headers)

        busSelectionResponseText = busSelectionResponse.html.html
        print("bus no response status code ",busSelectionResponse.status_code)
        
      
       
    except Exception as e:    
        print(e)
    finally:
        await session.close()
asyncio.run(main())        














































































