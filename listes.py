
is_Run = True
liste = []
def quick():
    print("1. Einen Artikel hinzufügen")
    print("2. Einen Artikel löschen.")
    print("3. Die Einkaufsliste anzeigen. ")
    print("4. Die Einkaufsliste leer machen.")
    print("5. Das Programm beenden.")


print("Willkommen in dem Programm Liste")
while is_Run:
    print("\n")
    quick()
    print("\n")
    number =input("Bitte wählen Sie eine Nummer: ")


    if number == "1":
        name = input("Geben Sie den Name des Artikels ein: ")
        liste.append(name)
    elif number == "2":
        print("Ihre Aktuelle Liste: ")
        for i in range(len(liste)):
            print(f"{i+1}. {liste[i]}")
        index = int(input("Geben Sie die Nummer des Artikels der sie löschen wollen:  "))
        del liste[index-1]
    elif number == "3":
       if len(liste) == 0:
           print("Ihre Liste ist leer.")
       else:
           for i in liste:
               print(i)
    elif number == "4":
        if liste:
            liste.clear()
            print("Die Einkaufsliste wurde leer gemacht.")

    elif number == "5":
        print("Good bye !")
        is_Run = False
    else:
        print("Die angegebene Zahl war leider ungüldig.")