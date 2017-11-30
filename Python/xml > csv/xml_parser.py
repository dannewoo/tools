import csv
import xml.etree.ElementTree as ET
# First cd into the folder once in the same folder as the xml file you can just reference the file name.
tree = ET.parse('vicki-health.xml')
root = tree.getroot()

with open('vicki-health.csv', 'w') as csvfile:
  csv_writer = csv.writer(csvfile)

  # Write headers to the CSV file
  csv_writer.writerow(['Type', 'Value', 'Date', 'Unit'])

  for child in root:
    if child.get('type'):
      data_type = child.get('type')
    else:
      data_type = 'null'
    if child.get('value'):
      data_value = child.get('value')
    else:
      data_value = 'null'
    if child.get('startDate'):
      data_date = child.get('startDate')
    else:
      data_date = 'null'
    if child.get('unit'):
      data_unit = child.get('unit')
    else:
      data_unit = 'null'

    csv_writer.writerow([data_type, data_value, data_date, data_unit])