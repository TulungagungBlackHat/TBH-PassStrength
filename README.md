# TBH-PassStrength

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-PassStrength/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-PassStrength/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/type-defensive-green.svg" alt="Defensive">
</p>

Password strength checker and generator with actionable advice. Defensive tool — for auditing your own credentials, building password policies, or awareness training.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## Scoring

Passwords are scored **0–7** across length, character classes, and pattern penalties, with a verdict and concrete advice:

```
Skor: 2/7 LEMAH | Saran: tambah huruf besar, angka, simbol; hindari kata umum
```

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-PassStrength
cd TBH-PassStrength
pip install -r requirements.txt
```

## Usage

```
usage: checker.py [-h] [-p PASSWORD] [-g] [-l LENGTH] [--json JSON]

options:
  -p, --password PASSWORD   Check a password
  -g, --generate            Generate a strong password
  -l, --length LENGTH       Generated password length
  --json JSON               Save result as JSON
```

### Examples

```bash
python3 checker.py -p "correct horse battery staple"
python3 checker.py -g -l 20
python3 checker.py -p "Summer2026!" --json audit.json
```

## Sample Output

```
Skor: 5/7 CUKUP | Saran: tambah simbol; jangan pakai pola tahun
```

## Notes

- Analysis runs **locally** — passwords never leave your machine (check the source if you don't believe it)
- Scoring is heuristic; NIST guidelines remain the reference for policy design
- The generator is suitable for passphrases and service credentials

## Authorized Use Only

Audit passwords you own or have permission to test. Never test other people's credentials. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-Utils](https://github.com/TulungagungBlackHat/TBH-Utils) — hash and encode helpers
- [TBH-PhishDetector](https://github.com/TulungagungBlackHat/TBH-PhishDetector) — credential-theft defense companion

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
