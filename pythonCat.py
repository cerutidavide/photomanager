#!/usr/bin/python -tt
import sys

def Cat(filename):
    f=open(filename,'r')
    for line in f:
        print line,
        righe=f.readlines()
        print righe
        
        f.close()
def main():
    Cat(sys.argv[1])
    

if __name__ == '__main__':
    main()