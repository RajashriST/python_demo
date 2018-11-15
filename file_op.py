#file operations
import os
print
fo=open(r'D:\rt00444029\TECHM\file_1.txt','r+')
print(fo.readline())
print(fo.readlines())



#print all .html files
for r,d,f in os.walk(r'D:\rt00444029\TECHM'):
	       for fl in f:
		       if '.html' in fl: print(os.path.join(r,fl))
