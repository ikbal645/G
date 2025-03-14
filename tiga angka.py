angka1  = int(input('masukan angka :'))
angka2 = int(input('masukan angka :'))
angka3 = int(input('masukan angka :'))
# MENCARI NILAI TERBESAR
if angka1 >= angka2 and angka1 >= angka3:
    print(angka1, "adalah nilai terbesar")
elif angka2 >= angka1 and angka2 >= angka3:
    print(angka2, "adalah nilai terbesar")
elif angka3 >= angka1 and angka3 >= angka2:
    print(angka3, "adalah nilai terbesar")
