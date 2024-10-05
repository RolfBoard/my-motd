import argparse
import random
import os
import pyperclip

def main():
    parser = argparse.ArgumentParser(description="Quotes of the day, with some Star Wars juice.")

    parser.add_argument(
        '-i', '--install',
        action='store_true',
        help='Install the script into zshrc or bash'
    )
    parser.add_argument(
        '-r', '--remove',
        action='store_true',
        help='Remove the script from zshrc or bash'
    )
    parser.add_argument(
        '-a', '--add',
        type=str,
        help='Add a new quote to the quotes.txt file'
    )
    parser.add_argument(
        '-t', '--transfer',
        action='store_true',
        help='Transfer content from clipboard to the figures.txt file'
    )

    args = parser.parse_args()

    if args.install:
        install_script()
    elif args.remove:
        remove_script()
    elif args.add:
        add_message_source(args.add)
    elif args.transfer:
        add_from_clipboard()
    else:
        quotes = load_quotes('quotes.txt')
        arts = load_ascii_arts('figures.txt')
        print_random_message(quotes, arts)

def load_quotes(file_name):
    """Load the quotes from a file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, 'r') as file:
        quotes = [line.strip() for line in file if line.strip()]
    return quotes

def load_ascii_arts(file_name):
    """Load all ASCII illustrations split by '###'"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, 'r') as file:
        content = file.read()
        arts = content.split('###')
    return arts

def print_random_message(quotes, arts):
    """Prints randomly a quote and an art"""
    quote = random.choice(quotes)
    art = random.choice(arts)

    print(art)
    print(f"Clone Wars - {quote}\n")

def install_script():
    """Install script into the correct shell configuration file (e.g., zshrc or bashrc)."""
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()
    script_line = f"python3 '{current_dir}/my_motd.py'\n"

    shell = os.getenv('SHELL')

    if 'zsh' in shell:
        rc_file = os.path.join(home_dir, ".zshrc")
    elif 'bash' in shell:
        rc_file = os.path.join(home_dir, ".bashrc")
    else:
        rc_file = os.path.join(home_dir, ".bashrc")

    if not os.path.exists(rc_file):
        open(rc_file, 'w').close()

    with open(rc_file, "a") as file:
        file.write(script_line)

    print(f"Script installed in {rc_file}.")

def remove_script():
    """Remove the script from the correct shell configuration file (e.g., zshrc or bashrc)."""
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()
    script_line = f"python3 '{current_dir}/project.py'\n"

    shell = os.getenv('SHELL')

    if 'zsh' in shell:
        rc_file = os.path.join(home_dir, ".zshrc")
    elif 'bash' in shell:
        rc_file = os.path.join(home_dir, ".bashrc")
    else:
        rc_file = os.path.join(home_dir, ".bashrc")

    if os.path.exists(rc_file):
        with open(rc_file, "r") as file:
            lines = file.readlines()

        new_lines = [line for line in lines if line.strip("\n") != script_line.strip("\n")]

        with open(rc_file, "w") as file:
            file.writelines(new_lines)

        print(f"Script removed from {rc_file}.")
    else:
        print(f"{rc_file} does not exist.")

def add_message_source(new_message, file_path='quotes.txt'):
    """Add a new quote to the quotes file."""
    with open(file_path, 'r') as file:
        existing_messages = [line.strip() for line in file if line.strip()]

    if new_message in existing_messages:
        print(f"A mensagem '{new_message}' it is already exists in quotes.txt")
        return

    with open(file_path, 'a+') as file:
        file.seek(0, os.SEEK_END)
        if file.tell() > 0:
            file.seek(file.tell() - 1)
            last_char = file.read(1)
            if last_char != '\n':
                file.write('\n')

        file.write(new_message + '\n')

    print(f"New Quote '{new_message}' added...")

def add_from_clipboard():
    """Add content from clipboard to the appropriate file with ### as a delimiter."""
    clipboard_content = pyperclip.paste().strip()

    if clipboard_content:
        if not clipboard_content.startswith('###'):
            clipboard_content = '###\n' + clipboard_content

        parts = clipboard_content.split('###')

        if len(parts) > 1:
            art = parts[1].strip()
            add_ascii_source(art)
        else:
            print("The clipboard content does not contain '###' delimiter.")
    else:
        print("Clipboard is empty.")

def add_ascii_source(ascii_art, file_path='figures.txt'):
    """Add a new ASCII art to the figures file."""
    with open(file_path, 'r') as file:
        existing_art = [line.strip() for line in file if line.strip()]

    if ascii_art in existing_art:
        print(f"A arte ASCII already exists.")
        return

    with open(file_path, 'a+') as file:
        file.seek(0, os.SEEK_END)
        if file.tell() > 0:
            file.seek(file.tell() - 1)
            last_char = file.read(1)
            if last_char != '\n':
                file.write('\n')

        file.write('###\n' + ascii_art + '\n')

    print(f"New ASCII Art added...\n{ascii_art}")

if __name__ == "__main__":
    main()