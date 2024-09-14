# Wemod Premium Unlocker - Hira

Welcome to the **Wemod Premium Unlocker** repository developed by Hira. This script is designed to patch and restore WeMod application files. Please follow the instructions below to set up and use the script.

## Description

This Python script allows you to:
- **Patch** the WeMod application by replacing the `app.asar` file with a modified version.
- **Restore** the original `app.asar` file from a backup.
- Includes integrity checks to ensure the script has not been modified.

## Compatibility

**The script works with all versions of the WeMod application, except for version 9.10.0.**

| Version         | Status           |
|-----------------|------------------|
| All versions    | ✅ Supported      |
| Version 9.10.0  | ❌ Not Supported  |

## Prerequisites

Before running the script, ensure you have:
- Python 3 installed on your machine.
- The required Python dependencies installed. (see below)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Stochalt/Wemod-Premium-Unlocker
    cd Wemod-Premium-Unlocker
    ```

2. **Install the dependencies:**

    Ensure the following modules are installed:
    - `colorama`
    - `tqdm`
    - `yaspin`
    - `rich`

    You can install these dependencies using `pip`:

    ```bash
    pip install colorama tqdm yaspin rich
    ```

3. **Place your files:**

    Ensure that the `app.asar` file is present in the working directory.

## Usage

1. **Run the script:**

    To run the script, use the `start.bat` file included in the repository. This batch file sets up the environment and launches the Python script.

    ```bash
    start start.bat
    ```

2. **Follow the Instructions:**

    The script will display a menu with the following options:
    - **1** : Patch app
    - **2** : Restore app
    - **3** : Exit

    Follow the displayed instructions to use the script's features.

## Integrity Check

The script includes an integrity check to ensure it has not been modified. If the check fails, the script will terminate with an error message.

## Notes

- **Ensure** that the `signature.txt` file is up-to-date and matches the current hash of the script.
- **Modify** file paths and options according to your specific needs.
- **Works with all versions of the WeMod application, except for version 9.10.0.** ⚠️

## Contact

For any questions or issues, please contact Hira on Discord: [vbvt].

---

Thank you for using **Wemod Premium Unlocker - Hira**! 🎉
