import json
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.text
    else:
        title = "No title found"
    
    
    return {'title': title}

def main(event, context):
    url = 'https://orm.drizzle.team/docs/overview' 
    result = scrape_website(url)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

# For local testing
if __name__ == "__main__":
    print(main(None, None))