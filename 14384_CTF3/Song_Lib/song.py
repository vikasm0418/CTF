import requests
from PIL import Image
import base64
import os
import sys
from bs4 import BeautifulSoup
import time
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
orig = Image.open("download.png")
orig_p,orig_w, orig_h = orig.convert("RGB"),orig.size

def xor(im):
    c = 0
    width,height = im.size
    imp = im.convert("RGB")
    for x in range(width):
        for y in range(height):
            pix1 = orig_p.getpixel((x,y))
            if (pix1 == (255, 255, 255)):
                pix1 = 1
            else:
                pix1 = 0
            pix2 = imp.getpixel((x,y))
            if (pix2 == (255, 255, 255)):
                pix2 = 1
            else:
                pix2 = 0
            if(pix1 ^ pix2 == 0):
                c += 1
    return c

def extract(html):
	soup = BeautifulSoup(html, 'html.parser')
        gu = (soup.find('img')['src'])
        return (gu[gu.find("base64,") + 7:])
	
#832a850aaaaaaaaaaaaaaaaaaaaaaaaaa

str1 = list("cs628a{" + "a" * 33)
for i in range (7,40):
    cnt = -1
    ascii = "a"
    for j in "0123456789abcdefghijklmnopqrstuvwxyz}":
        curr,curr[i] = str1,j
        g = open("check.png", "wb")
        r = requests.post("https://cseproj91.cse.iitk.ac.in:8020/", data={'text': ''.join(blah)})
        res = extract(r.text)
        g.write(base64.b64decode(extract(r.text)))
        g.close()
        gu = Image.open("check.png")
        anr = xor(gu)
        if(anr == cnt):
            print("problem")
        if (anr > cnt):
            cnt,ascii = anr,j
        os.remove("check.png")
    str1[i] = ascii
    print("".join(str1))