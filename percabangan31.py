#Format inputan salah pada contoh 3.1
suhu = input("Masukkan suhu tubuh: ")

try:
    suhu = int(suhu)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
        
except:
    print("Inputan anda salah")