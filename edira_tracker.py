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
    conn = connect_db()
    c = conn.cursor()
    # Pastikan nama kolom sesuai dengan tabel transaksi kamu
    c.execute("INSERT INTO transaksi (tanggal, kategori, tipe, nominal) VALUES (?, ?, ?, ?)", 
              (str(tanggal), kategori, tipe, nominal))
    conn.commit()
    conn.close()
    st.success("Data berhasil disimpan ke database!")

    elif pilihan == "Lihat Data":
    st.subheader("Data Transaksi")
    conn = connect_db()
    # Mengambil data menggunakan pandas agar rapi
    df = pd.read_sql_query("SELECT * FROM transaksi", conn)
    conn.close()

    if not df.empty:
        st.dataframe(df) # Menampilkan tabel interaktif
    else:
        st.warning("Belum ada data transaksi.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()