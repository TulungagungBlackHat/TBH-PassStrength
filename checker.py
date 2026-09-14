#!/usr/bin/env python3
# TBH-PassStrength v2.0 Pro - Generator + JSON
import re, argparse, string, random, secrets, json

BANNER = """\033[92m╔════════════════════════════════════╗
\033[92m║ \033[97mTBH-PassStrength v2.0 Pro \033[92m- JSON/Gen \033[92m║
\033[92m║ \033[90mTulungagung Black Hat | uchil404 \033[92m║
\033[92m╚════════════════════════════════════╝\033[0m"""

COMMON = ["123456","password","qwerty","admin","12345678","iloveyou","123123","abc123"]

def check(pwd):
    score=0; adv=[]
    if len(pwd)>=12: score+=2
    elif len(pwd)>=8: score+=1
    else: adv.append("12 karakter")
    if re.search(r"[A-Z]",pwd): score+=1
    else: adv.append("Huruf besar")
    if re.search(r"[a-z]",pwd): score+=1
    else: adv.append("Huruf kecil")
    if re.search(r"[0-9]",pwd): score+=1
    else: adv.append("Angka")
    if re.search(r"[!@#$%^&*]",pwd): score+=2
    else: adv.append("Simbol")
    if pwd.lower() in COMMON: score=0; adv.append("Terlalu umum")
    score=max(0,min(7,score))
    verdict="SANGAT KUAT" if score>=6 else "KUAT" if score>=4 else "LEMAH" if score>=2 else "SANGAT LEMAH"
    return score,verdict,adv

def generate(l=16):
    chars=string.ascii_letters+string.digits+"!@#$%^&*"
    pwd=[secrets.choice(string.ascii_uppercase),secrets.choice(string.ascii_lowercase),secrets.choice(string.digits),secrets.choice("!@#$%^&*")]
    for _ in range(l-4): pwd.append(secrets.choice(chars))
    random.shuffle(pwd); return ''.join(pwd)

def main():
    print(BANNER)
    parser=argparse.ArgumentParser(description="v2.0 Pro")
    parser.add_argument("-p","--password",help="Cek password")
    parser.add_argument("-g","--generate",action="store_true",help="Generate")
    parser.add_argument("-l","--length",type=int,default=16)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    if args.generate:
        pwd=generate(args.length); s,v,a=check(pwd)
        print(f"[+] Generated: {pwd} | {s}/7 {v}")
        if args.json: open(args.json,'w').write(json.dumps({"password":pwd,"score":s,"verdict":v},indent=2)); print(f"[✓] JSON: {args.json}")
        return
    pwd=args.password or input("Password: ")
    s,v,a=check(pwd)
    print(f"Skor: {s}/7 {v} | Saran: {a}")
    if args.json: open(args.json,'w').write(json.dumps({"password":"*","score":s,"verdict":v,"advices":a},indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
