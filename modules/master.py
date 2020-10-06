import helper as h

def name_in_master():
    return __name__

if __name__ == "__main__":
    print(name_in_master(), "\t< name in this file (master.py)")
    print(h.name_in_helper(), "\t\t< name of imported file (helper.py)")