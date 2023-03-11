import random
import function as fungsi

# code
print('''
  +======= +-+-+-+-+-+-+-+ ========+
  | Selamat Datang Dipermainan ini |
  +======= +-+-+-+-+-+-+-+ ========+ ''')
kondisi = True
while kondisi:
    print('''
  +======= +-+-+-+-+-+-+-+ ========+
  |           1. Gunting           |
  |           2. Batu              |
  |           3. Kertas            |
  +======= +-+-+-+-+-+-+-+ ========+
  ''')
    users = int(input(" Masukkan angka pilihan anda : "))
    com = random.randint(1, 3)
    if users > 3:
        print('''
    !!! maaf anda salah input ''')
    else:
        print(fungsi.Ai(users, com))
        ask = input("apakah ingin bermain lagi?y/n : ")
        if ask == 'y':
            kondisi = True
        else:
            break
