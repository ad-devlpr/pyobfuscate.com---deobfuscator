import os
from win32ui import CreateFileDialog

def clone(f):
    return f

def get_file_name(path):
    return os.path.splitext(os.path.basename(path))[0]

os.system("title PyObfuscate.com - Decompiler / @virtualqueryex")

pause = lambda: os.system("pause")

print("Choose a file to decompile...")

dlg = CreateFileDialog(1)
dlg.DoModal()
file_path = dlg.GetPathName()

print(get_file_name(file_path))

if not file_path:
    print("Invalid file!")
    pause()
    exit()

obfuscated_code = open(file_path, "r", encoding="utf-8").read()

old_exec = clone(exec)

decompiled_file = get_file_name(file_path) + "-decompiled.txt"

def hooked_exec(src, *args, **kwargs):
    with open(decompiled_file, "w", encoding="utf-8") as f:
        f.write(str(src))

exec = hooked_exec
old_exec(obfuscated_code)
exec = old_exec

print("Successfully decrypted and saved file to: " + str(decompiled_file))
pause()
