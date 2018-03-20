#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -tt
import sys
import shutil
import os
import stat
from pathlib import Path
import time
import re


#
#   inserire il logging e ripulire i commenti e le procedure
#
# accetta in input un file con questo tracciato:
# find mypath -type f -exec md5 {} \;
def printFileDetails(filename):
    #    print 'Nome file:' + filename
    print (stat.filemode (os.stat (filename).st_mode))


# stat.filemode(mode

def loadHashFromFile(filename):
    f = open (filename , 'r' , encoding="utf-8")
    hashresult = {}
    alllines = f.readlines ()
    rownumber = 0
    keynumber = 0
    for row in alllines:
        key = row.split ()[3]
        if key in hashresult.keys ():
            hashresult[key].append (row.split ()[1][1:-1])
        else:
            hashresult[key] = row.split ()[1][1:-1].split ()
            keynumber = keynumber + 1
        rownumber = rownumber + 1
    f.close ()
    print ('Il numero delle linee lette è ' + str (rownumber))
    print ('Il numero dei file univoci è ' + str (keynumber))
    return hashresult
    pass


def printHashKeysAndValuesFormatted(hashtable):
    for key in hashtable.keys ():
        print (key + "||" + '||'.join (hashtable[key]))
    print ('Hashtable contiene in totale ' + str (countHashValueItemsTotal (hashtable)) + ' oggetti')
    print ('Hashtable raggruppa tali oggetti in ' + str (len (hashtable)) + ' liste ')
    pass


def countHashValueItemsTotal(hashtable):
    itemnumber = 0
    for key in hashtable.keys ():
        itemnumber = itemnumber + len (hashtable[key])
        #        print('>>>>>>>>'+str(hashtable[key]))
        pass
    return itemnumber
    pass


########retrieveUniqFileHash(hashtable,destinationPath,preferredPathSubstr)##
####hashtable################################################################
######## è un hash costruito con loadHashFromFile(filename) dove il file ####
######## filename ha questa struttura: ######################################
######## MD5 (/albero/sottoalbero/nomefile) = MD5code #######################
######## ad esempio ottenibile con find path -type f -exec md5 {} \; ########
####destinationPath##########################################################
######## è il percorso su cui si vuole creare l'alberatura di cartelle e 
######## file
######## contenente solo i file non duplicati
####preferredPathSubstr#################
######## è il path da cui preferibilmente si vogliono copiare i file 
######## nel caso di file duplicati in percorsi origine differenti     
def retrieveUniqFileHash(hashtable , preferredPathSubstr):
    hashresult = {}
    strfield = ''
    for key in hashtable.keys ():
        if len (hashtable[key]) == 1:
            hashresult[key] = hashtable[key]
        else:
            for strfield in hashtable[key]:
                if strfield.find (preferredPathSubstr) > -1:
                    hashresult[key] = strfield.split ()
                else:
                    if key in hashresult:
                        pass
                    else:
                        hashresult[key] = strfield.split ()
                    pass
            pass
    return hashresult
    pass


# ATTENZIONE check is_absolute()  Path.chmod(mode)¶ Path.is_dir()¶
def copyUniqFileToFolder(hashtable , destinationPath):
    p = Path (destinationPath)
    if p.exists () and p.is_dir ():
        #       print(destinationPath+' esiste')
        giro = 0
        for key in hashtable.keys ():
            giro = giro + 1
            #           print('>>>>'+str(giro))
            f = Path (hashtable[key][0])
            print (str (f))
            if f.exists () and f.is_file ():
                print (time.ctime (os.stat (f).st_mtime).split ()[1:5:3])
                d1 = Path (destinationPath + '/' + time.ctime (os.stat (f).st_mtime).split ()[1:5:3][1] + '/')
                # print(d1)
                d1.mkdir (exist_ok=True)
                if d1.exists () and d1.is_dir ():
                    d2 = Path (destinationPath + '/' + time.ctime (os.stat (f).st_mtime).split ()[1:5:3][1] + '/' +
                               time.ctime (os.stat (f).st_mtime).split ()[1:5:3][0] + '/')
                    print (d2)
                    d2.mkdir (exist_ok=True)
                    if d2.exists () and d2.is_dir ():

                        # print('>>>>>>>>'+hashtable[key][0])
                        ext = ''
                        m = re.search ('\..*$' , hashtable[key][0])
                        if m:
                            ext = ext + m.group ().lower ()
                            print ('estensione: ' + ext)
                        d = p.joinpath (d1).joinpath (d2).joinpath (key + ext)
                        print ('>>>>>NOME FILE DA COPIARE>>>>>' + str (d))
                        if d.exists ():
                            print ('GIA COPIATO IN PRECEDENZA')
                            pass
                        else:
                            dst = shutil.copy2 (f , d)
                            if Path (dst).exists ():
                                print ('Il file ' + str (dst) + " è stato copiato correttamente")
                            else:
                                print ('Errore nella creazione del file')
                    else:
                        print ('Errore nella creazione della sottodirectory' + str (d2))
                else:
                    print ('Errore nella creazione della sottodirectory' + str (d1))
            else:
                print ('Errore il file non esiste o non è accessibile' + str (f))
    else:
        print ('errore il percorso di destinazione non esiste o non accessibile' + str (p))


def main():
    # inserire controlli sui parametri di ingresso

    myhash = loadHashFromFile (sys.argv[1])
    myreducedhash = retrieveUniqFileHash (myhash , sys.argv[3])
    copyUniqFileToFolder (myreducedhash , sys.argv[2])


#   printHashKeysAndValuesFormatted(myhash)
#   myhashresult=copyUniqFileToFolder(myhash,'/tmp','Photos')
#   printHashKeysAndValuesFormatted(myhashresult)
if __name__ == '__main__':
    main ()
