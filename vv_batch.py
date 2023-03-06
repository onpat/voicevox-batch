# -*- coding: utf-8 -*-
import sys
import time
import urllib.request
import urllib.parse

host = "http://127.0.0.1:50021"

def vv(voice, text, dest):
    qreq = urllib.request.Request(host+'/audio_query?text='+urllib.parse.quote(text)+'&speaker='+voice, method="POST")
    qresp = urllib.request.urlopen(qreq)
    vreq = urllib.request.Request(host+'/synthesis?speaker='+voice, data=qresp, method="POST", headers={"Content-Type" : "application/json"})
    vresp = urllib.request.urlopen(vreq).read()
    filevoice = open(dest, 'wb')
    filevoice.write(vresp)
    filevoice.close()
    return 1
    
print("start ...")

args = sys.argv
if (len(args) != 2):
    print("vv_batch.py [filename]/voices")
    print("please select sprict file")
    print()
    print("sprict file example:")
    print("0 [voice type]")
    print("aaaaaa [text]")
    print("bbbbbb [text]")
    print("<> [parition]")
    print("encoding is no bom utf-8, cr")
    quit()

if (args[1] == "voices"):
    voices = urllib.request.urlopen(host+'/speakers').read()
    print(urllib.parse.unquote(voices))
    quit()

# read sprict file
print("loading sprict file")
filesprict = open(args[1], 'r', encoding='UTF-8')

inmode = 0 # 0=voice, 1=text
voice = 0 # voice type
speak = ""
ocount = 0 # for output file name
tmptime = 0
elapsed = 0
while True:
    line = filesprict.readline()
    line = line.rstrip('\r\n')
    if (inmode == 0):
        voice = line
        inmode = 1
        continue
    if (inmode == 1):
        if (line == "<>"):
            print(ocount, "start")
            tmptime = time.time()
            vv(voice, speak, str(ocount)+".wav")
            elapsed = time.time() - tmptime
            speaklen = len(speak)
            print(ocount, "ok,", format(elapsed, '.3f'), "sec,", format(elapsed / speaklen, '.3f'), "per char")
            speak = ""
            ocount = ocount + 1
            inmode = 0
            continue
        speak = speak + line + ","
    if line == '':
        break
filesprict.close()
print("end")
