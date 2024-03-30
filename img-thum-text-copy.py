from bs4 import BeautifulSoup
import requests

# Download website source
r = requests.get("https://www.foxnews.com/")
data = r.text

# Setup BeautifulSoup
soup = BeautifulSoup(data, "html.parser")

# Find all image tags with src attribute and their corresponding headlines
image_data = []
for img in soup.find_all('img', src=True):
    image_src = img['src']
    # Replace http with https if necessary
    
    image_src = "https:" + image_src
    # Find the closest parent element with class 'title' containing the headline
    parent_title = img.find_parent(class_='article')
    headline = parent_title.get_text() if parent_title else "No headline available"
    headline = headline.replace("\n","")
    parent_link = img.find_parent('a')
    link_href = parent_link['href'] if parent_link and 'href' in parent_link.attrs else image_src
    image_data.append((image_src, headline, link_href))

# Write image links with thumbnails and headlines to an HTML file
with open("image_links_with_headlines.html", "w") as file:
    file.write("<html>\n<head>\n<title>Image Links with Headlines</title>\n</head>\n<body>\n")
    for image_src, headline, link_href in image_data:
        # Write image with headline and link
        file.write(f"<div>")
        file.write(f"<a href='{link_href}' target='_blank'>")
        file.write(f"<img src='{image_src}' alt='{headline}'>")
        file.write(f"<br>{headline}</a><br>\n")
        file.write("</div>")
    file.write("</body>\n</html>")

print("Image links with headlines saved to image_links_with_headlines.html")
