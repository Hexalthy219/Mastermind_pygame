import pygame
import math
import random

# VARIABLES----------------------------------------------------------------------
FENETRE_HAUTEUR = 700
FENETRE_LARGEUR = FENETRE_HAUTEUR*6//10
TAILLE_CASE = FENETRE_LARGEUR//6
RAYON = (TAILLE_CASE *5//7)//2

ROUGE  = (255,   0,   0)
VERT   = (  0, 255,   0)
ORANGE = (255, 165,   0)
BLEU   = (  0,   0, 255)
VIOLET = (238, 130, 238)
JAUNE  = (255, 255,   0)
NOIR   = (  0,   0,   0)
BLANC  = (255, 255, 255)
GRIS   = (110, 113, 127)

COLORS = [ROUGE, VERT, ORANGE, BLEU, VIOLET, JAUNE]

Color = {
   "RED" : 0,
   "GREEN" : 1,
   "ORANGE" : 2,
   "BLUE" : 3,
   "PURPLE" : 4,
   "YELLOW" : 5 
}

# Listes des essais
guess = []
# [0] == nb_incorrect, [1] == nb_mauvaise_position, 1 == correct
infoGuess = []
# guess = [(Color["BLUE"],Color["BLUE"],Color["BLUE"])]
nb_guess = 0
# Combinaison à deviner générée aléatoirement
combinaison = []

choixCouleur = -1
fini = False

# Inputs------------------------------------------------------------------------
def gestionEntree():
   global fini, choixCouleur
   choixCouleur = -1
   while choixCouleur == -1:
      evenement = pygame.event.wait()
      if evenement.type==pygame.QUIT:
         fini=True
         break
      elif evenement.type == pygame.MOUSEBUTTONDOWN:
         convertMousePositionChoix(pygame.mouse.get_pos())

def convertMousePositionChoix(pos_souris):
   for i in range(len(COLORS)):
      centre = ((5*TAILLE_CASE)+TAILLE_CASE//2, (i*TAILLE_CASE)+TAILLE_CASE//2)
      distance = math.sqrt((pos_souris[0] - centre[0])**2 + (pos_souris[1] - centre[1])**2)
      if distance <= RAYON:
         choixCouleur = i
         updateGuess()
      else:
         choixCouleur = -1

# Affichages---------------------------------------------------------------------
def affichage():
   affichageGuess()
   separateurs()
   affichageChoix()
   affichageInforEssais()
   
def separateurs():
   pygame.draw.line(fenetre, NOIR, (FENETRE_LARGEUR*2//3, 0), (FENETRE_LARGEUR*2//3, FENETRE_HAUTEUR))
   pygame.draw.line(fenetre, NOIR, (FENETRE_LARGEUR*5//6, 0), (FENETRE_LARGEUR*5//6, FENETRE_HAUTEUR))

def affichageGuess():
   # affichage guess
   for i in range(nb_guess):
      for j in range(4):
         if j >=len(guess[i]):
            couleur = NOIR
         else:
            couleur = COLORS[guess[i][j]]
         centre = ((j*TAILLE_CASE)+TAILLE_CASE//2, (i*TAILLE_CASE)+TAILLE_CASE//2)
         pygame.draw.circle(fenetre, couleur, centre, RAYON)
   # affichage essais non utilisés
   for i in range(10-nb_guess):
      for j in range(4):
         centre = ((j*TAILLE_CASE)+TAILLE_CASE//2, ((i+nb_guess)*TAILLE_CASE)+TAILLE_CASE//2)
         pygame.draw.circle(fenetre, NOIR, centre, RAYON)

def affichageChoix():
   for i in range(len(COLORS)):
      centre = ((5*TAILLE_CASE)+TAILLE_CASE//2, (i*TAILLE_CASE)+TAILLE_CASE//2)
      pygame.draw.circle(fenetre, COLORS[i], centre, RAYON)
      
def affichageInforEssais():
   for index, info in infoGuess:
      if info["correct"]>0:
         texte = "{}".format(info["correct"])
         texte_surface = police.render(texte, True, ROUGE)
         text_pos = ((TAILLE_CASE*4)+TAILLE_CASE//4, (index*TAILLE_CASE+(TAILLE_CASE//2))-10)
         fenetre.blit(texte_surface, text_pos)
      if info["mauvaise_place"]>0:
         texte = "{}".format(info["mauvaise_place"])
         texte_surface = police.render(texte, True, JAUNE)
         text_pos = ((TAILLE_CASE*4)+TAILLE_CASE*3//4, (index*TAILLE_CASE+(TAILLE_CASE//2))-10)
         fenetre.blit(texte_surface, text_pos)
      
# Logique--------------------------------------------------------------------
def nouveauInfoGuess(nb_correct, nb_mauvaise_place):
   return {
      "mauvaise_place":nb_mauvaise_place,
      "correct":nb_correct
   }
   
def addNewGuess(nb_correct, nb_mauvaise_place):
   infoGuess.append(nouveauInfoGuess(nb_correct, nb_mauvaise_place))
   
def updateGuess():
   return

def initCombinaison():
   return

# ***Vas y, mets ton code ici connards <3***



# Initialisation-------------------------------------------------------------
pygame.init()
police = pygame.font.SysFont("monospace", 20)
fenetre_taille = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(fenetre_taille)
pygame.display.set_caption('Mastermind')


# Boucle principale du jeu---------------------------------------------------
while not fini:
   # Affichage
   fenetre.fill(GRIS)
   affichage()
   pygame.display.flip()
   
   # Input
   gestionEntree()

# Fin prog--------------------------------------------------------------------
pygame.display.quit()
pygame.quit()
exit()