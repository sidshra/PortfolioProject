from bs4 import BeautifulSoup
import requests

# Download website source
r = requests.get("https://www.foxnews.com/")
data = r.text

# Setup BeautifulSoup
soup = BeautifulSoup(data, "html.parser")

# Find all image tags
image_links = []
for link in soup.find_all("img", src=True):  # Ensure the img tag has a 'src' attribute
    image_src = link.get("src")
    image_links.append(image_src)

# Write image links to an HTML file
with open("image_links.html", "w") as file:
    file.write("<html>\n<head>\n<title>Image Links</title>\n</head>\n<body>\n")
    for image_link in image_links:
        file.write(f"<img src='{image_link}' alt='image'><br>\n")
    file.write("</body>\n</html>")

print("Image links saved to image_links.html")
