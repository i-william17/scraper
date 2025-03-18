import requests
from bs4 import BeautifulSoup

#url to be scraped
url = "https://google.com"

#get requests from websites
response = requests.get(url)

#check successful requests
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all('h2', class_ ='title')

    #print titles
    for titles in titles:
        print(titles.text.strip())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
