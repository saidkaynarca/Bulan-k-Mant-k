import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
from fpdf import FPDF

def pdf_kaydet(sulama, gubre, kontrol):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Tarim Destek Sistemi Raporu", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Sulama Suresi: %{sulama:.1f}", ln=True)
        pdf.cell(200, 10, txt=f"Gubre Miktari: %{gubre:.1f}", ln=True)
        pdf.cell(200, 10, txt=f"Topragin Kontrol Ihtiyaci: %{kontrol:.1f}", ln=True)

        dosya_adi = "tarim_destek_raporu.pdf"
        pdf.output(dosya_adi)
    except Exception as e:
        messagebox.showerror("PDF Hatasi", f"PDF olusturulamadi:\n{str(e)}")

def oran_hesapla(nem, sicaklik, gunes, ruzgar, urun):
    sulama = (nem * 1.5 + (10 - ruzgar) * 1.2 + sicaklik * 0.8) / 3.5
    gubre = ((gunes + urun) * 1.2 + ruzgar * 0.5) / 2.9
    kontrol = ((10 - gunes) + urun + (10 - sicaklik)) / 3

    toplam = sulama + gubre + kontrol
    sulama = sulama / toplam * 100
    gubre = gubre / toplam * 100
    kontrol = kontrol / toplam * 100
    return sulama, gubre, kontrol

def grafik_goster(s, g, k):
    try:
        destek_grafigi, ax = plt.subplots(figsize=(7.5, 5))  # genişlik 7.5 yapıldı
        icerikler = ['Sulama Süresi', 'Gübre Miktarı', 'Toprağın Kontrol İhtiyacı']
        oranlar = [s, g, k]
        renkler = ['#aed9e0', '#70c1b3', '#b2dbbf']

        ax.pie(oranlar, labels=icerikler, autopct='%1.1f%%', colors=renkler, startangle=90)
        ax.axis('equal')
        plt.title("Tarım Destek Dağılımı", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Grafik gösterilirken hata oluştu:", e)

def hesapla(event=None):
    try:
        girdi_degerleri = []
        for entry in girisler:
            deger = entry.get()
            if deger == "":
                messagebox.showerror("Eksik Girdi", "Lütfen tüm alanlara 0 ile 10 arasında geçerli sayılar giriniz.")
                return
            girdi_degerleri.append(int(deger))
        
        if any(deger < 0 or deger > 10 for deger in girdi_degerleri):
            raise ValueError

        sulama, gubre, kontrol = oran_hesapla(*girdi_degerleri)
        sonuc_etiketi.config(
            text=f"\nTopraginiz icin onerilen destek oranlari:\n\nSulama Suresi: %{sulama:.1f}\nGubre Miktari: %{gubre:.1f}\nToprakin Kontrol Ihtiyaci: %{kontrol:.1f}\n\nBu oranlar, girdiginiz verilere gore otomatik hesaplanmistir."
        )
        grafik_goster(sulama, gubre, kontrol)
        pdf_kaydet(sulama, gubre, kontrol)

    except ValueError:
        messagebox.showerror("Gecersiz Girdi", "Lütfen tüm alanlara 0 ile 10 arasında geçerli sayılar giriniz.")

pencere = tk.Tk()
pencere.title("Tarim Destek Sistemi")
pencere.geometry("500x550")
pencere.configure(bg="#e0f7fa")
pencere.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure("Custom.TEntry",
                foreground="black",
                fieldbackground="#ffcc80",
                background="#ffcc80",
                padding=5,
                relief="flat")

style.configure("Custom.TButton",
                font=('Helvetica', 12, 'bold'),
                background="#a5d6a7",
                foreground="black",
                padding=10)

frame = tk.Frame(pencere, bg="#e0f7fa", bd=2)
frame.pack(pady=30, padx=20)

etiketler = ["Toprak Nemi", "Sicaklik", "Gunes Isigi", "Ruzgar", "Urun Turu"]
girisler = []

def odakla_sonra(event, index):
    if index < len(girisler):
        girisler[index].focus()
    else:
        hesapla()

for i, etiket in enumerate(etiketler):
    l = tk.Label(frame, text=etiket + " (0-10)", bg="#e0f7fa", fg="black", font=('Helvetica', 11, 'bold'))
    l.grid(row=i, column=0, sticky="w", padx=10, pady=5)
    e = ttk.Entry(frame, style="Custom.TEntry", width=10)
    e.grid(row=i, column=1, pady=5, padx=10)
    girisler.append(e)
    
    # Enter tuşuna basıldığında odak sıradaki entry'e geçsin, en son kutuda Enter'a basınca hesapla
    def odakla_sonra(event, index=i):
        if index + 1 < len(girisler):
            girisler[index + 1].focus()
        else:
            hesapla()

    e.bind("<Return>", odakla_sonra)

hesapla_btn = ttk.Button(pencere, text="HESAPLA", style="Custom.TButton", command=hesapla)
hesapla_btn.pack(pady=20)



sonuc_etiketi = tk.Label(pencere, text="", bg="#e0f7fa", fg="black", font=('Helvetica', 11))
sonuc_etiketi.pack(pady=10)

pencere.mainloop()
