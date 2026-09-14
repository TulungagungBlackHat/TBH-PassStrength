#!/usr/bin/env python3
# TBH-PassStrength v1.1 - Checker + Generator (Defensive)
# Tulungagung Black Hat - uchil404

import re, argparse, string, random, secrets

BANNER = """\033[92m╔════════════════════════════════════╗
\033[92m║ \033[97mTBH-PassStrength v1.1 \033[92m- Checker+Gen \033[92m║
\033[92m║ \033[90mTulungagung Black Hat | uchil404 \033[92m║
\033[92m╚════════════════════════════════════╝\033[0m"""

COMMON = ["123456","password","qwerty","admin","12345678","iloveyou","123123","abc123"]

def check(pwd):
    score = 0
    advices = []
    if len(pwd) >= 12: score += 2
    elif len(pwd) >= 8: score += 1
    else: advices.append("Gunakan minimal 12 karakter")
    if re.search(r"[A-Z]", pwd): score += 1
    else: advices.append("Tambah huruf besar (A-Z)")
    if re.search(r"[a-z]", pwd): score += 1
    else: advices.append("Tambah huruf kecil (a-z)")
    if re.search(r"[0-9]", pwd): score += 1
    else: advices.append("Tambah angka (0-9)")
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", pwd): score += 2
    else: advices.append("Tambah simbol (!@#$%)")
    if pwd.lower() in COMMON:
        score = 0; advices.append("Password terlalu umum!")
    if re.search(r"(123|abc|qwe)", pwd.lower()):
        score -= 1; advices.append("Hindari urutan '123'/'abc'")
    score = max(0, min(7, score))
    if score >= 6: verdict="\033[92m[SANGAT KUAT ✅]\033[0m"
    elif score >= 4: verdict="\033[96m[KUAT 👍]\033[0m"
    elif score >= 2: verdict="\033[93m[LEMAH ⚠️]\033[0m"
    else: verdict="\033[91m[SANGAT LEMAH ⛔]\033[0m"
    return score, verdict, advices

def generate(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    # Ensure at least one of each
    pwd = [secrets.choice(string.ascii_uppercase), secrets.choice(string.ascii_lowercase), secrets.choice(string.digits), secrets.choice("!@#$%^&*")]
    for _ in range(length-4):
        pwd.append(secrets.choice(chars))
    random.shuffle(pwd)
    return ''.join(pwd)

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="TBH-PassStrength v1.1")
    parser.add_argument("-p","--password", help="Password untuk dicek")
    parser.add_argument("-g","--generate", action="store_true", help="Generate password kuat")
    parser.add_argument("-l","--length", type=int, default=16, help="Panjang generate (default 16)")
    args = parser.parse_args()
    
    if args.generate:
        pwd = generate(args.length)
        score, verdict, _ = check(pwd)
        print(f"\n\033[92m[+] Generated ({args.length} char): \033[97m{pwd}\033[0m")
        print(f"Skor: {score}/7 {verdict} - Siap pakai + simpan di password manager!\033[0m")
        return

    pwd = args.password or input("\033[96mMasukkan password: \033[0m")
    score, verdict, advices = check(pwd)
    print(f"\n\033[97mPassword: {'*'*len(pwd)} ({len(pwd)} char)\033[0m")
    print(f"Skor: {score}/7 {verdict}")
    if advices:
        print("\033[93mSaran:\033[0m")
        for a in advices: print(f"  - {a}")
        print(f"\n\033[96mMau generate yang kuat? Jalankan: python3 checker.py --generate\033[0m")
    else:
        print("\033[92mMantap! Aktifkan 2FA juga!\033[0m")

if __name__ == "__main__":
    main()
