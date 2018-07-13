# Entry : path, host, port 
# 	  Path: path to the emplacement of file that contains the name of the index, the number of days and the format of the date


import csv 
from elasticsearch import Elasticsearch
import sys
from datetime import date,timedelta

def setIndex(nameIndex,days,f):
        d = date.today()
        wd = d - timedelta(int(days))
        index =  nameIndex+"-"+wd.strftime(f)
	return index
def deleteIndex(index,host,port):
	es = Elasticsearch([{'host':host, 'port':port}])
	if es.indices.exists(index=index):
		es.indices.delete(index=index,ignore=[400,401])

#file = open(sys.argv[1],"r")
host = sys.argv[2]
port = int(sys.argv[3])

with open(sys.argv[1]) as cvsfile:
	reader = csv.DictReader(csvfile)
	for row in reader
		index = setIndex(row['name'],row['days'],row['format'])
		deleteIndex(index,host,port)

#for line in file:
#      	name,days,f = line.split(",")
#	index = setIndex(name,days,f)
#	deleteIndex(index,host,port)			
