import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging

flipkart_url="https://www.flipkart.com/search?q="+"iphone15"
#print(flipkart_url)

urlclient=uReq(flipkart_url)

flipkart_page=urlclient.read()
flipkart_html=bs(flipkart_page, 'html.parser')

# so far we have access to the entire page, now we need to perform clicks on separate products

bigBox=flipkart_html.findAll("div", {"class":"cPHDOP col-12-12"})
print(len(bigBox))
# it contains dashboard info in first 3 boxes, so remove them

del bigBox[0:3]
#bigBox[1].div.div.div.a['href']

prodLink="https://www.flipkart.com"+bigBox[1].div.div.div.a['href']

# for i in bigBox:
#     print("https://www.flipkart.com"+i.div.div.div.a['href'])


prodReq=requests.get(prodLink)

product_html=bs(prodReq.text,'html.parser')

comment_box=product_html.findAll("div",{"class":"RcXBOT"})

# print(len(comment_box))

comment_box[0].div.div.find_all('p',{"class":"_2NsDsF AwS1CA"})[0].text

# for i in comment_box:
#     print(i.div.div.find_all('p',{"class":"_2NsDsF AwS1CA"})[0].text)

# ratings
# for i in comment_box:
#     print(i.div.div.div.div.text)

# for i in comment_box:
#     print(i.div.div.div.p.text)

comment_box[0].div.div.find_all('div',{"class":''})[0].div.text

for i in comment_box:
    print(i.div.div.find_all('div',{"class":''})[0].div.text)

