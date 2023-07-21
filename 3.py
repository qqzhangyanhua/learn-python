from lxml import etree

# parser = etree.HTMLParser(encoding='utf-8')
# selector = etree.parse('./index.html', parser=parser)
# result =etree.tostring(selector)
# print(result.decode('utf-8'))

f =open('./index.html' , 'r',encoding='utf-8')
data =f.read()
tree =etree.HTML(data)


# 通过tostring方法输出
all_div =tree.xpath('//div')
print(etree.tostring(all_div[0],encoding='utf-8').decode('utf-8'))
print(etree.tostring(all_div[1],encoding='utf-8').decode('utf-8'))

h4 =tree.xpath('/html/body/h4')
print(etree.tostring(h4[0],encoding='utf-8').decode('utf-8'))
print(h4[0].xpath('./text()'))