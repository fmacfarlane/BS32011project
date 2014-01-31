SCRIPT FOR CREATING DATASET
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#make sure that script opens correct dataset
infile = 'GDS4477_full.soft'
#assign the function of opening file a variable
fh = open(infile)
#assign a variable that reads specific lines of the data
line = fh.readline()
while line[:20] != '!dataset_table_begin':
    line=fh.readline()

header= fh.readline().strip() #define the header as the line removing blank spaces

colnames={}#creating a dictionary for column names
#locates the column name
index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')
#assigning the correct fields for the correct tables
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']
#create a new row with the column headers
def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"
#add data from files to the  tables
def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
rows=0    
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
	rows=rows+1
    except:
	pass
genefile.close()
probefile.close()
expressionfile.close()
#print tables
print '%s rows processed'%rows
    
