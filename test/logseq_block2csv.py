#coding:utf8
import sys
import pandas as pd
# create a new dict
dict_data={}

# delete adjacent duplicate 
def del_adjacent(alist):
    for i in range(len(alist) - 1, 0, -1):
        if alist[i] == alist[i-1]:
            del alist[i]

# syntax
symb1 = '-'
symb2 = '::'
# open a md file
with open(sys.argv[1],'r')as file:
  # read everyline in file
    for line in file:
        # for line with '-', and without 'query' or '.csv', we put it in the dict and give it a key 'title' 
        if symb1 in line.strip()[:2]:
            if 'query' in line:
                continue
            elif '.csv' in line:
                continue
            # when meet a blank line, skip
            elif line.strip()[2:].count('\n') == len(line.strip()[2:]):
                continue
            else:
                dict_data.setdefault('title',[]).append(line.strip()[2:].strip(" #]\n").replace('[',''))
        # for line with ':: ', and without 'query' or '.csv', we treat the word before '::' as key, the words after '::' as value
        elif symb2 in line:
            if 'query' in line:
                continue
            elif '.csv' in line:
                continue
            else:
                for kv in [line.strip().split('::')]:
                    if len(kv) != 1:
                        dict_data.setdefault(kv[0],[]).append(kv[1].strip())
                    else:
                        dict_data.setdefault(kv[0],[]).append('')
        else:
            continue

if len(dict_data['title']) != len(dict_data[list(dict_data)[1]]):
    del_adjacent(dict_data['title'])
#print(dict_data)

# read all the keys as a list
columnsname=list(dict_data.keys())
# create a pandas dataframe, column names are the keys
frame = pd.DataFrame(dict_data,columns=columnsname)
# output dataframe to csv, without index '0,1,2...'
frame.to_csv('./'+sys.argv[1].split('.')[0]+'.csv',index=False)
