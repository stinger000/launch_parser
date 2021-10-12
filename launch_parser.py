import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

# doc = minidom.parse("clover.launch")
# items = doc.getElementsByTagName("arg")
# for i in items:
#     print(i.attributes['name'].value, i.attributes['default'].value)

# tree = ET.parse("clover.launch")
# root = tree.getroot()
# for elem in root:
#     if elem.tag == "arg":
#         print(elem.tag, elem.attrib)
#         elem.attrib["default"] = elem.attrib["default"] + "1"
# tree.write("test.launch")

class Argument:
    pass

class ArgumentBool(Argument):
    pass

class LaunchParser:
    def __init__(self, file: str, rule: dict):
        self.tree = ET.parse(file)
        root = self.tree.getroot()
        self.args = [elem for elem in root if elem.tag == "arg"]
        for i in self.args:
            if any([i.attrib["name"] == line["name"] for line in rule]):
                print(i.attrib)


    def parse(self, rules):
        pass

class LaunchDescription:
    def __init__(self, file) -> None:
        self.tree = ET.parse(file)
        
    
    def get_file_description(self, filename: str):
        sections = self.tree.findall(f".//*[@name='{filename}']/arg")
        args = [i.attrib.copy() for i in sections]
        return args
            
    

        
l = LaunchDescription("description.xml")
clover_args = l.get_file_description("clover.launch")
# print(clover_args)
LaunchParser("test.launch", clover_args)