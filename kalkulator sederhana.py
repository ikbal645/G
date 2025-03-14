# kalkulator sederhana
# inputan dari user
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

# menentukan operasi
operasi = input("Masukkan operasi (+, -, *, /): ")

# melakukan operasi
if operasi == "+":
    hasil = num1 + num2
    print(f"Hasil: {num1} + {num2} = {hasil}")
elif operasi == "-":
    hasil = num1 - num2
    print(f"Hasil: {num1} - {num2} = {hasil}")
elif operasi == "*":
    hasil = num1 * num2
    print(f"Hasil: {num1} * {num2} = {hasil}")
elif operasi == "/":
    if num2 == 0:
        print("Hasil: Pembagian dengan nol adalah tak terdefinisi.")
    else:
        hasil = num1 / num2
        print(f"Hasil: {num1} / {num2} = {hasil}")
else:
    print("Operasi tidak valid. Silakan masukkan salah satu dari +, -, *, /.")