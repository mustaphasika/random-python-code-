#L3ASR 2021/2022
#TOUATI Feriel
#SI KADDOUR Mustapha

import numpy as np

#-----------------------------------------------------LES FONCTIONS------------------------------------------------------------------------------------------------

def ProduitsAchetes(Panier):
    # La fonction nonzero nous donne deux tableau contenant des indices (i et j ) qui satisfaient panier [i][j] = 1 et dans ce cas on aura des tableux contenant les indices des clients (i) qui ont acheté le produit j et l'indince de produit acheté (j)
    client = np.nonzero(Panier)[0]  # on récupère la liste des indices de clients qui ont acheté le produit j
    produit = np.nonzero(Panier)[1] # on récupère la liste des indices de produits achetés et chaque case i dans le tableau correspend au produit acheté par le client i dans le tableau précédent
    Produits_par_client = [] 
    # Un tableau intermédiaire qui contient les indices des produits achetés par un client, sert a remplire le tableau Produits_par_tous_les_clients 
    Produits_par_tous_les_clients = [] 
    # un tableau contenant pour chaque indice correspondant a un client le tableau des indices des produits achetés par ce dernier.
    i = 0
    j = 0
    for n in client:
        if i == n: # si l'indice de client n'a pas changé on execute:
            Produits_par_client.append(produit[j]) # on ajoute au tableau Produits_par_client les produits achetés par le client i
            j = j + 1 # on avance dans les produits
        else:# sinon si on a fini avec le client i on insert le tableau Produits_par_client dans Produits_par_tous_les_clients dans l'indice du client correspondant
            Produits_par_tous_les_clients.append(Produits_par_client)
            Produits_par_client = [] # on met le tableau Produits_par_client à vide pour le prochain client
            Produits_par_client.append(produit[j]) # on rajoute le produit j dans la liste des produits acheté par le client i
            i = i + 1 # on avance dans le teableau d'indices des clients
            j = j + 1 # on avannce dans le tableau d'indices des produits achetes
    Produits_par_tous_les_clients.append(Produits_par_client) # c'est pour rajouter le dernier sous tableau dans le tableau Produits_par_tous_les_clients
    return Produits_par_tous_les_clients
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Nombre_Occurences(tab, x, y):
    #On compte le nombe d'occurance du couple (x,y) dans chaque sous tableau de tab
    #Cette fonction va nous permettre de connaitre le nombre de fois qu'un couple de produit est achetés a partir de Produits_par_tous_les_clients
    occ = 0
    for t in tab:
        if set([x, y]).issubset(set(t)): occ += 1
    return occ
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ExtraireTriplets(Panier):
    #Cette fonction permet d'extraire les triplets (a,b,n) tels que a et b sont les produit achetésensemble n fois (par n clients)
    #à partir du tableau contenant les produits achetés par clients(les indices sont les clients)
    triplets = []
    Produit = Panier.shape[1] #on récupère le nombre de colonnes
    for i in range(Produit):
        j = i + 1
        while j < (Produit):
            triplets.append((i, j, Nombre_Occurences(ProduitsAchetes(Panier), i, j)))  
            j += 1
        i += 1
    return triplets
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MaxOcc(triplets):
    #Cette fonction permet d'obtenir a partir de l'ensemble des triplets l'occurence maximale
    ListeOcc = []
    for trip in triplets:
        ListeOcc.append(trip[2]) #on récupere toutes les occurences de chaque triplets
    return max(ListeOcc) # on renvoie le maximum
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Max_trip(triplet):
    #Cette fonction renvoie les triplets ayant l'occurence maximale
    for trip in triplet:
        if trip[2] == MaxOcc(triplet): print(trip)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    # panier = np.random.randint(2, size=(10, 20))
    panier=np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])
    print(panier)
    print(ExtraireTriplets(panier))
    Max_trip(ExtraireTriplets(panier))
#----------------------------------------------------------------EXECUTION DU MAIN-----------------------------------------------------------------------------------------------------------

main()
    
