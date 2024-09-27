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
\\ \\      / /__ _ __ ___   ___   __| |       
 \\ \\ /\\ / / _ \\ '_ ` _ \\ / _ \\ / _` |       
  \\ V  V /  __/ | | | | | (_) | (_| |       
 __\\_/\\_/ \\___|_| |_| |_|\\___/ \\__,_|       
|  _ \\ _ __ ___ _ __ ___ (_)_   _ _ __ ___  
| |_) | '__/ _ \\ '_ ` _ \\| | | | | '_ ` _ \\ 
|  __/| | |  __/ | | | | | | |_| | | | | | |
|_|   |_|  \\___|_| |_| |_|_|\\__,_|_| |_| |_| 
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
    options.add_row("--help or ?", "Display help information")
    console.print(options, justify="center")
    console.print()

def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()} - {error_message}\n")  # Vérifiez l'indentation ici

def display_help():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen before displaying help
    console.print(Panel("[bold cyan]Help Information[/bold cyan]", title="Help", border_style="bright_blue"), justify="center")
    
    console.print("\n[bold green]Usage:[/bold green] Choose an option from the main menu.\n", justify="center")
    
    help_table = Table(show_header=True, header_style="bold yellow", border_style="bright_black", title="Available Commands")
    help_table.add_column("Option", style="bold magenta")
    help_table.add_column("Description", style="cyan")

    help_table.add_row("[bold magenta]1[/bold magenta]", "Patch the WeMod app to unlock Pro features.")
    help_table.add_row("[bold magenta]2[/bold magenta]", "Restore the WeMod app to its original state.")
    help_table.add_row("[bold magenta]3[/bold magenta]", "Exit the application.")
    help_table.add_row("[bold magenta]--help or ?[/bold magenta]", "Display this help information.")

    console.print(help_table, justify="center")
    
    console.print("\n[bold yellow]Note:[/bold yellow] Ensure to follow the instructions carefully.", justify="center")
    console.print("[cyan]Press Enter to return to the main menu...[/cyan]")
    
    console.input()  # Wait for user to press Enter
    display_start_menu()  # Return to the main menu after help

def wait_and_clear():
    console.input("[cyan]Press Enter to continue...[/cyan]")
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_searching():
    with yaspin(Spinners.dots, text="Searching for WeMod app folders", color="yellow") as spinner:
        time.sleep(random.uniform(1.5, 3.0))
        spinner.ok("[Done]")

def check_version(version):
    return SUPPORTED_VERSIONS.get(version, "[Not Supported]")

def ask_to_continue(version):
    console.print(f"[bold red]Warning: Version {version} is not supported.[/bold red]", justify="center")
    answer = console.input("[bold cyan]Are you sure you want to continue? (y/n): [/bold cyan]").strip().lower()
    return answer == 'y'

def patch_app():
    animate_searching()
    
    user_directory = os.path.expanduser("~")
    app_folders = glob.glob(os.path.join(user_directory, 'AppData', 'Local', 'WeMod', 'app-*'))

    if not app_folders:
        console.print("Error: No app- folders found.", style="bold red")
        log_error("No WeMod app folders found.")
        wait_and_clear()
        return

    for app_folder in app_folders:
        version = app_folder.split('-')[-1]
        version_status = check_version(version)

        console.print(f"Found version: {version} ({version_status})", style="green" if version_status == "[Supported]" else "red")

        if version_status == "[Not Supported]":
            if not ask_to_continue(version):
                console.print(f"Skipping unsupported version {version}.", style="yellow")
                continue

        source_path = os.path.join(os.getcwd(), 'app.asar')
        destination_path = os.path.join(app_folder, 'resources', 'app.asar')

        backup_folder = os.path.join(os.getcwd(), 'Backups')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            console.print(f"Backups folder created at: {backup_folder}", style="cyan")

        backup_path = os.path.join(backup_folder, f'app_backup_{version}.asar')

        try:
            if os.path.exists(destination_path):
                console.print("Backing up original app.asar...", style="yellow")
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
            else:
                console.print(f"Warning: No original app.asar found for version {version}. Skipping backup.", style="yellow")
                log_error(f"No original app.asar found for version {version}")
            
            console.print("Patching app.asar...", style="yellow")
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

            console.print("Patching completed successfully.", style="green")
        except Exception as e:
            console.print(f"Error during patching: {e}", style="bold red")
            log_error(f"Error during patching: {e}")
            wait_and_clear()
            return

    console.print("[bold green]All patches completed![/bold green]", justify="center")
    wait_and_clear()

def restore_app():
    user_directory = os.path.expanduser("~")
    backup_folder = os.path.join(os.getcwd(), 'Backups')

    if not os.path.exists(backup_folder):
        console.print("Error: No backup folder found.", style="bold red")
        log_error("No backup folder found for restoration.")
        wait_and_clear()
        return

    backup_files = glob.glob(os.path.join(backup_folder, '*.asar'))

    if not backup_files:
        console.print("Error: No backup files found.", style="bold red")
        log_error("No backup files found for restoration.")
        wait_and_clear()
        return

    for backup_file in backup_files:
        console.print(f"Restoring from backup: {backup_file}", style="yellow")
        try:
            version = os.path.basename(backup_file).replace('app_backup_', '').replace('.asar', '')
            app_folder = os.path.join(user_directory, 'AppData', 'Local', 'WeMod', f'app-{version}')
            destination_path = os.path.join(app_folder, 'resources', 'app.asar')

            shutil.copy(backup_file, destination_path)
            console.print(f"Successfully restored backup for version: {version}.", style="green")
        except Exception as e:
            console.print(f"Error during restoration: {e}", style="bold red")
            log_error(f"Error during restoration: {e}")

    console.print("[bold green]All restorations completed![/bold green]", justify="center")
    wait_and_clear()

def main():
    display_start_menu()
    
    while True:
        option = console.input("[bold cyan]Select an option: [/bold cyan]").strip()

        if option == "1":
            patch_app()
        elif option == "2":
            restore_app()
        elif option in ["3", "exit"]:
            console.print("[bold red]Exiting...[/bold red]")
            break
        elif option in ["--help", "?"]:
            display_help()
        else:
            console.print("[bold red]Invalid option. Please try again.[/bold red]")

if __name__ == "__main__":
    main()
