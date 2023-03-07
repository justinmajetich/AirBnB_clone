#!/usr/bin/python3

import ast

from pathlib import Path

parameters = {
    "input_filename": "console.py",
    "node_types": (ast.ClassDef, ast.FunctionDef),
    "target_dir": ""
}
all_src = Path(parameters["input_filename"]).read_text()

parsed_ast = ast.parse(all_src)

matching_nodes = [
    node for node
        in ast.walk(parsed_ast)
            if isinstance(node, parameters["node_types"])
]
parameters["class_name"] = matching_nodes.pop(0).name

methods = (
    {
        "src_file_name": "{}_{}.py".format(parameters["class_name"], node.name),
        "method_name": node.name,
        "code": "{}\n\n{}\n".format(
            (Path(__file__).read_text()).split("\n")[0],
            ast.get_source_segment(
                    all_src,
                    node,
                    padded=False
                )
        )
    } for node in matching_nodes
)
for info_method in methods:
    file_obj = Path(info_method["src_file_name"])
    file_obj.write_text(info_method["code"])
