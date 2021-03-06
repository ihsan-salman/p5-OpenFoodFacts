''' Importation of the moduls '''
import sys


class Menu:
    '''Main menu's reponsable class'''

    def __init__(self, favorite, app):
        self.favorite = favorite
        self.app = app
        self.choice = None
        self.welcome = print('---------------------------------'
                             '\nBienvenue dans OpenfoodFacts data'
                             '\n---------------------------------')
        self.display_menu()

    def display_menu(self):
        '''Display the menu with all choice'''
        print("\n-----------------------------------------------"
              "\n1 - Selectionner une catégorie ")
        print("2 - Retrouver mes aliments substitués.")
        print("3 - Réinitialiser la base de données")
        print("4 - Quitter le programme."
              "\n-----------------------------------------------")
        self.get_choice()

    def get_choice(self):
        '''Ask a number and send the user to the corresponding choice
           until the correct answer is given'''
        # return a message if the user enter another caracter than a number
        try:
            # Ask a number
            self.choice = input(
                "\nEntrez le chiffre correspondant à votre choix "
                "\npuis pressez sur ENTER :\n")
        # Get around the ValueError to ask again a number
        except ValueError:
            print('\nerreur')
            # Check if the choice is correct and display a message
        if self.choice == "1":
            print("------------------------------------------------"
                  "\nVous voulez trouver un aliment de substitution !"
                  "\n------------------------------------------------")
            # Send to the food category
            self.app.display_category()
            # When the step before is over, display the menu again
            self.display_menu()
        elif self.choice == "2":
            print('\n-------------------------------------------'
                  '\nVous voulez voir vos aliments substitués !'
                  '\n-------------------------------------------')
            # Send to the saved product
            self.favorite.display_saved_prod()
            self.display_menu()
        elif self.choice == "3":
            print("\n------------------------------------------------"
                  "\nVous voulez réinitialiser votre base de données !"
                  "\n------------------------------------------------")
            self.favorite.delete_saved_prod()
            # Display a message after deleting the saved products
            self.display_menu()
        elif self.choice == "4":
            # Display a bye message and close the program
            print("A bientôt ! \nFermeture du programme...")
            sys.exit()
        # If the choice isn't correct
        # display a message and send to the menu
        else:
            print("\nvotre réponse est incorrecte !"
                  " Veuillez entrer un chiffre valide !")
            self.display_menu()
