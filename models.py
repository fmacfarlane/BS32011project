'''Classes to represent our gene expression objects'''
#first of all we must create a connection to the mysql database and a cursor to us within python
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
#We then create a class that can be used to query the database
class Gene():
	gene_title=''
	gene_symbol=''
	gene_id=''
	probelist=[]
#We also input an sql query to run on the dataset
	def __init__(self,gene_id):
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_title, gene_symbol, gene_id from gene where gene_id=%s'
		self.gene_id=gene_id
		cursor.execute(sql,(gene_id,))
		#query database
				
		#get result and populate the class fields, fetchone collects a single response to the query

		result=cursor.fetchone()
		self.gene_title=result[0]
		self.gene_symbol=result[1]

		#now fetch the probes, we create another query to run and create a result list using the fetchall command, therefore all of the results will be collected

		probesql='select id_ref from probe where gene_id=%s'
		cursor.execute(probesql,(self.gene_id,))
		resultlist=cursor.fetchall()
		for result in resultlist:
			self.probelist.append(result[0])
#we define another item to get the gene expression, using another query and settin the sample id as another modifiable variable.
	def get_expression(self, sample_id):
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_expression, from expression where id_ref=%s and sample_id=%s'
		self.sample_id=sample_id
		exvals=[]
#We create an exception to indicate when the script does not run due to error
		for p in self.probelist:
			try:
				cursor.execute(sql,(p, sample_id))
				exvals.append(cursor.fetchone()[0])
			except Exception, e:
				raise Exception('Error occured retrieving expression data for id_ref %s and sample_id %s:%s'%(p,sample_id,e))
		return exvals
# get average allows us to see the average expression of a particular gene for all samples, therefore we can compare if a sample has high/low expression compared to others
	def get_average(self, gene_id):
		db=DBHandler()
		cursor=db.cursor()
		sql='select sum(gene_expression)/count(gene_expression) as average, g.gene_symbol, e.sample_id from expression e inner join probe p on e.id_ref=p.id_ref inner join gene g on g.gene_id=p.gene_id inner join sample s on s.experiment_id=e.sample_id where g.gene_id=%s'
		self.gene_id=gene_id
		cursor.execute(sql,(gene_id,))
		resultlist=cursor.fetchall()
		for result in resultlist:
			self.probelist.append(result[0])
			
		return resultlist
# the return command allows the data to be visualised and printed on screen
		

