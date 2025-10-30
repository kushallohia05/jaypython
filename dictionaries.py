studentdata={'id1':
    { 'name': ['Sara'],
      'class':['V'],   
      'subjectintegration': ['english, maths, science']},
'id2':
    { 'name': ['David'],
      'class':['V'],   
      'subjectintegration': ['english, maths, science']},
'id3':
    { 'name': ['Surya'],
      'class':['V'],   
      'subjectintegration': ['english, maths, science']}}
result={}
for key, value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)        