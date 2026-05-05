import sqlite3
import streamlit as st
st.title("Aplikasi Expense Tracker EDIRA")
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
    tanggal = st.number_input("Tanggal (YYYY-MM-DD): ")
    kategori = st.text_input("Kategori (makanan/transportasi/hiburan): ")
    tipe = st.text_input("Tipe (pemasukan/pengeluaran): ")
    nominal = int(st.number_input("Nominal: "))
    
    conn = connect_db()
    conn.execute("INSERT INTO transaksi (tanggal,kategori,tipe,nominal)Values (?,?,?,?)",(tanggal, kategori, tipe, nominal))
    conn.commit()
    conn.close()
    st.write("✅ Data berhasil ditambahkan!")
    
def lihat_data():
    conn = connect_db()
    data = conn.execute("SELECT * FROM transaksi").fetchall()
    
    saldo = 0
    st.write("\n=== DATA TRANSAKSI ===")
    for d in data:
        st.write(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | Rp{d[4]}")

        if d[3] == "pemasukan":
            saldo += d[4]
        else:
            saldo -= d[4]

    st.write(f"\n💰 Total Saldo: Rp{saldo}")
    conn.close()
    
def edit_data():
    id_data = st.number_input("Masukkan ID yang mau diedit: ")

    tanggal = st.number_input("Tanggal baru: ")
    kategori = st.text_input("Kategori baru: ")
    tipe = st.text_input("Tipe baru: ")
    nominal = int(st.number_input("Nominal baru: "))

    conn = connect_db()
    conn.execute("""
        UPDATE transaksi 
        SET tanggal=?, kategori=?, tipe=?, nominal=? 
        WHERE id=?
    """, (tanggal, kategori, tipe, nominal, id_data))

    conn.commit()
    conn.close()
    st.write("✏️ Data berhasil diupdate!")
    
def hapus_data():
    id_data = st.write("Masukkan ID yang mau dihapus: ")

    conn = connect_db()
    conn.execute("DELETE FROM transaksi WHERE id=?", (id_data,))
    conn.commit()
    conn.close()
    st.write("🗑️ Data berhasil dihapus!")
    
def menu():
    while True:
        st.write("\n=== EXPENSE TRACKER ===")
        st.write("1. Tambah Data")
        st.write("2. Lihat Data")
        st.write("3. Edit Data")
        st.write("4. Hapus Data")
        st.write("5. Keluar")

        pilihan = st.number_input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            st.write("Terima kasih!")
            break
        else:
            st.write("❌ Pilihan tidak valid!")
            
if __name__ == "__main__":
    init_db()
    menu()