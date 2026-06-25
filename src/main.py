"""
main.py

Purpose:
Entry point of RedHawk Copilot.

Why this file exists:
This file connects all modules together
and starts the application.

Version:
0.1
"""

from parser import load_xml


def main():
    """
    Main function.

    Why this function exists:
    It acts as the starting point of the program.
    """

    root = load_xml("scans/sample_scan.xml")

    print("XML loaded successfully.")

    print("Root tag:", root.tag)

if __name__ == "__main__":
    main()