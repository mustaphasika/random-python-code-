#L3ASR 2021/2022
#TOUATI Feriel
#SI KADDOUR Mustapha

#-----------------------------------------------------LES FONCTIONS-----------------------------------------------------------------------------------------------------

def distance(char1, char2):
    #distance entre deux caractères en utilisant le code ASCII
    return abs(ord(char1) - ord(char2))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def MotCroisants(word):
    #On vérifie si toutes les distances entre deux caractères  2 par 2
    distances = [distance(l, r) for l, r in zip(word, word[1:])]
    return all(l < r for l, r in zip(distances, distances[1:]))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def PhraseCroisante(phrase):
#voir si tous les mots sont croisants dans la phrase
    return all([MotCroisants(word) for word in phrase.split()])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print(PhraseCroisante("superb subway"))
#-------------------------------------------------EXECUTION DU MAIN----------------------------------------------------------------------------------------------------------------
main()