#!/usr/local/bin/python
import cgi
import cgitb
import models
cgitb.enable()

form = cgi.FieldStorage()
print "Content-Type: text/html"
print
print "<html><head><title>Project script output</title></head>"
print "<body><h1>form values</h1>"
form=cgi.FieldStorage()
db=models.DBHandler()
cursor=db.cursor()
cursor.execute('select id_ref from probe where gene_id=%s',(form['query'],))

print form['query']
print "<form method=POST action=models.py>"
print "<table><tr><td>select id_ref from probe where gene_id=</td><td><imput type=text name=query /></td></tr>"
print "</table>"
print "</form>"
print "</body></html>"

