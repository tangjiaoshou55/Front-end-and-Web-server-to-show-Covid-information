import urllib.request
import json
import csv

def dic_list_gen(x,y):
  re=[]
  for ys in y:
    ree={}
    for i in range(len(x)):
      ree[x[i]]=ys[i]
    re.append(ree)
  return re

def make_lists(k_list,d_list):
  re = []
  for d in d_list:
    new_list = []
    for k in k_list:
      val = d.get(k)
      new_list.append(val)
    re.append(new_list)
  return re

def read_values(x):
  with open(x) as f:
    re=[]
    reader=csv.reader(f)
    next(reader)
    for line in reader:
      re.append(line)
  return re

def  write_values(x,y):
  with open(x,"a") as f:
    writer=csv.writer(f)
    for ys in y:
      writer.writerow(ys)

def json_loader(url):
  content=urllib.request.urlopen(url)
  jsoncontent=content.read().decode()
  return json.loads(jsoncontent)

def make_values_numeric(list,dic):
  for i in list:
    dic[i]=float(dic[i])
  return dic

def save_data(list, list2, filename):
  with open(filename, "w") as f:
    header = csv.writer(f)
    header.writerow(list)
  re = []
  for dic in list2:
    ree = []
    for key in list:
      if key in dic.keys():
        ree.append(dic[key])
    re.append(ree)
  for ass in re:
    with open(filename, "a") as g:
      writer = csv.writer(g)
      writer.writerow(ass)

def load_data(filename):
  re=[]
  with open(filename) as f: 
    reader=csv.reader(f)
    header=next(reader)
    for line in reader:
      ree={}
      for lst in line:
          for i in range(len(line)):
            ree[header[i]]=line[i]
      re.append(ree) 
  return re