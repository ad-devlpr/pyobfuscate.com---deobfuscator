import os
from win32ui import CreateFileDialog

def clone(f):
    return f

def get_file_name(path):
    path = str(path)
    return path.split("\\")[path.count("\\")].split(".")[0]
    

os.system("title PyObfuscate.com - Decompiler / @virtualqueryex")

pause = lambda: os.system("pause")

print("Choose a file to decompile...")

dlg = CreateFileDialog(1)  # 1 = Open file dialog
dlg.DoModal()
file_path = dlg.GetPathName()

print(get_file_name(file_path))

if not file_path:
    print("Invalid file!")
    pause()
    exit()

obfuscated_code = open(file_path, "r", encoding="utf-8").read()

## place hook ##
old_exec = clone(exec)

decompiled_file = get_file_name(file_path) + "-decompiled.txt"

def hooked_exec(src, *args, **kwargs):
    open(decompiled_file, str(src)) # directly write passed src as its already decrypted

exec = hooked_exec
old_exec(obfuscated_code) # run the script so that it decrypts the actual script
exec = old_exec # restore [whats the point eitherways]

print("Successfully decrypted and saved file to: " + str(decompiled_file))
pause()