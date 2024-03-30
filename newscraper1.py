from bs4 import BeautifulSoup #Import stuff
import requests

r = requests.get("https://www.foxnews.com/")  # Download website source

data = r.text  #Get the website source as text

soup = BeautifulSoup( data, "html.parser")  # Setup a "soup" which BeautifulSoup can search

links = []

for link in soup.find_all('img'):  #Cycle through all 'img' tags
    imgSrc = link.get('src')   #Extract the 'src' from those tags
    links.append(imgSrc)    #Append the source to 'links'

# print(links)  #Print 'links'
    with open("image_links.html", "w") as file:
        file.write("<html>\n<head>\n<title>Image Links</title>\n</head>\n<body>\n")
        for img_src in links:
            file.write(f"<img src='{img_src}' alt='image'>\n")
        file.write("</body>\n</html>")

    print("Image links saved to image_links.html")
