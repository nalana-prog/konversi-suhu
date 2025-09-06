# =========================
# suhu.py
# Modul konversi suhu
# =========================

def konversi_suhu(suhu, dari, ke):
    suhu = float(suhu)
    dari = dari.upper()
    ke = ke.upper()

    if dari not in ['c','f','k']:
       return "Eror: satuan asal tidak valid, gunakann c, f, atau k"
    if ke not in ['c','f','k']:
       return "Eror: satuan tujuan tidak valid, gunakann C, F, atau K"


    if dari == 'C':
        if ke == 'F':
            return (suhu * 9/5) + 32
        elif ke == 'K':
            return suhu + 273.15
        elif ke == 'C':
            return suhu

    elif dari == 'F':
        if ke == 'C':
            return (suhu - 32) * 5/9
        elif ke == 'K':
            return (suhu - 32) * 5/9 + 273.15
        elif ke == 'F':
            return suhu

    elif dari == 'K':
        if ke == 'C':
            return suhu - 273.15
        elif ke == 'F':
            return (suhu - 273.15) * 9/5 + 32
        elif ke == 'K':
            return suhu
    elif ke == 'K' and hasil < 0:
    return "Eror: nilai suhu tidak valid"

