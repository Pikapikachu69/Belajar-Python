import datetime as dt

print("=" * 10 + " PENGECEKAN HARI LAHIR " + "="*10)

print("Masukan Tanggal Lahir anda")
hari = int(input("Masukan Hari  : "))
bulan = int(input("Masukan Bulan : "))
tahun = int(input("Masukan Tahun : "))

tanggal_lahir = dt.date(tahun,bulan,hari)

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print("\n" + "=" * 10 + " HASIL PENGECEKAN " + "="*10)
print(f"Tanggal lahir   anda adalah       : {tanggal_lahir}")
print(f"Hari lahir      anda adalah       : {tanggal_lahir:%A}")
print(f"Umur            anda adalah       : {umur_tahun}")