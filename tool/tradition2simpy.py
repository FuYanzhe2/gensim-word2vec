# -*- coding: utf-8 -*
from langconv import *  
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def simple2tradition(line):  
    #to tradition
    line = Converter('zh-hant').convert(line.decode('utf-8'))  
    line = line.encode('utf-8')  
    return line  
  
def tradition2simple(line):  
    # to simple  
    line = Converter('zh-hans').convert(line.decode('utf-8'))  
    line = line.encode('utf-8')  
    return line  
	
data_file=open("chat.txt","r")
output_flie=open("chat2simple.txt","w")

for line in data_file.readlines():
		line=tradition2simple(line)
		output_flie.write(line.encode("utf-8"))

output_flie.close()
