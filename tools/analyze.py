#coding=utf8
"""
# Author: host
# Created Time : 2023年04月27日 星期四 17时31分39秒

# File Name: analyze.py
# Description:

"""
import os
import csv

logs_dir = "logs"
logs_failed_dir = "logs_failed"

testsuites = os.listdir(logs_dir)
rows = []

testcases = []
for suite in testsuites:
    tc = os.listdir(logs_dir+"/"+suite)
    if suite in os.listdir(logs_failed_dir):
        if tc[0] in os.listdir(logs_failed_dir+"/"+suite):
            rows.append([suite,tc[0],"failed!"])
        else:
            rows.append([suite,tc[0],"passed!"])
        for tcs in tc[1:]:
            if tcs in os.listdir(logs_failed_dir+"/"+suite):
                rows.append([None,tcs,"failed!"])
            else:
                rows.append([None,tcs,"passed!"])
    else:
        rows.append([suite,tc[0],"passed!"])
        for tcs in tc[1:]:
            rows.append([None,tcs,"passed!"])


f = open("result.csv","w")
writer = csv.writer(f)

writer.writerows(rows)
