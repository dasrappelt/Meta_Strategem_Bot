# -*- coding: iso-8859-15 -*-

import tweepy
import sys
import time

ID = 0
s = 0
satz = 0

############Bot-Liste zur Überprüfung, welche Bot verwendet werden muss##################
bot0_liste = [1, 11, 12, 13,
              2, 21, 22, 23,
              3, 310, 320, 330,
              4, 41, 42, 43,
              5, 51, 52, 53,
              6, 61, 62, 63
              ]

bot1_liste = [7, 71, 72, 73,
              8, 81, 82, 83,
              9, 91, 92, 93,
              10, 101, 102, 103,
              11, 111, 112, 113,
              12, 121, 122, 123
              ]

bot2_liste = [13, 131, 132, 133,
              14, 141, 142, 143,
              15, 151, 152, 153,
              16, 161, 162, 163,
              17, 171, 172, 173,
              18, 181, 182, 183
              ]

bot3_liste = [19, 191, 192, 193,
              20, 201, 202, 203,
              21, 211, 212, 213,
              22, 221, 222, 223,
              23, 231, 232, 233,
              24, 241, 242, 243
              ]

bot4_liste = [25, 251, 252, 253,
              26, 261, 262, 263,
              27, 271, 272, 273,
              28, 281, 282, 283,
              29, 291, 292, 293,
              30, 301, 302, 303
              ]

bot5_liste = [31, 311, 312, 313,
              32, 321, 322, 323,
              33, 331, 332, 333,
              34, 341, 342, 343,
              35, 351, 352, 353,
              36, 361, 362, 363
              ]


