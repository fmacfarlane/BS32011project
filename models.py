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
class Probe():
	id_ref=''
	gene_id=''
	probelist=[]
	
	def __init__(self,id_ref):
		db=DBHandler()
		cursor=db.cursor()
		probesql='select gene_id from probe where id_ref=%s'
		cursor.execute(probesql,(id_ref))
		result=cursor.fetchone()
		self.gene_id=result[0]
		#fill in the blanks
		
class Expression():
	id_ref=''
	gene_expression=''
	sample_id=''
	probelist=[]

	def __init__(self,id_ref):
		db=DBHandler()
		cursor=db.cursor()
		expsql='select gene_expression, sample_id from expression where id_ref=%s'
		cursor.execute(expsql,(id_ref))
		result=cursor.fetchone()
		self.gene_expression=result[0]
		self.sample_id=result[1]

class Sample():
	experiment_id=''
	source=''
	probelist=[]

	def __init__(self,experiment_id):
		db=DBHandler()
		cursor=db.cursor()
		samplesql='select source from sample where experiment_id=%s'
		cursor.execute(samplesql,(experiment_id))
		result=cursor.fetchone()
		self.source=result[0]


		for result in cursor.fetchall():
			self.probelist.append(result[0])
		print ( gene_title, gene_symbol, gene_id, id_ref)		
#	def get_expression(self,experiment):
		 
#update and alter ,do at least two querys -TASK FOR THIS WEEK 
