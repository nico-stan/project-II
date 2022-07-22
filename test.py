import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
df = pd.read_csv ('attacks.csv', encoding='latin')

def types_(x):
    x.replace(['Questionable'],['Invalid'], inplace=True)
    x.replace(['Boat'],['Boating'], inplace=True)
    x.replace(['Boatomg'],['Boating'], inplace=True)
    return x

def sex (x):
    x = x.fillna('U')
    x= x.str.strip()
    x = x.apply(lambda x: 'U' if x!='M' and x!='F' else x)
    x.replace(['U'],[np.nan], inplace=True)
    return x

def age (x):
    if re.match("\d\d?", str(x)):
        x= re.match("\d\d?", str(x))[0]
    else:
        x=str(x)
    if re.match("^\d\d?$", str(x)):
        return 5*round(int(re.findall("^\d\d?$", str(x))[0])/5)
    else:
        return np.nan
    
def activities(string):
    #lowercase for functions and Title for Classes
    """Cleans the strings of text and converts it to useful simplifications"""
    string = str(string).lower().strip()
    if string != string:
        return np.nan
    elif "swimming" in string or"bathing" in string or "floating" in string or "splashing" in string or "jumped into the water" in string or "playing" in string or "escaping from alacatraz" in string:
        return "swimming"
    elif "diving" in string or "snorkel" in string:
        return "diving"
    elif "fishing" in string or "seine netting" in string or "spearing fish" in string:
        return "fishing"
    elif "surf" in string or "body boarding" in string or "body-boarding" in string or "boogie boarding" in string or "paddleskiing" in string:
        return "surf"
    elif "standing" in string:
        return "standing"
    elif "kayaking" in string or "ship" in string or "sail" in string or "boat" in string or "canoeing" in string or "board" in string or "rowing" in string or "fell into the water" in string:
        return "boating"
    elif "disaster" in string:
        return "sea disaster"
    elif "wading" in string or "walking" in string or "treading water" in string:
        return "walking"
    else:
        return np.nan