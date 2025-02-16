import xml.etree.ElementTree as ET
import json

def xml_to_dict(element):
    """Recursively converts XML elements into a dictionary."""
    data = {}
    
    # Convert attributes
    if element.attrib:
        data.update(element.attrib)
    
    # Convert child elements
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in data:
            if isinstance(data[child.tag], list):
                data[child.tag].append(child_data)
            else:
                data[child.tag] = [data[child.tag], child_data]
        else:
            data[child.tag] = child_data
    
    # Include text content if present
    text = element.text.strip() if element.text else ''
    if text and not data:
        return text
    if text:
        data['text'] = text
    
    return data

def convert_xml_to_json(xml_file, json_file):
    """Parses an XML file and saves it as a JSON file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data_dict = xml_to_dict(root)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4)
    
    print(f"JSON file saved as {json_file}")

# Example usage
xml_file_path = "resu.xml"  # Change this to your actual file path
json_file_path = "output.json"
convert_xml_to_json(xml_file_path, json_file_path)
