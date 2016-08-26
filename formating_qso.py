import csv
import sku_coor
f = open('QSO_Coor.csv', 'r+')
with open('coordenates_QSO.csv', 'rb') as ff:
    reader = csv.reader(ff)
    c=0
    s=""
    for row in reader:
	
        f.write(row[1])
	c=c+1
	if c==1:
		f.write(",");
		
	if c==2:
		f.write("\n");
		c=0
f = open('QSO_Coor_sky.csv', 'r+')
with open('QSO_Coor.csv', 'rb') as ff:
    reader = csv.reader(ff)

    for row in reader:
	ASC,DEC=sku_coor.skycoor(row[0],row[1])
	if (ASC!=0 and DEC!=0):
		f.write(str(ASC)+","+str(DEC)+"\n")
