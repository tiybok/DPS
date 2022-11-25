#!/usr/bin/env python
# coding: utf-8

import requests

url = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge'
myobj = {'github': 'https://github.com/tiybok/DPS',
         'email':'tiybok45@gmail.com',
         'url':'http://35.154.53.33:8501/',
         'notes':'I deployed using streamlit web app for the model. You can try it through this link: http://35.154.53.33:8501/'}

x = requests.post(url, json = myobj)

print(x.text)

