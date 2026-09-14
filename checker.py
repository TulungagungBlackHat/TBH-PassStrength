#!/usr/bin/env python3
# TBH-PassStrength - Password Strength Checker & Edukasi
# Tulungagung Black Hat - uchil404 | 100% Defensive & Aman

import re
import argparse
import string

BANNER = """\033[92m╔════════════════════════════════════╗
\033[92m║ \033[97mTBH-PassStrength \033[92m- Checker          \033[92m║
\033[92m║ \033[90mTulungagung Black Hat | uchil404 \033[92m║
\033[92m╚════════════════════════════════════╝\033[0m"""

COMMON = ["123456","password","qwerty","admin","12345678","iloveyou","123123","abc123"]

def check(pwd):
    score = 0
    advices = []
    # Length
    if len(pwd) >= 12: score += 2
    elif len(pwd) >= 8: score += 1
    else: advices.append("Gunakan minimal 12 karakter")
    # Upper/lower/digit/symbol
    if re.search(r"[A-Z]", pwd): score += 1
    else: advices.append("Tambah huruf besar (A-Z)")
    if re.search(r"[a-z]", pwd): score += 1
    else: advices.append("Tambah huruf kecil (a-z)")
    if re.search(r"[0-9]", pwd): score += 1
    else: advices.append("Tambah angka (0-9)")
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", pwd): score += 2
    else: advices.append("Tambah simbol (!@#$%)")
    # Common
    if pwd.lower() in COMMON:
        score = 0
        advices.append("Password terlalu umum! Jangan pakai 'password/123456'")
    # Sequential
    if re.search(r"(123|abc|qwe)", pwd.lower()):
        score -= 1
        advices.append("Hindari urutan '123'/'abc'/'qwe'")
    
    score = max(0, min(7, score))
    if score >= 6: verdict="\033[92m[SANGAT KUAT ✅]\033[0m"; color="Hijau"
    elif score >= 4: verdict="\033[96m[KUAT 👍]\033[0m"; color="Biru"
    elif score >= 2: verdict="\033[93m[LEMAH ⚠️]\033[0m"; color="Kuning"
    else: verdict="\033[91m[SANGAT LEMAH ⛔]\033[0m"; color="Merah"
    return score, verdict, advices

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Password Strength Checker - Edukasi")
    parser.add_argument("-p","--password", help="Password untuk dicek")
    args = parser.parse_args()
    pwd = args.password or input("\033[96mMasukkan password: \033[0m")
    score, verdict, advices = check(pwd)
    print(f"\n\033[97mPassword: {'*'*len(pwd)} ({len(pwd)} char)\033[0m")
    print(f"Skor: {score}/7 {verdict}")
    if advices:
        print("\033[93mSaran:\033[0m")
        for a in advices:
            print(f"  - {a}")
    else:
        print("\033[92mMantap! Password sudah kuat. Aktifkan 2FA juga ya!\033[0m")
    print("\n\033[90mTips: Gunakan passphrase 3-4 kata acak + simbol, misal: 'KopiPagi#Tulungagung2026!'\033[0m")

if __name__ == "__main__":
    main()
