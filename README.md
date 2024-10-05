# My_MOTD
## from StarWars - The Clone Wars Series
**_The Message of the day..._**  

`My MOTD` is a Python script that manages and displays quotes and ASCII art, inspired on StarWars, the Clone Wars Series.  
The script allows automatic installation into shell configuration (zsh or bash), adding new quotes and ASCII art, and transferring from clipboard contents to files, every time that you open your terminal!

#### Features

- **Install the script**: Adds a command to your shell configuration file (`.zshrc` or `.bashrc`) to run the script automatically.
- **Remove the script**: Removes the command from your shell configuration file.
- **Add a quote**: Adds a new quote to the `quotes.txt` file.
- **Transfer from clipboard**: Adds clipboard content to the `figures.txt` file as a new ASCII art.
- **Display random quote and ASCII art**: Shows a random quote and ASCII art from the `quotes.txt` and `figures.txt` files.

#### Requirements

- Python 3.x
- `pyperclip` (for clipboard operations)

You can install `pyperclip` using pip:

```bash
pip install pyperclip
```

#### Usage
**Install the Script**
To install the script into your shell, use the `-i` option:

```bash
python project.py -i
```
This command adds an entry to your _.zshrc_ or _.bashrc_ file, so the script will be executed automatically when a new terminal session starts.

**Remove the Script**
To remove the script from your shell configuration file, use the `-r` option:

```bash
python project.py -r
```
This command removes the entry from your _.zshrc_ or _.bashrc_ file.

**Add a Quote**
To add a new quote to the quotes.txt file, use the `-a` option:

```bash
python project.py -a "Your new quote here"
```
This command appends the specified quote to the quotes.txt file.

**Transfer from Clipboard**
To transfer content from the clipboard to the figures.txt file, use the `-t` option:

```bash
python project.py -t
```
This command takes the current clipboard content and adds it to the figures.txt file, formatted as a new ASCII art section.

**Display Random Quote and ASCII Art**
If no options are provided, the script will display a random quote and ASCII art from the quotes.txt and figures.txt files:

```bash
python project.py
```
This command randomly selects a quote and ASCII art and prints them to the terminal.

#### Functions
* `load_quotes(file_name)`: Loads quotes from a file.
* `load_ascii_arts(file_name)`: Loads ASCII arts from a file, separated by ###.
* `print_random_message(quotes, arts)`: Prints a random quote and ASCII art.
* `install_script()`: Installs the script into the shell configuration file.
* `remove_script()`: Removes the script from the shell configuration file.
* `add_message_source(new_message, file_path='quotes.txt')`: Adds a new quote to the quotes.txt file.
* `add_from_clipboard()`: Adds clipboard content to the figures.txt file.
* `add_ascii_source(ascii_art, file_path='figures.txt')`: Adds a new ASCII art to the figures.txt file.

#### Demo
![til](demo.gif)