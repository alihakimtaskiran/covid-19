#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:52:08 2020

@author: ali
"""

import time
import notify2 as not2
import requests
import os
ico=os.getcwd()+"/corona_ico.png"
url="https://www.worldometers.info/coronavirus/country/turkey"

while True:
    raw=requests.get(url).text.splitlines()
    ind=raw.index('<div class="maincounter-number">')
    raw_=(raw[ind+1],raw[ind+7],raw[ind+13])
    del raw
    data=[raw_[0].replace('<span style="color:#aaa">',"").replace(' </span>',"").replace(",","."),
        raw_[1].replace("<span>","").replace('</span>',"").replace(",","."),
        raw_[2].replace("<span>","").replace('</span>',"").replace(",",".")
    ]
    out="Vaka Sayısı:"+data[0]+"\nVefat:"+data[1]+"\nİyileşen:"+data[2]
    print(out)
    not2.init("Covid-19")
    n=not2.Notification("Covid-19",out,ico)
    n.show()
    time.sleep(3600)