import xml
handle = open("xml_input.xml","r")
content = handle.read()
# print(content)

d= xml.parsers(content)
print(d['Result']['RequestCode'])
d['Result']['RequestCode']=4
print(d)

x= xml.unparse(d)
print(x)



