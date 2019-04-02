from lxml import etree
import lxml.html

# PART 1 validating 
dtd_file = open("map1.dtd")
xml1 = open("map1.xml").read() 
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)
print(dtd.validate(root))

# PART 2 printing the elements
root = etree.XML(xml1)		# Where xml1 is XML text
print (root.tag)			# "map"
print (root[0].tag)			# "polygon"
print (root[0].get("id"))		# "p1"
print (root[1].tag)			# "polygon"
print (root[1].get("id"))		# "p2"
print (root[0][0].tag)		# "points"
print (root[0][0].text)		# "100,100 200,100" etc.
print (root[1][0].tag)		# "points2"
print (root[1][0].text)		# 

# PART 3 appending new polygon
#root = etree.XML(xml1)					# Could start from nothing
#p2 = etree.Element("polygon")				# Create polygon
#p2.set("id", "p2");					# Set attribute
#p2.append(etree.Element("points"))			# Append points
#p2[0].text = "120,150 150,250 200,200 100,000 100,100"	# Set points text
#root.append(p2)						# Append polygon
#print (root[1].tag)					# Check

# Producing the xml3
#out = etree.tostring(root, pretty_print=True)
#print(out)
#writer = open('xml3.xml', 'wb')		# Open for binary write
#writer.write(out)
#writer.close()

# printing the HTML
xslt_doc = etree.parse("map3.xsl")
xslt_transformer = etree.XSLT(xslt_doc)

source_doc = etree.parse("xml3_ours.xml")
output_doc = xslt_transformer(source_doc)
 
print(str(output_doc))
output_doc.write("output-toc.html", pretty_print=True)


