from datetime import datetime

i = 1
while i == 1:
    kenteken_input = input("Enter kenteken:")
    kenteken_control = ["AB", "HS", "LR"]

    def get_reaction():
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        if current_hour >= 6 and current_hour <= 12:
            return  "Goedemorgen"
        elif current_hour >= 13 and current_hour <= 18:
            return  "Goedemiddag"
        elif current_hour >= 19 and current_hour <= 23:
            return  "Goedenavond"
        else:
            return "Sorry, de parkeerplaats is ’s nachts gesloten"

    if kenteken_input in kenteken_control:
        print(get_reaction(), '! Welkom bij Fonteyn Vakantieparken')
    else:
        print("U heeft helaas geen toegang tot het parkeerterrein")
