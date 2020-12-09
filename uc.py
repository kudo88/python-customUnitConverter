import pickle
import shlex
import os

# Nama aplikasi : Custom Unit Converter 1.0
# Deskripsi : Aplikasi Unit Converter yang Unit-nya bisa ditambah, diubah dan dihapus menyesuaikan kebutuhan
# Pembuat : github.com/kudo88
# Catatan : sertakan file "uc.var", file ini yang menampung data-data kategori dan satuan yang nanti digunakan oleh aplikasi.

header = b"Unit Converter Sederhana :)"
satuan = {None}
selesai = False
dir = os.getcwd()

def desimal(nilai):
  try:
    float(nilai)
    return True
  except ValueError:
    return False

def getAlter(data,kunci):
    try:
        return data[kunci]
    except:
        return None

def pesan(pesan):
    input('\n'+pesan+' ')
    os.system('cls')

def simpanSatuan():
    global satuan
    try:
        with open(dir+'uc.var','wb') as data:
            pickle.dump({'ident':header,'data':satuan}, data)
    except:
        pesan('Terjadi kesalahan ketika sedang menyimpan file data unit,\nperubahan data unit tidak tersiman.')
        
def muatSatuan():
    global satuan, selesai
    try:
        if os.path.exists(dir+'uc.var'):
            with open(dir+'uc.var','rb') as data:
                satuan = pickle.load(data)['data']
    except:
        selesai = True
        pesan('Terjadi kesalahan ketika sedang membuka file data unit,\nmohon hapus file tersebut, lalu jalankan program ini kembali.')

def bantuan():
    teks = """
Selamat datang di aplikasi sederhana Custom Unit Converter (versi 1.0).
Aplikasi ini dibuat, khususnya bagi mereka yang ingin mempelajari Python.

Berikut akan dijelaskan beberapa fungsi baris perintah serta tips yang disediakan aplikasi ini.

BARIS PERINTAH :
0. hitung : melakukan perhitungan konversi
   -> Sintaks : hitung [namaJenis] [nilai] [namaSatuanAsal] [namaSatuanTujuan]
   -> Contoh  : hitung panjang 10 cm mm
   -> Deskr.  : Ini akan mengkonversi nilai '10 cm' menjadi 'mm'
   
1. selesai : menutup aplikasi ini
   -> Sintaks : selesai

2. tolong : menampilkan halaman bantuan ini
   -> Sintaks : tolong
   
3. lihatJenis : berfungsi untuk melihat, jenis / kategori unit apa yang sudah tersimpan disini.
   -> Sintaks : lihatJenis

4. lihatSatuan : berfungsi untuk melihat, satuan apa saja yang sudah tersimpan dalam suatu jenis / kategori.
   -> Sintaks : lihatSatuan [namaJenis]
   -> Contoh  : lihatSatuan panjang
   -> Deskr.  : Ini akan menampilkan semua satuan yang ada pada jenis / kategori 'panjang'
    
5. tambahJenis : berfungsi untuk menambahkan jenis / kategori baru.
   -> Sintaks : tambahJenis [namaJenisBaru]
   -> Contoh  : tambahJenis data
   -> Deskr.  : Ini akan menambahkan jenis / kategori baru bernama 'data'.
    
6. tambahSatuan : berfungsi untuk menambahkan satuan ke suatu jenis / kategori.
   -> Sintaks : tambahSatuan [namaJenis] [namaSatuan] [nilaiSatuan]
   -> Contoh  : tambahSatuan data byte 1
   -> Deskr.  : Ini akan menambahkan satuan baru bernama 'byte' dengan nilai '1' ke jenis / kategori 'data'.
   
7. ubahJenis : berfungsi untuk mengubah nama jenis / kategori.
   -> Sintaks : ubahJenis [namaJenisLama] [namaJenisBaru]
   -> Contoh  : ubahJenis data media
   -> Deskr.  : Ini akan mengubah nama jenis / kategori yang awalnya 'data' menjadi 'media'.
   
8. ubahSatuanNama : berfungsi untuk mengubah nama satuan dalam suatu jenis / kategori.
   -> Sintaks : ubahSatuanNama [namaJenis] [namaSatuanLama] [namaSatuanBaru]
   -> Contoh  : ubahSatuanNama media byte bit
   -> Deskr.  : Ini akan mengubah nama satuan yang awalnya 'byte' menjadi 'bit' yang ada di jenis / kategori 'media'.
   
9. ubahSatuanNilai : berfungsi untuk mengubah nilai satuan dalam suatu jenis / kategori.
   -> Sintaks : ubahSatuanNilai [namaJenis] [namaSatuan] [nilaiSatuanBaru]
   -> Contoh  : ubahSatuanNilai media bit 8
   -> Deskr.  : Ini akan mengubah nilai lama satuan bernama 'bit' sebesar '8' yang ada di jenis / kategori 'media'.
   
10. hapusJenis : berfungsi untuk menghapus suatu jenis / kategori 
                (ini juga akan menghapus seluruh satuan yang ada didalamnya)
   -> Sintaks : hapusJenis [namaJenis]
   -> Contoh  : hapusJenis media
   -> Deskr.  : Ini akan menghapus jenis / kategori yang bernama 'media'.
   
11. hapusSatuan : berfungsi untuk menghapus satuan dalam suatu jenis / kategori.
   -> Sintaks : hapusSatuan [namaJenis] [namaSatuan]
   -> Contoh  : hapusSatuan media bit
   -> Deskr.  : Ini akan menghapus satuan bernama 'bit' yang ada di jenis / kategori 'media'.
   
TIPS :
 -> Sediakan hanya satu patokan yang bernilai 1 (satu) untuk setiap jenis / kategori yang dibuat.
    Misalnya, dalam jenis / kategori 'panjang', 'meter' digunakan sebagai patokan, dan nilainya 1 (satu).
    Satuan yang lain, nilainya menyesuaikan dengan satuan 'meter' tadi. 

 -> Selalu tutup program dengan perintah 'selesai'
"""
    print(teks)
    pesan('Tekan "Enter" jika sudah selesai.')

