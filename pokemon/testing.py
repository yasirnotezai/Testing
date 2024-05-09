import tkinter as tk
from tkinter import ttk, Listbox, messagebox
from PIL import Image, ImageTk
import pandas as pd
import random

class PokemonGame:
    def __init__(self):
        self.selected_pokemon1 = None
        self.selected_pokemon2 = None
        self.player1_score = 0
        self.player2_score = 0
        self.max_health = 100
        self.attack_damage = 10

    def dataCleaning(self):   
        self.data = pd.read_csv("D:\\Coding\\PythonVScode\\PokemonProject\\pokemon.csv")
        self.copied_data = self.data.copy()
        self.copied_data = self.copied_data.drop(["Type 2", "Total", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"], axis=1)
        self.copied_data = self.copied_data.drop([19, 12, 7, 8, 3], axis=0)
        self.copied_data = self.copied_data.rename(columns={"Type 1": "Element"})
        self.copied_data = self.copied_data[:18]
        self.copied_data.to_csv("cleanPokeData.csv", index=False)

    def choose_pokemon_gui(self):
        def choose_pokemon_for_player(player):
            selected_pokemon = None  # Initialize selected pokemon variable

            def player_listbox_select(event=None):
                nonlocal selected_pokemon
                selected_pokemon = listBox.get(tk.ACTIVE)
                image_path = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\{selected_pokemon}.png"
                image = Image.open(image_path)
                resized_image = image.resize((170, 170))
                image_reference = ImageTk.PhotoImage(resized_image)
                image_label.configure(image=image_reference)
                image_label.image = image_reference

            def choose_pokemon():
                nonlocal selected_pokemon
                selected_pokemon = listBox.get(tk.ACTIVE)
                root.quit()

            # Create a new Toplevel window
            root = tk.Toplevel()
            frame = tk.Frame(root)
            labelFrame = tk.LabelFrame(frame)
            labelFrame.grid(row=0, column=0)

            default_image_path = "D:\\Coding\\PythonVScode\\PokemonProject\\Images\\none.png"
            default_image = Image.open(default_image_path)
            default_resized_image = default_image.resize((170, 170))
            default_image = ImageTk.PhotoImage(default_resized_image)
            image_label = tk.Label(labelFrame, image=default_image)
            image_label.grid(row=1, column=1)

            label_text = f"Player {player} chooses Pokemon"
            label = tk.Label(labelFrame, font=('Times New Roman', 10, 'bold'), text=label_text)
            label.grid(row=0, column=0)

            warning_label = tk.Label(labelFrame, font=('Times New Roman', 9, 'bold'), text="Warning! Click the element in listBox \n two times for selection \n (Slowly).")
            warning_label.grid(row=2, column=0)

            listBox = Listbox(labelFrame, width=18, height=10)
            listBox.grid(row=1, column=0)
            pokemon_names = self.copied_data['Name'].tolist()
            for i in range(len(pokemon_names)):
                listBox.insert(i, pokemon_names[i])

            listBox.bind("<<ListboxSelect>>", player_listbox_select)

            button = ttk.Button(labelFrame, text="Choose!", command=choose_pokemon)
            button.grid(row=2, column=1, pady=10)

            frame.pack()
            root.mainloop()

            return selected_pokemon

        # Player 1 selects Pokemon
        self.selected_pokemon1 = choose_pokemon_for_player(1)

        # Player 2 selects Pokemon
        self.selected_pokemon2 = choose_pokemon_for_player(2)

        # Now, both players have selected their Pokemon, start the battle GUI
        battle_gui_instance = BattleGui(self)
        battle_gui_instance.gui3()
                
class BattleGui:
    def __init__(self, pokemon_game_instance):
        self.pokemon_game_instance = pokemon_game_instance
        self.image_references = []
    
    def gui3(self):
        def attack_physical():
            nonlocal player_turn
            if player_turn == 1:
                
                self.opponent_health2 = progressbar2_1['value']
                selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                player_attack_value = selected_pokemon_row.iloc[0]["Attack"]
                damageable_attack_value = int(random.randint(75, 100)  / 100 * float(player_attack_value))
                new_health = max(self.opponent_health2 - damageable_attack_value, 0)
                print(new_health)
                progressbar2_1['value'] = new_health
                
                
                if new_health == 0:
                    messagebox.showinfo("Result", "Player 1 wins!")
                    self.pokemon_game_instance.player1_score += 1
                    label_score1.config(text=f"Score: {self.pokemon_game_instance.player1_score}")
                    reset_battle()
                else:
                    player_turn = 2
                    toggle_player_turn()

            else:
                self.opponent_health1 = progressbar1_1['value']
                selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                player_attack_value = selected_pokemon_row.iloc[0]["Attack"]
                damageable_attack_value = int(random.randint(75, 100)  / 100 * float(player_attack_value)) 
                new_health = max(self.opponent_health2 - damageable_attack_value, 0)
                progressbar1_1['value'] = new_health
                
                if new_health == 0:
                    messagebox.showinfo("Result", "Player 2 wins!")
                    self.pokemon_game_instance.player2_score += 1
                    label_score2.config(text=f"Score: {self.pokemon_game_instance.player2_score}")
                    reset_battle()
                else:
                    player_turn = 1
                    toggle_player_turn()

        def attack_elemental():
            nonlocal player_turn
            if player_turn == 1:
                opponent_health2 = progressbar2_1['value']
                new_health = max(opponent_health2 - self.pokemon_game_instance.attack_damage, 0)
                progressbar2_1['value'] = new_health
                if new_health == 0:
                    messagebox.showinfo("Result", "Player 1 wins!")
                    self.pokemon_game_instance.player1_score += 1
                    label_score1.config(text=f"Score: {self.pokemon_game_instance.player1_score}")
                    reset_battle()
                else:
                    player_turn = 2
                    toggle_player_turn()

            else:
                opponent_health1 = progressbar1_1['value']
                new_health = max(opponent_health1 - self.pokemon_game_instance.attack_damage, 0)
                progressbar1_1['value'] = new_health
                if new_health == 0:
                    messagebox.showinfo("Result", "Player 2 wins!")
                    self.pokemon_game_instance.player2_score += 1
                    label_score2.config(text=f"Score: {self.pokemon_game_instance.player2_score}")
                    reset_battle()
                else:
                    player_turn = 1
                    toggle_player_turn()

        def toggle_player_turn():
            if player_turn == 1:
                button_physical2.config(state=tk.DISABLED)
                button_elemental2.config(state=tk.DISABLED)
                button_physical1.config(state=tk.NORMAL)
                button_elemental1.config(state=tk.NORMAL)
                label_turn.config(text="Player 1's Turn")
            else:
                button_physical1.config(state=tk.DISABLED)
                button_elemental1.config(state=tk.DISABLED)
                button_physical2.config(state=tk.NORMAL)
                button_elemental2.config(state=tk.NORMAL)
                label_turn.config(text="Player 2's Turn")

        def reset_battle():
            progressbar1_1['value'] = self.pokemon_game_instance.max_health
            progressbar2_1['value'] = self.pokemon_game_instance.max_health
            player_turn = random.randint(1, 2)
            toggle_player_turn()
            
                # display selected Pokemon for player 1
        
        # def display_selected_pokemon():
        #     # Display selected Pokemon images
        #     if self.pokemon_game_instance.selected_pokemon1:
        #         image_path1 = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\{self.pokemon_game_instance.selected_pokemon1}.png"
        #         image1 = Image.open(image_path1)
        #         resized_image1 = image1.resize((170, 170))
        #         self.image1_tk = ImageTk.PhotoImage(resized_image1)
        #         self.image_label1.config(image=self.image1_tk)
        #         self.image_references.append(self.image1_tk)  # Store image reference
                
        #     if self.pokemon_game_instance.selected_pokemon2:
        #         image_path2 = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\{self.pokemon_game_instance.selected_pokemon2}.png"
        #         image2 = Image.open(image_path2)
        #         resized_image2 = image2.resize((170, 170))
        #         self.image2_tk = ImageTk.PhotoImage(resized_image2)
        #         self.image_label2.config(image=self.image2_tk)
        #         self.image_references.append(self.image2_tk)
        
        
        root = tk.Tk()
        root.title("Pokemon Battle")

        self.frame = tk.Frame(root)
        self.labelFrame = tk.LabelFrame(self.frame)
        self.labelFrame.grid(row=0, column=0)

        # player 1 title
        self.name1 = tk.Label(self.labelFrame, text="Player 1")
        self.name1.grid(row=0, column=0, padx=70)

        # player 2 title
        self.name2 = tk.Label(self.labelFrame, text="Player 2")
        self.name2.grid(row=0, column=1, padx=70)
        
        # self.image_label1 = tk.Label(self.labelFrame)
        # self.image_label1.grid(row=4, column=0)  # Player 1 image

        # self.image_label2 = tk.Label(self.labelFrame)
        # self.image_label2.grid(row=4, column=1)
        
        # display_selected_pokemon()
        
        
        # score 1
        self.score1 = tk.Label(self.labelFrame, text=f"Score: {self.pokemon_game_instance.player1_score}")
        self.score1.grid(row=1, column=0)
        label_score1 = self.score1

        # score 2
        self.score2 = tk.Label(self.labelFrame, text=f"Score: {self.pokemon_game_instance.player2_score}")
        self.score2.grid(row=1, column=1)
        label_score2 = self.score2

        # turn indicator
        player_turn = random.randint(1, 2)
        label_turn = tk.Label(self.labelFrame, text=f"Player {player_turn}'s Turn")
        label_turn.grid(row=2, columnspan=2)

        # progress bar 1 for player 1
        progressbar1_1 = ttk.Progressbar(self.labelFrame, orient='horizontal', mode='determinate', length=100)
        progressbar1_1.grid(row=3, column=0, padx=5, pady=5)
        progressbar1_1['value'] = self.pokemon_game_instance.max_health

        # progress bar 1 for player 2
        progressbar2_1 = ttk.Progressbar(self.labelFrame, orient='horizontal', mode='determinate', length=100)
        progressbar2_1.grid(row=3, column=1, padx=5, pady=5)
        progressbar2_1['value'] = self.pokemon_game_instance.max_health
        print(self.pokemon_game_instance.selected_pokemon1)
        print(self.pokemon_game_instance.selected_pokemon2)


        

        # physical attack button for player 1
        button_physical1 = ttk.Button(self.labelFrame, text="Physical Attack", command=attack_physical)
        button_physical1.grid(row=5, column=0, padx=5, pady=5)

        # elemental attack button for player 1
        button_elemental1 = ttk.Button(self.labelFrame, text="Elemental Attack", command=attack_elemental)
        button_elemental1.grid(row=6, column=0, padx=5, pady=5)

        # physical attack button for player 2
        button_physical2 = ttk.Button(self.labelFrame, text="Physical Attack", command=attack_physical)
        button_physical2.grid(row=5, column=1, padx=5, pady=5)

        # elemental attack button for player 2
        button_elemental2 = ttk.Button(self.labelFrame, text="Elemental Attack", command=attack_elemental)
        button_elemental2.grid(row=6, column=1, padx=5, pady=5)

        toggle_player_turn()

        self.frame.pack()
        root.mainloop()


pokemon_game_instance = PokemonGame()
pokemon_game_instance.dataCleaning()
pokemon_game_instance.choose_pokemon_gui()
