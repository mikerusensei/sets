import random
import os
import string

from module2 import *

class App:
    def __init__(self):
        self.running = True

    def generate_list(self, universal, length):
        list_sample = random.sample(universal, length)
        list_sample.sort()
        return list_sample
    
    def automatic_generation(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Automatic Genearation\n")
        length_universal = input("Input length of universal set: ")
        hasNumbers = input("Include Numbers? [Y/N]: ")
        hasCharacters = input("Include Characters? [Y/N]: ")
        length_f_set = input("Length of first set: ")
        length_s_set = input('Length of second set: ')
        print()

        concat = ''
        
        if hasNumbers.lower() == 'y':
            concat += string.digits
        
        if hasCharacters.lower() == 'y':
            concat += string.ascii_lowercase

        geneated_universal = random.sample(concat, int(length_universal))
        geneated_universal.sort()

        set_a = self.generate_list(geneated_universal, int(length_f_set))
        set_b = self.generate_list(geneated_universal, int(length_s_set))

        union_list = union(set_a, set_b)
        intersection_list = intersection(set_a, set_b)
        difference_list = difference(set_a, set_b)
        a_complement = complement(geneated_universal, set_a)
        b_complement = complement(geneated_universal, set_b)
        symmetrical_list = symmetrical(set_a, set_b)

        print(f"Universal Set: {geneated_universal}")
        print(f"Set A: {set_a}")
        print(f"Set B: {set_b}")
        print(f"Union: {union_list}")
        print(f"Intersecton: {intersection_list}")
        print(f"Difference: {difference_list}")
        print(f"A Complement: {a_complement}")
        print(f"B Complement: {b_complement}")
        print(f"Symmetrical: {symmetrical_list}")

        try_again = input("\nTry Again? [Y/N]: ")
        
        if try_again.lower() == 'y':
            self.automatic_generation()

    def manual_generation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Manual Genearation\n")
        print("Note: Please separate the elements by [Space]")
        universal_input = input("Enter Universal Set: ")
        splitted_universal = universal_input.split(" ")
        
        set_a = []
        set_b = []
        auto_generate = input("Auto Generate Both Sets? [Y/N]: ")

        if auto_generate.lower() == 'y':
            length_sets = input("Length of Sets: ")
            set_a += self.generate_list(splitted_universal, int(length_sets))
            set_b += self.generate_list(splitted_universal, int(length_sets))
        else:
            inputted_set_a = input("Input Set A: ")
            inputted_set_b = input("Input Set B: ")
            splitted_set_a = inputted_set_a.split(" ")
            splitted_set_b = inputted_set_b.split(" ")
            set_a += splitted_set_a
            set_b += splitted_set_b

        union_list = union(set_a, set_b)
        intersection_list = intersection(set_a, set_b)
        difference_list = difference(set_a, set_b)
        a_complement = complement(splitted_universal, set_a)
        b_complement = complement(splitted_universal, set_b)
        symmetrical_list = symmetrical(set_a, set_b)

        print()
        print(f"Universal Set: {splitted_universal}")
        print(f"Set A: {set_a}")
        print(f"Set B: {set_b}")
        print(f"Union: {union_list}")
        print(f"Intersecton: {intersection_list}")
        print(f"Difference: {difference_list}")
        print(f"A Complement: {a_complement}")
        print(f"B Complement: {b_complement}")
        print(f"Symmetrical: {symmetrical_list}")

        try_again = input("\nTry Again? [Y/N]: ")
        
        if try_again.lower() == 'y':
            self.manual_generation()
    
    def run(self):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Basic Sets Operation\n")
            print("Select type of generation\nA. Automatic Generation\nB. Manual Generation\nC. Exit\n")
            choice = input("Enter Choice: ")
            
            if choice.lower() == 'a':
                self.automatic_generation()
            elif choice.lower() == 'b':
                self.manual_generation()
            elif choice.lower() == 'c':
                self.running = False
            else:
                input('Invalid Entry press [Enter] to continue')
            
        
if __name__ == '__main__':
    app = App()
    app.run()