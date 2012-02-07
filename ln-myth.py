#!/usr/bin/env python

from optparse import OptionParser
import os
import MySQLdb

parser = OptionParser()
parser.add_option("-u", "--user", action="store", dest="user")
parser.add_option("-p", "--password", action="store", dest="password")
parser.add_option("-d", "--destdir", action="store", dest="destdir")

(options, args) = parser.parse_args()

db = MySQLdb.connect(host="localhost", port=3306, user=options.user, passwd=options.password, db="mythconverg")
cursor = db.cursor()
cursor.execute("select starttime, title, basename from recorded where basename like '%mpg'")
recordings = [[recording[2], "%s %s.mpg" % (recording[0], recording[1])] for recording in cursor.fetchall()]
db.close

for filename in recordings :
	print filename

existingLns = set(os.listdir(options.destdir))
for fname in existingLns:
    print fname

#select starttime, title, basename from recorded;
