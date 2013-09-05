# -*- coding: utf-8 -*-
"""
Created on Wed Sep 04 15:05:14 2013

@author: henriette
"""

import re
from collections import Counter

text = re.sub('<[^<]+>', "", open("shakespeer/hamlet.xml").read())
text = re.sub(' ', "\n", text)
text = text.lower()
text = re.sub('(?imu)^\s*\n', "", text)
text = re.sub("[^\w\n]", "", text)
list = text.split("\n")



list.sort()


counter=Counter(list)

file = open("hamlet.txt", "w")
for key,value in sorted(counter.items()):
        print (key,value)
        file.write(str(value) + ", "+key+"\n")

file.close()