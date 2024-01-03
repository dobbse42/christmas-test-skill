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
  return "done!"

def nth_day():
  my_arr = np.ones(12)
  return str(my_arr[3])
