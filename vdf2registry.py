from os import path
from glob import glob
from subprocess import check_output
from vdf import loads

def main():
    for files in glob("*.vdf"):
        with open(files, "r") as file:
            try:
                keys = loads(file.read())["InstallScript"]["Registry"]
                for key in keys:
                    try:
                        try_type(key, keys[key]["dword"], "REG_DWORD")
                    except KeyError:
                        pass
                    try:
                        try_type(key, keys[key]["string"], "REG_SZ")
                    except KeyError:
                        pass
            except KeyError:
                print("Warning: Nothing to add from " + files)
    input("Press Enter to continue...")

def get_cur_dir():
    return path.dirname(path.realpath(__file__))

def proc(string):
    return string.replace("\\\\", "\\").replace("%INSTALLDIR%", get_cur_dir())

def try_type(key, input, type):
    for entry in input:
        reg_add(proc(key), proc(entry), proc(input[entry]), type)

def reg_add(key, name, data, type):
    args = ["REG", "ADD", key, "/v", name, "/t", type, "/d", data, "/f"]
    print("Adding:", key, name, data)
    return check_output(args)

if __name__ == "__main__":
    main()