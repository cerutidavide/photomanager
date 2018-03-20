#!/usr/bin/python -tt
import sys

def ConCat(filename1,filename2,filename3):
    f1=open(filename1, 'r')
    f2=open(filename2,'r')
    str1=f1.read()
    str2=f2.read() 
    f3=open(filename3, 'w+')
    f3.write(str1+str2)
    
def main():
    ConCat(sys.argv[1],sys.argv[2],sys.argv[3])
    

if __name__ == '__main__':
    main()