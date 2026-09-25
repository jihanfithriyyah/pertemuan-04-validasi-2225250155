# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Jihan Fithriyyah  
NIM: 2225250155  
Kelas: 3A  

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
```bash
python3 praktik/validasi_klasifikasi_nilai.py
Tabel KeputusanKategoriSyarat KodeContoh MasukanKeluaran DiharapkanAakhir >= 8590, 80, 95Predikat A, LulusBakhir >= 7075, 70, 85Predikat B, LulusCakhir >= 6060, 60, 80Predikat C, LulusDakhir >= 5055, 50, 90Predikat D, Belum lulusEselain di atas40, 30, 100Predikat E, Belum lulusHasil PengujianUjianTugasKehadiranKeluaran DiharapkanKeluaran AktualStatus908095Nilai akhir 86.00, Predikat A, LulusNilai akhir 86.00, Predikat A, LulusSesuai757085Nilai akhir 73.00, Predikat B, LulusNilai akhir 73.00, Predikat B, LulusSesuai606080Nilai akhir 60.00, Predikat C, LulusNilai akhir 60.00, Predikat C, LulusSesuai555090Nilai akhir 53.00, Predikat D, Belum lulusNilai akhir 53.00, Predikat D, Belum lulusSesuai4030100Nilai akhir 36.00, Predikat E, Belum lulusNilai akhir 36.00, Predikat E, Belum lulusSesuai909075Status: Tidak memenuhi syarat kehadiranStatus: Tidak memenuhi syarat kehadiranSesuai1058090Pesan penolakan rentang nilai ujianMasukan ditolak: nilai ujian di luar rentang 0 sampai 100Sesuai80-590Pesan penolakan rentang nilai tugasMasukan ditolak: nilai tugas di luar rentang 0 sampai 100Sesuai8080abcPesan penolakan tipeMasukan ditolak: seluruh data harus berupa angkaSesuaiRefleksiPenggunaan try-except dan rantai if-elif-else sangat membantu memastikan data yang diinput pengguna benar-benar valid sebelum diproses ke perhitungan akhir.