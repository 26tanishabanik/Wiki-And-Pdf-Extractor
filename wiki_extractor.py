import json
import argparse
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re


def wiki_extractor(query, n, output_filename):
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
      
  out_file = open(output_filename+".json", "w")  
  json.dump(res, out_file, indent = 6) 
  out_file.close() 

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keyword", required=True,
	help="type your query to search")
ap.add_argument("-n", "--num_urls",type=int, required=True,
	help="number of urls to give as a result")
ap.add_argument("-o", "--output", required=True,
	help="output json file name")
args = vars(ap.parse_args())


wiki_extractor(args['keyword'],args['num_urls'],args['output'])
  
