import bottle
import json
import data
import processing
import os.path

def load_data( ):
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer',\
    'administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'saved_data.csv')

@bottle.route('/')
def index():
  return bottle.static_file('index.html',root='.')

@bottle.route('/barchart')
def bar():
  re=data.load_data('saved_data.csv')
  max_date=processing.max_value(re,'date')
  match_dic_lst=processing.copy_matching(re,'date',max_date)
  re=json.dumps(match_dic_lst)
  return re

@bottle.route('/piechart')
def pie():
  re=data.load_data('saved_data.csv')
  max_date=processing.max_value(re,'date')
  j=processing.sum_matches(re,'date',max_date,'administered_janssen')
  m=processing.sum_matches(re,'date',max_date,'administered_moderna')
  p=processing.sum_matches(re,'date',max_date,'administered_pfizer')
  u=processing.sum_matches(re,'date',max_date,'administered_unk_manuf')
  re=[j,m,p,u]
  re=json.dumps(re)
  return re

@bottle.route('/ajax.js')
def graph():
  return bottle.static_file('ajax.js',root='.')

def sort(dict):
  return dict['date']

@bottle.route('/js.js')
def js():
  return bottle.static_file("js.js",root=".")

@bottle.post('/linechart')
def line():
  content=bottle.request.body.read().decode()
  content=json.loads(content)
  dic_lst=data.load_data('saved_data.csv')
  match_dic_lst=processing.copy_matching(dic_lst,'location',content)
  match_dic_lst.sort(key=sort)
  match_dic_lst=json.dumps(match_dic_lst)
  return match_dic_lst

load_data()
bottle.run(host='0.0.0.0',port=8080,debug=True)