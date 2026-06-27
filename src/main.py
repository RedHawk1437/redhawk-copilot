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
    root = load_xml("scans/metasploitable2_scan.xml")

    # Find required XML elements
    host = root.find("host")
    host_status = host.find("status")
    host_address = host.find("address")
    ports = host.find("ports")
    all_ports = ports.findall("port")

    # Extract attribute values
    host_state = host_status.get("state")
    ip_address = host_address.get("addr")

    print("XML loaded successfully.")

    # Printing the host information
    print("\nHost Information")
    print("-"*20)
    print("Status : ", host_state)
    print("IP Address : ", ip_address)
    print("\nOpen Ports")
    print("-" * 20)

    for port in all_ports:
        state = port.find("state")
        service =port.find("service")
        port_id = port.get("portid")
        protocol = port.get("protocol")
        port_state = state.get("state")
        service_name = service.get("name")
        service_product = service.get("product")
        service_version = service.get("version")
        print("-" * 20)
        print(f"Port : {port_id}/{protocol}")
        print(f"Port State :  {port_state}")
        print(f"Port Service :  {service_name}")
        print(f"Port Product :  {service_product}")
        print(f"Port Version :  {service_version}")



if __name__ == "__main__":
    main()