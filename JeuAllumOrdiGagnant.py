from random import* # importation des modules que l'on utilise (que j'avais oublié lol)
from turtle import*

def config_ecran():
    setup(width=0.9, height=0.9) 
    setworldcoordinates(-1100, -1100, 1100, 1100)
    tracer(0) 
    hideturtle()
    title("Jeu de Nim - Orage")

def sumNimXOR(nim1, nim2):
    return nim1^nim2
def mex(l):
    if l==[]:
       return 0
    n=0
    for i in range(len(l)+1): 
        if n in l:
            n=n+1
        if n not in l:
            return n
def valPileAllumettes(n,r):
    res=[]
    if n <=0:
        return 0
    for i in r:
        if i <= n:
            val=valPileAllumettes((n-i),r)
            res.append(val)
    return mex(res)
def valJeuAllumettes(l,r):
    resf=[]
    if l ==[]:
        return 0
    for i in l:
        a=valPileAllumettes(i,r)
        resf.append(a)
    resa=0
    for x in resf:
        resa=sumNimXOR(resa,x)
    return resa

def afficheJoueurStratGagnanteAllumettes(j,l):
    a = valJeuAllumettes(j,l)
    if a==0:
        return 2
    else:
        return 1

def valJeuAllumettesPremiersCoups(a,l):
    #examen des coups possibles
    j=[a]
    for pile in range(len(j)):
        for nb in l:
            if(j[pile]-nb>=0):
                j[pile]-=nb
                if valJeuAllumettes(j,l) == 0:
                    return nb
                j[pile]+=nb
    return l[0] 

# --- DESSINS ---

def etoiles(nbe):           # fonction dessinant les étoiles dans le ciel
     color('gold')
     for i in range(nbe):
          x = randint(-1000,1000)       # les étoiles sont placés aléatoirement dans le ciel
          y = randint(-270,900)
          te = randint(2,5)
          up()
          goto(x,y)
          down()
          dot(te)          # permet de dessiner les points représentant les étoiles

def Lune(TailleCroissant):       # fonction dessinant la lune
    up()
    goto(-720,320)
    down()
    fillcolor('yellow')
    begin_fill()
    circle(70)
    end_fill()
    fillcolor('midnightblue')
    begin_fill()
    color('midnightblue')
    forward(TailleCroissant) #Avance un peu pour superposer 2 cercles et donner un croissant de lune
    circle(70)
    end_fill()

def cercleRempli(rayon,couleur): #Dessine un cercle rempli, utile pour les nuages/Lune
    color('silver')
    fillcolor(couleur)
    begin_fill()
    circle(rayon)
    end_fill()


def nuage(rayon,couleur):
    color('silver')
    x=randint(-900,900)
    y=randint(400,800)
    up()
    goto(x,y)
    down()
    cercleRempli(rayon,couleur)
    forward(rayon)
    for i in range(4):
        cercleRempli(rayon,couleur)
        right(90)

def ciel():      # fonction dessinant le ciel
    color('midnightblue')
    begin_fill()
    fillcolor('midnightblue')
    goto(-1100,-1100)
    goto(1100,-1100)          #coordonnées ou l'on dessine une gros rectangle bleu qui représente le ciel
    goto(1100,1100)
    goto(-1100,1100)
    goto(-1100,-1100)
    end_fill()
    nbe = randint(100,200)
    etoiles(nbe)          # appelle de la fonction etoiles et les dessine les étoiles
    nbrenuage=randint(8,12)      # donne le nombre de nuage qu'il y aura sur l'écran
    for i in range(nbrenuage):   #appelle la fonction que crée un nuage autant de fois qu'il y a de nuages
     nuage(50,'silver')
    Lune(25)           #dessine la lune

def arbreMort(taille):
    color("black")
    width(5)
    if taille < 10: #Condition pour appliquer la suite de la fonction
        return
    forward(taille)
    left(30)
    arbreMort(taille * 0.6) #Rappel de la fonction tant que la condition "taille <10" du if n'est pas complétée
    right(60)
    arbreMort(taille * 0.6)
    left(30)
    backward(taille) #Le turtle recule et fait les autres branches petit à petit au fur et à mesure que la condition sur la taille se remplit
    width(2)

def sol():         # fonction dessinant le sol
    begin_fill()
    fillcolor('saddlebrown')
    up()
    goto(-1100,-310)
    down()
    color('saddlebrown')
    goto(1100,-310)            #crée un rectangle marron qui représente le sol
    goto(1100,-1100)
    goto(-1100,-1100)
    goto(-1100,-310)
    end_fill()

