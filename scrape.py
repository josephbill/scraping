import requests
from bs4 import BeautifulSoup

search_term = input('What do you want to scrape ?')
print(search_term)
url = f"https://www.jumia.co.ke/catalog/?q={search_term}"
print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# img : product image , name : product name , prc : price
# extracting the product titles 
product_titles = soup.find_all('h3', class_='name')
print("PRODUCT TITLES:")
for title in product_titles:
    print(title.get_text().strip())
    

# extracting the product price 
product_price = soup.find_all('div', class_='prc')
print("PRODUCT PRICE:")
for price in product_price:
    print(price.get_text().strip())
    
# extract images 
product_images = soup.find_all('img', class_='img')
print("PRODUCT IMAGE")
for img in product_images:
    imageUrl = img['data-src'] 
    print(imageUrl)
    
### TO DO : CREATE A MAPPING FOR THE DETAILS 
'''
   [
       {
           product_image: '',
           product_price: '', 
           product_title: ''
       }
       
   ]

'''