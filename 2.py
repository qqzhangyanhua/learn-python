from bs4  import BeautifulSoup

html_doc = '<div>sssss<span class="name name2">222</span><h3>4444444444</h3><span>3333</span> </div>'

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.span)
# print(soup.span.string)
# print(soup.div.text)
# print(soup.div.get_text())
# print(soup.div.contents)
# print(soup.div.children)
# for i in soup.div.children:
#     print(i)
print(soup.div.span.attrs)