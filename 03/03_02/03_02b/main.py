# Key: State
# Value: Capital

province_capitals = {
  'British Columbia' : 'Victoria',
  'Ontario' : 'Ottawa',
  'Alberta' : 'Edmonton'
}

print(province_capitals['Alberta'])

for key, value in province_capitals.items():
  print(key + ' -> ' + value)