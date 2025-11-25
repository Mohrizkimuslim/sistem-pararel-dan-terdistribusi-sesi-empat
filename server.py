impor stopkontak
impor pemasangan benang

TUAN RUMAH = '0.0.0.0'
PELABUHAN = 65432

klien =[]
kunci_klien = pemasangan benang.Kunci()

pasti siaran(pesan,pengirim_koneksi=Tidak ada):
    dengan kunci_klien:
        untuk C di dalam klien:
            jika C != pengirim_koneksi:
                mencoba:
                    C.sendall(pesan.menyandi())
                kecuali:
                    lulus

pasti menangani_klien(koneksi,alamat):
    mencetak(f"[+] Klien terhubung:{alamat}")
    dengan kunci_klien:
        klien.menambahkan(koneksi)
    mencoba:
        ketika BENAR:
            data = koneksi.menerima(1024)
            jika bukan data:
                merusak
            pesan = data.membaca sandi().mengupas()
            mencetak(F"{alamat}:{pesan}")
            siaran(F"[{alamat[0]}]{pesan}",pengirim_koneksi=koneksi)
    kecuali Pengecualian sebagai e:
        mencetak(Kesalahan f"[!]{alamat}:{e}")
    Akhirnya:
        dengan kunci_klien:
            klien.menghapus(koneksi)
        koneksi.menutup()
        mencetak(f"[-] Klien terputus:{alamat}")

pasti server_send_loop():
    ketika BENAR:
        pesan = masukan()
        jika pesan.lebih rendah()== "KELUAR":
            mencetak("[i] Mematikan server...")
            dengan kunci_klien:
                untuk C di dalam klien:
                    mencoba:
                        C.sendall("[SERVER] Server sedang dimatikan.\N".menyandi())
                        C.menutup()
                    kecuali:
                        lulus
                klien.jernih()
            merusak
        siaran(f"[SERVER]{pesan}")

pasti utama():
    pelayan = stopkontak.stopkontak(stopkontak.AF_INET,stopkontak.ALIRAN KAUS KAKI)
    pelayan.mengikat((TUAN RUMAH,PELABUHAN))
    pelayan.mendengarkan()
    mencetak(f"Server berjalan pada{TUAN RUMAH}:{PELABUHAN}")

    pemasangan benang.Benang(target=server_send_loop,setan=BENAR).awal()

    mencoba:
        ketika BENAR:
            koneksi,alamat = pelayan.menerima()
            pemasangan benang.Benang(target=menangani_klien,argumen=(koneksi,alamat),setan=BENAR).awal()
    kecuali Interupsi Keyboard:
        mencetak("\N[i] Server dimatikan...")

jika _nama_ == "_utama_":
    utama()
