from io import TextIOWrapper
import sys

if len(sys.argv) != 2:
    print("Usage: generate_ast <output_directory>")
    sys.exit(64)

output_dir = sys.argv[1]


def define_ast(output_dir: str, file_name: str, base_name: str, types: list[str]):
    path = output_dir + "/" + file_name + ".py"

    file = open(path)
    file.write("class " + base_name + ":\n")
    file.write("\t")
    file.write("pass\n\n")

    for type in types:
        class_name = type.split(":")[0].strip()
        fields = type.split(":")[1].strip()
        define_type(file, base_name, class_name, fields)

    file.close()


def define_type(file: TextIOWrapper, base_name, class_name, field_list: str):
    file.write("class " + class_name + "(" + base_name + "):\n")
    # Constructor
    file.write("\tdef __init__(self, " + field_list + ")\n\t")
    # Store parameters in fields
    fields: list[str] = field_list.split(" ")
    for field in fields:
        name = field.split(" ")[1]
        file.write("self." + name + " = " + name + "\n")


define_ast(output_dir, "lx_ast", "Expr",
           ["Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right"])
