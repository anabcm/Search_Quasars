import numpy as np
import csv
import mysql.connector
from math import sqrt,pow
import matplotlib.pylab as plt
def numero_pulsar():
    cnx = mysql.connector.connect(user="root", password="06140571",
                                      host="127.0.0.1",
                                      database="CHASE")
    cursor=cnx.cursor(buffered=True) 
    
    cursoraux=cnx.cursor(buffered=True) 
    query="select table_name from information_schema.tables where table_name like \'%ref_star\';";
    print query
    cursor.execute(query)
    num_ref=0
    num_pulsars=0
    num_quasars=0
    for table in cursor:
	print table[0]
        query="select * from "+table[0]
        cursoraux.execute(query)
        for row in cursoraux:
            num_ref=num_ref+1
            #if exist_p(row[0],row[1]):
            #    num_pulsars=num_pulsar+1
	    if exist_quasar(row[0],row[1]):
                num_quasars=num_quasars+1
                
    #print "total de estrellas ",num_ref
    #print "total de pulsars ",num_pulsars
    #print "porcentaje de pulsares ",num_pulsars*100/num_ref
    print "total de quasars ",num_quasars
    print "porcentaje de quasars ",num_quasars*100/num_ref
    
def exist_p(a,b):
    with open('QSO_Coor_sky.csv', 'rb') as ff:
        reader = csv.reader(ff)
        ans=False
        for row in reader:
            if (float(row[0])==float(a) and float(row[1])==float(b)):
                ans=True
    return  ans
def exist_quasar(a,b):
    with open('milliquas.csv', 'rb') as ff:
        reader = csv.reader(ff)
        ans=False
        for row in reader:
            if (float(row[0])==float(a) and float(row[1])==float(b)):
                ans=True
		break
    return  ans
numero_pulsar()
