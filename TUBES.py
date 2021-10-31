import requests
import json

endpoint = "https://data.covid19.go.id/public/api/update.json"

def data_covid():
    response = requests.get(endpoint)
    data = json.loads(response.text)
    return data

update = data_covid().get("update")
penambahan = update.get("penambahan")
total = update.get("total")
tanggal = penambahan.get("tanggal")
isRunning = True

# Data untuk pertambahan
penambahan_positif = penambahan.get("jumlah_positif")
penambahan_meninggal = penambahan.get("jumlah_meninggal")
penambahan_sembuh = penambahan.get("jumlah_sembuh")
penambahan_dirawat = penambahan.get("jumlah_dirawat")

#Data untuk total
total_positif = total.get("jumlah_positif")
total_meninggal = total.get("jumlah_meninggal")
total_sembuh = total.get("jumlah_sembuh")
total_dirawat = total.get("jumlah_dirawat")

# Data untuk harian

def PertambahanHarian(indeks):
    # Memasukkan data positif harian ke array data harian positif
    arrHarian = update.get("harian")
    arr_positif_harian = [2]
    temp = 0
    for i in range(1, len(arrHarian)):
        temp = arrHarian[i].get("jumlah_positif").get("value")
        arr_positif_harian.append(temp)

    # Memasukkan data positif harian ke array data harian dirawat
    arr_dirawat_harian = [2]
    temp = 0
    for j in range(1, len(arrHarian)):
        temp = arrHarian[j].get("jumlah_dirawat").get("value")
        arr_dirawat_harian.append(temp)

    # Memasukkan data positif harian ke array data harian sembuh
    arr_sembuh_harian = [0]
    temp = 0
    for k in range(1, len(arrHarian)):
        temp = arrHarian[k].get("jumlah_sembuh").get("value")
        arr_sembuh_harian.append(temp)

    # Memasukkan data positif harian ke array data harian meninggal
    arr_meninggal_harian = [2]
    temp = 0
    for l in range(1, len(arrHarian)):
        temp = arrHarian[l].get("jumlah_meninggal").get("value")
        arr_meninggal_harian.append(temp)
    
    output_data_harian = f"Jumlah data covid hari ke {indeks} \nJumlah Positif : {arr_positif_harian[indeks-1]} \nJumlah Dirawat : {arr_dirawat_harian[indeks-1]} \nJumlah Sembuh : {arr_sembuh_harian[indeks-1]} \nJumlah Meninggal : {arr_meninggal_harian[indeks-1]} \n"
    return output_data_harian


# User Interface
while(isRunning == True):
    print("="*50)
    print("Data apa yang mau dicari?")
    print("1. Data Total Covid \n2. Data Covid Harian Terbaru\n3. Data Covid pada tanggal tertentu\n4. Keluar")
    print("="*50)
    inputPengguna = int(input("Masukkan pilihan : "))
    print("="*50)
    print("")

    if(inputPengguna == 1):
        print(f"Data Total Covid hingga tanggal {tanggal} : \n" + f"Jumlah Positif : {total_positif}")
        print(f"Jumlah Dirawat : {total_dirawat}")
        print(f"Jumlah Sembuh : {total_sembuh}")
        print(f"Jumlah Meninggal : {total_meninggal}\n")
        print("="*50)
    elif(inputPengguna == 2):
        print(f"Data Penambahan Kasus Covid pada tanggal {tanggal} : \n" + f"Pertambahan Kasus Positif : {penambahan_positif}")
        print(f"Pertambahan Kasus Dirawat : {penambahan_dirawat}")
        print(f"Pertambahan Kasus Sembuh : {penambahan_sembuh}")
        print(f"Pertambahan Kasus Meninggal : {penambahan_meninggal}\n")
        print("="*50)
    elif(inputPengguna == 3) :
        indeks = int(input("Data covid hari ke (02-03-2020 adalah hari ke 1) : "))
        print(PertambahanHarian(indeks))
        print("")
        print("="*50)
    elif(inputPengguna == 4):
        print("")
        print("Thank you for using this application! :D")
        break

    lanjut = input("Ingin mencari data lain? (Y/N) : ").upper()
    if (lanjut == "N"):
        print("")
        print("Thank you for using this application! :D")
        break
    else :
        continue
