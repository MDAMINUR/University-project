from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from bs4 import BeautifulSoup
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
from .models import *
#Getting news from BdNews24

BDNews24_URL = "https://bdnews24.com/"
BDNews24_r = requests.get(BDNews24_URL)
BDNews24_soup = BeautifulSoup(BDNews24_r.content, 'html5lib')
BDNews24 = []

hdiv = BDNews24_soup.find('div', attrs = {'class':"F4BJV"}) 

hdivnews = hdiv.findAll('h6', attrs = {'class' : "headline-m_headline__3_NhV headline-m_dark__en3hW"})
print(hdivnews)

for news in hdivnews:
    ns = news.text
    print(ns)
    try:
        AllNews.objects.create(                                    
            title = ns
        )
        print("DB append done")

    except:
        print("DB append Failed")

    BDNews24.append(ns)

#Getting news from Prothom Alo

prothomAlo_URL = "https://prothomalo.com/"
prothomAlo_r = requests.get(prothomAlo_URL).content
prothomAlo_soup = BeautifulSoup(prothomAlo_r, 'html5lib') 
Palo = [] 

for news in prothomAlo_soup.find_all('h3', attrs = {'class' :'tilte-no-link-parent'}):
    news = news.text
    Palo.append(news)

#Getting news from The Daily Star

tds_URL = "https://www.thedailystar.net/bangla/"
tds_r = requests.get(tds_URL)
tds_soup = BeautifulSoup(tds_r.content, 'html5lib') 
tds_news = []

for news in tds_soup.findAll('div', attrs = {'class':'highlight-text'}) :

    news = news.h1.text
    print(news)
    print()
    tds_news.append(news)

"""
morehighlight = tds_soup.find('div', attrs = {'class':'more-highlight'})

for news in morehighlight.find_all('div', attrs = {'class':'two-50'}) :
    
    news = news.h3.text
    tds_news.append(news)

for news in morehighlight.findAll('div', attrs = {'class':'three-33 margin-bottom-zero'}) :
    
    news = news.h4.text
    tds_news.append(news)


for news in tds_soup.findAll('h5') :
    
    news = news.a.text
    tds_news.append(news)
"""
#Getting news from Dhaka Tribune

dt_URL = "https://bangla.dhakatribune.com/"
dt_r = requests.get(dt_URL)
dt_soup = BeautifulSoup(dt_r.content, 'html5lib') 
dt_news = []

singlenews = dt_soup.find( 'ul', attrs = {'class': 'just_in_news'} )
style = dt_soup.find( 'div', attrs = {'class': 'single-list-style-news-area'})


for news in dt_soup.findAll( 'div', attrs = {'class': 'dt-strem-cont'}) :
    
    news = news.h2.text
    dt_news.append(news)
"""
for news in style.findAll( 'div', attrs = {'class': 'single-news-style'}) :
    
    news = news.h4.text
    dt_news.append(news)
"""
#Defining functions to connect the URLs 

def bdNews24(req):
    name = "BDNews24.com"
    obj = AllNews.objects.all()

    return render(req, 'news/index.html', {'post': obj, 'name' : name})


def theDailyStar(req):

    name = "The Daily Star"
    obj = tds_news
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})

def prothomAlo(req):
    name = "Prothom Alo"
    obj = Palo
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


def dhakaTribune(req):

    name = "Dhaka Tribune"
    obj = dt_news
    return render(req, 'news/index.html', {'post' : obj, 'name' : name})


# def home(request):
#     txt = "news" 
#     return HttpResponse(txt)



# for news in hdiv:
#     ns = news.h6.text
#     li = news.a['href']
#     print(li)
#     try:
#         AllNews.objects.create(                                    
#             title = ns,
#             link = li
#         )
#         print("DB append done")

#     except:
#         print("DB append Failed")


# hv = BDNews24_soup.find('div', attrs = {'class':"YugbO"}) 
# hdivnews = hv.findAll('h6', attrs = {'class' :"headline-m_headline__3_NhV headline-m_dark__en3hW"})
# for news in hdivnews:
#     ns = news.text
#    # li = news.a['href']
#     print(ns)
#     try:
#         AllNews.objects.create(                                    
#             title = ns,
#           #  link = li
#         )
#         print("DB append done")

#     except:
#         print("DB append Failed")

  