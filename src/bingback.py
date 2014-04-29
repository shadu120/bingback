#!/usr/bin/python
'''
Download today's bing background images
This script will create an folder 'archive' in current directory.
by shadu{at} foxmail.com
'''
import json
import urllib2
import time
import os
import sys


def download(url):
    str = ''
    try:
        str = urllib2.urlopen(url).read()
    except:
        pass
    return str


def mkdir(backdir):
    try:
        os.mkdir(backdir)
    except:
        pass
    return os.path.exists(backdir)


def bingback():
    backDir = os.path.dirname(__file__) + os.path.sep + 'archive' + os.path.sep + time.strftime('%Y-%m-%d')
    if not mkdir(backDir):return
    for cc in ['cn', 'jp', 'fr', 'us', 'de', 'it']:
        url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&cc=%s' % cc
        try:
            html      = urllib2.urlopen(url).read()
            jsonStr   = json.loads(html)
            url       = jsonStr['images'][0]['url']
            urlbase   = jsonStr['images'][0]['urlbase']     # /az/hprichbg/rb/MingunPahtodawgyi_ROW13596316452
            startdate = jsonStr['images'][0]['startdate']
            jsonFile  = cc + '_' + urlbase.split('/')[-1] + '.json'
            imageUrl  = 'http://www.bing.com' + url
            imageName = cc + '_' + url.split('/')[-1]       # http://s.cn.bing.net/az/hprichbg/rb/CityscapeHongKong_ZH-CN11566614572_1366x768.jpg
            try:
                fileJson = open(backDir + os.path.sep + jsonFile, 'w+')
                fileJson.write(html)
                fileJson.close()
            except Exception, e1:
                print e1
                pass
         
            try:
                fileImage = open(backDir + os.path.sep + imageName, 'wb+')
                fileImage.write(download(imageUrl))
                fileImage.close()
            except Exception, e2:
                print e2
                pass
        except Exception,e:
            print e
            pass
if mkdir(os.path.dirname(__file__) + os.path.sep + 'archive'):
    bingback()
