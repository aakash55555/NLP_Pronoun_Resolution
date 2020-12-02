# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:37:18 2020

@author: Abhilasha Mandal
"""

import xml.etree.ElementTree as et
import pandas as pd

# filepath = './balanced_copa/balacopa-dev-all.xml'
filepath = './intermediate_files/generated_xml.xml'

xtree = et.parse(filepath)
xroot = xtree.getroot()

rows = []

for node in xroot:
    itemid = node.attrib.get('id')
    p = node.find('p').text
    a1 = node.find('a1').text
    a2 = node.find('a2').text
    
    rows.append([itemid, p, a1, a2])
    
df = pd.DataFrame(rows, columns=['id','p','a1','a2'])

# newfilepath = './balanced_copa/balacopa-dev-all.csv'
newfilepath = './intermediate_files/new_csv_generated.csv'

df.to_csv(newfilepath, index=False)