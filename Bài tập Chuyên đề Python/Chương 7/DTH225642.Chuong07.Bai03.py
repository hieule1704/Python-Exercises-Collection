from xml.dom.minidom import parse
import xml.dom.minidom

def main():
    DOMTree = xml.dom.minidom.parse("D:\Python\Chuong7\employees.xml")
    collection = DOMTree.documentElement

    employees = collection.getElementsByTagName("employee")

    for employee in employees:
        tag_id = employee.getElementsByTagName('id')[0]
        id=tag_id.childNodes[0].data
        tag_name = employee.getElementsByTagName('name')[0]
        name=tag_name.childNodes[0].data
        print(id,' | ',name)

if __name__ == "__main__":
    main()