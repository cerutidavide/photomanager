'''
Created on Mar 9, 2018

@author: davideceruti
'''
import sys
def main():
    filename=sys.argv[1]
    f=open(filename,'r')
    hashtable={}
    for line in f:
        key=line.split('=')[0]
        value=line.split('=')[1]
        if key in hashtable.keys():
            hashtable[key]=hashtable[key].append(value)
        else:
            hashtable[key]=value        
    f.close()
    print hashtable
    
    
    
    
    
    
    
    
#     
#     myhash={} #hashtable di input
#     myhash2={} #hashtable di output
#     aList=[]
#     aList.append('/Volumes/TOSHIBAEXT/MASTERFoto/MasterFotoDisco///010.jpg')
#     myhash['4d9f980b35232a3f8762f4a800b2459c']=['/Volumes/TOSHIBAEXT/MASTERFoto/MasterFotoDisco///010.jpg']
#     myhash['a5866ca92bb05bbf9cfdecb2f092b278']=['/Volumes/TOSHIBAEXT/MASTERFoto/MasterFotoPhotos///MasterFotoPhotosOriginali/xyz.jpg','/Volumes/TOSHIBAEXT/MASTERFoto/MasterFotoDisco///xyz.jpg']
#     print myhash.keys()
#     print myhash.values()
#     print myhash.items()
#     if len(myhash['a5866ca92bb05bbf9cfdecb2f092b278']) > 1:
#         print 'da cancellare'
#         myhash2['a5866ca92bb05bbf9cfdecb2f092b278']=myhash['a5866ca92bb05bbf9cfdecb2f092b278'][0]
#     else:
#         print 'singolo'    
#     if len(myhash['4d9f980b35232a3f8762f4a800b2459c']) > 1:
#         print 'da cancellare'
#         myhash2['4d9f980b35232a3f8762f4a800b2459c']=myhash['4d9f980b35232a3f8762f4a800b2459c'][0]
#     else:
#         myhash2['4d9f980b35232a3f8762f4a800b2459c']=myhash['4d9f980b35232a3f8762f4a800b2459c'][0]
#         print 'singolo'    
#     print myhash2
# #non serve nemmeno la if perch comunque devi inserire nell hash solo il primo elemento
    pass
if __name__ == '__main__':
    main()
