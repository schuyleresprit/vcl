import os
import pandas as pd
import json


ENGLISH_JSON = os.getcwd() + '/data/english.json'
getJSON = os.getcwd() + '/data/languages.json'
languages = {}

def getList(languages):
    list = []
    for key in dict.keys('English'):
        list.append(key)

    return list
print(list)
