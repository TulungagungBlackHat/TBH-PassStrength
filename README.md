# TBH-PassStrength v1.1 - Checker + Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Version-v1.1-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/New-Generator-green?style=for-the-badge">
</p>

> **v1.1 Update** - Tambah **Generator Password Kuat** (defensive).

## ✨ v1.1 vs v1.0
- ✅ **Generator** (`--generate`) - Buat 16 char acak (A-Z, a-z, 0-9, simbol) pakai `secrets`
- ✅ Skor langsung, siap pakai

## 🚀 Usage
```bash
# Cek
python3 checker.py -p "password123"

# Generate kuat
python3 checker.py --generate
python3 checker.py --generate -l 20

# Output
[+] Generated (16 char): Xk9$mP2!qL8@vB4#
Skor: 7/7 [SANGAT KUAT ✅]
```

## 🛡️ Defensive
Gunakan generator + password manager + 2FA. Jangan pakai password sama.

## 👥 TBH
uchil404 - Tulungagung Black Hat

## 📄 License
MIT
