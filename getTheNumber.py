import random

tries = 6
jokers = 1

regel = '''In diesem Spiel geht es darum, die geheime Zahl des Computers zu erraten. 
Dafür stehen Ihnen nur 5 Versuche zur Verfügung.
Nach jedem Versuch wird die Anzahl der verbleibenden Versuche angezeigt, sodass Sie stets den Überblick über Ihren Fortschritt behalten.
Sobald Ihnen nur noch 2 Versuche bleiben, können Sie einmalig einen Joker einsetzen, um zusätzliche Hinweise zu erhalten, die Ihnen beim Erraten der Zahl helfen.
Setzen Sie diesen Joker klug ein, denn er könnte den entscheidenden Unterschied machen!
Zusammengefasst: Erraten Sie die Zahl, bleiben Sie strategisch, und beachten Sie, dass die Herausforderung mit jedem fehlgeschlagenen Versuch steigt.
Viel Erfolg – und vor allem: Viel Spaß! 🎉  
    \n'''

mistery_number = random.randint(1,100)

print('''  ✮✮✮ Willkommen im GET THE NUMBER ✮✮✮  ''')
print(regel)

def getIn():
   print(f"\033[38;5;129mVersuch: {tries}\033[0m")
   print(f"\033[38;5;39mJoker: {jokers}\033[0m")

while tries > 0:
    try:
        number = int(input("👉🏽Geben Sie ihre Zahl ein:  "))
        if 1 <= number <= 100:
            if number == mistery_number:
                print("✔︎ Glückwunsch Sie haben die Zahl erratten ✅︎")
                break
            elif number < mistery_number:
                print("\033[38;5;214mIhre Zahl ist niedriger als die geheime Zahl.\033[0m")
                tries -= 1
                getIn()
            elif number > mistery_number:
                print("\033[34mIhre Zahl ist größer als die geheime Zahl.\033[0m")
                tries -= 1
                getIn()
        else:
            print("\033[33mDie angegebene Zahl muss zwischen 1 und 100 sein.\033[0m")
        if tries == 2:
            question = input("\033[96m Wollen Sie den Joker nutzen ?: y/n   \033[0m")
            if question == "n":
                continue
            else:
                jokers -= 1
                if mistery_number % 2 == 0:
                    print("\033[37mDie geheime Zahl ist eine gerade Zahl\033[0m")
                else:
                    print("\033[37mDie geheime Zahl ist eine ungerade Zahl\033[0m")
        if tries == 0:
            print(f"\033[96m Sie haben leider kein Versuch mehr und die geheime Zahl war: {mistery_number} \033[0m")
    except ValueError:
        print("\033[91m Fehler: Bitte geben Sie eine gültige Zahl ein.\033[0m")



