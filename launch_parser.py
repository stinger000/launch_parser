from _typeshed import Self
from os import name
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
    def __init__(self, arg, rule) -> None:
        self.arg = arg
        self.rule = rule
        
    def get(self):
        pass

    def get_datatype(self):
        return self.rule.get("datatype")

    def set(self, new_val):
        Self.validate(new_val)

    def validate(self):
        pass

class ArgumentBool(Argument):
    pass

def get_argument_class_from_datatype(datatype: str):
    types = {"bool" : ArgumentBool,}
    argument_class = types.get(datatype)
    if not argument_class:
        raise ValueError(f"Unknown datatype - {datatype}")
    else:
        return argument_class

class LaunchParser:
    def __init__(self, file: str, rules: list):
        self.tree = ET.parse(file)
        root = self.tree.getroot()
        self.args = [elem for elem in root if elem.tag == "arg"]
        self.filtered_args = []
        for arg in self.args:
            for rule in rules:
                if arg.attrib[name] == rule[name]:
                    # add new filtered_arg
                    argument_class = get_argument_class_from_datatype(rule.get)
                    self.filtered_args.append(argument_class(arg, rule))
                    break
        


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