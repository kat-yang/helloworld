# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:48:51 2016

@author: Yang
"""

import pymongo 

#激活，在本地创建数据库，如果要部署到网络，这个就要调整了
clint=pymongo.MongoClient("localhost",27017)

#Create a walden file, better use the same name
walden=clint["walden"]
# create a table
sheet_tab=walden["shee_tab"]

#path="C:\\Users\\Yang\\Desktop\\walden.txt"
#with open(path,'r') as f:
#    lines=f.readlines()
#
#    for index, line in enumerate(lines):
#        if not line =="\n":
#            data={
#            "index":index,
#            "line":line,
#            "length" :len(line.split())
#            }
#           
#            print (data)   
#            sheet_tab.insert_one(data)
#
for item in sheet_tab.find():
    print(item["line"])