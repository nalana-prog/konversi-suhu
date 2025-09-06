#Rumus Konversi Suhu
def celsius_ke_fahrenheit(c):
  return (c * 9/5) + 32

def celsius_ke_kelvin(c):
  return c + 273.15

def fahrenheit_ke_celsius(f):
  return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
  return (fahrenheit_ke_celsius(f) + 273.15)

def kelvin_ke_celsius(k):
  return k - 273.15

def kelvin_ke_fahrenheit(k):
  return (kelvin_ke_celsius(k) * 9/5) + 32

#Pemilihan Rumus Konversi

if dari == "C" and ke == "F":
  hasil = celsius_ke_fahrenheit(suhu)
elif dari == "C" and ke == "K":
  hasil = celsius_ke_kelvin(suhu)
elif dari == "F" and ke == "C":
  hasil = fahrenheit_ke_celsius(suhu)
elif dari == "F" and ke == "K":
  hasil = fahrenheit_ke_kelvin(suhu)
elif dari == "K" and ke == "C":
  hasil = kelvin_ke_celsius(suhu)
elif dari == "K" and ke == "F":
  hasil = kelvin_ke_fahrenheit(suhu)
else:
    print("Satuan suhu tidak valid.")

#Hasil Konversi
print(f"Hasil konversi: {suhu}° {dari} = {hasil}° {ke}")
