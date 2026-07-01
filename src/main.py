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

# Printing the host information
def print_host_information(host_state, ip_address):
    print(f"\nHost Information")
    print(f"-" * 20)
    print(f"Status : {host_state}")
    print(f"IP Address : {ip_address}")

#Get Target Service from User
def get_target_service():
    print("\nTarget Service")
    print("-" * 20)
    target_service = input("Enter the Target Service : ").lower().strip()
    print(f"Searching For Target Service : {target_service} ")
    return target_service

#Analyze all open ports and find the requested service.
def port_analyzer(all_ports, target_service):
    """
    Analyze all open ports and find the requested service.

    Returns:
        target_service_found
        target_service_count
    """
    # Initialize analysis state
    target_service_found = False
    target_service_count = 0
    for port in all_ports:
        state = port.find("state")
        service = port.find("service")
        port_id = port.get("portid")
        protocol = port.get("protocol")
        port_state = state.get("state")
        service_name = service.get("name")

        # Compare the targeted service with the XML data
        if service_name == target_service:
            target_service_found = True
            service_product = service.get("product")
            service_version = service.get("version")
            print("-" * 20)
            print(f"Port : {port_id}/{protocol}")
            print(f"Port State :  {port_state}")
            print(f"Port Service :  {service_name}")
            print(f"Port Product :  {service_product}")
            print(f"Port Version :  {service_version}")
            target_service_count += 1
    return target_service_found, target_service_count


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

    # Printing the Host Information
    print_host_information(host_state, ip_address)

    # Getting Input from the Targeted Service Function
    target_service = get_target_service()

    # Printing the Targeted services with their Ports and other information
    print("\nOpen Ports")

    # Analyze requested service
    target_service_found, target_service_count = port_analyzer(
        all_ports,
        target_service
    )

    # Target Service Status
    if not target_service_found:
        print(f"\nTarget Service Status")
        print("-" * 20)
        print("Target Service not found.")

    # Count the Founded Targeted Services
    print(f"\nTotal Target Service Count")
    print("-" * 20)
    print(f"Matching Target Services Count is : {target_service_count}")



if __name__ == "__main__":
    main()