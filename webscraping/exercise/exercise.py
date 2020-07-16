import requests 
import bs4

# assignment wants only the first page of authors
quotes_authors = []
base_url = 'http://quotes.toscrape.com/page/1/'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
authors = soup.select('small.author')
# needs to loop through for each author
for author in authors:
            # .text shows text in the html.example h1 will show whats in the h1 tags
            quotes_authors.append(author.text)

print(quotes_authors)
print('\n')

# gets quote in span text containing quotes
quotes = []
quotes_text = soup.select('span.text')
for quote in quotes_text:
    quotes.append(quote.text)

print(quotes)
print('\n')

# selects top 10 quotes
top_ten = []

for n in range(1,11):
        top_tags = soup.select('.tag-item')
        for tags in top_tags:
            print(tags.text)



