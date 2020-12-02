from xml.dom import minidom 
import os  
import xml.etree.ElementTree as et  
import re

f = open("./input/data_text.txt", "r", encoding='utf-8')
file_contents = f.read()

file_contents = re.sub(r'[^a-zA-Z0-9\s.]','', file_contents)
# print(file_contents) 

file_contents = file_contents.strip("\n")

lines = file_contents.split(".")
lines = [line.strip("\n") for line in lines if line.strip() != '']

# print(lines)

num_lines = len(lines)

# writing to xml
root = minidom.Document() 
  
xml = root.createElement('root')  
root.appendChild(xml) 

root = et.Element("myroot")
for i in range(0,num_lines-2):
    m1 = et.Element("item")
    root.append (m1)
    p = et.SubElement(m1, "p")
    p.text = lines[i]
    a1 = et.SubElement(m1, "a1")
    a1.text = lines[i+1]
    a2 = et.SubElement(m1, "a2") 
    a2.text = lines[i+2]

tree = et.ElementTree(root) 

fileName = "intermediate_files/generated_xml.xml"    
with open (fileName, "wb") as files : 
    tree.write(files) 

# xml_str = root.toprettyxml(indent ="\t")  
# save_path_file = "generated_xml.xml"
# with open(save_path_file, "w") as f: 
#     f.write(xml_str)  


