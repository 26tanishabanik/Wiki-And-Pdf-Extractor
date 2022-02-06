from urllib.parse import urlparse
from urllib.request import urlopen
import urllib.request 
import requests
import json
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
import urllib
from urllib.request import unquote
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import easyocr
import pandas as pd

def pdf_extractor():
  out_dict = dict()
  res = list()
  for i in range(df.shape[0]):
    if df.iloc[i,0].endswith('.pdf'):
      out_dict['page_url'] = df.iloc[i,0]
      out_dict['pdf_url'] = df.iloc[i,0]
      pdf_url = df.iloc[i,0]
      pdf_response = requests.get(pdf_url)
      filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
      with open(filename, 'wb') as f:
          f.write(pdf_response.content)
      f.close()
      pages = convert_from_path(filename)
      image_name = './images'+filename+"_"+str(i)+".jpg"
      pages[3].save(image_name, 'JPEG')
			output = reader.readtext(filename, paragraph=True, detail = 0)
			output = ' '.join(output)
			out_dict['pdf-content'] = output[:500]
			res.append(out_dict)
      out_dict = dict()
    else:
			out_dict['page_url'] = df.iloc[i,0]
    
      links = []
      html = urlopen(df.iloc[i,0]).read()
      html_page = BeautifulSoup(html, features="html.parser") 
      og_url = html_page.find("meta",  property = "og:url")
      base = urlparse(df.iloc[i,0])
      for link in html_page.find_all('a'):
          current_link = link.get('href')
          try:
              if current_link.endswith('pdf'):
                  if og_url:
                      links.append(og_url["content"] + current_link)
                  else:
                      links.append(base.scheme + "://" + base.netloc + current_link)
          except:
              print("Not a pdf url")

      for link in links:
          if link.startswith('https'):
            out_dict['pdf_url'] = df.iloc[i,0]
            out_dict['pdf-content'] = ""
            print(link)
            break
      res.append(out_dict)
      out_dict = dict()
			
	out_file = open("pdf_extract.json", "w")  
	json.dump(res, out_file, indent = 6) 
	out_file.close()

pdf_extractor()

      
  
        
