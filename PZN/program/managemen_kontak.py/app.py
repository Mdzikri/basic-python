
import function

daftar_kontal=[]
daftar_kontal.append({
    "nama":"dzikri",
    "email":"dzikrifft@gmail.com",
    "telepon":"087898392"
})

# program

while True:
    
    print("=======Menu=======")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. hapus kontak")
    print("4. cari kontak")
    print("0. keluar program ")
    
    menu = int(input("masukan pilihan "))
    if menu ==0:
        break;
    elif menu == 1:
        function.display_kontak(daftar_kontal)
        print("")
    elif menu ==2:
        kontak = function.new_kontak()
        daftar_kontal.append(kontak)
        print("")
    elif menu ==3:
        function.hapus_kontak(daftar_kontal)
        print("")
    elif menu == 4 :
        function.cari_kontak(daftar_kontal)
        print("")
    
    else:
        print("========================")
        print("")
        print("tidak ada dalam daftar")
        print("")
        print("masukan nomer susai dengan yang ada dibawah")
    