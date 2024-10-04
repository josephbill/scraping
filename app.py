from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# function to scrape data from elements in a webpage 
def scrape_data():
    # url 
    url = "https://moringaschool.com"
    # get the data from webpage
    response = requests.get(url)
    print(response)
    # using bs to extract our details 
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    ## extract titles of webpages 
    title = soup.title.string
    # to get all webpages 
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return title, links

@app.route('/')
def index():
    # get user agent 
    user_agent = request.headers.get('User-Agent')
    #scraped data 
    title, links = scrape_data()
    return render_template('index.html', title=title , links=links, user_agent=user_agent )

if __name__ == '__main__':
    app.run(debug=True)
    
    
    