#PROGRAM SIMULASI GERBANG TOL BERPIKIR KOMPUTASIONAL KELAS 30 KELOMPOK 9

#KAMUS
#lokasi_gate: dictionary[string,int]
#daftar_golongan: dictionary[string,int]
#masuk: string
#keluar: string
#saldo: int
#golongan: string
#jarak: int
#harga: int
#endline: function(void) -> void

#ALGORITMA
#Deklarasi semua golongan dan harganya
daftar_golongan = {
    "1":1000,
    "2":2000,
    "3":3000,
    "4":4000,
    "5":5000,
}

#Deklarasi semua lokasi gerbang
lokasi_gate = {
    "cileunyi":0,
    "jatinangor":100,
    "pamulihan":200,
    "sumedang":300,
    "cimalaka":400,
    "paseh":500,
    "cisumdawu":600
}

def clearscreen(): #Untuk mengakhiri setiap sesi program agar command line tidak penuh text
    input("Tekan enter untuk memulai ulang program")
    for i in range(30):
        print('\n')

while(True):
    print("=====SELAMAT DATANG======")
    #Pemaparan semua lokasi gate tol
    print("Daftar lokasi gate:")
    print("Cileunyi")
    print("Jatinangor")
    print("Pamulihan")
    print("Sumedang")
    print("Cimalaka")
    print("Paseh")
    print("Cisumdawu\n")
    #Pemaparan golongan
    print("=====Daftar Golongan======")
    print("Golongan 1: Mobil, bus")
    print("Golongan 2: Truk 2 gandar")  
    print("Golongan 3: Truk 3 gandar")
    print("Golongan 4: Truk 4 gandar")
    print("Golongan 5: Truk 5 gandar\n")

    #Meminta input saldo dari pengguna
    try:
        saldo = int(input("Masukkan jumlah saldo tol anda: "))
    except: #Untuk mengantisipasi input saldo yang tidak valid dan memulai program dari awal apabila benar terjadi error
        print("Tolong masukkan saldo berupa angka tanpa simbol, spasi, atau huruf!")
        clearscreen()
        continue

    masuk = input("Masukkan lokasi masuk tol anda: ")
    masuk = masuk.lower()
    keluar = input("Masukkan lokasi keluar tol anda: ")
    keluar = keluar.lower()
    golongan = input("Masukkan golongan kendaraan anda: ")

    try:
        jarak = abs(lokasi_gate[keluar]-lokasi_gate[masuk])
    except: #Untuk mengantisipasi apabila lokasi yang dimasukkan tidak termasuk lokasi yang tertera dan memulai program dari awal apabila benar terjadi error
        print("Tolong masukkan lokasi masuk dan keluar yang benar!")
        clearscreen()
        continue

    try:
        harga = (jarak*daftar_golongan[golongan])
    except: #Untuk mengantisipasi apabila golongan yang dimasukkan tidak termasuk golongan yang tertera dan memulai program dari awal apabila benar terjadi error
        print("Tolong masukkan golongan yang tertera!")
        clearscreen()
        continue 

    if(harga>saldo): #Cek apakah saldo cukup untuk perjalanan yang ingin dilakukan
        print("Saldo anda tidak mencukupi untuk melakukan perjalanan ini.")
        clearscreen()
        continue

    elif(harga==0): #Cek apakah pengguna memasukkan lokasi masuk dan keluar yang sama
        print("Anda tidak bisa masuk dan keluar pada gate yang sama!")
        clearscreen()
        continue

    else: #Memberitahukan jarak tempuh perjalanan yang dilakukan, serta sisa saldo e-money setelah melakukan perjalanan
        print(f"Anda menempuh perjalanan sejauh {jarak} km")
        print(f"Saldo anda berkurang dari {saldo} menjadi {saldo-harga}")
        clearscreen()

