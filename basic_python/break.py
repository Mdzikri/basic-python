data = ''
for i in range(1,10):
    if i%8  == 0:
        break
    print(i)
    
while True:
    data = int(input("data:"))
    if data == 2:
        break
    
    print(data)