# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:16:00 2021

@author: Master Race
"""

import subprocess, csv
from datetime import datetime

now = datetime.now()
fecha = now.strftime('%Y/%m/%d')
hora = now.strftime('%H:%M:%S')
dia = now.strftime('%Y%m%d')

subprocess_text = subprocess.Popen("D:\OneDrive - TPS S.A\Documentos\speedtest\speedtest.exe", shell=True, stdout=subprocess.PIPE ,stderr=subprocess.STDOUT)
stdout,stderr = subprocess_text.communicate()
test = stdout.decode("utf-8")
test = test.rstrip()
test = test.splitlines()

# Parseo del test en una lista

server = test[3]
isp = test[4].split()
isp = isp[1]
ping = test[5].split()
ping = ping[1]
down = test[7].split()
down = down[1]
up = test[9].split()
up = up[1]
pack = test[10].split()
pack = pack[2]

results2 = [fecha, hora, isp, ping, down, up, pack]

print(results2)

# Escribir el log

with open('%s.csv' % dia,'a',newline='') as out:
    writer = csv.writer(out, delimiter='\t')
    writer.writerow(results2)

# Realizado por los hermanos Facundo Y Juan Redon.
