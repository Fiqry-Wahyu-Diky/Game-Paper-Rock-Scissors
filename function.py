# function
brain = {1:"Gunting",2:"Batu",3:"Kertas"}
def Ai(user,com):
  if user > com:
    result = (f'''
  Anda memilih = {brain[user]}
  Komputer = {brain[com]}
  {brain[user]} melawan {brain[com]}
  Result : Anda MENANG
    ''')
  elif user == com:
    result = (f'''
  Anda memilih = {brain[user]}
  Komputer = {brain[com]}
  {brain[user]} melawan {brain[com]}
  Result : Anda SERI
    ''')
  else:
    result = (f'''
  Anda memilih = {brain[user]}
  Komputer = {brain[com]}
  {brain[user]} melawan {brain[com]}
  Result : Anda KALAH
    ''')
  return result

