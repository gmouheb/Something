import xml.etree.ElementTree as ET
import json
import argparse


def parse_xml_to_json(xml_file, json_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        data = {"scan_results": []}

        for host in root.findall(".//host"):
            host_data = {
                "ip": host.findtext("address", default="Unknown"),
                "os": host.findtext("os", default="Unknown"),
                "ports": [],
                "vulnerabilities": []
            }

            for port in host.findall(".//port"):
                port_data = {
                    "port": port.get("portid"),
                    "protocol": port.get("protocol", "Unknown"),
                    "service": port.findtext("service", default="Unknown")
                }
                host_data["ports"].append(port_data)

            for vuln in host.findall(".//vulnerability"):
                vuln_data = {
                    "id": vuln.findtext("id", default="Unknown"),
                    "cve": vuln.findtext("cve", default="N/A"),
                    "cvss": vuln.findtext("cvss", default="N/A"),
                    "risk": vuln.findtext("risk", default="Unknown"),
                    "description": vuln.findtext("description", default="No description"),
                    "solution": vuln.findtext("solution", default="No solution provided")
                }
                host_data["vulnerabilities"].append(vuln_data)

            data["scan_results"].append(host_data)

        with open(json_file, "w") as json_out:
            json.dump(data, json_out, indent=4)

        print(f"✅ Extraction completed. JSON saved as {json_file}")

    except Exception as e:
        print(f" Error parsing XML: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert XML vulnerability scan report to JSON.")
    parser.add_argument("xml_file", help="Path to the input XML file")
    parser.add_argument("json_file", help="Path to save the output JSON file")
    args = parser.parse_args()

    parse_xml_to_json(args.xml_file, args.json_file)
