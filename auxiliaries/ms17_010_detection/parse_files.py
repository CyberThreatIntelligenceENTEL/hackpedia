#!/usr/bin/python
import xml.etree.ElementTree as ET
import os, sys

if len(sys.argv) > 1:
	file = open(sys.argv[1])

	output = open(sys.argv[1].split('.')[0]+".csv",'w')
	output.write("IP; Estado; Puerto 445; Puerto 3389\n")
	
	tree = ET.parse(file)
	root = tree.getroot()

	for child in root:
		if child.tag == "host":
			ip = child.find("address").attrib['addr']
			for puerto in child.find("ports"):
				if puerto.attrib['portid'] == '445':
					p445 = puerto.find("state").attrib['state']
				#elif puerto.attrib['portid'] == '3389':
				#	p3389 = puerto.find("state").attrib['state']
			if child.find("hostscript") is not None:
				script = child.find("hostscript").find("script")
				if "VULNERABLE" in script.attrib['output']:
					status = "Vulnerable"
				else:
					status = "No Vulnerable"
			else:
				status = "No Vulnerable"
			output.write(";".join([ip,status, p445, 'Not Scanned'])+"\n")
output.close()
print "Done!"
				
