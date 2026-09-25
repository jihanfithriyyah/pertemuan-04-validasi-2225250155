# Pertemuan 04 – Seleksi Multi-Kondisi dan Validasi Input

## Identitas
Nama  : Jihan Fithriyyah  
NIM   : 2225260001  
Kelas : S1 Pendidikan Matematika FKIP Untirta  

## Tujuan
Repositori ini berisi latihan Python tentang seleksi multi-kondisi (if-elif-else) dan validasi input (tipe, rentang, domain).

## Struktur Folder
pertemuan-04-validasi-NIM/  
├── README.md  
├── latihan/  
│   ├── 01_predikat_nilai.py  
│   ├── 02_kategori_bilangan.py  
│   ├── 03_validasi_rentang.py  
│   ├── 04_validasi_tipe.py  
│   └── 05_klasifikasi_segitiga_sudut.py  
└── praktik/  
    └── validasi_klasifikasi_nilai.py  

## Tabel Keputusan – Predikat Nilai
| Kategori | Syarat Kode       | Contoh Masukan | Keluaran Diharapkan |
|----------|------------------|----------------|---------------------|
| A        | nilai >= 85       | 85, 100        | A                   |
| B        | nilai >= 70       | 70, 84.9       | B                   |
| C        | nilai >= 60       | 60, 69.9       | C                   |
| D        | nilai >= 50       | 50, 59.9       | D                   |
| E        | selain di atas    | 0, 49.9        | E                   |

## Tabel Pengujian
| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|---------|---------------------|-----------------|--------|
| 92      | Predikat A          | A               | ✔      |
| 85      | Predikat A          | A               | ✔      |
| 84.9    | Predikat B          | B               | ✔      |
| 49.9    | Predikat E          | E               | ✔      |
| -1      | Pesan penolakan     | Ditolak         | ✔      |
| abc     | Pesan penolakan     | Ditolak         | ✔      |

## Refleksi
Program berhasil menangani seluruh kondisi sesuai spesifikasi: validasi tipe, rentang, dan domain berjalan, serta klasifikasi nilai menghasilkan predikat yang benar.