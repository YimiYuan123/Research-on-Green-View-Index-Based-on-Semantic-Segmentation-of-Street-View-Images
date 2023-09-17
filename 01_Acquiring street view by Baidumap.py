# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:09:21 2020

"""
#-*-coding:utf-8-*-
import os
import os.path
import xlrd 
import urllib.request
import sys
import time
import socket
import urllib.error

import requests

def isFile(fname):
    return os.path.isfile(fname)

def getFile(fname):
    data = ""
    with open(fname, "r", encoding='utf-8') as f:
        data = f.read()
    return data

def DownloadFile(url, save_url,file_name):
    try:
        if url is None or save_url is None or file_name is None:
            print('参数错误parameter fault')
            return None
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        res = requests.get(url,stream=True) 
        total_size = int(int(res.headers["Content-Length"])/1024+0.5)

        n = len(res.text)

        if n==59:
            print("限额reach the limitation")
            return
        
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        from tqdm import tqdm
        with open(file_path, 'wb') as fd:
            print('开始下载文件start：{},当前文件大小currentfile：{}KB'.format(file_name,total_size))
            for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
                fd.write(chunk)
            print(file_name+' 下载完成！Done!')
            flag = 1
    except:
        print("程序错误fault")
        flag = 0
    return flag
 
def sleep(mytime= ''):
	time.sleep(mytime)
 
def download(url, name):
	try:
		conn = urllib.request.urlopen(url,timeout=5)
		flag = 1
	except:
	#except urllib.error.URLError as e:
		#if isinstance(e.reason, socket.timeout):
			 #print("Time out!")
		flag = 0
	if flag == 0:
		return flag
	else:
		return flag
 

key = "6NkHxxxxxxxxxxxxxxxxxxxxxx" #type your key here

data = xlrd.open_workbook("addr.xlsx")
SamplePoint = data.sheet_by_name(u'Sheet1')
nrows = SamplePoint.nrows
ncols = SamplePoint.ncols
valueName = []
valueLongitude = []
valueLatitude = []

for i in range(nrows-1):
    valueName.append(SamplePoint.cell(i+1 ,0).value)
    valueLongitude.append(SamplePoint.cell(i+1, 1).value)
    valueLatitude.append(SamplePoint.cell(i+1, 2).value)
    print(valueName[-1])
    print(valueLongitude[-1])
    print(valueLatitude[-1])
    

    for heading in [90, 180, 270, 360]:
        url = "http://api.map.baidu.com/panorama/v2?ak=" + key + "&width=600&height=450&coordtype=wgs84ll&heading="+ str(heading) + "&pitch=0&location=" + str(valueLongitude[-1]) + "," + str(valueLatitude[-1]) + "&fov=90"
        path = "./pic3/"
        outname = "./pic3/" + str(valueName[-1]) + "_" + str(valueLongitude[-1]) + "_" + str(valueLatitude[-1]) + "_" + "30_" + str(heading) + ".jpg"
        fname = str(valueName[-1]) + "_" + str(valueLongitude[-1]) + "_" + str(valueLatitude[-1])+ "_30_" + str(heading) +  ".jpg"        
        if isFile(outname):
            print("文件存在跳过下载")
        else:
            print("开始下载")
            print(outname)
            print (url)
            flag = DownloadFile(url, path, fname)
            sleep(0.01)
            print('call delay')
