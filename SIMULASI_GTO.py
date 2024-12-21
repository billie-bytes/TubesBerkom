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

jarak = 0
golongan = 0

def hitung_harga(km, golongan):
    return

#-----------------------------------------------TKINTER SCRIPT----------------------------------------------#
window = tkinter.Tk()
window.title("Simulasi Gate Tol")
window.geometry("1280x720")


#---side windows----#
frame_golongan = tkinter.Frame(window, bg="grey")
frame_saldo = tkinter.Frame(window, bg="light blue")
frame_golongan.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.5, anchor=tkinter.CENTER)
frame_saldo.place(relx=0.1,rely=0.75,relwidth=0.2,relheight=0.5, anchor=tkinter.CENTER)
text_golongan = tkinter.Label(frame_golongan, text="Pilih Golongan")
text_golongan.place(relx=0.25,rely=0.01, relwidth=0.5, relheight=0.1)
text_header_saldo = tkinter.Label(frame_saldo, text="Saldo")
text_header_saldo.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.1)

saldo=0
text_saldo = tkinter.Label(frame_saldo, text=saldo)
text_saldo.place(relx=0.1,rely=0.25, relwidth=0.8, relheight=0.1)

input_saldo = tkinter.Text(frame_saldo, font=("Arial",19))
input_saldo.place(relx=0,rely=0.4,relheight=0.1,relwidth=0.7)
#---side windows----#

#-----map frame----#
roadmap_frame = tkinter.Frame(window,bd=5, bg="dark grey" ) #Creates a frame for the map
roadmap_frame.place(relx=0.6, rely=0.5, relwidth=0.8, relheight=1, anchor=tkinter.CENTER) #Places the map in the desired place
roadmap_drawing = tkinter.Canvas(roadmap_frame, bg="light green") #Canvas for the map
roadmap_drawing.place(relwidth=1,relheight=1) #Places the canvas on the frame
roadmap_drawing.create_line(100,500, 150,420, 250,400, 350,340, 390,380, 450,320, 490,360, 590,330, 690,360, 740,200, 790,250, 890,290, 960,270, width=4) #Draws the line for the map
#-----map frame----#

#------buttons------#
map_buttons = []

def delete_buttons(arr):
    for button in arr:
        button.destroy()
    arr.clear()

def pressed_golongan(golongan_num):
    global golongan
    golongan = daftar_golongan[golongan_num]
    return

def pressed_lokasi(lokasi, destination, km):
    delete_buttons(map_buttons)
    global jarak
    if(destination == False):
        make_map_buttons(lokasi, button_color="green", destination=True)
        jarak = km
        return
    elif(destination == True):
        make_map_buttons("banyuwangi", button_color="red", destination=False)
        jarak = abs(jarak-km)
        return
    
def make_golongan_buttons():
    b_mobil = tkinter.Button(frame_golongan,text="Mobil")
    b_mobil.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.15)
    b_truk1 = tkinter.Button(frame_golongan,text="Truk 1 gandar")
    b_truk1.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.35)
    b_truk2 = tkinter.Button(frame_golongan,text="Truk 2 gandar")
    b_truk2.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.55)
    b_truk3 = tkinter.Button(frame_golongan,text="Truk 3 gandar")
    b_truk3.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.75)
    b_truk4 = tkinter.Button(frame_golongan,text="Truk 4 gandar")
    b_truk4.place(relheight=0.2, relwidth=0.5, relx=0.25, rely=0.75)

def make_saldo_button():
    b_saldo = tkinter.Button(frame_saldo, text="Input saldo")
    b_saldo.place(relx=0.7,rely=0.4,relheight=0.1,relwidth=0.3)

def make_map_buttons(lokasi="banyuwangi", button_color="red", destination=False):
    if(lokasi!="cileunyi"):
        b_cileunyi = tkinter.Button(roadmap_frame, text="Cileunyi", bg=button_color, command=lambda:pressed_lokasi("cileunyi", destination, 156))
        b_cileunyi.place(x=100,y=500, height=20, width=20)
        map_buttons.append(b_cileunyi)  

    if(lokasi!="jatinangor" and (lokasi=="cileunyi" or lokasi=="banyuwangi")):
        b_jatinangor = tkinter.Button(roadmap_frame, text="Jatinangor", bg=button_color, command=lambda:pressed_lokasi("jatinangor", destination, 161))
        b_jatinangor.place(x=150,y=420, height=20, width=20)
        map_buttons.append(b_jatinangor)

    if(lokasi!="pamulihan"):
        b_pamulihan = tkinter.Button(roadmap_frame, text="Pamulihan", bg=button_color, command=lambda:pressed_lokasi("pamulihan", destination, 166))
        b_pamulihan.place(x=250,y=400, height=20, width=20)
        map_buttons.append(b_pamulihan)

    if(lokasi!="sumedang"):
        b_sumedang = tkinter.Button(roadmap_frame, text="Sumedang", bg=button_color, command=lambda:pressed_lokasi("sumedang", destination, 183))
        b_sumedang.place(x=490,y=360, height=20, width=20)
        map_buttons.append(b_sumedang)   

    if(lokasi!="cimalaka"):
        b_cimalaka = tkinter.Button(roadmap_frame, text="Cimalaka", bg=button_color, command=lambda:pressed_lokasi("cimalaka", destination, 186))
        b_cimalaka.place(x=590,y=330, height=20, width=20)
        map_buttons.append(b_cimalaka)

    if(lokasi!="paseh"):
        b_paseh = tkinter.Button(roadmap_frame, text="Paseh", bg=button_color, command=lambda:pressed_lokasi("paseh", destination, 194))
        b_paseh.place(x=690,y=360, height=20, width=20)
        map_buttons.append(b_paseh)

    if(lokasi!="cisumdawu jaya"):
        b_cisumdawujaya = tkinter.Button(roadmap_frame, text="Cisumdawu Jaya", bg=button_color, command=lambda:pressed_lokasi("cisumdawu jaya", destination, 211))
        b_cisumdawujaya.place(x=890,y=290, height=20, width=20)
        map_buttons.append(b_cisumdawujaya)

    if(lokasi!="cisumdawu utama"):
        b_cisumdawuutama = tkinter.Button(roadmap_frame, text="Cisumdawu Utama", bg=button_color, command=lambda:pressed_lokasi("cisumdawu utama", destination, 214))
        b_cisumdawuutama.place(x=960,y=270, height=20, width=20)
        map_buttons.append(b_cisumdawuutama)    
    return

make_map_buttons()
make_golongan_buttons()
make_saldo_button()
#------buttons------#

window.mainloop()
#-----------------------------------------------------------------------------------------------------------#
