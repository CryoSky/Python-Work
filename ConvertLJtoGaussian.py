#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This script will help convert LJ interaction to Gaussian type 6
# This is for a Calpha version, so A has been sent as 0.1;
# Written by Shikai Jin, 10/20/2017

import os
import re
import math
import shutil

# First back up original file
def copyfile(fname):
    fnew = fname + '_old'
    shutil.copyfile(fname, fnew)
    print('File name is %s and I have copied it to %s' % (fname , fnew))


# Open the file, output the pairs part, copy the corresponding data to temporary.txt
def data_output(fname):
    try:
        fobj = open(fname,'r')  # Here, r means read only. Do not use os.open or the compiler will report an error
        # return fobj # be cautious about function return, once return, following code will not be executed
    except IOError:
        print('File open error')  # Python handling exception
    ftemp = open("temporary.txt", 'w+')
    flag = 0  # Use this flag to judge whether this line should be copied
    a = fobj.readlines()
    #    for i in range (0,200,2):
    #       print(a[i])  # Check the file by each lines
    for lines in a:
        #    print(flag) # Check whether flag is correct
        if str(re.search(r'\[\sbonds\s\]', str(lines))) != 'None':
            flag = 0
        elif str(re.search(r'\[\spairs\s\]', str(lines))) != 'None':
            flag = 1
        if flag == 1:
            ftemp.write(lines)
    fobj.close()
    ftemp.close()


# Open a new temporary2.txt file to convert LJ to Gaussian data
def data_analysis():
    ftemp1 = open("temporary.txt", 'r')
    ftemp2 = open("temporary2.txt", 'w+')
    a = ftemp1.readlines()
    ftemp2.write(a[0])
    ftemp2.write('; i j type A mu sigma and exvol\n')

    for lines in range(2,len(a)-1):
        predata = a[lines].split( )
        print(predata)  # Check whether data is corrected
        mu = math.pow(float(predata[4])*2 / float(predata[3]), 1/6)
#        A = float(predata[4]) / math.pow(mu , 12)
        sigma = mu * 0.2 / math.pow(2 * math.log(2), 1/2)
        Avalue = 1.0
        exvol = math.pow(0.25, 12)
#        print("%.9E" % sigma)  # Check formatting
        ftemp2.write("%6d"% int(predata[0])+"%7d"% int(predata[1])+"%2d" % 6+'   '+ str(Avalue)+'   '+'%.9E' % mu+'   '+"%.9E" % sigma+'   '+"%.9E" % exvol+'\n')  # Use formatting symbol% to convert to Scientific notation
#        ftemp2.write()
    ftemp1.close()
    ftemp2.close()


# Open a new result.txt file to get result
def data_input(fname):
    ftemp2 = open("temporary2.txt", 'r')
    ftemp2.seek(0,0)
    fori = open(fname, 'a+')
    fori.seek(0,0)
    temp2cont = ftemp2.readlines()
    print(len(temp2cont))
    temp2flag = 0
    oriflag = 0
    a = fori.readlines()
    
    fout = open("result.txt","w")
    for lines in a:
        print(oriflag) # Check whether flag is correct
        if str(re.search(r'\[\sbonds\s\]', str(lines))) != 'None':
            oriflag = 0
        if str(re.search(r'\[\spairs\s\]', str(lines))) != 'None':
            oriflag = 1
        if temp2flag == len(temp2cont):
            fout.write('\n')
            temp2flag = 0
            continue
        if oriflag == 1:
            lines = temp2cont[temp2flag]
            print(temp2cont[temp2flag])
            print(temp2flag)
            temp2flag += 1
        fout.write(lines)
    fori.close()
    ftemp2.close()
    fout.close()

    
# Replace result.txt to original file    
def file_replace(fname):
    os.remove(fname)
    os.rename('result.txt', fname)

def main():
#    fname = "TopStructure.txt"
    fname = input('Enter your top filename with suffix:')
    copyfile(fname)
    data_output(fname)
    data_analysis()
    data_input(fname)
    file_replace(fname)


if __name__== '__main__':
    main()
