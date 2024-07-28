import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

ascii_title = """


©Copyright T7C and Friends.

                                   ###system info###

   _/
_/_/_/_/        _/_/        _/  _/_/      _/_/_/  _/_/        _/    _/      _/    _/
 _/          _/_/_/_/      _/_/          _/    _/    _/      _/    _/        _/_/
_/          _/            _/            _/    _/    _/      _/    _/      _/    _/
 _/_/       _/_/_/      _/            _/    _/    _/        _/_/_/      _/    _/    v.1.2.0



Available on Termux Android/ Author: T7C.
"""


def get_datetime_info():
    result = os.popen('date').read().strip()
    if result:
        return {"Date and Time": result}
    else:
        return {"error": "Failed to retrieve date and time"}

def get_uptime_info():
    result = os.popen('uptime -p').read().strip()
    if result:
        return {"Uptime": result}
    else:
        return {"error": "Failed to retrieve uptime information"}

def get_cpu_info():
    result = os.popen('cat /proc/cpuinfo').read().strip()
    if result:
        return {"CPU Info": result}
    else:
        return {"error": "Failed to retrieve CPU information"}

def get_ram_info():
    result = os.popen('free -h').read().strip()
    if result:
        return {"RAM Info": result}
    else:
        return {"error": "Failed to retrieve RAM information"}

def get_storage_info():
    result = os.popen('df -h').read().strip()
    if result:
        return {"Storage Info": result}
    else:
        return {"error": "Failed to retrieve storage information"}

def get_system_info():
    result = os.popen('uname -a').read().strip()
    if result:
        return {"System Info": result}
    else:
        return {"error": "Failed to retrieve system information"}

def get_python_version():
    result = os.popen('python --version').read().strip()
    if result:
        return {"Python Version": result}
    else:
        return {"error": "Failed to retrieve Python version"}

def list_files_in_directory():
    result = os.popen('ls -lh').read().strip()
    if result:
        return {"Files": result}
    else:
        return {"error": "Failed to list files"}

def get_network_info():
    result = os.popen('ip addr show').read().strip()
    if result:
        return {"Network Info": result}
    else:
        return {"error": "Failed to retrieve network information"}

def get_termux_version():
    result = os.popen('termux-info | grep "Termux version"').read().strip()
    if result:
        return {"Termux Version": result}
    else:
        return {"error": "Failed to retrieve Termux version"}

def list_installed_packages():
    result = os.popen('pkg list-installed').read().strip()
    if result:
        return {"Installed Packages": result}
    else:
        return {"error": "Failed to list installed packages"}

def get_swap_info():
    result = os.popen('free -h | grep "Swap"').read().strip()
    if result:
        return {"Swap Info": result}
    else:
        return {"error": "Failed to retrieve swap information"}

def check_internet_speed():
    result = os.popen('speedtest-cli').read().strip()
    if result:
        return {"Internet Speed": result}
    else:
        return {"error": "Failed to check internet speed"}

def display_info(title, data):
    console.print(f"\n[bold green]{title}[/bold green]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Key", style="dim", width=25)
    table.add_column("Value")

    if isinstance(data, dict):
        for key, value in data.items():
            table.add_row(str(key), str(value))
    else:
        for item in data:
            table.add_row(str(item), str(data[item]))

    console.print(table)

def display_menu():
    console.print(Panel(ascii_title, style="bold blue"))
    console.print("=== [bold magenta]Menu[/bold magenta] ===")
    console.print("[cyan]1.[/cyan] Check Date and Time")
    console.print("[cyan]2.[/cyan] Check System Uptime")
    console.print("[cyan]3.[/cyan] Check CPU Information")
    console.print("[cyan]4.[/cyan] Check RAM Information")
    console.print("[cyan]5.[/cyan] Check Storage Information")
    console.print("[cyan]6.[/cyan] Check System Information")
    console.print("[cyan]7.[/cyan] Check Python Version")
    console.print("[cyan]8.[/cyan] List Files in Directory")
    console.print("[cyan]9.[/cyan] Check Network Information")
    console.print("[cyan]10.[/cyan] Check Termux Version")
    console.print("[cyan]11.[/cyan] List Installed Packages")
    console.print("[cyan]12.[/cyan] Check Swap Information")
    console.print("[cyan]13.[/cyan] Check Internet Speed")
    console.print("[cyan]14.[/cyan] Others")
    console.print("[cyan]15.[/cyan] Exit")
    choice = Prompt.ask("Enter your choice", choices=[str(i) for i in range(1, 16)])
    return choice

