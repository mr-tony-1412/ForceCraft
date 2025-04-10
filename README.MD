# 🔐 Personalized Password Generator

A powerful CLI tool that generates personalized wordlists based on a user's full name, date of birth, and nicknames.  
This tool is especially useful for penetration testers, ethical hackers, or CTF players who need custom dictionaries for brute-force attacks.

---

## 📌 Features

- ✅ Generate combinations using full name, date of birth, and nicknames
- ✅ Adds common special characters like `.` and `@`
- ✅ Generates TitleCase variations for alphabetic passwords
- ✅ CLI with `argparse` and colored output using `colorama`
- ✅ Outputs passwords with a minimum length of 8 characters
- ✅ Saves output into a structured file inside `PasswordLists/`

---

## 💻 Requirements

- Python >= 3.6
- `colorama` library

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
colorama
```

---

## 📥 Installation

Clone this repository:

```bash
git clone https://github.com/mr-tony-1412/ForceCraft.git
cd ForceCraft
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python ForceCraft.py [OPTION]
```

### 🧩 Available Options

| Option         | Description                                           |
|----------------|-------------------------------------------------------|
| `-f <path>`    | Read input data from a file                          |
| `-m`           | Enter information manually via terminal prompts      |
| `-h` or `--help` | Show help message                                  |

---

## 📁 Input Format (for `-f` option)

Create a text file with exactly 3 lines:

```
John Michael Smith
12 07 1995
johnny jmsmith
```

- Line 1: Full name
- Line 2: Date of birth in format `dd mm yyyy`
- Line 3: Nicknames separated by spaces

Example usage:

```bash
python ForceCraft.py -f data.txt
```

---

## 🖥 Manual Input (for `-m` option)

Run:

```bash
python ForceCraft.py -m
```

You will be prompted to enter the data step-by-step:

```
➡️  Full name: John Michael Smith
➡️  Date of birth (dd mm yyyy): 12 07 1995
➡️  Nicknames (space-separated): johnny jmsmith
```

---

## 📂 Output

The generated wordlist will be saved in the `PasswordLists/` directory, with a filename formatted as:

```
<joinedname><dd><mm><yyyy>.txt
```

Example:

```
PasswordLists/johnmichaelsmith12071995.txt
```

All passwords have a minimum of 8 characters. If a password starts with a letter, a TitleCase version will also be included.

---

## 🧪 Example Output

```bash
$ python ForceCraft.py -m
🔐 Password Generator Started
🛠  Manual Input Mode:
➡️  Full name: John Michael Smith
➡️  Date of birth (dd mm yyyy): 12 07 1995
➡️  Nicknames (space-separated): johnny jmsmith

✅ 642 passwords saved to: PasswordLists/johnmichaelsmith12071995.txt
```

---

## 🛡 Use Cases

- ✅ Ethical hacking & red teaming
- ✅ Custom wordlists for brute-force tools
- ✅ CTF competitions
- ✅ Security testing for personal systems
- ✅ OSINT and social engineering simulations

> ⚠️ **Disclaimer**: This tool is intended strictly for educational and ethical use. Do **not** use it for unauthorized access or illegal activities.

---

## 📜 License

MIT License — free to use, modify, and distribute with attribution.

---

## 👨‍💻 Author

Made with ❤️ by [Mr.Tony]

- GitHub: [github.com/mr-tony-1412](https://github.com/mr-tony-1412)
- Telegram: [Grey Hat Community](https://t.me/+Q_K4_AHwxOVhZTk1)

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have suggestions, feel free to [open an issue](https://github.com/mr-tony-1412/ForceCraft/issues).