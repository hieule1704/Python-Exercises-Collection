import xml.etree.ElementTree as ET

# Parse the XML files
tree_nhom = ET.parse('nhomthietbi.xml')
tree_thietbi = ET.parse('thietbis.xml')

root_nhom = tree_nhom.getroot()
root_thietbi = tree_thietbi.getroot()


# Function to display all device groups
def display_groups():
    print("Danh sách Nhóm Thiết bị:")
    for nhom in root_nhom.findall('nhom'):
        ma = nhom.find('ma').text
        ten = nhom.find('ten').text
        print(f'Mã nhóm: {ma}, Tên nhóm: {ten}')


# Function to display all devices
def display_devices():
    print("Danh sách Thiết bị:")
    for thietbi in root_thietbi.findall('thietbi'):
        ma = thietbi.find('ma').text
        ten = thietbi.find('ten').text
        manhom = thietbi.attrib['manhom']  # attribute of thietbi
        print(f'Mã thiết bị: {ma}, Tên thiết bị: {ten}, Thuộc nhóm: {manhom}')


# Function to filter devices by group
def filter_devices_by_group(group_id):
    print(f"Thiết bị trong Nhóm {group_id}:")
    for thietbi in root_thietbi.findall('thietbi'):
        if thietbi.attrib['manhom'] == group_id:
            ma = thietbi.find('ma').text
            ten = thietbi.find('ten').text
            print(f'Mã thiết bị: {ma}, Tên thiết bị: {ten}')


# Function to find the group with the most devices
def group_with_most_devices():
    group_count = {}

    # Count devices per group
    for thietbi in root_thietbi.findall('thietbi'):
        group_id = thietbi.attrib['manhom']
        group_count[group_id] = group_count.get(group_id, 0) + 1

    # Find the group with the most devices
    max_group = max(group_count, key=group_count.get)
    print(f"Nhóm {max_group} có nhiều thiết bị nhất: {group_count[max_group]} thiết bị")


# Example usage:
display_groups()  # Display all groups
display_devices()  # Display all devices
filter_devices_by_group('n1')  # Filter devices by group 'n1'
group_with_most_devices()  # Find the group with the most devices