def display_others_menu():
    console.print("=== [bold magenta]Others Menu[/bold magenta] ===")
    console.print("[cyan]1.[/cyan] About Me")
    console.print("[cyan]2.[/cyan] Contact")
    console.print("[cyan]3.[/cyan] Help")
    console.print("[cyan]4.[/cyan] Changelog")
    console.print("[cyan]5.[/cyan] Credits")
    console.print("[cyan]6.[/cyan] Settings")
    console.print("[cyan]7.[/cyan] Feedback")
    console.print("[cyan]8.[/cyan] Version")
    console.print("[cyan]9.[/cyan] Back to Main Menu")
    choice = Prompt.ask("Enter your choice", choices=[str(i) for i in range(1, 10)])
    return choice

def display_about_me():
    content = """
    Author: T7C and Friends
    Purpose: To check various system information on Termux android.
    The source code was built with the function of viewing some information related to the device and not accessing any user information.
    """
    console.print(Panel(content, title="About Me", style="bold magenta"))

def display_contact():
    content = """
    For inquiries or support, please contact us at:
    Email: tranminhtan4953@gmail.com
    Telegram: t.me/tanbaycu
    Github: lysandraBars
    Facebook: https://www.facebook.com/tan.hurican/
    Thank you so much.
    """
    console.print(Panel(content, title="Contact Information", style="bold magenta"))

def display_help():
    content = """
    This program allows you to check various system information on Termux Android.
    Use the main menu to select the information you want to retrieve.
    If you encounter any issues, please refer to the Contact section.
    We use other functions to find information instead of using Termux: API.
    After trying everything, we removed some functions that are blocked in higher Android versions.
    
    """
    console.print(Panel(content, title="Help", style="bold magenta"))

def display_changelog():
    content = """
    Version 1.0.0: Initial release with basic system information checks.
    Version 1.1.0: Added more detailed system information checks and improved UI.
    Version 1.2.0: Added additional features and fixed minor bugs.
    """
    console.print(Panel(content, title="Changelog", style="bold magenta"))

def display_credits():
    content = """
    Developed by T7C and Friends.
    Special thanks to all contributors and testers.
    """
    console.print(Panel(content, title="Credits", style="bold magenta"))

def display_settings():
    content = "Settings options will be available in future updates. Available on Termux Android."
    console.print(Panel(content, title="Settings", style="bold magenta"))

def display_feedback():
    content = """
    We value your feedback. Please send your suggestions or report issues to:
    Email: tranminhtan4953@gmail.com
    """
    console.print(Panel(content, title="Feedback", style="bold magenta"))

def display_version():
    content = "Current version: 1.2.0"
    console.print(Panel(content, title="Version", style="bold magenta"))

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            console.print("Checking date and time...")
            datetime_info = get_datetime_info()
            display_info("Date and Time", datetime_info)
        elif choice == '2':
            console.print("Checking system uptime...")
            uptime_info = get_uptime_info()
            display_info("System Uptime", uptime_info)
        elif choice == '3':
            console.print("Checking CPU information...")
            cpu_info = get_cpu_info()
            display_info("CPU Information", cpu_info)
        elif choice == '4':
            console.print("Checking RAM information...")
            ram_info = get_ram_info()
            display_info("RAM Information", ram_info)
        elif choice == '5':
            console.print("Checking storage information...")
            storage_info = get_storage_info()
            display_info("Storage Information", storage_info)
        elif choice == '6':
            console.print("Checking system information...")
            system_info = get_system_info()
            display_info("System Information", system_info)
        elif choice == '7':
            console.print("Checking Python version...")
            python_version = get_python_version()
            display_info("Python Version", python_version)
        elif choice == '8':
            console.print("Listing files in directory...")
            files = list_files_in_directory()
            display_info("Files in Directory", files)
        elif choice == '9':
            console.print("Checking network information...")
            network_info = get_network_info()
            display_info("Network Information", network_info)
        elif choice == '10':
            console.print("Checking Termux version...")
            termux_version = get_termux_version()
            display_info("Termux Version", termux_version)
        elif choice == '11':
            console.print("Listing installed packages...")
            installed_packages = list_installed_packages()
            display_info("Installed Packages", installed_packages)
        elif choice == '12':
            console.print("Checking swap information...")
            swap_info = get_swap_info()
            display_info("Swap Information", swap_info)
        elif choice == '13':
            console.print("Checking internet speed...")
            internet_speed = check_internet_speed()
            display_info("Internet Speed", internet_speed)
        elif choice == '14':
            while True:
                others_choice = display_others_menu()
                if others_choice == '1':
                    display_about_me()
                elif others_choice == '2':
                    display_contact()
                elif others_choice == '3':
                    display_help()
                elif others_choice == '4':
                    display_changelog()
                elif others_choice == '5':
                    display_credits()
                elif others_choice == '6':
                    display_settings()
                elif others_choice == '7':
                    display_feedback()
                elif others_choice == '8':
                    display_version()
                elif others_choice == '9':
                    break
                else:
                    console.print("[red]Invalid choice. Please try again.[/red]")
        elif choice == '15':
            console.print("See you later...")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")

if __name__ == "__main__":
    main()

