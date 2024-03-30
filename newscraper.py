from requests_html import HTMLSession

session = HTMLSession()

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKT1dpZ0FQAQ?hl=en-NZ&gl=NZ&ceid=NZ%3Aen"
r = session.get(url)

# r.html.render(sleep=1, scrolldown=1)
r.html.arender(timeout=0, sleep=20)


articles = r.html.find('article')

print(articles)

# for item in articles:
#     newsitem = item.find('h3',first=True)
#     title = newsitem.text
#     link = newsitem.absolute_links
#     print(title,link)