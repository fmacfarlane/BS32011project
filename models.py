'''Classes to represent our gene expression objects'''

import MySQLdb
class DBHandler():
	connection=None
	dbname='fmacfarlane'
	dbuser='fmacfarlane'
	dbpassword='SX8i3hAw'

	def __init__(self):
		if DBHandler.connection == None:
			DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
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
		self.gene_id=gene_id
		cursor.execute(sql,(gene_id,))
		#query database
				
		#get result and populate the class fields.

		result=cursor.fetchone()
		self.gene_title=result[0]
		self.gene_symbol=result[1]

		#now fetch the probes..

		probesql='select id_ref from probe where gene_id=%s'
		cursor.execute(probesql,(self.gene_id,))
		resultlist=cursor.fetchall()
		for result in resultlist:
			self.probelist.append(result[0])
		
	def get_expression(self, sample_id):
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_expression from expression where id_ref=%s and sample_id=%s'
		self.sample_id=sample_id
		exvals=[]
		for p in self.probelist:
			try:
				cursor.execute(sql,(p, sample_id))
				exvals.append(cursor.fetchone()[0])
			except Exception, e:
				raise Exception('Error occured retrieving expression data for id_ref %s and sample_id %s:%s'%(p,sample_id,e))
		return exvals

		 
#update and alter ,do at least two querys -TASk FOR NEXT WEEK !!!!!!!!
 

