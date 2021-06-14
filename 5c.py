ulang = "y"
while ulang=="y" or ulang=="Y":
    print("===========================")
    print(" Menampilkan Nilai Huruf")
    print("===========================")
    n=1
    while n>=0 and n<=100:
        u = input(" Masukkan Nilai = ")
        n=int(u)
        if n>=0 and n<=100:
            if n>80:      
                sts=" Baik Sekali"
            elif n>=65:    
                sts=" Baik"
            elif n>=55:    
                sts=" Cukup"
            elif n>=40:    
                sts=" Kurang"
            else:               
                sts=" Kurang Sekali"
            print (sts)
            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break
    else:
        pesan=" Masukkan kembali angka nilai antara 0-100"
        print(pesan)
        print()   