#suhuu.py

def konversi_suhu(suhu, dari, ke):
    suhu = float(suhu)
    dari = dari.upper()
    ke = ke.upper()

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

    return "Satuan tidak valid!"
