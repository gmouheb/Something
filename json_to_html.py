import json
from html import escape

def dict_to_html(data, indent=0):
    """Recursively converts a dictionary to an HTML formatted string."""
    html = """<ul>"""
    for key, value in data.items():
        html += f"<li><strong>{escape(str(key))}</strong>: "
        if isinstance(value, dict):
            html += dict_to_html(value, indent + 4)
        elif isinstance(value, list):
            html += "<ul>"
            for item in value:
                if isinstance(item, dict):
                    html += f"<li>{dict_to_html(item, indent + 4)}</li>"
                else:
                    html += f"<li>{escape(str(item))}</li>"
            html += "</ul>"
        else:
            html += f"{escape(str(value))}"
        html += "</li>"
    html += "</ul>"
    return html

def convert_json_to_html(json_file, html_file):
    """Reads a JSON file and converts it into an HTML file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html_content = """<html><head><title>JSON Data</title></head><body>""" + dict_to_html(data) + "</body></html>"
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML file saved as {html_file}")

# Example usage
json_file_path = "output.json"  # Change this to your actual JSON file path
html_file_path = "output.html"
convert_json_to_html(json_file_path, html_file_path)