import os
import shutil
import glob
import time
import random
import json
from colorama import init
from tqdm import tqdm
from yaspin import yaspin
from yaspin.spinners import Spinners
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.box import ROUNDED
import ctypes

init(autoreset=True)
console = Console()

ctypes.windll.kernel32.SetConsoleTitleW("Wemod Premium Unlocker - Hira")

SUPPORTED_VERSIONS = {
    "4.0.7": "[Supported]",
    "4.0.8": "[Supported]",
    "4.0.9": "[Supported]",
    "4.0.10": "[Supported]",
    "4.0.11": "[Supported]",
    "4.0.12": "[Supported]",
    "4.0.13": "[Supported]",
    "5.0.0": "[Supported]",
    "5.0.1": "[Supported]",
    "5.0.2": "[Supported]",
    "5.0.3": "[Supported]",
    "5.0.4": "[Supported]",
    "5.0.5": "[Supported]",
    "7.0.0": "[Supported]",
    "8.2.0": "[Supported]",
    "8.3.0": "[Supported]",
    "9.0.0": "[Not Supported]",
    "9.10.0": "[Not Supported]"
}

WEMOD_ASCII = """
__        __                       _        
\ \      / /__ _ __ ___   ___   __| |       
 \ \ /\ / / _ \ '_ ` _ \ / _ \ / _` |       
  \ V  V /  __/ | | | | | (_) | (_| |       
 __\_/\_/ \___|_| |_| |_|\___/ \__,_|       
|  _ \ _ __ ___ _ __ ___ (_)_   _ _ __ ___  
| |_) | '__/ _ \ '_ ` _ \| | | | | '_ ` _ \ 
|  __/| | |  __/ | | | | | | |_| | | | | | |
|_|   |_|  \___|_| |_| |_|_|\__,_|_| |_| |_| 
"""

def choose_language():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold cyan]Select Language[/bold cyan]", title="Language Selection", border_style="bright_blue"), justify="center")
    console.print("\n1. English\n2. Français\n3. Español\n4. Deutsch\n5. Русский\n", justify="center")
    choice = console.input("[bold cyan]Choose your language (default: English): [/bold cyan]").strip()

    if choice == "2":
        return 'fr'
    elif choice == "3":
        return 'es'
    elif choice == "4":
        return 'de'
    elif choice == "5":
        return 'ru'
    else:
        return 'en'  # Default to English

def load_language(lang='en'):
    with open(f'lang/{lang}.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def display_animated_text(text, color='white', delay=0.02):
    for char in text:
        console.print(char, style=color, end='', flush=True)
        time.sleep(delay)
    console.print()

def display_ascii_art():
    console.print(Panel(WEMOD_ASCII, border_style="bold magenta", expand=False))

def display_start_menu(language):
    os.system('cls' if os.name == 'nt' else 'clear')
    display_ascii_art()
    console.print(language['author'], style="yellow bold", justify="center")
    console.print()

    info_table = Table(show_header=False, box=ROUNDED, expand=False, border_style="cyan")
    info_table.add_column(language['unlock_key'], style="green")
    info_table.add_column(language['unlock_value'], style="yellow")
    info_table.add_row(language['unlock_label'], language['pro_on_wemod'])
    info_table.add_row(language['tested_on'], language['version_8_13_14'])
    info_table.add_row(language['not_working'], language['rc_from_phone'])
    console.print(info_table, justify="center")
    console.print()

    instructions = Table(title=language['instructions_title'], show_header=False, box=ROUNDED, expand=False, border_style="green")
    instructions.add_column(language['step_column'], style="cyan")
    instructions.add_row("1", language['close_app'])
    instructions.add_row("2", language['restore_if_fail'])
    console.print(instructions, justify="center")
    console.print()

    options = Table(title=language['options_title'], show_header=False, box=ROUNDED, expand=False, border_style="yellow")
    options.add_column(language['option_column'], style="magenta")
    options.add_column(language['description_column'], style="cyan")
    options.add_row("1", language['patch_app'])
    options.add_row("2", language['restore_app'])
    options.add_row("3", language['exit'])
    options.add_row("--help or ?", language['display_help'])
    console.print(options, justify="center")
    console.print()

def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()} - {error_message}\n")  

def display_help(language):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold cyan]Help Information[/bold cyan]", title=language['help_title'], border_style="bright_blue"), justify="center")
    
    console.print(f"\n{language['usage']}", justify="center")
    
    help_table = Table(show_header=True, header_style="bold yellow", border_style="bright_black", title=language['commands_title'])
    help_table.add_column(language['option_column'], style="bold magenta")
    help_table.add_column(language['description_column'], style="cyan")

    help_table.add_row("[bold magenta]1[/bold magenta]", language['patch_app_help'])
    help_table.add_row("[bold magenta]2[/bold magenta]", language['restore_app_help'])
    help_table.add_row("[bold magenta]3[/bold magenta]", language['exit_help'])
    help_table.add_row("[bold magenta]--help or ?[/bold magenta]", language['display_help'])

    console.print(help_table, justify="center")
    
    console.print(f"\n{language['note']}", justify="center")
    console.print("[cyan]Press Enter to return to the main menu...[/cyan]")
    
    console.input()  
    display_start_menu(language)

