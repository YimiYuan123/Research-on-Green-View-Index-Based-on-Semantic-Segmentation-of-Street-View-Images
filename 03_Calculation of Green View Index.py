# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:36:14 2021

@author: Administrator
"""
import time
start =time.clock()
from PIL import Image
import pandas as pd
import os
import os.path
import xlrd 
from numpy import *
#f = open("o.txt", 'w+')  
data = xlrd.open_workbook("addr.xlsx")
SamplePoint = data.sheet_by_name(u'Sheet1')
nrows = SamplePoint.nrows
ncols = SamplePoint.ncols
valueName = []
valueLongitude = []
valueLatitude = []
lsl1=[]
#lsl2=[]
for i in range(nrows-1):
    valueName.append(SamplePoint.cell(i+1 ,0).value)
    valueLongitude.append(SamplePoint.cell(i+1, 1).value)
    valueLatitude.append(SamplePoint.cell(i+1, 2).value)
    lsl_list=[]
    for head in [90,180,270,360]:
        fname="C:/本科毕业论文专题/工作空间/google-street/output/"+str(valueName[-1]) + "_" + str(valueLongitude[-1]) + "_" + str(valueLatitude[-1]) + "_30_" + str(head)+ ".bmp"
        im = Image.open(fname)
        im = im.convert('RGB')
        count=0
        for w in range(im.width):
            for h in range(im.height):
                r, g, b = im.getpixel((w, h))
                #print(r, g, b)
                if r==182 and g==91 and b==223:
                    count+=1
        lsl=count/(im.width*im.height)
        lsl_list.append(lsl)
        #lsl2.append(lsl)
    lslmean=mean(lsl_list)       
    lsl1.append(lslmean)
    print("finish:"+str(i),lslmean)

#
lsl2=pd.DataFrame(lsl1)
lsl2.to_excel("lsl.xlsx")

end = time.clock()
print('Running time: %s Seconds'%(end-start))









