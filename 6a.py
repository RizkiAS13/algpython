ulang="y"
while ulang=="y" or ulang =="Y":
    print("===========================")
    print(" Pembelian printer")
    print("===========================")
    u=1
    u =input(" Masukkan Banyak Printer = ")
    n=int(u)
    harga = n * 660000
    print(" Total Harga Pembelian Printer= Rp.",harga)
    ulang = input(" Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break