import tkinter as tk
from tkinter import messagebox

total_belanja = 0

def tambah_barang():
    global total_belanja

    try:
        nama = entry_nama.get()
        harga = int(entry_harga.get())
        jumlah = int(entry_jumlah.get())

        subtotal = harga * jumlah
        total_belanja += subtotal

        label_total.config(text=f"Total Belanja: Rp {total_belanja}")

        listbox.insert(tk.END, f"{nama} - {jumlah} x {harga} = {subtotal}")

        entry_nama.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Harga dan jumlah harus angka!")

# Membuat jendela
root = tk.Tk()
root.title("Aplikasi Kasir Mini")
root.geometry("400x450")

# Judul
judul = tk.Label(root, text="APLIKASI KASIR MINI", font=("Arial", 16, "bold"))
judul.pack(pady=10)

# Input Nama Barang
tk.Label(root, text="Nama Barang").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Input Harga
tk.Label(root, text="Harga").pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

# Input Jumlah
tk.Label(root, text="Jumlah").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol Tambah
btn_tambah = tk.Button(root, text="Tambah Barang", command=tambah_barang)
btn_tambah.pack(pady=10)

# List Barang
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Total Belanja
label_total = tk.Label(root, text="Total Belanja: Rp 0", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()