import tkinter

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
#tkinter: module

#ALGORITMA

#-----------------------------------------------TKINTER SCRIPT----------------------------------------------#
window = tkinter.Tk()
window.title("Simulasi Gate Tol")
window.geometry("1280x720")

frame_saldo = tkinter.Frame(window, bg="grey")
frame_confirm = tkinter.Frame(window, bg="light blue")
frame_saldo.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.5, anchor=tkinter.CENTER)
frame_confirm.place(relx=0.1,rely=0.75,relwidth=0.2,relheight=0.5, anchor=tkinter.CENTER)

roadmap_frame = tkinter.Frame(window,bd=5, bg="dark grey" ) #Creates a frame for the map
roadmap_frame.place(relx=0.6, rely=0.5, relwidth=0.8, relheight=1, anchor=tkinter.CENTER) #Places the map in the desired place

roadmap_drawing = tkinter.Canvas(roadmap_frame, bg="light green") #Canvas for the map
roadmap_drawing.place(relwidth=1,relheight=1) #Places the canvas on the frame
roadmap_drawing.create_line(100,500, 150,420, 250,400, 350,340, 390,380, 450,320, 490,360, 590,330, 690,360, 740,200, 790,250, 890,290, 960,270, width=4) #Draws the line for the map

#------buttons------#
map_buttons = []

def delete_buttons(arr):
    for button in arr:
        button.destroy()
    arr.clear()

def pressed(lokasi, destination, km):
    delete_buttons(map_buttons)
    if(destination == False):
        make_map_buttons(lokasi, button_color="green", destination=True)
        return
    elif(destination == True):
        make_map_buttons("banyuwangi", button_color="red", destination=False)
        return

def make_map_buttons(lokasi="banyuwangi", button_color="red", destination=False):
    if(lokasi!="cileunyi"):
        b_cileunyi = tkinter.Button(roadmap_frame, text="Cileunyi", bg=button_color, command=lambda lokasi="cileunyi":pressed(lokasi, destination, 156))
        b_cileunyi.place(x=100,y=500, height=20, width=20)
        map_buttons.append(b_cileunyi)    

    if(lokasi!="jatinangor" and (lokasi=="cileunyi" or lokasi=="banyuwangi")):
        b_jatinangor = tkinter.Button(roadmap_frame, text="Jatinangor", bg=button_color, command=lambda lokasi="jatinangor":pressed(lokasi, destination, 161))
        b_jatinangor.place(x=150,y=420, height=20, width=20)
        map_buttons.append(b_jatinangor)

    if(lokasi!="pamulihan"):
        b_pamulihan = tkinter.Button(roadmap_frame, text="Pamulihan", bg=button_color, command=lambda lokasi="pamulihan":pressed(lokasi, destination, 166))
        b_pamulihan.place(x=250,y=400, height=20, width=20)
        map_buttons.append(b_pamulihan)

    if(lokasi!="sumedang"):
        b_sumedang = tkinter.Button(roadmap_frame, text="Sumedang", bg=button_color, command=lambda lokasi="sumedang":pressed(lokasi, destination, 183))
        b_sumedang.place(x=490,y=360, height=20, width=20)
        map_buttons.append(b_sumedang)   

    if(lokasi!="cimalaka"):
        b_cimalaka = tkinter.Button(roadmap_frame, text="Cimalaka", bg=button_color, command=lambda lokasi="cimalaka":pressed(lokasi, destination, 186))
        b_cimalaka.place(x=590,y=330, height=20, width=20)
        map_buttons.append(b_cimalaka)

    if(lokasi!="paseh"):
        b_paseh = tkinter.Button(roadmap_frame, text="Paseh", bg=button_color, command=lambda lokasi="paseh":pressed(lokasi, destination, 194))
        b_paseh.place(x=690,y=360, height=20, width=20)
        map_buttons.append(b_paseh)

    if(lokasi!="cisumdawu jaya"):
        b_cisumdawujaya = tkinter.Button(roadmap_frame, text="Cisumdawu Jaya", bg=button_color, command=lambda lokasi="cisumdawu jaya":pressed(lokasi, destination, 211))
        b_cisumdawujaya.place(x=890,y=290, height=20, width=20)
        map_buttons.append(b_cisumdawujaya)

    if(lokasi!="cisumdawu utama"):
        b_cisumdawuutama = tkinter.Button(roadmap_frame, text="Cisumdawu Utama", bg=button_color, command=lambda lokasi="cisumdawu utama":pressed(lokasi, destination, 214))
        b_cisumdawuutama.place(x=960,y=270, height=20, width=20)
        map_buttons.append(b_cisumdawuutama)    
    return

make_map_buttons()
#------buttons------#

window.mainloop()
#-----------------------------------------------------------------------------------------------------------#

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
    "cileunyi":156,
    "jatinangor":161,
    "pamulihan":166,
    "sumedang":183,
    "cimalaka":186,
    "paseh":194,
    "cisumdawu":211
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

