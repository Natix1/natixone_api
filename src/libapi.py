# Library for my API
# Contains funcs like I/O from views.txt

VISITS_FILE = "./cfg/views.txt"
MOTD_FILE = "./cfg/motd.txt"

def get_visits():
    with open(VISITS_FILE, "r") as f:
        return str(f.read())

def increment_visits():
    visits = get_visits()
    visits = int(visits) + 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))
        
def get_motd():
    with open(MOTD_FILE, "r") as f:
        return f.read()