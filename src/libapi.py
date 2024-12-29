# Library for my API
# Contains funcs like I/O from visits.txt

VISITS_FILE = "visits.txt"

def get_visits():
    with open(VISITS_FILE, "r") as f:
        return int(f.read())

def increment_visits():
    visits = get_visits()
    visits += 1
    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))