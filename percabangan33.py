bulan = input("Masukkan bulan(1-12): ")
try:
    bulan = int(bulan)
    if bulan == 1:
        print("Januari, jumlah hari: 31")
    
    elif bulan == 2:
        print("Februari, jumlah hari: 29")
        
    elif bulan == 3:
        print("Maret, jumlah hari: 31")

    elif bulan == 4:
        print("April, jumlah hari: 30")

    elif bulan == 5:
        print("Mei, jumlah hari: 31")
        
    elif bulan == 6:
        print("Juni, jumlah hari: 30")

    elif bulan == 7:
        print("Juli, jumlah hari: 31")

    elif bulan == 8:
        print("Agustus, jumlah hari: 31")

    elif bulan == 9:
        print("September, jumlah hari: 30")
        
    elif bulan == 10:
        print("Oktober, jumlah hari: 31")
        
    elif bulan == 11:
        print("November, jumlah hari: 30")
        
    elif bulan == 12:
        print("Desember, jumlah hari: 31")
        
    else:
        print("Bulan tidak ada!")

except:
    print("Format salah!")    
