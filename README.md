# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: [Jihan Fithriyyah]
NIM: [2225250155]
Kelas: [3A]

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
```bash
python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan
| Kategori | Syarat Utama |
| :--- | :--- |
| Predikat A | Nilai Akhir >= 85 dan Kehadiran >= 80% |
| Predikat B | 70 <= Nilai Akhir < 85 dan Kehadiran >= 80% |
| Predikat C | 60 <= Nilai Akhir < 70 dan Kehadiran >= 80% |
| Predikat D | 50 <= Nilai Akhir < 60 dan Kehadiran >= 80% |
| Predikat E | Nilai Akhir < 50 dan Kehadiran >= 80% |
| Tidak Memenuhi Kehadiran | Kehadiran < 80% |
| Ditolak (Rentang) | Input < 0 atau > 100 |
| Ditolak (Tipe) | Input bukan angka (ValueError) |

## Hasil Pengujian
| Ujian | Tugas | Kehadiran | Keluaran Diharapkan | Keluaran Aktual | Status |
| :---: | :---: | :---: | :--- | :--- | :---: |
| 90 | 80 | 95 | Nilai Akhir 86.00, Predikat A, Lulus | Nilai akhir: 86.00, Predikat: A, Status: Lulus | Sesuai |
| 75 | 70 | 85 | Nilai Akhir 73.00, Predikat B, Lulus | Nilai akhir: 73.00, Predikat: B, Status: Lulus | Sesuai |
| 60 | 60 | 80 | Nilai Akhir 60.00, Predikat C, Lulus | Nilai akhir: 60.00, Predikat: C, Status: Lulus | Sesuai |
| 55 | 50 | 90 | Nilai Akhir 53.00, Predikat D, Belum lulus | Nilai akhir: 53.00, Predikat: D, Status: Belum lulus | Sesuai |
| 40 | 30 | 100 | Nilai Akhir 36.00, Predikat E, Belum lulus | Nilai akhir: 36.00, Predikat: E, Status: Belum lulus | Sesuai |
| 90 | 90 | 75 | Status Tidak memenuhi syarat kehadiran | Nilai akhir: 90.00, Status: Tidak memenuhi syarat kehadiran. | Sesuai |
| 105 | 80 | 90 | Pesan rentang nilai ujian | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | Sesuai |
| 80 | -5 | 90 | Pesan rentang nilai tugas | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100. | Sesuai |
| 80 | 80 | abc | Pesan penolakan tipe | Masukan ditolak: seluruh data harus berupa angka. | Sesuai |

## Refleksi
Penerapan validasi tipe dan rentang di awal program (guard clause) membantu mencegah terjadinya runtime error dan memastikan data yang diolah pada perhitungan nilai akhir serta penentuan predikat sudah benar-benar valid.

---
*Dokumentasi ini dibuat untuk memenuhi tugas Pertemuan 04 Praktikum Algoritma dan Pemrograman.*