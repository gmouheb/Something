import json

def extract_all_ports(json_data):
    """
    Extract all port IDs and protocols from Nmap JSON data
    
    Args:
        json_data: The parsed JSON data
        
    Returns:
        List of dictionaries containing port information
    """
    results = []
    
    try:
        # Navigate to the ports section
        host = json_data.get("nmaprun", {}).get("host", {})
        ports = host.get("ports", {})
        port_list = ports.get("port", [])
        
        # Handle case where there's only one port (not in a list)
        if port_list and not isinstance(port_list, list):
            port_list = [port_list]
        
        # Process each port
        for i, port in enumerate(port_list):
            port_info = {
                "index": i,
                "portid": port.get("@portid"),
                "protocol": port.get("@protocol"),
                "state": port.get("state", {}).get("@state") if isinstance(port.get("state"), dict) else None,
                "service": port.get("service", {}).get("@name") if isinstance(port.get("service"), dict) else None
            }
            results.append(port_info)
        
    except (AttributeError, KeyError, TypeError) as e:
        print(f"Error accessing port data: {str(e)}")
    
    return results

# Main function
def main():
    filename = "outputNew.json"
    
    try:
        # Open and read the JSON file
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Extract all port information
        all_ports = extract_all_ports(data)
        
        if all_ports:
            print(f"Found {len(all_ports)} ports in the scan results:\n")
            print("PORT ID\tPROTOCOL\tSTATE\tSERVICE")
            print("-" * 50)
            
            for port in all_ports:
                print(f"{port['portid']}\t{port['protocol']}\t\t{port['state'] or 'N/A'}\t{port['service'] or 'N/A'}")
                
            print("\nDetailed information:")
            for i, port in enumerate(all_ports, 1):
                print(f"\nPort #{i}:")
                print(f"  Port ID: {port['portid']}")
                print(f"  Protocol: {port['protocol']}")
                print(f"  State: {port['state'] or 'N/A'}")
                print(f"  Service: {port['service'] or 'N/A'}")
                print(f"  JSON path: nmaprun.host.ports.port[{port['index']}]")
        else:
            print("No port information found in the JSON file.")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()