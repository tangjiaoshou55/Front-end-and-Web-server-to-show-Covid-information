def max_value(alist,key1):
  re = ''
  for dic in alist:
    if re > str(dic[key1]):
      re = re
    else:
      re = str(dic[key1])
  return re

def sum_matches(lod,k,v,tgt):
  re=0
  for lists in lod:
    if lists[k]==v:
      re+=int(lists[tgt])
  return re

def copy_matching(lod,k,v):
  re=[]
  for lists in lod:
    if lists[k]==v:
      re.append(lists)
  return re


def init_dictionary(x,y):
  re = {}
  for dic in x:
    for k in dic.keys():
      if y == k:
        val = dic[k]
        re[val] = 0
  return re
