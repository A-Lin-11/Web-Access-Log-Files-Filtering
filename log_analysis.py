# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:36:53 2017

@author: andre
"""

import re
from pprint import pprint 

f = open('access_log.txt','rU')

log = []

for i in f.readlines():
    log.append(i[:-1])

def valid_visit(entry):
    match = re.search(r'\[.*\]\s+"([A-Z]+)\s+(.*?)"\s+(\d+)\s+', entry, re.IGNORECASE)     
    try:
        if match.group(1) == 'GET' or match.group(1) == 'POST':                     #condition 1
            if match.group(3) == '200':                                             #condition 2
                domain_search = re.match(r'https?://[a-z][:\-\.\w\/]+?\.([a-z]+?)(:*\d*)/\S', match.group(2),re.IGNORECASE) 

                if domain_search:                                                   #condition 3&4
                    return domain_search.group(1)
                elif re.match(r'https?://[a-z][^/][:\-\.\w/]+?\.([a-z]+?)\s?', match.group(2),re.IGNORECASE):
                    return re.match(r'https?://[A-Za-z][^/][:\-\.\w/]+\.([a-z]+)\s?', match.group(2), re.IGNORECASE).group(1)
        return False
    except:
        return False


def get_date(entry):
    date = re.search(r'\[(\d+\/[A-Za-z]+\/\d+):', entry)
    return date.group(1)

valid_count = {}

for i in log:
    if valid_visit(i):
        if get_date(i) in valid_count:
            valid_count[get_date(i)][valid_visit(i).lower()] = valid_count[get_date(i)].get(valid_visit(i).lower(), 0) + 1
        else:
            valid_count[get_date(i)] = {valid_visit(i).lower():1}

iva = open('invalid_access_log_ljumsi.txt','wb')

for i in log:
    if valid_visit(i) == False:
        iva.write(i+'\n')
        
iva.close()            


# pprint(valid_count)


def convert_to_str(dic):
	l = []
	for i in dic:
		s = '{}:{}\t'.format(i,dic[i])
		l.append(s)
	l.sort()
	return l

valid_count_file = open('valid_log_summary_ljumsi.txt','wb')

res = []
for i in valid_count:
	s=i + '\t'
	for j in convert_to_str(valid_count[i]):
		s += j
	res.append(s)
res.sort()

for i in res:
	valid_count_file.write(i[:-1]+'\n') 



valid_count_file.close()

