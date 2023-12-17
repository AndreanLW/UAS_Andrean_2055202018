# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="datasetandrean"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'perpustakaan'

create_table_query = """

CREATE TABLE perpustakaan (

    id INT,

    kode_provinsi INT,

    nama_provinsi VARCHAR(30),

    kode_kabupaten_kota INT,

    nama_kabupaten_kota VARCHAR(50),

    jumlah_perpustakaan INT,

    satuan VARCHAR(30),

    tahun INT

)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()