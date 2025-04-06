import os
from win32ui import CreateFileDialog

decryption_factor = 64 # CURRENT PYOBFUSCATE LAYERS - might change - 04/06/25 #

global gcode
old_exec = None
is_exec_hooked = False

def clone(f):
    return f

def hook_exec():
    global old_exec
    global is_exec_hooked

    def hooked_exec(src, *args, **kwargs) -> str:
        global gcode
        if isinstance(src, bytes):
            gcode = src.decode()
        else:
            gcode = str(src)

    if not is_exec_hooked:
        old_exec = clone(exec) 
        globals()['exec'] = hooked_exec
        is_exec_hooked = True

# for pyobfuscate code to run in our emulated environment
import ctypes
import sys
import os

def decrypt(src):
    global gcode

    if not is_exec_hooked:
        hook_exec()

    _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1])) # pyobfuscate decrypt proto as of 04/06/25 - might change #
    
    old_exec(src)

    return gcode

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
decompiled_file = get_file_name(file_path) + "-decompiled.txt"

gcode = obfuscated_code

for _ in range(decryption_factor):
    if gcode:
        gcode = decrypt(gcode)
    else:
        gcode = decrypt(obfuscated_code)

with open(decompiled_file, "w", encoding="utf-8") as f:
    f.write(gcode)

print("Successfully decrypted and saved file to: " + str(decompiled_file))
pause()
