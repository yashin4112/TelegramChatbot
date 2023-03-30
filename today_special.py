import bs4
import requests

def today_is():
    url=requests.get("https://nationaldaycalendar.com/what-day-is-it/")
    soup = bs4.BeautifulSoup(url.content,features="html.parser")
    event_html=(soup.find(attrs={'id':'evcal_list'}))
    specialdays=[]
    for div in event_html.find_all(attrs={'class':'evcal_desc2 evcal_event_title'}):
        specialdays.append(div.text)
    return specialdays[0:5]
