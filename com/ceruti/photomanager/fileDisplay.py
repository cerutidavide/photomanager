'''
Created on Mar 13, 2018

@author: davideceruti
'''
import sys
import os
import stat
import time




def main():
    pass
    print(sys.argv[1])
def fileDisplay(nomefile):
    print(os.stat(nomefile))    
def listFileNameMonthYear(listfname):
    print(stat.filemode(os.stat(listfname).st_mode))
    #ctime=time.ctime(os.stat(listfname).st_ctime)

    #ctime=os.stat(listfname).st_ctime
    print(time.ctime(os.stat(listfname).st_mtime).split()[1:5:3])


    pass

if __name__ == '__main__':
#    fileDisplay(sys.argv[1])
    listFileNameMonthYear(sys.argv[1])
    pass