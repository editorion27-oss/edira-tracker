import streamlit as st
import sqlite3

# --- KONEKSI DATABASE ---
def connect_db():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    return conn

# --- MENU UTAMA (Gunakan Sidebar) ---
def main():
    st.title("Aplikasi Expense Tracker EDIRA")

    # Navigasi menggunakan sidebar di sebelah kiri
    menu = ["Tambah Data", "Lihat Data", "Edit Data", "Hapus Data"]
    pilihan = st.sidebar.selectbox("Pilih Menu", menu)

    if pilihan == "Tambah Data":
        st.subheader("Tambah Transaksi Baru")
        # Contoh input ala Streamlit
        tanggal = st.date_input("Pilih Tanggal")
        kategori = st.selectbox("Kategori", ["Makanan", "Transportasi", "Hiburan"])
        tipe = st.radio("Tipe", ["Pemasukan", "Pengeluaran"])
        nominal = st.number_input("Nominal", min_value=0)
        
        if st.button("Simpan Data"):
            # Panggil fungsi tambah_data kamu di sini
            st.success("Data berhasil disimpan!")

    elif pilihan == "Lihat Data":
        st.subheader("Data Transaksi")
        # Panggil fungsi lihat_data kamu di sini
        st.info("Fitur Lihat Data akan tampil di sini")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()