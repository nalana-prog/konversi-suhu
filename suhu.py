# =========================
# suhu.py
# Modul konversi suhu
# =========================

def konversi_suhu(suhu, dari, ke):
    suhu = float(suhu)
    dari = dari.upper()
    ke = ke.upper()

    # Validasi input
    if dari not in ['C','F','K']:
        return "Error: satuan asal tidak valid, gunakan C, F, atau K"
    if ke not in ['C','F','K']:
        return "Error: satuan tujuan tidak valid, gunakan C, F, atau K"

    # Konversi
    if dari == 'C':
        if ke == 'F':
            result = (suhu * 9/5) + 32
        elif ke == 'K':
            result = suhu + 273.15
        else:
            result = suhu

    elif dari == 'F':
        if ke == 'C':
            result = (suhu - 32) * 5/9
        elif ke == 'K':
            result = (suhu - 32) * 5/9 + 273.15
        else:
            result = suhu

    elif dari == 'K':
        if ke == 'C':
            result = suhu - 273.15
        elif ke == 'F':
            result = (suhu - 273.15) * 9/5 + 32
        else:
            result = suhu

    # Validasi suhu Kelvin tidak negatif
    if ke == 'K' and result < 0:
        return "Error: nilai suhu tidak valid (Kelvin tidak bisa negatif)"

    return result
