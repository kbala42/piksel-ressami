import numpy as np
import matplotlib.pyplot as plt

# 1. Matris Tanımlama (Resmi Sayılarla Çiziyoruz)
# Burası 8x8'lik bir ızgara.
# 0: Siyah (Arka Plan), 1: Sarı (Çizim)
# Bir "Gülen Yüz" tasarlayalım:

resim_matrisi = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0], # Gözler
    [0, 1, 1, 0, 0, 1, 1, 0], # Gözler
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0], # Burun
    [1, 0, 0, 0, 0, 0, 0, 1], # Ağız kenarları
    [0, 1, 1, 1, 1, 1, 1, 0], # Gülümseme
    [0, 0, 0, 0, 0, 0, 0, 0]
])

print("🤖 Bilgisayar bu resmi şöyle görüyor (Sayısal Matris):")
print(resim_matrisi)

# 2. Terminalde Görselleştirme (ASCII Sanatı)
print("\n👀 İnsan gözü için önizleme:")
for satir in resim_matrisi:
    satir_gorsel = ""
    for piksel in satir:
        if piksel == 1:
            satir_gorsel += "🟨"  # 1 olan yerlere Sarı Kare
        else:
            satir_gorsel += "⬛"  # 0 olan yerlere Siyah Kare
    print(satir_gorsel)

# 3. Profesyonel Çıktı (PNG Olarak Kaydetme)
# Matplotlib kütüphanesi ile sayıları renklere dönüştürüyoruz
plt.figure(figsize=(5, 5))
plt.imshow(resim_matrisi, cmap='cividis') # 'cividis', 'gray', 'plasma' deneyebilirsin
plt.title("Yapay Zeka Görusu: 8x8 Matris")
plt.axis('off') # Eksenleri (x,y sayılarını) kapat

# Dosyayı kaydet
dosya_adi = "piksel_yuzu.png"
plt.savefig(dosya_adi)

print(f"\n✅ Resim oluşturuldu! '{dosya_adi}' dosyasına tıklayıp bakabilirsin.")