#########Alle Strategem-Sätze################
saetze = {11: "Diese Aussage hat es in sich, ich würde das beinahe unterstreichen.",
    12: "Diese Aussage wird bei jemanden Anklang finden.",
    13: "Das ist aber eine tolle Idee! ",
    21: "Offensichtlich muss ich meine Enttäuschung über diese Aussage klarstellen.",
    22: "Klar ist, dass ich nicht meinte, wovon gerade ausgegangen wird.",
    310: "Wie bereits von exponierten Teilnehmern eindeutig gesagt wurde, das der Schwerpunkt so aussieht, schließe ich mich nachfolgend an.",
    320: "Laut deiner Twitter Timeline hast du oefters Versucht deine Meinung kund zu tun, ohne Erfolg und ohne Glaubwürdigkeit. Sieh selbst nach.",
    4: "Informiere dich dazu lieber nochmal (random WikipediaLink zum #Thema)",
    41: "", 42: "", 43: "",
    5: "Da ich das vorhergesehen habe, füge ich meine Missachtung der Sache hinzu.",
    51: "", 52: "", 53: "",
    6: "Das sich jemand dieser Sache annimmt ist ein Zeichen, jedoch benoetigt es dafür noch einiges mehr an fundiertem Fachwissen.",
    61: "", 62: "", 63: "", 7: "Wenn die Diskussion hier so weitergeht, haben wir auch bald so einen Trump in Deutschland sitzen.", 71: "", 72: "", 73: "", 8: "Da hast du vollkommen Recht. [Im Gesprächsverlauf mit anderem Strategem “angreifen”]", 81: "", 82: "", 83: "", 9: "@flinkerfinker: Vielleicht solltest du @User A (-) das @User B (+) nochmal erläutern.",
    91: "", 92: "", 93: "", 10: "Da hast du den Nagel auf den Kopf getroffen.",
    101: "", 102: "", 103: "", 11: "Da hast du schon Recht, aber vielleicht solltest du nochmal die andere Seite der Medaille betrachten.", 111: "", 112: "", 113: "",
    12: "Da fällt dir jetzt auch nichts mehr ein oder?", 121: "", 122: "", 123: "",
    13: "", 131: "Bezieh doch endlich mal eindeutig Stellung! Du redest hier doch nur um den heißen Brei.", 132: "Was soll dieses Stammtischgequatsche?", 133: "",
    14: "RT von einem anderen Nutzer zu dem Hashtag", 141: "", 142: "", 143: "",
    15: "Was ist eigentlich so schwierig an korrekter Zeichensetzung?", 151: "", 152: "", 153: "",
    16: "Wahrscheinlich hast du Recht...", 161: "", 162: "", 163: "",
    17: "", 171: "Um das richtig einschaetzen zu koennen benoetigt man genaueres Hintergrundwissen, aber das sind vertrauliche Informationen.", 172: "Wenn du wüsstest was da hinter den Kulissen abgeht...", 173: "Schreib mir mal ne PM, wenn du da was vertrauliches hoeren willst.",
    18: "", 181: "", 182: "", 183: "",
    19: "Eines Tages schauen wir hierdrauf zurück und fragen uns, warum wir uns jemals damit beschaeftigt haben.", 191: "", 192: "", 193: "",
    20: "Sagen Sie, haben sie eine Wiederholung geschaut? Das waere ja amuesant! :D", 201: "", 202: "", 203: "",
    21: "Ich habe ganz gute Verbindungen nach oben und da habe ich anderes gehoert. #journalistsbestfriends", 211: "", 212: "", 213: "",
    22: "Koennen Sie das nochmal erklaeren? Was wollen Sie damit sagen?", 221: "", 222: "", 223: "",
    23: "@lenakonfus: Also ich gebe da @landich eher Recht. Sie @UserXY betrachten es von der falschen Sicht aus.", 231: "", 232: "", 233: "",
    24: "", 241: "", 242: "", 243: "",
    25: "Überleg dir noch einmal genau, mit wem du da in eine Ecke gestellt werden willst.", 251: "", 252: "", 253: "",
    26: "Ich arbeite seit 8 Jahren in diesem Feld. Das haben wir alles schon gehoert. Nenn mir bitte einen Grund, warum jetzt auf einmal alles anders sein sollte.", 261: "", 262: "", 263: "",
    27: "Tweet von Person übernehmen und jeden zweiten Buchstaben groß", 271: "", 272: "", 273: "",
    28: "Koenntest du das bitte noch einmal für Leute unter deinem Niveau erklaeren? || [Erklaert es noch einmal vereinfacht.] || Haha, das stellst du dir nun wirklich zu einfach vor.", 281: "", 282: "", 283: "",
    29: "Zufaellig habe ich das studiert. Mit etwas Sachverstand wüsste man, dass es nicht ganz so einfach sein kann, wie es hier dargestellt wird.", 291: "", 292: "", 293: "",
    30: "Entschuldigung, das ist nun eine wirklich dumme Frage.", 301: "", 302: "", 303: "",
    31: "A strong woman once said fuck that shit and lived happily ever after.", 311: "", 312: "", 313: "",
    32: "Das einzige Problem hier sind deine Erwartungen.", 321: "", 322: "", 323: "",
    33: "Seltsames Team seid ihr.", 331: "", 332: "", 333: "",
    34: "Damit hast du genau meine groeßte Schwaeche getroffen: Sometimes I just don’t give a fuck.", 341: "", 342: "", 343: "",
    35: "", 351: "", 352: "", 353: "",
    36: "Das kann ich mir nicht mehr angucken. Bin jetzt erstmal afk.", 361: "", 362: "", 363: ""}


# Persona
# 0 superior
# 1 confrontation
# 2 attack
# 3 confusing
# 4 gaining
# 5 desperate

############Alle Tokens################
def bot0():
    # Tokens Bot0
    ckey_bot0 = ""
    csecret_bot0 = ""
    akey_bot0 = ""
    asecret_bot0 = ""
    auth = tweepy.OAuthHandler(ckey_bot0, csecret_bot0)
    auth.set_access_token(akey_bot0, asecret_bot0)
    api = tweepy.API(auth)
    return api


def bot1():
    # Tokens Bot1
    ckey_bot1 = ""
    csecret_bot1 = ""
    akey_bot1 = ""
    asecret_bot1 = ""
    auth = tweepy.OAuthHandler(ckey_bot1, csecret_bot1)
    auth.set_access_token(akey_bot1, asecret_bot1)
    api = tweepy.API(auth)
    return api


