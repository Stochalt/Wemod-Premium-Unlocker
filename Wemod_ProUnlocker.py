lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl = exit, open, print, Exception, bytes, getattr, bool

from hashlib import sha256 as llllIIlIlIlIlI
from os.path import abspath as llIlIIlllIIllI, dirname as lIIllIIllIIlII, join as IlIIIIIllIIIll

def lllIIlllIIllIlIlIl(IllIllllIIlllIllll, IIIlIllIllIIlIIlII):
    try:
        with llllllllllllllI(IIIlIllIllIIlIIlII, 'r') as lllllIIIIllIIIIIll:
            llIllllIllIlIIllIl = llllllllllllIlI(lllllIIIIllIIIIIll.read(), llllllllllllIlI(llllllllllllIll, 'fromhex')('7374726970').decode())()
        with llllllllllllllI(IllIllllIIlllIllll, 'rb') as IllIIllIIIIIlIlIlI:
            IIlllIIIllIllIIllI = llllIIlIlIlIlI()
            while (chunk := llllllllllllIlI(IllIIllIIIIIlIlIlI, llllllllllllIlI(llllllllllllIll, 'fromhex')('72656164').decode())(8192)):
                llllllllllllIlI(IIlllIIIllIllIIllI, llllllllllllIlI(llllllllllllIll, 'fromhex')('757064617465').decode())(chunk)
        return IIlllIIIllIllIIllI.hexdigest() == llIllllIllIlIIllIl
    except lllllllllllllII as IlllIlIIllllIllIll:
        lllllllllllllIl(f'Error during verification: {IlllIlIIllllIllIll}')
        return llllllllllllIIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
IllIllllIIlllIllll = llIlIIlllIIllI(__file__)
IIIlIllIllIIlIIlII = IlIIIIIllIIIll(lIIllIIllIIlII(IllIllllIIlllIllll), 'signature.txt')
if not lllIIlllIIllIlIlIl(IllIllllIIlllIllll, IIIlIllIllIIlIIlII):
    lllllllllllllIl('Integrity check failed! The script has been modified. SKID.')
    lllllllllllllll(1)

import os
import shutil
import glob
import time
import random
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

def display_animated_text(text, color='white', delay=0.02):
    for char in text:
        console.print(char, style=color, end='', flush=True)
        time.sleep(delay)
    console.print()

def display_ascii_art():
    console.print(Panel(WEMOD_ASCII, border_style="bold magenta", expand=False))

def display_start_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_ascii_art()
    console.print("By Hira", style="yellow bold", justify="center")
    console.print()

    info_table = Table(show_header=False, box=ROUNDED, expand=False, border_style="cyan")
    info_table.add_column("Key", style="green")
    info_table.add_column("Value", style="yellow")
    info_table.add_row("Unlocks", "Pro on WeMod")
    info_table.add_row("Tested on version", "8.13.14")
    info_table.add_row("What doesn't work", "RC from phone (server-side feature)")
    console.print(info_table, justify="center")
    console.print()

    instructions = Table(title="Instructions", show_header=False, box=ROUNDED, expand=False, border_style="green")
    instructions.add_column("Step", style="cyan")
    instructions.add_row("1. Close app fully from task manager if it's running")
    instructions.add_row("2. If patch fails, run 'Restore app'")
    console.print(instructions, justify="center")
    console.print()

    options = Table(title="Options", show_header=False, box=ROUNDED, expand=False, border_style="yellow")
    options.add_column("Option", style="magenta")
    options.add_column("Description", style="cyan")
    options.add_row("1", "Patch app")
    options.add_row("2", "Restore app")
    options.add_row("3", "Exit")
    console.print(options, justify="center")
    console.print()

def wait_and_clear():
    console.input("[cyan]Press Enter to continue...[/cyan]")
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_searching():
    with yaspin(Spinners.dots, text="Searching for WeMod app folders", color="yellow") as spinner:
        time.sleep(random.uniform(1.5, 3.0))
        spinner.ok("✔")

def patch_app():
    animate_searching()
    app_folders = glob.glob(os.path.join(user_directory, 'AppData', 'Local', 'WeMod', 'app-*'))

    if not app_folders:
        console.print("Error: No app- folders found.", style="bold red")
        wait_and_clear()
        return

    for app_folder in app_folders:
        version = app_folder.split('-')[-1]
        console.print(f"Found version: {version}", style="green")

        source_path = os.path.join(os.getcwd(), 'app.asar')
        destination_path = os.path.join(app_folder, 'resources', 'app.asar')

        backup_folder = os.path.join(os.getcwd(), 'Backups')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            console.print(f"Backups folder created at: {backup_folder}", style="cyan")

        backup_path = os.path.join(backup_folder, f'app_backup_{version}.asar')

        if os.path.exists(destination_path):
            console.print("Backing up original app.asar...", style="yellow")
            try:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(),
                    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                ) as progress:
                    task = progress.add_task("[cyan]Backing up...", total=100)
                    shutil.copy(destination_path, backup_path)
                    while not progress.finished:
                        progress.update(task, advance=1)
                        time.sleep(0.02)
                console.print(f"Backup created for version: {version}.", style="green")
            except Exception as e:
                console.print(f"Error backing up original app.asar: {e}", style="bold red")
                continue
        else:
            console.print(f"Warning: No original app.asar found for version {version}. Skipping backup.", style="yellow")

        console.print("Patching app.asar...", style="yellow")
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                task = progress.add_task("[cyan]Patching...", total=100)
                shutil.copy(source_path, destination_path)
                while not progress.finished:
                    progress.update(task, advance=1)
                    time.sleep(0.02)
            console.print("Patch successful.", style="green bold")
        except Exception as e:
            console.print(f"Error patching app.asar: {e}", style="bold red")
        
    wait_and_clear()

def restore_app():
    animate_searching()
    backup_folder = os.path.join(os.getcwd(), 'Backups')

    if not os.listdir(backup_folder):
        console.print("Error: No backup files found.", style="bold red")
        wait_and_clear()
        return

    for backup_file in os.listdir(backup_folder):
        if backup_file.startswith('app_backup_') and backup_file.endswith('.asar'):
            version = backup_file.split('_')[2][:-5]
            console.print(f"Restoring version: {version}", style="cyan")

            source_path = os.path.join(backup_folder, backup_file)
            destination_path = os.path.join(user_directory, 'AppData', 'Local', 'WeMod', f'app-{version}', 'resources', 'app.asar')

            console.print("Restoring app.asar...", style="yellow")
            try:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(),
                    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                ) as progress:
                    task = progress.add_task("[cyan]Restoring...", total=100)
                    shutil.copy(source_path, destination_path)
                    while not progress.finished:
                        progress.update(task, advance=1)
                        time.sleep(0.02)
                console.print(f"Restore successful for version: {version}.", style="green")
            except Exception as e:
                console.print(f"Error restoring version {version}: {e}", style="bold red")
                continue

    wait_and_clear()

if __name__ == "__main__":
    user_directory = os.path.expanduser("~")

    while True:
        display_start_menu()
        option = console.input("[cyan]Enter the option number: [/cyan]").strip()

        if option == '1':
            patch_app()
        elif option == '2':
            restore_app()
        elif option == '3':
            console.print("Thank you for using WeMod Patcher. Goodbye!", style="green")
            break
        else:
            console.print("Invalid option. Please enter a valid option.", style="bold red")
            wait_and_clear()
