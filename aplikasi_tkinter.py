import tkinter as tk  


def prediksi_prodi():
    # periksa apakah semua input di entry_list telah diisi
    for entry in entry_list:
        if not entry.get(): 
            hasil_label.config(text="Error: nguawur cik", fg="red")
            return  # Hentikan fungsi jika ada yang kosong

    # Jika semua input terisi, ubah hasil_label untuk menampilkan hasil prediksi
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi", fg="black")


root = tk.Tk()  # bikin jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  
root.geometry("400x600")  


judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
# bikin label judul di bagian atas dengan .pack()
judul_label.pack(pady=10)  

# Frame utama untuk menampung semua label dan input secara vertikal
frame = tk.Frame(root)  # pake Frame untuk mengelompokkan widget
frame.pack(pady=10)  # Menempatkan frame dengan jarak vertikal 10 piksel dari elemen lainnya

# Input nilai mata pelajaran
entry_list = []  # pake list untuk widget entry (input teks)
for i in range(10):  # Loop untuk membuat 10 input nilai mata pelajaran
    # Sub-frame untuk setiap pasangan label dan entry mata pelajaran
    sub_frame = tk.Frame(frame)  # Membuat sub-frame untuk setiap baris input
    sub_frame.pack(pady=5)  # Menambahkan jarak vertikal antara setiap input

    # bikin Label untuk setiap mata pelajaran, menggunakan f-string untuk menampilkan angka pelajaran
    label = tk.Label(sub_frame, text=f"Nilai Mata Pelajaran {i+1}:")
    # .pack(side="left") menempatkan label di sebelah kiri dalam sub-frame
    label.pack(side="left", padx=10)  # padx=10 menambahkan jarak horizontal antara label dan frame

    # bikin entry untuk input nilai mata pelajaran
    entry = tk.Entry(sub_frame)  # Membuat kotak input teks (entry) untuk pengguna
    entry.pack(side="right")  # Menempatkan entry di sebelah kanan dalam sub-frame
    entry_list.append(entry)  # Menambahkan entry ke list agar bisa diakses nanti

# Membuat tombol "Hasil Prediksi" dengan .Button() dan mengaitkan fungsi prediksi_prodi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
# .pack() untuk menempatkan tombol di bawah semua input
prediksi_button.pack(pady=10)  # pady=10 menambahkan jarak vertikal antara tombol dan elemen lainnya

# Membuat Label hasil prediksi atau pesan error
hasil_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
# .pack() menempatkan label hasil di bagian bawah
hasil_label.pack(pady=10)  # pady=10 menambahkan jarak vertikal di sekitar label hasil

#jalanin program
root.mainloop()  
