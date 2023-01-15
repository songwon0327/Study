num = int(input())
record = []

for i in range(num):
    price = int(input())
    
    if (price == 0) and (len(record) > 0):
        record.pop()
    else:
        record.append(price)    
        
total = sum(record)   
print(total) 