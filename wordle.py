import random

slowa = {
    "1": "trawa",
    "2": "drzwi",
    "3": "chleb",
    "4": "rybka",
    "5": "wiatr",
    "6": "kwiat",
    "7": "nocny",
    "8": "słoik",
    "9": "kotek",
    "10": "morze",

    "11": "lasem",
    "12": "góral",
    "13": "rzeka",
    "14": "super",
    "15": "kamyk",
    "16": "ogień",
    "17": "deska",
    "18": "śnieg",
    "19": "liści",
    "20": "drwal",

    "21": "niebo",
    "22": "chmura",
    "23": "burza",
    "24": "plaża",
    "25": "fala",
    "26": "mosty",
    "27": "droga",
    "28": "ulica",
    "29": "domki",
    "30": "okapy",

    "31": "dachy",
    "32": "kubek",
    "33": "taler",
    "34": "banan",
    "35": "mleko",
    "36": "wodny",
    "37": "kawka",
    "38": "rower",
    "39": "motyl",
    "40": "ptaki",

    "41": "żaba",
    "42": "lisek",
    "43": "wilki",
    "44": "zamek",
    "45": "pokój",
    "46": "świat",
    "47": "skarb",
    "48": "głosy",
    "49": "piesy",
    "50": "ogród",

    "51": "szopa",
    "52": "kreda",
    "53": "farba",
    "54": "szafa",
    "55": "krata",
    "56": "karta",
    "57": "mapka",
    "58": "trakt",
    "59": "płoty",
    "60": "kwiat",

    "61": "sarna",
    "62": "dzika",
    "63": "kuna",
    "64": "sowa",
    "65": "orlik",
    "66": "gęśla",
    "67": "łania",
    "68": "kocio",
    "69": "myszy",
    "70": "płasz",

    "71": "butla",
    "72": "kabel",
    "73": "pilot",
    "74": "sznur",
    "75": "torba",
    "76": "pudeł",
    "77": "klucz",
    "78": "zegar",
    "79": "okres",
    "80": "sklep",

    "81": "szosa",
    "82": "wagon",
    "83": "torow",
    "84": "lotny",
    "85": "state",
    "86": "łódka",
    "87": "płynę",
    "88": "wiara",
    "89": "honor",
    "90": "duma",

    "91": "serce",
    "92": "głowa",
    "93": "palec",
    "94": "zębat",
    "95": "kości",
    "96": "mięso",
    "97": "skóra",
    "98": "dusza",
    "99": "sfera",
    "100": "posta"
}

proby = 8

rand = random.randrange(1, 100)

chosen = slowa.get(f"{rand}")

sliced = []

slowo = []

for i in range(5):
    slicedi = chosen[i]
    sliced.append(slicedi)

for i in range (8):
    zgadyanie = input("Wprowadz słowo: ").lower()
    if len(zgadyanie) > 5:
        print("Hej, słowo jest zbyt długie! MAX: 5 znaków")
        continue

    if zgadyanie == chosen:
        print("Zgadłeś Wygrałeś!")
        break

    if any(s in sliced for s in zgadyanie):
        dopasowania = [f for f in sliced if f in zgadyanie]
        proby -= 1
        print("Zgadłeś litere pozostało prob:", proby, "Zgadnięta litera", dopasowania)
    else:
        proby -= 1
        print("Nic nie zgadłeś", proby)

    if proby == 0:
        print("Przegrałeś", chosen)
        break