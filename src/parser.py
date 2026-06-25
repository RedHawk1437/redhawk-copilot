"""
parser.py

Purpose:
Read Nmap XML files.

Why this file exists:
Before we can analyze scan results,
we must first extract information from XML.

Version:
0.1
"""

import xml.etree.ElementTree as ET


def load_xml(file_path):
    """
    Load an XML file.

    Parameters:
        file_path (str): Path to XML file.

    Returns:
        XML root object.

    Why this function exists:
        Before we can analyze scan data,
        we must first load the XML file.
    """

    tree = ET.parse(file_path)

    root = tree.getroot()

    return root