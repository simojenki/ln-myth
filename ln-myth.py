#!/usr/bin/env python

from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-u", "--user", action="store", dest="user")
parser.add_option("-p", "--password", action="store", dest="password")
parser.add_option("-d", "--destdir", action="store", dest="destdir")

(options, args) = parser.parse_args()

user = options.user 
password = options.password

existingLns = set(os.listdir(options.destdir))
for fname in existingLns:
    print fname

#select starttime, title, basename from recorded;
