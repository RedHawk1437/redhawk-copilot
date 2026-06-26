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

    # Load XML file
    root = load_xml("scans/sample_scan.xml")

    # Find required XML elements
    host = root.find("host")
    status = host.find("status")
    address = host.find("address")

    # Extract attribute values
    state = status.get("state")
    ip_address = address.get("addr")
    address_type = address.get("addrtype")

    print("XML loaded successfully.")

    print("Root tag:", root.tag)

    # Printing the host information
    print("\nHost Information")
    print("-"*20)
    print("Status : ", state)
    print("IP Address : ", ip_address)
    print("Address Type : ", address_type)

if __name__ == "__main__":
    main()