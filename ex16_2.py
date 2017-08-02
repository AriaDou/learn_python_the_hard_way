# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv
enter = "\n"

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

line = line1 + enter + line2 + enter + line3 + enter
target.write(line)

print "And finally, we close it."
target.close()
