import re,sys
import urllib.request as urlb
erreur=0
if(len(sys.argv)==3):
    port=sys.argv[2]
    if(re.match("[A-Z]-[A-Z]",sys.argv[1])):
        if(sys.argv[1][0]>sys.argv[1][2]):
            #ord donne le code ASCII d'une lettre
            min=ord(sys.argv[1][2])
            sup=ord(sys.argv[1][0])
            print("L'intervalle d'extraction est : "+sys.argv[1][2]+"-"+sys.argv[1][0])
        else:
            min=ord(sys.argv[1][0])
            sup=ord(sys.argv[1][2])
            print("L'intervalle d'extraction est : "+sys.argv[1])

    else:
        erreur=1
else:
    if(len(sys.argv)==2):
        port="80"
        print("le port est par défaut")
        if(re.match("[A-Z]-[A-Z]",sys.argv[1])):
            if(sys.argv[1][0]>sys.argv[1][2]):
                #ord donne le code ASCII d'une lettre
                min=ord(sys.argv[1][2])
                sup=ord(sys.argv[1][0])
                print("L'intervalle d'extraction est : "+sys.argv[1][2]+"-"+sys.argv[1][0])
            else:
                min=ord(sys.argv[1][0])
                sup=ord(sys.argv[1][2])
                print("L'intervalle d'extraction est : "+sys.argv[1])
        else:
            erreur=1
            print("Erreur dans le 1er argument, Vous n'avez respecter le format : A-Z, B-F ")
    else:
        print("Le port est par défaut ")
        print("L'intevalle est : A-Z")
        port="80"
        min=ord('A')
        sup=ord('Z')
if(erreur==1):
    print("Erreur dans le 1er argument, Vous n'avez respecter le format : A-Z, B-F ")

else:
    info1 = open("info1.txt", 'w')
    var = 0
    dic = open("subst.dic", 'w', encoding="utf-16-le")
    dic.write('\ufeff')
    for i in range(min, sup + 1):
        #la fonction chr donne le caractere a partir d'un code ascii
        lettre = chr(i)

        response = urlb.urlopen("http://127.0.0.1:" + port + "/vidal/vidal-Sommaires-Substances-" + lettre + ".htm")

        fichHtml = response.read().decode("utf-8")
        trouver = re.findall(r"(?<=[0-9]\.htm\">).+(?=</a>)", fichHtml)

        for j in trouver:
            dic.write(j + ",.N+subst\n")
        info1.write("le nombre d'entités medicales généré pour la lettre " + lettre + " est : " + str(len(trouver)) + "\n")
        var = var + len(trouver)
    info1.write("le nombre total d’entités médicales de type noms de médicaments par substance active de ce dictionnaire est  : " + str(var))
    info1.close()
