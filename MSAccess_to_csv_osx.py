#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 13:59:50 2018

@author: Danny
"""
import os
import platform

# check os
if platform.system() == 'Darwin':
    print('OSX')  # further call function for osx reading ms access
elif platform.system() == 'Windows':
    print('Windows')  # call function for windows
elif platform.system() == 'Linux':
    print('Linux')  # call function for linux

# Os = OSX
# use mdbtools export to csv

# create temp dir for storing csv file
try:
    os.mkdir('../temp_csv')
except:
    print('temp_csv already created')

# use supprocess with mdbtools extract all table names

import subprocess

access_db = '/Users/Danny/Share Win7/OSS DataSales 201802.mdb'

table_names = subprocess.Popen(['mdb-tables', '-1', access_db],
                               stdout = subprocess.PIPE)\
                               .communicate()[0].decode('utf-8')
tables = table_names.split('\n')

# convert each tabls to temp_csv
os.chdir('../temp_csv')

for table in tables:
    if table != '':
        filename = table.replace(" ","_") + ".csv"
        file = open(filename, 'w')

        print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", access_db, table],
                                    stdout = subprocess.PIPE)\
                                    .communicate()[0].decode('utf-8')
        file.write(contents)
        file.close()