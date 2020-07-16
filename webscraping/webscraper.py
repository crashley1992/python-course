# always try to gett permission before scraping
# too many requests or requests can result in IP being blocked
# some site automatically block scraping

# 3 libraries 
# pip install requests
# pip install lxml
# pip install bs4

import requests
import bs4

import requests
# get request for website, should be direct link
# own firewall could block python
# result = requests.get("http://www.example.com")

# import bs4
# # beatiful soup uses lxml to sort through info
# soup = bs4.BeautifulSoup(result.text, "lxml")

# # will return a specific value for html tag, reports it back as a list
# print(soup.select("title")[0].getText()) #only returns the title as text
# print(soup.select("p"))

# res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

# soup2 = bs4.BeautifulSoup(res.text, "lxml")

# soup2.select('.toctext')[0]

# for item in soup2.select('.totext'):
#     print(item.text)


# for images check copyright
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.thumbimage')

computer = soup.select('.thumbimage')[0]
print(computer)

computer['src']


image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
image_link.content

f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()
