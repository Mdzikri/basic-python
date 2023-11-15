
# def jumlahkan(satu,dua):
#     total=satu+dua
#     print(f"total {satu, dua} adalah = {total} ")
    
# jumlahkan(10,10)

#argument list satu prameter bisa memasukan beberapa nilai 

def angka(*lis_angka):
    total=0
    for data in lis_angka:
        hasil = data+total 
    print(f"hasil akhir {lis_angka}={hasil}")
        
angka(10,10,10)