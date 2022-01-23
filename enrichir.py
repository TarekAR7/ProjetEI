#AROUA Tarek 181831016288
#KHEMAMIL Sabrina 171731077726
#ACAD C

import re, sys, urllib.request
from string import ascii_uppercase


corpus = open(sys.argv[1], 'r+', encoding='utf-8')
 # sauvgarder avant l'enrechissment
tmp = open('subst.dic', 'r+', encoding='utf-16')
dic = open('subst.dic', 'a+', encoding='utf-16')
dicenri = open('subst_corpus.dic', 'w+', encoding='utf-16')
#nb des substances
listCorpus = corpus.readlines()
# liste des mots a eviter
eviter = ["intraveineuse","posologie","hémoglobine","crp","eau","kt","kcl","nfs"]
for l in listCorpus:
    trouver = re.search(r'''^[-*]?\s?(\w+)\s:?\s?(\d+|,|\d+.\d)+\s(mg|ml|µg|mcg|g|cp|amp|flacon).+''', l, re.I)
    # si une substance est trouvée
    if trouver:
        if trouver.group(1).lower() not in eviter:
            # ecrire la substance dans les 2 dictionnaires
            dicenri.write(trouver.group(1).lower()+',.N+subst\n')
            dic.write(trouver.group(1).lower()+',.N+subst\n')

# Tri et suppression des doublons de subst.dic
dic = open('subst.dic', 'r+', encoding='utf-16')
tri = sorted(list(set(dic.readlines())))
dic = open('subst.dic', 'w+', encoding='utf-16')
for i in tri:
    dic.write(i)
# Creation et remplissage du fichier info2.txt
infos2 = open('infos2.txt', 'w+', encoding='utf-8')
dicenri = open('subst_corpus.dic', 'r+', encoding='utf-16')
listDicEnri = dicenri.readlines()
#compter le nombre de substances par lettre de l'alphabet
for letter in ascii_uppercase:
    nbLettre=0
    for elem in list(set(listDicEnri)):
        if letter == elem[0].upper():
            nbLettre+=1
            infos2.write(elem)
    infos2.write('Nombre de Substance issus du corpus pour la lettre '+letter+' est : '+str(nbLettre)+'\n')
    infos2.write('---------------------------------------------------\n')
infos2.write('Nombre Total medicament issus du corpus : '+str(len(list(set(listDicEnri)))) + '\n')
infos2.write('\n---------------------------------------------------')
infos2.close()
# Creation et remplissage du fichier info3.txt
infos3 = open('infos3.txt', 'w+', encoding='utf-8')
dicenri = open('subst_corpus.dic', 'r+', encoding='utf-16')
lst = tmp.readlines()
listDicEnri = dicenri.readlines()
nbLettre = 0
for j in listDicEnri:
    #verifie l'existence de medicament dans subst génré d'aprés VIDAL
    if j not in lst:
        nbLettre+=1
        infos3.write(j)
infos3 = open('infos3.txt', 'r+', encoding='utf-8')
listi = infos3.readlines()
infos3 = open('infos3.txt', 'w+', encoding='utf-8')
#compter le nombre de substances par lettre de l'alphabet
for letter in ascii_uppercase:
    nbLettre=0
    for i in listi:
        if letter == i[0].upper():
            nbLettre+=1
            infos3.write(i)
    infos3.write("Nombre de mediaments issus de l'enrichissement pour la lettre "+letter+' est : '+str(nbLettre)+'\n')
    infos3.write('---------------------------------------------------\n')


infos3.write("Nombre Total de medicament issus de l'enrechissment : "+str(len(list(set(listi)))))
infos3.write('\n---------------------------------------------------')
infos3.close()
