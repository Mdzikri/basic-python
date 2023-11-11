print("===============")
print("calculator")

    


while True:
    
    print("1. tambah : ")
    print("2. kali : ")
    print("3. kurang : ")
    print("4. bagi : ")
    print("0. exit bro ")
    print("===============")
    data = int(input("masukan pilihan mu berapa angka "))
    data1=int(input("nilai pertama : "))
    data2=int(input("nilai pertama : "))
    
    if data ==1:
        total= data1 + data2
        print (f" hasilnya {total}")
    elif data ==2:
        total= data1*data2
        print(f"hasil nya adalah {total}")
        
    elif data ==3:
        total = data1-data2
        print(f"hasilnya adalah {total}")
        
    elif data ==4 :
        total = data1 / data2
        print(f"hasilnya adalah {total}")
        
    elif data == 0 :
        break;