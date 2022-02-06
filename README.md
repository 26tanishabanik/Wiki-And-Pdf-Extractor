# Wiki-And-Pdf-Extractor

## [wiki_extractor.py](https://github.com/26tanishabanik/Wiki-And-Pdf-Extractor/blob/main/wiki_extractor.py) is a python script which extracts various wikipedia urls from a given user query and outputs one para from each url using [beautifulsoup library](https://pypi.org/project/beautifulsoup4/) in python and saves the output in a json format. The output when opened using any text editor might not show the correct format, but after loading using json it gives the proper language format.

## Here's the way to run this script:
#### python3 wiki_extractor.py --keyword="Indian Historical Events" --num_urls=100 --output="wiki_extracted"


## [pdf_extractor.py](https://github.com/26tanishabanik/Wiki-And-Pdf-Extractor/blob/main/pdf_extractor.py) is a python script which extracts various content from the pdfs using easyocr and saves it as a json file.


## Here's the way to run this script:
#### python3 pdf_extractor.py
