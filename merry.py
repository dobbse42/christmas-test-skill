import numpy as np
import urllib, urllib.request
import requests
import feedparser
#import arxiv
#import nltk
#nltk.download('punkt')

def be_merry():
#  paper = next(arxiv.Client().results(arxiv.Search(id_list = ["2107.09200"])))
#  my_filename = paper.get_short_id() + '_' + paper.title.replace(' ', '_') + '.pdf'
#  return my_filename
#  url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
#  data = urllib.request.urlopen(url)
#  print(data.read().decode('utf-8'))
  id = "1904.12956"
  feed = get_feed(id)
  pdf = get_pdf(feed)
  return "done!"

def get_feed(id):
  url = 'http://export.arxiv.org/api/query?id_list=' + str(id)
  data = requests.get(url)
  return data.text

def get_pdf(my_xml):
  feed = feedparser.parse(my_xml)
  for link in feed['entries'][0]['links']:
    if link['rel'] == 'related' and link['title'] == 'pdf':
      pdf_url = link['href']
  pdf = requests.get(pdf_url)
  return pdf.content

def nth_day():
  my_arr = np.ones(12)
  return str(my_arr[3])
