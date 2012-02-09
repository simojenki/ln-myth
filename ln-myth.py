#!/usr/bin/env python

from optparse import OptionParser
import os
import os.path
import MySQLdb

parser = OptionParser()
parser.add_option("-u", "--user", action="store", dest="user")
parser.add_option("-p", "--password", action="store", dest="password")
parser.add_option("-d", "--destdir", action="store", dest="destdir")
parser.add_option("-r", "--recordingsdir", action="store", dest="recordingsdir")

(options, args) = parser.parse_args()

os.chdir(options.destdir)

db = MySQLdb.connect(host="localhost", port=3306, user=options.user, passwd=options.password, db="mythconverg")
cursor = db.cursor()
cursor.execute("select starttime, title, basename from recorded where basename like '%mpg' and storagegroup != 'LiveTV'")
recordings = [[recording[2], "%s %s.mpg" % (recording[0], recording[1])] for recording in cursor.fetchall()]
db.close

for toDelete in set(os.listdir(options.destdir)) - set([recording[1] for recording in recordings ]) :
	os.remove(toDelete)

for recording in recordings :
	mythRecording = os.path.join(options.recordingsdir, recording[0])
	if os.path.isfile(mythRecording):
		if not(os.path.isfile(recording[1])) : os.link(os.path.join(options.recordingsdir, recording[0]), recording[1]) 	
	else:
		print "Error %s, %s recording isn't actually on the disk!!" % (mythRecording, recording[1])
