'''Classes to represent our gene expression objects'''

import MySQLdb
class DBHandler():
	connection=None
	dbname='fmacfarlane'
	dbuser='fmacfarlane'
	dbpassword='SX8i3hAw'

	def __init__(self):
		if DBHandler.connection == None:
			DBHandler.connection == MySQLdb.connect(db=DBHandler.dbname, \ user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

	def cursor(self):
			return DBHandler.connection.cursor()

class Gene():
	gene_title=''
	gene_symbol=''
	gene_id=''
	probelist=[]

	def __init__(self,geneid):
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_title, gene_symbol, gene_id from gene where gene_id=%s'
		cursor.execute9sql,(geneid,))
		#query database
		#get result and populate the class fields.
		result=cursor.fetchone()
		self.gene_title =result[0]
		self.gene_symnol=result[1]
		#now fetch the probes..
		probesql='select id-ref from probe where gene_id=%s'
		#fill in the blanks
		

		for result in cursor.fetchall():
			self.probelist.append(result[0])

	def get_expression(self,experiment):
#update and alter ,do at least two querys -TASK FOR THIS WEEK 