def wait_and_clear():
    console.input("[cyan]Press Enter to continue...[/cyan]")
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_searching(language):
    with yaspin(Spinners.dots, text=language['searching_text'], color="yellow") as spinner:
        time.sleep(random.uniform(1.5, 3.0))
        spinner.ok("[Done]")

def check_version(version):
    return SUPPORTED_VERSIONS.get(version, "[Not Supported]")

def ask_to_continue(version, language):
    console.print(f"[bold red]{language['warning']} {version} {language['not_supported']}[/bold red]", justify="center")
    answer = console.input("[bold cyan]Are you sure you want to continue? (y/n): [/bold cyan]").strip().lower()
    return answer == 'y'

def patch_app(language):
    animate_searching(language)
    
    user_directory = os.path.expanduser("~")
    app_folders = glob.glob(os.path.join(user_directory, 'AppData', 'Local', 'WeMod', 'app-*'))

    if not app_folders:
        console.print(language['error_no_folders'], style="bold red")
        log_error(language['error_no_folders_log'])
        wait_and_clear()
        return

    for app_folder in app_folders:
        version = app_folder.split('-')[-1]
        version_status = check_version(version)

        console.print(f"{language['found_version']} {version} ({version_status})", style="green" if version_status == "[Supported]" else "red")

        # Suppression de la condition pour demander confirmation si non supporté
        if version_status == "[Not Supported]":
            console.print(f"[bold yellow]Continuing with non-supported version: {version}[/bold yellow]")

        source_path = os.path.join(os.getcwd(), 'app.asar')
        destination_path = os.path.join(app_folder, 'resources', 'app.asar')

        backup_folder = os.path.join(os.getcwd(), 'Backups')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            console.print(f"{language['backups_folder_created']} {backup_folder}", style="cyan")

        backup_path = os.path.join(backup_folder, f'app_backup_{version}.asar')

        try:
            if os.path.exists(destination_path):
                console.print(language['creating_backup'], style="yellow")
                shutil.copy(destination_path, backup_path)
                console.print(f"{language['backup_done']} {backup_path}", style="green")
                wait_and_clear()

            if os.path.exists(source_path):
                console.print(language['patching'], style="yellow")
                shutil.copy(source_path, destination_path)
                
                # Afficher le message de succès après le patch
                console.print(language['patch_done_message'].format(destination_path), style="green")
            else:
                console.print(language['error_patch_file_missing'], style="red")
                log_error(language['error_patch_file_missing_log'])
        except Exception as e:
            console.print(language['patching_failed'], style="red")
            log_error(f"{language['patching_failed_log']}: {str(e)}")
    
    console.print(language['all_patches_done'], style="green")
    wait_and_clear()

def restore_app(language):
    animate_searching(language)
    
    user_directory = os.path.expanduser("~")
    backup_folder = os.path.join(os.getcwd(), 'Backups')
    app_folders = glob.glob(os.path.join(user_directory, 'AppData', 'Local', 'WeMod', 'app-*'))

    if not app_folders or not os.path.exists(backup_folder):
        console.print(language['error_no_folders'], style="bold red")
        log_error(language['error_no_folders_log'])
        wait_and_clear()
        return

    for app_folder in app_folders:
        version = app_folder.split('-')[-1]
        backup_path = os.path.join(backup_folder, f'app_backup_{version}.asar')

        if os.path.exists(backup_path):
            destination_path = os.path.join(app_folder, 'resources', 'app.asar')
            console.print(language['restoring'], style="yellow")
            shutil.copy(backup_path, destination_path)
            console.print(f"{language['restore_done']}: {destination_path}", style="green")
        else:
            console.print(f"[bold red]{language['backup_not_found']} {backup_path}[/bold red]")

    console.print(language['all_restores_done'], style="green")
    wait_and_clear()

def main():
    language_code = choose_language()
    language = load_language(language_code)
    
    while True:
        display_start_menu(language)
        
        option = console.input("[bold cyan]Select an option: [/bold cyan]").strip()

        if option == "1":
            patch_app(language)
        elif option == "2":
            restore_app(language)
        elif option == "3":
            console.print(language['exit_message'], style="yellow")
            break
        elif option in ["--help", "?"]:
            display_help(language)
        else:
            console.print(language['invalid_option'], style="red")
            wait_and_clear()

if __name__ == "__main__":
    main()
