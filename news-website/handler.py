from bs4 import BeautifulSoup
import datetime


import requests
import datetime
import json
import boto3
dynamodb = boto3.client("dynamodb")

print("I am working")


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
        parent_link = img.find_parent("a")
        link_href = (
            parent_link["href"]
            if parent_link and "href" in parent_link.attrs
            else image_src
        )
        image_data.append([image_src, headline, link_href])
        no_of_lines += 1
        if no_of_lines > 10:
            break
    print(image_data)
    json_image_data = json.dumps(image_data)
    
    return json_image_data

def hello(event, context):
    print("I am inside")
    # print(table.creation_date_time)
    page_content = web_scrape("https://www.foxnews.com/")
    
    my_time = str(datetime.datetime.now())
    item = {"timestamp": my_time, "section": "Home", "content": page_content}
    print(item)
    dynamodb.put_item(
            TableName='EnDyDBTable',
            Item={
                'timestamp': {'S': my_time},
                'section': {'S': "Home"},
                'content': {'S': page_content},
            }
        )
