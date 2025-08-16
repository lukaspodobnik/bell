import os

command = "typer {{ path }} utils docs --name {{ name }} --output {{ output }}"

path_commands = "src/bell/commands/"
path_add = path_commands + "/add"
path_init = path_commands + "/init"
path_remove = path_commands + "/remove"
path_show = path_commands + "/show"

for group in ["add", "init", "remove", "show"]:
    for file_name in os.listdir(path_commands + group):
        if "__init__.py" in file_name or "__pycache__" in file_name:
            continue

        cmd = command.replace("{{ path }}", path_commands + group + "/" + file_name)
        cmd = cmd.replace("{{ name }}", f'"bell {group} {file_name[:-3]}"')
        cmd = cmd.replace(
            "{{ output }}",
            f"docs/{group}_{file_name}.md",
        )

        os.system(cmd)
