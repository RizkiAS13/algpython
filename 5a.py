ulang="y"
while ulang=="y" or ulang =="Y":
    print("===========================")
    print(" CEK KELULUSAN")
    print("===========================")
    m=1
    while m>0 and m<=100:
        n = input("Masukan Nilai = ")
        m = int(n)
        if m>=0 and m<=100:
            if m>60:
                sts = "Lulus"
            else:
                sts = "Ulang"
            print (sts)
            ulang=input("Ingin Mengecek Kembali? y/t =")
            if ulang=="t" or ulang =="T":
                break
        else: 
            pesan="Masukan Kembali Angka Usia Antara 0-100"
            print(pesan)
            print()

