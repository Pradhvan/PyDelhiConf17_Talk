from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website URL ")  

r  = requests.get("http://" +url) #Getting the content

data = r.text	

soup = BeautifulSoup(data,"html.parser") # Parsing the response 	

for link in soup.find_all('a'):
    var = link.get('href')	
    outfile = open('scrapper.txt',"a")
    outfile.write(var + '\n') #Preserving the data 
    outfile.close()
    print var
