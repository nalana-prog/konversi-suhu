def konversi_suhu(nilai, dari, ke):
    nilai = float(nilai)
    dari = dari.upper()
    ke = ke.upper()

    if dari == 'C':
        if ke == 'F':
            hasil = (nilai * 9/5) + 32
        elif ke == 'K':
            hasil = nilai + 273.15
        elif ke == 'C':
            hasil = nilai
        else:
            hasil = "Invalid target unit"

    elif dari == 'F':
        if ke == 'C':
            hasil = (nilai - 32) * 5/9
        elif ke == 'K':
            hasil = (nilai - 32) * 5/9 + 273.15
        elif ke == 'F':
            hasil = nilai
        else:
            hasil = "Invalid target unit"

    elif dari == 'K':
        if ke == 'C':
            hasil = nilai - 273.15
        elif ke == 'F':
            hasil = (nilai - 273.15) * 9/5 + 32
        elif ke == 'K':
            hasil = nilai
        else:
            hasil = "Invalid target unit"
    else:
        hasil = "Invalid source unit"

    return hasil
