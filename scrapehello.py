#scrapehello.py

from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

all_goodbye_elements = soup.find_all(class_='goodbye')

all_french_list_items = soup.find_all('li', class_='french')

all_hello_elements = soup.find_all(id='hello-list')

print('list items:', all_list_items)
print('------')
print('divs:', all_divs)
print('------')
print('goodbye elements:', all_goodbye_elements)
print('------')
print('french stuff:', all_french_list_items)
print('------')
print('hello id elements:', all_hello_elements)
print('------')

for li in all_list_items:
    print(li.string)
print('--------')

for child in all_hello_elements[0].children:
    print(child.string)
print('--------')

print('List items within hello tag')
hello_list_items = all_hello_elements[0].find_all('li')
for li in hello_list_items:
    print(li.string)
print('--------')

img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('--------')
print('The img width:')
print(img_tag['width'])
print('--------')

print('List items within goodbye list')
goodbye_list_items = all_goodbye_elements[0].find_all('li')
for li in goodbye_list_items:
    print(li.string)
print('--------')

a_url = soup.find('a')
print('URL of "say hello in lots of languages!":')
print(a_url['href'])
print('--------')