def bot2():
    # Tokens Bot2
    ckey_bot2 = ""
    csecret_bot2 = ""
    akey_bot2 = ""
    asecret_bot2 = ""
    auth = tweepy.OAuthHandler(ckey_bot2, csecret_bot2)
    auth.set_access_token(akey_bot2, asecret_bot2)
    api = tweepy.API(auth)
    return api


def bot3():
    # Tokens Bot3
    ckey_bot3 = ""
    csecret_bot3 = ""
    akey_bot3 = ""
    asecret_bot3 = ""
    auth = tweepy.OAuthHandler(ckey_bot3, csecret_bot3)
    auth.set_access_token(akey_bot3, asecret_bot3)
    api = tweepy.API(auth)
    return api

def bot4():
    # Tokens Bot4
    ckey_bot4 = ""
    csecret_bot4 = ""
    akey_bot4 = ""
    asecret_bot4 = ""
    auth = tweepy.OAuthHandler(ckey_bot4, csecret_bot4)
    auth.set_access_token(akey_bot4, asecret_bot4)
    api = tweepy.API(auth)
    return api


def bot5():
    # Tokens Bot5
    ckey_bot5 = ""
    csecret_bot5 = ""
    akey_bot5 = ""
    asecret_bot5 = ""
    auth = tweepy.OAuthHandler(ckey_bot5, csecret_bot5)
    auth.set_access_token(akey_bot5, asecret_bot5)
    api = tweepy.API(auth)
    return api

# RANDOM-TWITTERN: Soll die Sichtbarkeit als Bot mindern


def randomTweet(api, Hashtag):
    twt = tweepy.Cursor(api.search, q=Hashtag + " -filter:retweets",
                        lang="de", result_type="mixed").items(1)

    for status in twt:
        satz = status.text
        m = satz
        print("\nBot twittert zur Veringerung seiner Sichtbarkeit:\n",m)
        #api.update_status(m)

############Tweetgenerierung und Post-Funktion#################


def twittern(ID, satz, api, Hashtag, strategem):
    twt = api.get_status(id=ID)
    s = twt
    sn = s.user.screen_name
    m = "@%s " % (sn) + satz
    s = api.update_status(m, s.id)
    print("\nDer Bot hat folgendes getwittert:\n", s.text)

    # Setzt zusätzlich einen randomTweet ab
    randomTweet(api, Hashtag)
    return s


###########Bot-Decider: Entscheidet, welcher Bot zu dem Strategem passt###########
def bot_decider(strategem):
    if strategem in bot0_liste:
        api0 = bot0()
        liste0=[api0, "derDotzkal"]
        return liste0

    elif strategem in bot1_liste:
        api1 = bot1()
        liste1=[api1, "AlexthemanKraft"]
        return liste1

    elif strategem in bot2_liste:
        api2 = bot2()
        liste2=[api2, "flinkerfinker"]
        return liste2

    elif strategem in bot3_liste:
        api3 = bot3()
        liste3=[api3, "lenakonfus"]
        return liste3

    elif strategem in bot4_liste:
        api4 = bot4()
        liste4=[api4, "timlandich"]
        return liste4

    elif strategem in bot5_liste:
        api5 = bot5()
        liste5=[api5, "nadjerado"]
        return liste5
    else:
        print("Error: Der richtige Bot zu dem Strategem wurde nicht gefunden.")
        sys.exit(0)


def strategem_poster(ID, strategem, Hashtag):
    back = bot_decider(strategem)
    api = back[0]
    bot_name = back[1]

    print("\nDie Berechnung hat folgendes Strategem ergeben:", strategem)
    satz = saetze[strategem]
    print("\nFolgender Bot wird angesteuert:", bot_name)
    _twt = [twittern(ID, satz, api, Hashtag, strategem), bot_name]
    time.sleep(5)
    #_twt=api.user_timeline(screen_name=bot_name, count=1)


    return _twt
