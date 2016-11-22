from apk import apk
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import json



def getapk(name):
    print("Looking for"+name+" ...")
    with open('sources.json') as sources:    
        apkpure = json.load(sources)["source"][0]["apkpure"][0]
    print("Source apkpure Selected..")
        

    http = httplib2.Http()
    print("Fetching "+name+" from source..")
    status, response = http.request(apkpure["search"].replace("{q}", name))

    
    status, response = http.request(apkpure["homepage"]+BeautifulSoup(response, 'html.parser').p.a["href"])
    search = BeautifulSoup(response, 'html.parser')
    for i in search.find_all('div', 'main'):
        print i.div['class']
        for d in i.find_all('div', 'box'):
           
    
    

    


        


getapk("j")
