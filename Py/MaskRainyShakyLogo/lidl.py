# -*- coding: utf-8 -*-
import cv2
import os
import sys
import numpy as np
import math
#import copy
#import navigate
#import convert2
''' 
PURPOSE: Automatically remove a logo in shaky, rainy, noisy video and preserve the raindrops crossing the logo
ЦЕЛ: Автоматично премахване на лого в нестабилно, дъждовно и шумно видео, като се запазят дъждовните капки пред логото.

* Video filmed with shaking camera and big zoom, noisy image, during heavy rain with clearly visible raindrops - devise a simple way for automatically deleting an annoying supermarket logo which should be unnoticeable by the viewers of the video (at least at first view), while preserving the raindrops which pass through the logo area. Test: one test viewer didn't notice there was an effect.

-- Used in the episode "A Dream During a Summer Rain" from "The Wild Plovdiv" series. 

http://eim.twenkid.com/div.html#11
https://youtu.be/TWRIotZSbqE?t=147

* Видео с голямо увеличение, заснето с нестабилна камера от ръка, с шумна картина в пороен дъжд, при което се виждат отделните капки. По хитър прост начин автоматично да се заличи нежелано лого на верига магазини (постоянно пресичано от капките дъжд), като ефектът да не изглежда неестествено, поне на зрителите на първо гледане, докато е във видео - трябва да се запазят дъждовните капки.

-- Използван в епизода "Сън в летен дъжд" от поредицата "Дивия Пловдив".

Coded: 28.11.2019 - 29.11.2019 in Plovdiv, Bulgaria

''' 

'''
MIT License

Copyright 2020, Todor "Tosh" Arnaudov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

'''
Part of Python-part of Twenkid FX Studio ("inhouse" experimental prototype).
It inherits code and ideas from some of the effects in "Star Symphony in Chepelare" (2018)

Част от питонската част на "Twenkid FX Studio". Наследява код и идеи от ефекти за автоматичен рисуващ ретуш, използвани в "Звездна симфония в Чепеларе" (2018), няколко кадъра от "екшън" частта.

Disclaimer: This is not an advertising, just that annoying logo was in a sequence which I wanted to use in my video and I had to remove it.

Внимание: Това не е реклама на въпросната верига магазини, просто исках да използвам кадъра заради останалата част от него, логото ми го разваляше и трябваше да го премахна някакси.

За "контрареклама": ASDA, Мазда, Трабант, Слънчеви лъчи, Wallmart, Т-Маркет, Carfour, Триумф, Ролс Ройс, Пени маркет, Мени дзаржляб, Събота пазара, Четвъртък пазара, Женския пазар, Руския пазар, Форума в Тракия, Декатлон, РУМ универмаг "Молдавия", РУМ "Евмолпия" и т.н. 

'''

#Author: (C) Todor "Tosh" Arnaudov, http://twenkid.com 
#License: MIT
#fix_lidl.py 28-11-2019 - 29.11.2019 + comments 10.9.2020, 15.9.2020
#D:\Py\pyimage\CV5_USB\scan.py
#D:\Py\pyimage\CV5_USB\lidl.py

'''Direction: Selectively alter the colors inside a region of interest (the logo). Since the camera is unstable, that region would move a bit. It may be located by some CV methods, or you can direct it manually or semi-automatic (approximately) experimentally. It is important when there are similarly coloured areas in the image and altering the colors there may "damage" adjacent areas which shouldn't be changed.

Насоки: Избирателна промяна на цветовете в рамките на дадена целева област (логото). Тъй като камерата не е устойчива, регионът се премества от кадър в кадър. Може да се локализира чрез методи от компютърното зрение, или да го насочвате ръчно или полу-автоматично по експериментален начин. Областта е важна, когато в изображението има и други области с подобни цветове като логото.

