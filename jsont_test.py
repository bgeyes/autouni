import json

make = ['merc', 'audi', 'bmw']

model = ['1', '2', '3']

data = {} 

data['cars'] = []

count = 0

for x in make:
    
    data['make'] = x
    #data['model'] = model
    data['cars'].append([{"make" : x}, {"model": model}, {"run": model[count]}])
    #data['people'] = []  
    #data['model'] = []
    #data['people'].append({  
    #    'name': 'Scott',
    #    'website': 'stackabuse.com',
    #    'from': 'Nebraska'
    #})
    #data['model'].append(['model1','model2','model3'])
    #data['people'].append({  
    #    'name': 'Larry',
    #    'website': 'google.com',
    #    'from': 'Michigan'
    #})
    #data['model'].append(['model4','model5','model6'])
    #data['people'].append({  
    #    'name': 'Tim',
    #    'website': 'apple.com',
    #    'from': 'Alabama'
    #})
    #data['model'].append(['model7','model8','model9'])
    with open('data1.txt', 'w') as outfile: 
        outfile.write("inca o data ")
        cars = json.dumps(data, sort_keys=True, indent=4)
        outfile.write(cars)
    count += 1

#print(json.dumps(data, sort_keys=True, indent=4))

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)


