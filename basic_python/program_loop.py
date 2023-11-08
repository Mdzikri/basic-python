data = int(input("masukan data anda :"))

nama=[]
umur=[]

for i in range(0,data):
    input_nama= input("nama :")
    input_umur= input("umur :")
    
    nama.append(input_nama)
    umur.append(input_umur)

for a in range(0, len(nama)):
    data_nama=nama[a]
    data_umur=umur[a]
    print(f"{data_nama} berumur {data_umur}")