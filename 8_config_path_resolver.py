def resolve_path(path, current_dir):
    if path.startswith("/"):
        return path
    if path.startswith("~/"):
        path = path.replace("~", "/home/gackmar", 1)
        return path
    path = current_dir + "/"  + path
    return path

print(resolve_path("/usr/bin/python", "/home/gackmar"))
print(resolve_path("~/projects/tool.py", "/tmp"))
print(resolve_path("data.txt", "/home/gackmar/projects"))