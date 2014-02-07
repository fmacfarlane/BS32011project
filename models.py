'''Classes to represent our gene expression objects'''

import MySQLdb
class DBHandler():
	connection=None
	dbname='fmacfarlane'
	dbuser='fmacfarlane'
	dbpassword='SX8i3hAw'

	def __init__(self):
		if DBHandler.connection == None:
			DBHandler.connection == MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
	def cursor(self):
			return DBHandler.connection.cursor()

class Gene():
	gene_title=''
	gene_symbol=''
	gene_id=''
	probelist=[]

	def __init__(self,gene_id):
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_title, gene_symbol, gene_id from gene where gene_id=%s'
		cursor.execute(sql,(gene_id,))
		#query database
		#get result and populate the class fields.
		result=cursor.fetchone()
		self.gene_title =result[0]
		self.gene_symbol=result[1]
		#now fetch the probes..
		probesql='select id_ref from probe where gene_id=%s'
		cursor.execute(probesql,(gene_id))
		result=cursor.fetchone()
		self.id_ref=result[0]
		#fill in the blanks
		

		for result in cursor.fetchall():
			self.probelist.append(result[0])
		print ( gene_title, gene_symbol, gene_id, id_ref)		
#	def get_expression(self,experiment):
		 
#update and alter ,do at least two querys -TASK FOR THIS WEEK 
