#!/usr/bin/python
from datetime import date
import os
import re

u_title =  raw_input("Please ENTER the Title:\n")
p_title = re.sub(r'\s+', '-', u_title.strip())

# post
rakecmd = "rake post title=" + "'" + p_title + "'"
os.popen(rakecmd)

# print
now = date.today()
p_date =  now.strftime("%Y-%m-%d")

# info
print 'File has been Created:\n' './_posts/'+ p_date + '-' + p_title.lower() + '.md'
print 'Done...'