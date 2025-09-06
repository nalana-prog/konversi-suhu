#Rumus Konversi Suhu
def celsius_ke_fahrenheit(suhu):
  return (suhu * 9/5) + 32

def celsius_ke_kelvin(suhu):
  return suhu + 273.15

def fahrenheit_ke_celsius(suhu):
  return (suhu - 32) * 5/9

def fahrenheit_ke_kelvin(suhu):
  return (fahrenheit_ke_celsius(suhu) + 273.15)

def kelvin_ke_celsius(suhu):
  return suhu - 273.15

def kelvin_ke_fahrenheit(suhu):
  return (kelvin_ke_celsius(suhu) * 9/5) + 32

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

