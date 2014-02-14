#!/usr/local/bin/python
import models
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
print "Content-Type: text/html"
print
print "<html><head><TITLE>Project script output</TITLE></head>"
print "<body><H1>Form Values</H1>"
print "<form *action=project/models.py method=POST>"
print "<table><tr><td>enter query</td><td><imput type=text name=query /></td></tr>"
print "</table>"
print "</form>"
print "</body></html>"


form=cgi.FieldStorage()
cursor=db.cursor()
cursor.execute(form['query'])
