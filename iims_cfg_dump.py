#!/usr/bin/env  python
# -*- coding: utf-8 -*-
#pip2 install --no-cache xlsxwriter==2.0.0
#pip2 install pandas==0.23.0 numpy==1.16.6

import os
import time
import sys
import pandas as pd
import xlsxwriter
import subprocess
import json
import shutil

file_name = 'iims_cfg_dump.xlsx'

host_output = subprocess.check_output(["thruk","r","service"])
host_jsons = json.loads(host_output)

df = pd.DataFrame(columns = ['host_name','host_address','host_alias','host_check_command','description','check_command','display_name','host_groups','groups','contacts','contact_groups','check_interval','perf_data','peer_name'])
# print host_jsons
# print host_output

for host_json in host_jsons:
    hostgroups = ",".join(host_json['host_groups'])
    groups = ",".join(host_json['groups'])
    contacts = ",".join(host_json['contacts'])
    contact_groups = ",".join(host_json['contact_groups'])
    df = df.append({'host_name' : host_json['host_name'] , 'host_address' : host_json['host_address'], 'host_alias' : host_json['host_alias'],'host_check_command' : host_json['host_check_command'],'description' : host_json['description'],'check_command' : host_json['check_command'],'display_name' : host_json['display_name'],'check_interval' : host_json['check_interval'],'perf_data' : host_json['perf_data'],'host_groups' : hostgroups,'groups' : groups,'contacts' : contacts,'contact_groups' : contact_groups,'peer_name' : host_json['peer_name']}, ignore_index=True)
    # df.to_excel("/tmp/"+file_name,sheet_name= "services",index=False, encoding="utf-8")
    # print("done")
# print df

df.to_excel(file_name,sheet_name= "services",index=False, encoding="utf-8")
# print("success")
shutil.copyfile(file_name,'/var/www/html/' + file_name)
shutil.copyfile(file_name,'/var/www/html/nagiosql/admin/' + file_name)