def herbe():          # fonction dessinant l'herbe
    up()
    goto(-1100,-260)
    down()
    color('forestgreen')
    fillcolor('forestgreen')
    begin_fill()
    goto(-1100,-310)           #crée un rectangle avec une petite largeur juste au dessus du sol pour faire de l'herbe
    goto(1100,-310)
    goto(1100,-260)
    goto(-1100,-260)
    end_fill()
    up()
    goto(-550,-310)        #coordonnées pour dessiner l'arbre mort
    down()
    left(90)
    arbreMort(100)            #appelle de la fonction arbre mort pour dessiner des arbres juste sur l'herbe
    up()
    goto(570,-310)         #coordonnées pour dessiner l'arbre mort
    down()
    setheading(90) 
    arbreMort(100)              #appelle de la fonction arbre mort pour dessiner des arbres juste sur l'herbe

def thunder(l,x,y,t):        # fonction pour dessiner un éclair
    t.up()
    t.goto(x,y)        # permet de dessiner l'éclair à plusieurs endroit en changeant ses coordonnées
    t.down()
    t.speed(0) 
    t.color('darkorange')
    t.begin_fill()
    t.fillcolor('darkorange')
    t.goto(x-l,y)
    t.goto(x,y+4*l)        #dessine l'éclair qui mesure 7*l de hauteur et 2*l de largeur
    t.goto(x,y-3*l)
    t.goto(x+l,y+l)
    t.goto(x,y+l)
    t.end_fill()

def nb_thunder(nb, tb):         # fonction pour dessiner plusieurs éclairs
    l = 540/(nb*2)         # la valeur l change en fonction du nombre d'éclair
    x = -400
    y = 100 
    for i in range (nb):      # appelle de la fonction qui dessine un éclair et la répète en fonction du nombre d'éclair que l'on souhaite
        thunder(l,x,y,tb)
        x = x+l*3.3           # change la valeur de x pour que les éclairs ne soit pas superposées


def disparition(nbd,x,y,t, l):    # fonction pour faire disparaitre l'éclair
    t.speed(0)
    t.color('midnightblue')
    for i in range(nbd):
        t.begin_fill()
        t.fillcolor('midnightblue')
        t.up()
        t.goto(x-l,4*l+y)
        t.down()
        t.goto(x+l,4*l+y)               #cela crée un rectangle ou est contenu 1 éclair pour le faire disparaitre sans faire disparaitre les autres éclairs
        t.goto(x+l,-3*l+y)
        t.goto(x-l,-3*l+y)
        t.goto(x-l,4*l+y)
        t.end_fill()
        x = x + l * 3.3           # cela permet de prendre indivuduellement chaque éclair


def reaparition(nbd,x,y,t, l):             #fonction pour faire réapparaitre l'éclair
    t.speed(6) 
    y = y-(410/2)+3*l             # calcul pour savoir de combien doit baisser l'éclair pour qu'il soit entre sa position initiale et sa position finale
    for i in range(nbd):
        thunder(l,x,y,t)         #appelle de la fonction thunder pour le dessiner dans sa position intermédiaire
        x = x + l * 3.3           # cela permet de prendre indivuduellement chaque éclair

def final(nbd,x,y,t, l):              # fonction pour que les éclairs choisis se retrouvent dans leur position finale
    t.speed(6)
    y = y-410+3*l                   # calcul pour que l'éclair arrive bien sur le sol
    for i in range(nbd):
        thunder(l,x,y,t)            #appelle de la fonction thunder pour le dessiner dans sa position finale
        t.begin_fill()
        t.fillcolor('orange')
        t.up()
        t.goto(x,y-3*l)
        t.down()
        t.goto(x-3,y-3*l)
        t.goto(x-3*l,y+2*l)             #cela crée les étincelles quand l'éclair arrive sur le sol.
        t.goto(x,y-3*l)
        t.goto(x+3,y-3*l)
        t.goto(x+3*l,y+2*l)
        t.goto(x,y-3*l)
        t.end_fill()
        x = x + l * 3.3

def compteur(nbre_allum,t):
    t.clear()
    t.color('white')
    t.up()
    t.goto(-800,-500)
    t.down()
    t.write("Allumettes restantes : " + str(nbre_allum), font=("Arial", 20, "normal"))


def QuiGagne(t,a):     # fonction pour afficher qui gagne
     t.up()
     t.goto(0,0)
     t.down()
     if a==1 : #La variable a est affectée au nombre 1 ou 2 selon qui a gagné
       t.color('green')
       t.write("Le joueur a gagné, bravo !",align="center",font=("Verdana", 25, "bold"))
       t.goto(0,-10)
       t.color('midnightblue')
     if a==2:
       t.color('red')
       t.write("L'ordinateur a gagné, dommage !",align="center",font=("Verdana", 25, "bold"))
       t.goto(0,-10)
       t.color('midnightblue')
     t.hideturtle()

# --- JEU ---