'''


def FixLidl(path=None, pathOut=None): #Esc-9, #28-11-2019_A
   #13840, 13955
   #553, 317, 93, 46     
   frSt = 0; frEnd = 4405 #13955 //Frame Range
   x1,y1 = (590,619)  #Approximate Region of Interest (ROI) box, top-left
   w11x = 10
   #maxx1 = x1+w11x
   w,h = 330, 256 #270 #317 #Width, Height
   x2, y2 = (x1+w,y1+h) #Bottom-right
    
   #cv2.rectangle(frame,(x1,y1),(x2, y2),color,1) #Debug Display
   
   #paths = []
   #paths.append( r"P:\Video\Star_Symphony_57_27_14-10-2018_xvidc1_-1673203093.avi")
   #4591
   
   #Frame range to process   
   frProcessStart = 0 #4591+150 #4785 #4591 + 155
   frProcessEnd = frEnd
   
   #If no Explicit path was give, use the default
   if (path==None):
     path = r"E:\dujd_lidl_244MTS_18-84.mp4" 
     path = r"e:\00244_lidl_rain_14.0_R25.mp4"
     #path = r"E:\lidl\00244_lidl_rain_14.0_r50qscale_2.avi_537462455.avi"
     #path = r"P:\Arnaud\1309\00182.MTS_8201.avi" 
   #path = r"P:\Video\Star_Symphony_57_27_14-10-2018_xvidc1_-1673203093.avi"  
   print(path)   
   cap = cv2.VideoCapture(path)   
   cap.set(cv2.CAP_PROP_POS_FRAMES, frSt)
   cur = frSt
   color = (0,255,0) #of the ROI box
   #13911   
   if (pathOut==None): videoOutPath = "fixed_logo" #curr.dir #E:\\lidl.mp4
   else: videoOutPath = pathOut
   
   size = (1920,1080)
   fourcc = cv2.VideoWriter_fourcc(*'FFV1');
   #with avi and less lossy compression - the video will be used as a clip in editing
   
   #fourcc = cv2.VideoWriter_fourcc(*'mp4v');
   #fourcc = cv2.VideoWriter_fourcc(*'xvid');
   #ext = ".mp4"   
   ext = ".avi"
   videoOutPath+=ext
   videoOut = cv2.VideoWriter(videoOutPath, fourcc, 50.0, size);
   #bRect = True #False #True #False
   iBoldSegment = 1 # 2
 
   stx =4; sty=1 #.4
   fy1 = y1
   
   bRoi = False #True
   #bRect = False
   bRect = True #show region
   
   imgPath="E:\\"
   counter = 0
   bProcess = True #     False
   
   mapr = []
   #for i in range(0,255):
   # mapr.append()
   #Should adjust current frame ... 
   
   x10 = x1; y10 = y1;
   x1_left = [] #Left-side of the region of interest - camera is moving
   bVideoSave = False #turn on at the end
   while (cur<frEnd):
     #y1 = int(fy1)
     
     x1 = x10; y1 = y10; #scan from the initial beginning - drift      
     ret, frame = cap.read();          
     changed = []
     if not ret:
       videoOut.release()
       print("End of video")
       return
       
     if (ret and cur>=frProcessStart and cur < frProcessEnd): 
     
       if (bRoi):
         x11,y11,w11,h11 = cv2.selectROI("Out", frame)
         if (x11!=None):
           x1 = x11; y1 = y11; x2=x1+w11; y2=y1+h11; bProcess=True
         else: bProcess = False
       
       br = 0
       y = y1; xs = x1; q = False #break the top cycle  
       for y in range(y1,y1+200,10):
         #for x in range(x1, x2):
         if q: break
         for x in range(x1,x1+w11x):
          p = frame[y,x]
          r = p[2]  #BGR --> red channel
          if (r<150):
            #xs+= x; br+=1; break
            #xs = max(xs, x); q = True; break
            xs = min(xs, x); q = True; break
       
       x1 = xs - 1  #shifting approximately 1 px left per frame (estimated experimentally)
       x1_left.append(x1)
       
       if (cur==88): x1 = x1_left[87]
       elif (cur==85): x1 = x1_left[84]   
       elif (cur==81): x1 = x1_left[80]
       
       #if bRect: cv2.rectangle(frame,(x1,y1),(x2, y2),color,1)  #Debug
       if (bProcess):
           print("PROCESS?")
           for x in range(x1, x2):
             for y in range(y1,y2): 
               #try:
               p = frame[y,x]
               
               #except:
                 #print(y,x)
               #if (p[0]<33) and (p[2]<16) and p[1]<24 and p[0]>10 and p[1]>10 and p[2]>10: frame[y,x] = [0, 0, 255]
               
               #if (p[0]<41) and (p[2]<38) and p[1]<36 and p[0]>3 and p[1]>3 and p[2]>3:  
               #[0] = b, [1] = g, [2] = r
               b = p[0]; g = p[1]; r = p[2]
               red = (r>(b+5)) and (r>g)  #"reddish" tint
               
               
               if red or ((b<135) and (g>b) and (r>100) and (r<230)): #more greenish than blueish, red in certain range
                 #br = r+g+b     
                 #b = (int)(0.37*br)                 
                 #g = (int)(0.31*br)
                 #r = (int)(0.32*br)
                 #b+=np.random.randint(10,16) #15
                 b=min(b+np.random.randint(7,11), 255) #15  #Change the actual color with slightly randomized colors (small range of fluctuation) to fill the region and let it be more "natural" (not uniform)
                 r = b-np.random.randint(0,7)
                 g = b-np.random.randint(8,10)
                 #if (b-r) < 10: r-=np.random.randint(10,15)
                 #if (b-g) < 10: r-=np.random.randint(10,15)             
                 #b+=min(b+np.random.randint(40,45), 255)
                 #g+=np.random.randint(35,40)
                 #r+=np.random.randint(30,40)

               if b<100: # and b>r and b-r<10:  #If not bluish tint
                 b+=np.random.randint(7,14) 
                 r = b+np.random.randint(-3,3)   
                 g = r+np.random.randint(-9,-3)   
                 if (b>90) and g<100: g=min(100,g+np.random.randint(8,15)) #max
                 
                 #r-=np.random.randint(8,12)   
                 #b+=np.random.randint(10,15)             
               if r>70 and r<100:   #Particular red range
                 r = b-np.random.randint(-3,3)    #-4,6
                 g = b-np.random.randint(4,10)#-3,3
               if g<100: g=min(92,g+np.random.randint(5,15))
               if g>r : g = r - np.random.randint(2,4)  #If still more Green than Red - desaturate the Green 
               if g>b : g = b - np.random.randint(1,3)  #If still Green more than Blue - desaturate the Green more
               if (b<90): df = 90-b; r+=np.random.randint(15,25); g+=np.random.randint(15,25); b+=np.random.randint(25,30) #if blue below a threshold, alter the G and B within a random range
               frame[y,x] = [b, g, r] #Paint back

     
     if (bVideoSave): videoOut.write(frame)     
     cv2.imwrite(imgPath+str(counter)+".png", frame)
     #cv2.imwrite(imgPath+str(counter)+".jpg", frame)
     if bRect: cv2.rectangle(frame,(x1,y1),(x2, y2),color,1) 
     cv2.imshow("Lidl", frame)
     
     k = cv2.waitKey(1) & 0xff     
     if (k==27):
       videoOut.release()
       return
     cur+=1
     counter+=1
     print(str(cur)+", ")# end="")  
    
if __name__ == "__main__": FixLidl()
