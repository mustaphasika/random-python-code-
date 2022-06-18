#L3ASR 2021/2022
#TOUATI Feriel
#SI KADDOUR Mustapha

#-----------------------------------------------------LES FONCTIONS------------------------------------------------------------------------------------------------
def dict(path):
     try:
         with open(path, 'r') as f:
             fichiertxt = f.read()
         return {line.strip().upper() for line in fichiertxt.split('\n') if line}
     except OSError:
         return {"Erreur d'ImportErrortion de fichier"}
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def WordTriad(mot, words):
    return mot[::2] in words and mot[1::2] in words
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def PhraseTriad(phrase, words):
    #all permet de vérifier si tous les elements d'une liste vérifie la condition
    return all([WordTriad(mot.upper(), words) for mot in phrase.split()])
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    englishwords= dict(r"C:\Users\Feriel Touati\Documents\VSC PYTHON\DM\DM L3 ASR TOUATI Feriel & SI KADDOUR Mustapha\words.txt")
    print(PhraseTriad("learned theorem", englishwords))
#----------------------------------------------------------------EXECUTION DU MAIN-----------------------------------------------------------------------------------------------------------
main()
