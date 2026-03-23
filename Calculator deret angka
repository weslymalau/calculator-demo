import tkinter as tk

def hitung_aritmatika():
    try:
        a = float(entry_a.get())
        d = float(entry_d.get())
        n = int(entry_n.get())

        hasil = (n / 2) * (2 * a + (n - 1) * d)
        label_hasil.config(text=f"Hasil: {hasil}")

    except:
        label_hasil.config(text="Input salah!")


def hitung_geometri():
    try:
        a = float(entry_a.get())
        r = float(entry_d.get())  # pakai field d sebagai r
        n = int(entry_n.get())

        if r == 1:
            hasil = a * n
        else:
            hasil = a * (r**n - 1) / (r - 1)

        label_hasil.config(text=f"Hasil: {hasil}")

    except:
        label_hasil.config(text="Input salah!")


# Window
root = tk.Tk()
root.title("Kalkulator Deret")
root.geometry("300x300")

# Input
tk.Label(root, text="Suku pertama (a)").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Beda / Rasio (d / r)").pack()
entry_d = tk.Entry(root)
entry_d.pack()

tk.Label(root, text="Jumlah suku (n)").pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Button
tk.Button(root, text="Hitung Aritmatika", command=hitung_aritmatika).pack(pady=5)
tk.Button(root, text="Hitung Geometri", command=hitung_geometri).pack(pady=5)

# Output
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.pack(pady=10)

root.mainloop()
