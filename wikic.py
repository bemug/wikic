#!/usr/bin/env python
import sys, getopt, pydoc
import urllib2
from HTMLParser import HTMLParser

content_id = "id=\"mw-content-text\""
end_content_id = "id=\"bandeau-portail\""

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def usage():
	print "wikic <page title>"

def main():
	print sys.argv

	if len(sys.argv) != 2:
		usage()
		sys.exit(2)
	
	#Format the arg for the wiki url
	topic = sys.argv[1].replace(' ', '_')

	#Download the wiki page
	downloaded_data  = urllib2.urlopen('http://fr.wikipedia.org/wiki/' + topic)

	buf = ""
	line = downloaded_data.readline()
	while line.find(content_id) == -1:
		line = downloaded_data.readline()
	
	while line.find(end_content_id) == -1:
		buf += strip_tags(line)
		line = downloaded_data.readline()


	#Use the "less" style for display
	pydoc.pager(buf)

if __name__ == "__main__":
    main()
