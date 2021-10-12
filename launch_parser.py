import xml.etree.ElementTree as ET
from typing import List


# tree = ET.parse("clover.launch")
# root = tree.getroot()
# for elem in root:
#     if elem.tag == "arg":
#         print(elem.tag, elem.attrib)
#         elem.attrib["default"] = elem.attrib["default"] + "1"
# tree.write("test.launch")

class Argument:
    def __init__(self, arg: ET.Element, rule: dict) -> None:
        self.arg = arg
        self.rule = rule
        
    def get(self):
        return self.arg.attrib["default"]

    def get_name(self):
        return self.rule.get("name")

    def get_datatype(self):
        return self.rule.get("datatype")

    def set(self, new_val):
        if self.validate(new_val):
            self.arg.attrib["default"] = str(new_val)

    def validate(self):
        return True

class ArgumentBool(Argument):
    def get(self):
        s: str = super().get()
        if s.lower() == "false":
            return False
        return True
        
    def set(self, new_val):
        if new_val:
            self.arg.attrib["default"] = "true"
        else:
            self.arg.attrib["default"] = "false"

class ArgumentStr(Argument):
    pass

class ArgumentInt(Argument):
    def get(self):
        return int(super().get())

class ArgumentFloat(Argument):
    def get(self):
        return float(super().get())

class ArgumentEnum(Argument):
    def get_variants(self):
        return self.rule["items"]

def get_argument_class_from_datatype(datatype: str):
    """
    Return Argument class corresponding to given datatype
    """
    types = {"bool" : ArgumentBool,
            "str" : ArgumentStr,
            "int" : ArgumentInt,
            "float" : ArgumentFloat,
            "enum" : ArgumentEnum}
    argument_class = types.get(datatype)
    if not argument_class:
        raise ValueError(f"Unknown datatype - {datatype}")
    else:
        return argument_class

class LaunchParser:
    filtered_args: List[Argument]

    def __init__(self, file: str, rules: list):
        self.tree = ET.parse(file)
        root = self.tree.getroot()
        self.args = [elem for elem in root if elem.tag == "arg"]
        self.filtered_args = []
        for arg in self.args:
            for rule in rules:
                if arg.attrib["name"] == rule["name"]:
                    # add new filtered_arg
                    argument_class = get_argument_class_from_datatype(rule.get("datatype"))
                    self.filtered_args.append(argument_class(arg, rule))
                    break
        


    def get_args(self):
        return self.filtered_args

class LaunchDescription:
    def __init__(self, file) -> None:
        self.tree = ET.parse(file)
        
    
    def get_file_description(self, filename: str):
        sections = self.tree.findall(f".//*[@name='{filename}']/arg")
        args = []
        for i in sections:
            attrib = i.attrib.copy()
            if i.attrib["datatype"] == "enum":
                items = i.findall("item")
                attrib["items"] = [item.attrib["value"]for item in items]
            args.append(attrib)

        return args
            
    

        
l = LaunchDescription("description.xml")
clover_args = l.get_file_description("aruco.launch")
pars =  LaunchParser("aruco.launch", clover_args)
a = pars.get_args()
for i in a:
    print(i.get_name(), i.get_datatype(), i.get())
    if i.get_datatype() == "enum":
        print(i.get_variants())