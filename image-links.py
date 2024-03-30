from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# Download website source
r = requests.get("https://www.foxnews.com/")
data = r.text

# Setup BeautifulSoup
soup = BeautifulSoup(data, "html.parser")

# Find all image tags with src attribute and their parent anchor tags
image_links = []
for img in soup.find_all("img", src=True):
    image_src = img["src"]
    parent_link = img.find_parent("a")
    if parent_link:
        parent_href = parent_link.get("href")
        if parent_href:
            parent_href = urljoin(
                r.url, parent_href
            )  # Convert relative URL to absolute URL
    else:
        parent_href = None
    image_links.append(("https:"+image_src, parent_href))

# Write image and link pairs to an HTML file
with open("image_and_link.html", "w") as file:
    file.write("<html>\n<head>\n<title>Images and Links</title>\n</head>\n<body>\n")
    for image_link, parent_link in image_links:
        if parent_link:
            file.write(
                f"<a href='{parent_link}'><img src='{image_link}' alt='image'></a><br>\n"
            )
        else:
            file.write(f"<img src='{image_link}' alt='image'><br>\n")
    file.write("</body>\n</html>")

print("Image and link pairs saved to image_and_link.html")
