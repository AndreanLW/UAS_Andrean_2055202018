import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="datasetandrean"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM perpustakaan"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["id", "kode_provinsi", "nama_provinsi", "kode_kabupaten_kota", "nama_kabupaten_kota", "jumlah_perpustakaan", "satuan", "tahun"])

 

# Simpan dataframe sebagai file CSV

df.to_csv("dispusipda-od_18301_jumlah_perpustakaan_umum_berdasarkan_kabupatenkota_data.csv", index=False)

 

print("Data telah disimpan dalam file CSV 'dispusipda-od_18301_jumlah_perpustakaan_umum_berdasarkan_kabupatenkota_data.csv'") #csv / xlsx

 