import argparse
import os
import unicodedata
from colorama import init, Fore, Style

init(autoreset=True)

def remove_accents(text):
    text = unicodedata.normalize('NFD', text)
    return ''.join(c for c in text if unicodedata.category(c) != 'Mn')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="🔐 Personalized Password Generator - Create a password list based on personal info"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-f', '--input-file',
        type=str,
        help="Path to input file (line 1: full name, line 2: date of birth, line 3: nicknames)"
    )
    group.add_argument(
        '-m', '--manual',
        action='store_true',
        help="Manually enter information via terminal prompts"
    )

    return parser.parse_args()

def get_user_info(args):
    if args.input_file:
        if not os.path.exists(args.input_file):
            print(Fore.RED + f"❌ File '{args.input_file}' not found.")
            exit(1)
        with open(args.input_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            full_name = lines[0].lower()
            day, month, year = map(int, lines[1].split())
            nicknames = lines[2].lower().split()
    elif args.manual:
        print(Fore.YELLOW + "🛠  Manual Input Mode:")
        full_name = input(Fore.CYAN + "➡️  Full name: ").lower()
        dob = input(Fore.CYAN + "➡️  Date of birth (dd mm yyyy): ")
        nicknames_input = input(Fore.CYAN + "➡️  Nicknames (space-separated): ")
        day, month, year = map(int, dob.split())
        nicknames = nicknames_input.lower().split()

    return remove_accents(full_name).split(), day, month, year, nicknames

def generate_passwords(full_name, day, month, year, nicknames):
    special_char = ".@"
    passwords = set()

    part_1 = {
        full_name[-1],
        full_name[0] + full_name[-1],
        full_name[-1] + full_name[0],
        full_name[-2] + full_name[-1] if len(full_name) > 1 else '',
        full_name[-1] + full_name[-2] if len(full_name) > 1 else '',
        ''.join(full_name),
        full_name[0][0] + full_name[-1],
        full_name[-1] + full_name[0][0],
        full_name[-2][0] + full_name[-1] if len(full_name) > 1 else ''
    }

    t = ''.join([s[0] for s in full_name])
    part_1.add(t[:-1] + full_name[-1])
    part_1.add(full_name[-1] + t[:-1])
    part_1.update(nicknames)

    part_2 = {
        str(day), str(month), str(year),
        f'{day:02}', f'{month:02}',
        f'{day:02}{month:02}{year}',
        f'{day:02}{month:02}'
    }

    part_3 = {"123"}

    for one in part_1:
        passwords.add(one)
        for sp_one in special_char:
            passwords.update({
                one + sp_one,
                one + sp_one * 2,
                sp_one + one,
                sp_one * 2 + one
            })
            for two in part_2:
                passwords.update({
                    two,
                    two + sp_one,
                    two + sp_one * 2,
                    sp_one + two,
                    sp_one * 2 + two,
                    one + two,
                    two + one,
                    one + sp_one + two
                })
                for three in part_3:
                    passwords.add(one + three)
                    passwords.add(one + two + three)
                    for sp_two in special_char:
                        passwords.add(one + sp_one + two + sp_two)
                        passwords.add(one + sp_one + two + sp_two * 2)

    return sorted([p for p in passwords if len(p) >= 8])

def save_passwords(filename, passwords):
    length = 0
    with open(filename, "w", encoding="utf-8") as f:
        for pas in passwords:
            f.write(pas + "\n")
            length += 1
            if pas[0].isalpha():
                f.write(pas.title() + "\n")
                length += 1
    return length

def main():
    print(Fore.YELLOW + "🔐 Password Generator Started")
    args = parse_arguments()
    full_name, day, month, year, nicknames = get_user_info(args)
    passwords = generate_passwords(full_name, day, month, year, nicknames)

    output_dir = "PasswordLists"
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{''.join(full_name)}{day:02}{month:02}{year}.txt"
    output_path = os.path.join(output_dir, file_name)

    count = save_passwords(output_path, passwords)
    print(Fore.GREEN + f"\n✅ {count} passwords saved to: {output_path}\n")

if __name__ == "__main__":
    main()
