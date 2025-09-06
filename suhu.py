# =========================
# suhu.py
# Modul konversi suhu
# =========================

def konversi_suhu(suhu, dari, ke):
    suhu = float(suhu)
    dari = dari.upper()
    ke = ke.upper()

    if dari == 'C':
        if ke == 'F':
            hasil = (suhu * 9/5) + 32
        elif ke == 'K':
            hasil = suhu + 273.15
        else:
            hasil = suhu

    elif dari == 'F':
        if ke == 'C':
            hasil = (suhu - 32) * 5/9
        elif ke == 'K':
            hasil = (suhu - 32) * 5/9 + 273.15
        else:
            hasil = suhu

    elif dari == 'K':
        if ke == 'C':
            hasil = suhu - 273.15
        elif ke == 'F':
            hasil = (suhu - 273.15) * 9/5 + 32
        else:
            hasil = suhu

    else:
        return "Error: satuan asal tidak valid"

    
    if ke == 'K' and hasil < 0:
        return "Error: nilai suhu tidak valid (Kelvin < 0)"

    return hasil
