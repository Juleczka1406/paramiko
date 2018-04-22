#! /usr/bin/python

import paramiko
import re

UserName = 'tester01'

remote_cli=paramiko.SSHClient()
remote_cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_cli.connect("localhost", username='tester01', password="tester01")
a,b,c=remote_cli.exec_command("cat /etc/passwd")
z=b.read()
linie=z.split('\n')

for element in linie:

    if re.search(UserName, element):
        print ('User ' + UserName + ' EXISTS')
        break
else:
    print ('User ' + UserNameSkrypt 2
