from bs4 import BeautifulSoup
import datetime
import requests
import datetime
import json
import boto3


def web_scrape(site_url):
    
    print("inside web scraper")
    r = requests.get(site_url)
    data = r.text

    # Setup BeautifulSoup
    soup = BeautifulSoup(data, "html.parser")

    # Find all image tags with src attribute and their corresponding headlines
    image_data = []
    no_of_lines=0
    for img in soup.find_all("img", src=True):

        image_src = img["src"]
        # Replace http with https if necessary

        image_src = "https:" + image_src
        # Find the closest parent element with class 'title' containing the headline
        parent_title = img.find_parent(class_="article")
        headline = parent_title.get_text() if parent_title else "No headline available"
        headline = headline.replace("\n", "")
        parent_link = img.find_parent("a")
        link_href = (
            parent_link["href"]
            if parent_link and "href" in parent_link.attrs
            else image_src
        )
        image_data.append([image_src, headline, link_href])
        no_of_lines += 1
        if no_of_lines > 11:
            break
    print(image_data)
    json_image_data = json.dumps(image_data)

    return json_image_data

def handler(event, context):
    try:

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("EnDyDBTable")

        page_content = web_scrape("https://www.foxnews.com/")
        my_date = str(datetime.datetime.now().date())

        item = {"date": my_date, "section": "Home", "content": page_content}
        
   
        return item

    except Exception as e:

        print(e)
        # logging.error("An error occurred in handler function: %s", e, exc_info=True)




