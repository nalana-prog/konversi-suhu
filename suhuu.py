#Rumus Konversi Suhu
if dari == 'C':
    if ke == 'F':
        hasil = (suhu * 9/5) + 32
    elif ke == 'K':
        hasil = suhu + 273.15
    elif ke == 'C':
        hasil = suhu
    else:
        hasil = "Invalid target unit"
elif dari == 'F':
    if ke == 'C':
        hasil = (suhu - 32) * 5/9
    elif ke == 'K':
        hasil = (suhu - 32) * 5/9 + 273.15
    elif ke == 'F':
        hasil = suhu
    else:
        hasil = "Invalid target unit"
elif dari == 'K':
    if ke == 'C':
        hasil = suhu - 273.15
    elif ke == 'F':
        hasil = (suhu - 273.15) * 9/5 + 32
    elif ke == 'K':
        hasil = suhu
    else:
        hasil = "Invalid target unit"
else:
    hasil = "Invalid source unit"