def joueur(nbre_allum, r):         #fonction du tour du joueur
     msg = "Combien d'allumettes tirer ? Vous pouvez tirer "+str(r)+" allumettes."
     tirage=numinput('éclair', msg)
     if tirage is None: return nbre_allum, 0
     tirage = int(tirage)
     
     while nbre_allum-tirage < 0 or not(tirage in r) :       #le nombre d'allumette ne tombe pas en dessous de 0 et obligé de joueur un nombre de r
             tirage=numinput('éclair',"Erreur. "+msg)
             if tirage is None: return nbre_allum, 0
             tirage = int(tirage)

     nbre_allum=nbre_allum-tirage
     print("Il reste",nbre_allum,"allumettes")
     return nbre_allum,tirage


def ordi(nbre_allum, r):           #fonction du tour de l'ordi
       tirage= valJeuAllumettesPremiersCoups(nbre_allum,r)              #permet à l'ordinateur de choisir au hasard un certain nombre d'allumette dans r                                #permet à l'ordinateur de choisir au hasard un certain nombre d'allumette dans r
       
       if tirage > nbre_allum:
           for x in r:
               if x <= nbre_allum:
                   tirage = x
                   break
                   
       nbre_allum=nbre_allum-tirage
       print("L'ordinateur a tiré",tirage,"allumettes")
       print("Il reste",nbre_allum,"allumettes")
       return nbre_allum,tirage

def all(nb, r, ta, tb):                  # permets d'avoir dans le shell le déroulement de la partie
  nbre_allum = nb
  l = 540/(nb*2)
  x = -400
  y = 100 
  
  print('il y a en tout ',nb,' allumettes')
  compteur(nb,ta)
  
  if afficheJoueurStratGagnanteAllumettes([nbre_allum],r)==2 : # nombre de tour qui permet de savoir qui joue/gagne
      jo=0
  else:
      jo=1

  print(nbre_allum)
  while nbre_allum > 0:
   
   if min(r) > nbre_allum:
       if jo%2==0: return QuiGagne(ta, 2)
       else: return QuiGagne(ta, 1)

   if jo%2==0 :     # paire joueur joue
     j=joueur(nbre_allum, r)
     nbre_allum =j[0]
     tirage =j[1]
     if tirage == 0: return 
     
     disparition(tirage,x,y,tb, l)
     reaparition(tirage,x,y,tb, l)             #cela fait une petite animation de l'éclair qui tombe sur le sol
     disparition(tirage,x,y-(410/2)+3*l,tb, l)
     final(tirage,x,y,tb, l)
     compteur(nbre_allum,ta)
     x = x + tirage * l* 3.3
     jo=jo+1
   
   if nbre_allum == 0: break 

   if jo%2 != 0 and nbre_allum != 0:     #impair ordi joue
       o=ordi(nbre_allum, r)
       nbre_allum =o[0]
       tirage =o[1]
       disparition(tirage,x,y,tb, l)
       reaparition(tirage,x,y,tb, l)                    #cela fait une petite animation de l'éclair qui tombe sur le sol
       disparition(tirage,x,y-(410/2)+3*l,tb, l)
       final(tirage,x,y,tb, l)
       compteur(nbre_allum,ta)
       x = x + tirage * l* 3.3
       jo=jo+1
  
  jo=jo+1
  if jo%2==0 :
    print("Le joueur a gagné")
    a=1
  else:
    print("L'ordinateur a gagné")
    a=2
  print(QuiGagne(ta,a))

# --- BOUCLE PRINCIPALE POUR REJOUER (Ne touche pas à la boucle stp Titouan je la corrige ce soir normalement---

while True:
    clearscreen() # Nettoie tout pour recommencer
    config_ecran() # Remet les bonnes coordonnées

    # Initialisation du décor
    ciel()       # appelle de la fonction ciel qui va dessiner le ciel, les étoiles, les nuages et la lune
    sol()                   #appelle le fonction sol et dessine le sol
    herbe()                # appelle la fonction herbe et dessiner l'herbe et les arbres morts
    update()

    # Initialisation des variables de jeu (aléatoires à chaque partie)
    r=[]
    a = randint(2,5)
    for i in range(a):
        b = randint(1,13)
        while b in r:
            b=randint(1,13)      
        r.append(b)         #nombre d'allumettes autorisé à tirer
    r.sort()

    nb = randint(14,25)    #random le nbre d allum

    tb = Turtle()         # création d'un 2ème turtle pour les éclairs
    tb.hideturtle()
    ta = Turtle()         # création d'un 3ème turtle pour le compteur
    ta.hideturtle()

    nb_thunder(nb, tb) # Dessine les éclairs de départ
    
    tracer(1) # Réactive l'animation pour jouer
    all(nb, r, ta, tb) # Lance la partie

    # Demande pour rejouer
    reponse = textinput("Fin de partie", "Voulez-vous rejouer ? (oui/non)")
    if reponse is None or reponse.lower() not in ['oui', 'o', 'yes', 'y']:
        print("Merci d'avoir joué !")
        bye()
        break
