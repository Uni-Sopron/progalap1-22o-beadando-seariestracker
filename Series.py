import json
with open ("Series.json") as f:
    series = json.load(f)

#ez a függvény bekéri, hogy mit szeretnél csináni a megadott pontok közül. A menü megszámozott szorszámai alapján választhatsz.Ezután vissza adja a számot, amit választottál.
def select_the_menu ():
    question = int (input (f"Menü:""\n""1. Megnézni, hogyan állok a sorozatokkal \n""2. A kövezkező részt megnézni valamelyik sorozatból\n\n""A sorszám megadásával válassz, hogy mit szeretnél csinálni: "))
    while question != 1 and question != 2:
        question = int (input (f"Menü:""\n""1. Megnézni, hogyan állok a sorozatokkal \n""2. A kövezkező részt megnézni valamelyik sorozatból\n\n""Ilyen lehetőség nincs. Kérlek a sorszám megadásával a menüből válassz, hogy mit szeretnél csinálni: "))
    return question



#Megnézi, hogy adott sorozatban, mennyi részt láttál az allből. Ezután kiírja, hogy hogyan állsz a sorozatokkal.
def first_point_of_the_menu(choose_from_the_menu,series):
    if choose_from_the_menu == 1:
        print ("\nA következők szerint láttad eddig a sorozatok részeit:\n")
        for series_name,episodes in series.items():
            watched = 0
            all = 0 
            for idx,episode in enumerate (episodes):
                all +=1
                for key in episode:
                    if episode[key] == "yes":
                        watched +=1
            if watched != all:
                print (f"A {series_name} című sorozatból {watched} részt láttál már, a {all}-ból.\n")
            else:
                print (f"\n Megnézted a {series_name} című sorozatot. ")


def second_point_of_the_menu(choose_from_the_menu):
    if choose_from_the_menu == 2:
        print (f"\nA következő sorozatkoból választhatsz:""\nWednesday""\nThe Witcher""\nManifest""\nThe Queen's Gambit")
        question = input ("\nMelyik sorozatot szeretnéd nézni?")
        if question != "Wednesday" or question != "The Witcher" or question != "Manifest" or question != "The Queen's Gambit":
            print (f"\nA következő sorozatkoból választhatsz:""\nWednesday""\nThe Witcher""\nManifest""\nThe Queen's Gambit")
            question = input ("\nEz nincs a listába, kérlek abból válassz. Melyik sorozatot szeretnéd nézni?")
        return question


def watched_the_next_episode(selected_series,series):
    for series_name,episodes in series.items():
        if selected_series == series_name:
            for idx, episode in enumerate (episodes):
                if episode["watched"] == "no":
                    episode ["watched"] = "yes"
                    print(f"\nAz epizód címe: {episodes[0] ['name']} \n\nTartalom: {episodes[0] ['description']}\n\nIdőtartam: {episodes[0] ['minute']}perc.")
                    print (f"\nMegnézted a {series_name} sorozat {idx+1} epizódját")
                    break
            return series


def switch_watched_in_json (watched_series,choose_from_the_menu):
    if choose_from_the_menu == 2:
        with open ("Series.json", "w") as file:
            json.dump(watched_series,file,indent=4)

choose_from_the_menu = select_the_menu ()
check_out_series_status = first_point_of_the_menu(choose_from_the_menu,series)
selected_series = second_point_of_the_menu(choose_from_the_menu)
watched_series = watched_the_next_episode(selected_series,series)
Series_json = switch_watched_in_json (watched_series,choose_from_the_menu)


    





                        