#t63.py
# USAGE
# python find_screen.py --query queries/query_marowak.jpg
#
# import the necessary packages
#21/9/2015
#openCV blend
#http://www.bing.com/search?q=openCV+blend&src=IE-TopResult&FORM=IE11TR&conversationid=
#http://docs.opencv.org/doc/tutorials/core/adding_images/adding_images.html
#http://docs.opencv.org/modules/core/doc/operations_on_arrays.html?highlight=addweighted#void scaleAdd(InputArray src1, double alpha, InputArray src2, OutputArray dst)
#http://docs.opencv.org/modules/core/doc/operations_on_arrays.html?highlight=addweighted#void merge(const Mat* mv, size_t count, OutputArray dst)
#opencv convert to single channel
#http://www.bing.com/search?q=opencv+convert+to+single+channel&src=IE-TopResult&FORM=IE11TR&conversationid=
#http://www.stackoverflow.dluat.com/questions/15332163/opencv-convert-a-cv-8uc3-image-to-a-cv-32s1-image-in-c
#http://w3fstack.com/question/converting-to-single-channel-image-in-opencv/

#Usage:
# S:\Code\Python>r:\python27\python t63.py mix democritusBody-blue15.png democratius-12.png democratius-13_mask_black.png democritusBody-blue16.png
# S:\Code\Python>r:\python27\python t63.py mask democratius-16_edit2.png democratius-13_clean.png # democratius-13_mask_black2.png democritusBody-blue15.png
# t63.py: sys.argv: [1 = command, mix|mask] [2=background] [3=foreground] [4=mask] [5=output file]
# t63_2.py: sys.argv: [1 = command, mix|mask] [2=background] [3=foreground] [4=mask] [5=sum < ...] [6 = lineStart] [7 = lineEnd] [8=output file]
# if (sum < 520) ... --- adjust the level after which the image from the new source is used -- add a parameter or config or masks!
# mix, mixmask ...
# Used for "Democratius" painting - the mix of the pencil drawing with the colorized dollars, the blood and the blue background - however GIMP was also used for the finishing

from pyimagesearch import imutils
from skimage import exposure
import numpy as np
import argparse
import cv2
import sys

numArgs = 8

if (len(sys.argv)<numArgs):	print("\n\n8 parameters required!\n\nUsage: t63_2.py: sys.argv: [1 = command, mix|mask] [2=background] [3=foreground] [4=mask] [5=sum < ...] [6 = lineStart] [7 = lineEnd] [8=output file]\nmix: 200, 720, ...\nmask: 520, 720, ..."); exit(0)
command = sys.argv[1]
imageA = cv2.imread(sys.argv[2])
imageB = cv2.imread(sys.argv[3])
imageMask = cv2.imread(sys.argv[4]) 
maxSum = int(sys.argv[5])
lineStart = int(sys.argv[6])
lineEnd = int(sys.argv[7])
outputFile = sys.argv[8]
									#sys.argv[5] -- output, [6] = level (sum < [6])
									#A - back; B - white, mix
imageZ = imageA.copy()  			#output, prepare
a = 0; s = 0; c = []
level = "nowhite";

def mixmask():
	line = 0
	column = 0
	sum = (int) (0)
	for lines in imageMask:	
		column = 0
		if (line <  lineStart): #300):
								line = line + 1
								continue
		for c in lines:	
						sum = (int) (c[0]) + (int) (c[1]) + (int) (c[2])	#OK!
						if (sum < maxSum): #200):#720
										imageZ[line][column] = imageB[line][column];
						column = column + 1	
																
		line = line + 1
		if (line%500 == 0):
							print(line)
		if (line>lineEnd): #3099):
							break;
							
							

def mix():
	print('mix')
	line = 0
	column = 0
	sum = (int) (0)
	for lines in imageB:	
		column = 0
		if (line < lineStart): #350):
								line = line + 1
								continue
		for c in lines:	
							#if (s<20):
							#print(str(s) + ": "); print(columns); #print("===========")
							#print(str(c[0] + c[1] + c[2]), c[0], c[1], c[2])
							#sum = (int) (c[0]) + (int) (c[1]) + (int) (c[2])	#OK!
							#print(sum, c[0], c[1], c[2])
							sum = (int) (c[0]) + (int) (c[1]) + (int) (c[2])	#OK!
							if (sum < maxSum): #520):#720
											imageZ[line][column] = c
							column = column + 1							
		line = line + 1
		if (line%500 == 0):
							print(line)
		if (line> lineEnd): #3099):
							break;
							
							
def scan():
	s = 0
	for lines in imageB:
		for columns in lines:	
							#if (s<20):
							print(str(s) + ": "); print(columns); #print("===========")
							s = s + 1

if (command == 'mask'):
						mixmask()
if (command == 'mix'):
						mix()
#scan()
				
def linesScan():
	for v in imageB:
					#if (s<20):
					print(str(s) + ": "); print(v); #print("===========")
					s = s + 1
					#c = v[0] + v[1] + v[2]
					#if (c > 700):	
					#			level = "white"

print(level)				
				#if ((v[0] + v[1] + v[2]) < 740): imageZ[s] = v
cv2.imwrite(outputFile,  imageZ)

