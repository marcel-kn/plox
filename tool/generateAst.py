from io import TextIOWrapper
import sys

if len(sys.argv) != 2:
    print("Usage: generate_ast <output_directory>")
    sys.exit(64)

output_dir = sys.argv[1]


def define_ast(output_dir: str, file_name: str, base_name: str, types: list[str]):
    path = output_dir + "/" + file_name + ".py"

    file = open(path, "w")

    file.write("from ltoken import Token\n\n")

    file.write("class " + base_name + ":\n")
    file.write("\t")
    file.write("pass\n")

    for type in types:
        class_name = type.split(":")[0].strip()
        fields = type.split(":")[1].strip()
        define_type(file, base_name, class_name, fields)

    file.close()


def define_type(file: TextIOWrapper, base_name, class_name, field_list: str):
    file.write("\nclass " + class_name + "(" + base_name + "):\n")
    # Constructor
    fields: list[str] = field_list.split(", ")
    params_string = ""
    for field in fields:
        name = field.split(" ")[1]
        type = field.split(" ")[0]
        if not type == "Object":
            params_string += name + ": " + type + ", "
        else:
            params_string += name + ", "
    params_string = params_string[:-2]
    file.write("\tdef __init__(self, " + params_string + "):\n")
    # Store parameters in fields

    for field in fields:
        name = field.split(" ")[1]
        file.write("\t\tself." + name + " = " + name + "\n")


define_ast(output_dir, "lx_ast", "Expr",
           ["Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right"])
