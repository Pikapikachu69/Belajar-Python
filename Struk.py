# MEMBUAT STRUK BELANJA
import datetime

waktu = datetime.datetime.now().strftime("%X")
tanggal = datetime.datetime.now().strftime("%x")


namakasir = input("Masukan nama kasir : ")
# Tampilan awal
print(f"""
PT INDOMARCO PRISMATAMA      |===============|
GEDUNG MENARA INDOMARET      |==|INDOMARET|==|
BOULEVARD PANTAI INDAH KAPUK |===============|
JAKARTA UTARA
NPWP.01.337.994.6-092.000

             YOS SUDARSO
        JL. YOS SUDARSO NO. 12
          KOTA SORONG, 98413
----------------------------------------
    {tanggal}-{waktu} 935349/{namakasir}/01
----------------------------------------
""")
# 
hargatotal = 0
jumlahbelanjaan = 0
tambahbarang = input("Apakah ingin mengscan barang (y/n) ? \n").lower()
while "y" in tambahbarang == "y" :

    namabarang = input("Masukan nama barang   :  ")

    hargabarang = int(input("Masukan harga barang  :  Rp"))

    jumlahbarang = int(input("Masukan jumlah barang :  "))

    total = hargabarang * jumlahbarang
    
    print(f"""
    ----------------------------------------
    {namabarang} {jumlahbarang} Pcs Rp.{hargabarang}    Total : Rp.{total:,}
    ----------------------------------------
    """)
    hargatotal += (hargabarang * jumlahbarang)
    jumlahbelanjaan += jumlahbarang
    
    tambahbarang = input("Apakah ingin mengscan barang lagi (y/n) ? ").lower()
    
# Tampilkan barang

print(f"Harga Total : Rp.{hargatotal}")
tunai = int(input("MASUKAN NOMINAL TUNAI : Rp."))
kembalian = tunai - hargatotal

print(f"""
----------------------------------------
{jumlahbelanjaan} Pcs Rp.{hargatotal:,}
----------------------------------------
""")

print(f"""
        TOTAL   : {hargatotal:,}
        TUNAI   : {tunai:,}
        KENBALI : {kembalian:,}

PPN       : DPP= 17,838  PPN= 1,962
ID POINKU : xxxxxxxx142/Maxxxxxxxx Axxxxxx
CEK PEROLEHAN POIN/STAMP/LUCKY DI APPS POINKU
     LAYANAN KOSUMEN SMS 0811 1500 280
  CALL 1500 280 - KONTAK@INDOMARET.CO.ID

  TERIMAKASIH TELAH BERBELANJA DI INDOMARET
""")