def evalPerintah(perintah):
    global satuan
    dftPerintah = {'tambahJenis':2,'tambahSatuan':4,'hapusJenis':2,'hapusSatuan':3,'ubahJenis':3,'ubahSatuanNama':4,'ubahSatuanNilai':4,'lihatJenis':1,'lihatSatuan':2,'selesai':1,'hitung':5,'tolong':1}
    listPerintah = shlex.split(perintah)
    if dftPerintah.get(listPerintah[0]) == None:
        pesan(f'Perintah "{listPerintah[0]}" tidak dikenali.')
    elif len(listPerintah) != dftPerintah.get(listPerintah[0]):
        pesan(f'Sintaks untuk perintah "{listPerintah[0]}" salah.')
    else:
        if listPerintah[0] == 'tambahJenis':
            if satuan.get(listPerintah[1]) != None:
                pesan(f'Jenis "{listPerintah[1]}" sudah ada.')
            else:
                satuan[listPerintah[1]] = {'':'Belum ada data'}
        elif listPerintah[0] == 'tambahSatuan': 
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                if getAlter(getAlter(satuan,listPerintah[1]),'') != None:
                   getAlter(satuan,listPerintah[1]).pop('') 
                if getAlter(getAlter(satuan,listPerintah[1]),listPerintah[2]) != None:
                   pesan(f'Satuan "{listPerintah[2]}" di jenis "{listPerintah[1]}" sudah ada.')
                else:
                    if not desimal(listPerintah[3]):
                        pesan(f'Nilai "{listPerintah[3]}" bukanlah angka desimal yang benar.')
                    else:
                        satuan[listPerintah[1]][listPerintah[2]] = listPerintah[3]
        elif listPerintah[0] == 'hapusJenis':
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                satuan.pop(listPerintah[1])
        elif listPerintah[0] == 'hapusSatuan':
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                if getAlter(getAlter(satuan,listPerintah[1]),listPerintah[2]) == None:
                    pesan(f'Satuan "{listPerintah[2]}" di jenis "{listPerintah[1]}" tidak ada.')
                else:
                    getAlter(satuan,listPerintah[1]).pop(listPerintah[2]) 
        elif listPerintah[0] == 'ubahJenis':
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                if satuan.get(listPerintah[2]) != None:
                    pesan(f'Jenis "{listPerintah[2]}" sudah ada.')
                else:
                    satuan[listPerintah[2]] = satuan.pop(listPerintah[1])  
        elif listPerintah[0] == 'ubahSatuanNama':
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                if (satuan.get(listPerintah[1])).get(listPerintah[2]) == None:
                    pesan(f'Satuan "{listPerintah[2]}" di jenis "{listPerintah[1]}" tidak ada.')
                else:
                    satuan[listPerintah[1]][listPerintah[3]] = getAlter(satuan,listPerintah[1]).pop(listPerintah[2])
        elif listPerintah[0] == 'ubahSatuanNilai':
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                if (satuan.get(listPerintah[1])).get(listPerintah[2]) == None:
                    pesan(f'Satuan "{listPerintah[2]}" di jenis "{listPerintah[1]}" tidak ada.')
                else:
                    if not desimal(listPerintah[3]):
                        pesan(f'Nilai "{listPerintah[3]}" bukanlah angka desimal yang benar.')
                    else:
                        satuan[listPerintah[1]][listPerintah[2]] = listPerintah[3] 
        elif listPerintah[0] == 'lihatJenis':
            print(f'\nDaftar jenis yang tersimpan :')
            for a,b in satuan.items():
                print(f'-> {a}')
            pesan('Tekan "Enter" jika sudah selesai.')
        elif listPerintah[0] == 'lihatSatuan':
            if getAlter(satuan,listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            else:
                print(f'\nSatuan pada jenis "{listPerintah[1]}" :')
                for a,b in satuan.get(listPerintah[1]).items():
                    print(f'-> {a} : {b}')
                pesan('Tekan "Enter" jika sudah selesai.')
        elif listPerintah[0] == 'hitung':
            #hitung waktu 10 jam menit
            if satuan.get(listPerintah[1]) == None:
                pesan(f'Jenis "{listPerintah[1]}" tidak ada.')
            elif not desimal(listPerintah[2]):
                pesan(f'Nilai "{listPerintah[2]}" bukanlah angka desimal yang benar.')
            elif getAlter(getAlter(satuan,listPerintah[1]),listPerintah[3]) == None:
                pesan(f'Satuan "{listPerintah[3]}" di jenis "{listPerintah[1]}" tidak ada.')
            elif getAlter(getAlter(satuan,listPerintah[1]),listPerintah[4]) == None:
                pesan(f'Satuan "{listPerintah[4]}" di jenis "{listPerintah[1]}" tidak ada.')
            else:
                hasil = float(listPerintah[2])*float((satuan.get(listPerintah[1])).get(listPerintah[3]))/float((satuan.get(listPerintah[1])).get(listPerintah[4]))
                print(f'\n{listPerintah[2]} {listPerintah[3]} sama dengan {hasil} {listPerintah[4]}')
                pesan('Tekan "Enter" untuk melanjutkan.')
        elif listPerintah[0] == 'tolong':
            os.system('cls')
            bantuan()
        os.system('cls')
        simpanSatuan()
                
os.system('cls')
muatSatuan()
while not selesai:
    print('Custom Unit Converter 1.0, Oleh github.com/kudo88')
    print('Masukkan perintah anda, isikan "tolong" untuk menampilkan bantuan.')
    perintah = input('> ')
    selesai = (perintah == 'selesai')
    evalPerintah(perintah)
