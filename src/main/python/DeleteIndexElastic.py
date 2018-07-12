# Entry : path, host, port 
# 	  Path: path to the emplacement of file that contains the name of the index, the number of days and the format of the date



from elasticsearch import Elasticsearch
import sys
from datetime import date,timedelta

def setIndex(nameIndex,days,format):
        d = date.today()
        wd = d - timedelta(int(days))
        index =  nameIndex+"-"+wd.strftime(format)
	return index
def deleteIndex(index,host,port):
	es = Elasticsearch([{'host':host, 'port':port}])
	if es.indices.exists(index=index):
		es.indices.delete(index=index,ignore=[400,401])

file = open(sys.argv[1],"r")
host = sys.argv[2]
port = int(sys.argv[3])
for line in file:
       	l = line.split()
	index = setIndex(l(1),l(2),l(3))
	deleteIndex(index,host,port)			
