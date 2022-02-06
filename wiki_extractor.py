import json
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re


def wiki_extractor(query, n):
  output = dict()
  res = list()
  query =query +' wikipedia' #For better search results
  results = search(query, num=n, stop=20, pause=2) 
  for wiki_url in results:

    if 'wikipedia' in wiki_url:
      print(wiki_url)
      output['url'] = wiki_url
      response = requests.get(url=wiki_url)
      soup = BeautifulSoup(response.content, 'html.parser')

      allpara = soup.find(id="bodyContent").find_all("p")

      text = re.sub(re.compile('<.*?>'), '', str(allpara))

      text = text.replace('[', '')
      text = text.replace(']', '')
      wordList = text.replace(',', '')

      final = ''.join(str(wordList))

      final = final[:500].split('\n')
      para = ''
      for i,lines in enumerate(final):
          splitItems = final[i].split(' ')
          if len(splitItems)>14:
            length = len(splitItems)
            for i in range(0, length, 14):
              para += ' '.join(splitItems[i:i+14]) + '\n'
          else:
            para += ' '.join(splitItems) + '\n'
      output['paragraph'] = para
      res.append(output)
      output = dict()
      print(para)

    else:
      print("Url not needed")
      
  out_file = open("wiki_extracted.json", "w")  
  json.dump(res, out_file, indent = 6) 
  out_file.close() 

query = input("Enter your search query: ")
wiki_extractor(query)
  
