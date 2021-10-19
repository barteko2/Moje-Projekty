import os
import fire
cur_dir = os.getcwd()
print(cur_dir)

split_zm = os.path.split(cur_dir)
print(split_zm)

dirname_zm = os.path.dirname(cur_dir)
print(dirname_zm)

basename_zm = os.path.basename(cur_dir)
print(basename_zm)

while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)

def find_rc(rc_name=".examplerc"):
    #sprawdzenie zmiennej środowiskowej
    var_name ="EXAMPLERC_DIR"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}", rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Sprawdzenie {config_path}")
        if os.path.exists(config_path):
            return config_path

    #sprawdź bieżący katalog roboczy
    config_path = os.path.join(os.getcwd(),rc_name)
    print(f"sprawdzanie w katalogu roboczym {config_path}")
    if os.path.exists(config_path):
        return config_path

    #sprawdzanie katalogu macierzystego użytkownika
    home_dir = os.path.expanduser("~/")    #uzyskanie ścieżki do katalogu macierzystego
    config_path = os.path.join(home_dir,rc_name)
    print(f"sprawdzanie {config_path}")
    if os.path.exists(config_path):
        return config_path
    #sprawdzanie katalogu tego pliku
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Sprawdzanie{config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"nie znaleziono pliku {rc_name}")

print(find_rc())


#!!!!!!!!!!!!!!!!!!METODA WYPISUJE WSZYSTKIE PLIKI I KATALOGI W KATALOGU WRAZ Z INFORMACJAMI NA ICH TEMAT.!!!!!!!!!!!!
def walk_path(parent_path):
    print(f"sprawdzanie: {parent_path}")
    childs = os.listdir(parent_path)

    for child in childs:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"Plik: {child_path}")
            print(f"\tostatni dostęp: {last_access}")
            print(f"\trozmiar:{size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)

    #if __name__ == '__main__':
    #    fire.Fire()

#walk_path("/home/bartek/PycharmProjects/Moje-Projekty")

#PRZEGLĄDANIE DRZEW KATALOGÓW ZA POMOCĄ FUNKCJI OS.WALK

def walk_path_oswalk(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"sprawdzanie: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            if size > 1000:
                print(f"Plik: {file_path}")
                print(f"\tostatni dostęp: {last_access}")
                print(f"\trozmiar:{size}")

print(f"A TERAZ OS.WALK")
walk_path_oswalk("/home/bartek/PycharmProjects/Moje-Projekty")


