from lxml import etree


def read_groups_from_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = etree.parse(file)
        root = tree.getroot()
        groups = []
        for nhom in root.findall('nhom'):
            ma = nhom.find('ma').text
            ten = nhom.find('ten').text
            groups.append({'ma': ma, 'ten': ten})
        return groups


def add_group_to_xml(file_path, new_ma, new_ten):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = etree.parse(file)
    root = tree.getroot()
    new_nhom = etree.SubElement(root, 'nhom')
    ma = etree.SubElement(new_nhom, 'ma')
    ma.text = new_ma
    ten = etree.SubElement(new_nhom, 'ten')
    ten.text = new_ten
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')


def main():
    file_path = 'nhomthietbi.xml'
    groups = read_groups_from_xml(file_path)
    print("Danh sách nhóm thiết bị:")
    for group in groups:
        print(f"Ma: {group['ma']}, Ten: {group['ten']}")
    add_group_to_xml(file_path, 'n4', 'Nhóm 4')


if __name__ == "__main__":
    main()
