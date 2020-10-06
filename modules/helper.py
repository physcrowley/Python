import master as m

def name_in_helper():
    return __name__

if __name__ == "__main__":
    print(name_in_helper(), "\t< name in this file (helper.py)")
    print(m.name_in_master(), "\t\t< name of imported file (master.py)")