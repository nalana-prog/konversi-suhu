def konversi_suhu(suhu, dari, ke):
  suhu = float(suhu)
  dari = dari.lower()
  ke = ke.lower()

  if dari == 'c':
    if ke == 'f':
      return suhu * 9/5 + 32
    elif ke == 'k':
      return suhu + 273.15
    else:
      return suhu

  if dari == 'f':
    if ke == 'c':
      return (suhu - 32) * 5/9
    elif ke == 'k':
      return (suhu - 32) * 5/9 + 273.15
    else:
      return suhu

  if dari == 'k':
    if ke == 'c':
      return suhu - 273.15
    elif ke == 'f':
      return (suhu - 273.15) * 9/5 + 32
    else:
      return suhu

