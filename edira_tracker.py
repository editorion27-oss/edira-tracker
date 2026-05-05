import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("database.db")

def init_db():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS transaksi(id INTEGER PRIMARY KEY AUTOINCREMENT, tanggal TEXT, kategori TEXT, tipe TEXT, nominal INTEGER)""")
    conn.commit()
    conn.close()
    
def tambah_data():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    kategori = input("Kategori (makanan/transportasi/hiburan): ")
    tipe = input("Tipe (pemasukan/pengeluaran): ")
    nominal = int(input("Nominal: "))
    
    conn = connect_db()
    conn.execute("INSERT INTO transaksi (tanggal,kategori,tipe,nominal)Values (?,?,?,?)",(tanggal, kategori, tipe, nominal))
    conn.commit()
    conn.close()
    print("✅ Data berhasil ditambahkan!")
    
def lihat_data():
    conn = connect_db()
    data = conn.execute("SELECT * FROM transaksi").fetchall()
    
    saldo = 0
    print("\n=== DATA TRANSAKSI ===")
    for d in data:
        print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | Rp{d[4]}")

        if d[3] == "pemasukan":
            saldo += d[4]
        else:
            saldo -= d[4]

    print(f"\n💰 Total Saldo: Rp{saldo}")
    conn.close()
    
def edit_data():
    id_data = input("Masukkan ID yang mau diedit: ")

    tanggal = input("Tanggal baru: ")
    kategori = input("Kategori baru: ")
    tipe = input("Tipe baru: ")
    nominal = int(input("Nominal baru: "))

    conn = connect_db()
    conn.execute("""
        UPDATE transaksi 
        SET tanggal=?, kategori=?, tipe=?, nominal=? 
        WHERE id=?
    """, (tanggal, kategori, tipe, nominal, id_data))

    conn.commit()
    conn.close()
    print("✏️ Data berhasil diupdate!")
    
def hapus_data():
    id_data = input("Masukkan ID yang mau dihapus: ")

    conn = connect_db()
    conn.execute("DELETE FROM transaksi WHERE id=?", (id_data,))
    conn.commit()
    conn.close()
    print("🗑️ Data berhasil dihapus!")
    
def menu():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid!")
            
if __name__ == "__main__":
    init_db()
    menu()