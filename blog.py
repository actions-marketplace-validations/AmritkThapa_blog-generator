import yaml
import xml.etree.ElementTree as ET

# Load YAML file
with open("blog.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Create root RSS element
rss = ET.Element("rss", attrib={"version": "2.0"})

# Create channel element
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = data["title"]
ET.SubElement(channel, "link").text = data["link"]
ET.SubElement(channel, "description").text = data["description"]

for blog in data.get("blogs", []):
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = blog.get("title", "")
    ET.SubElement(item, "link").text = blog.get("link", "")
    ET.SubElement(item, "description").text = blog.get("description", "")
    ET.SubElement(item, "pubDate").text = blog.get("pubDate", "")

# Write XML to file
tree = ET.ElementTree(rss)
tree.write("blog.xml", encoding="utf-8", xml_declaration=True)

print("RSS feed generated successfully!")
