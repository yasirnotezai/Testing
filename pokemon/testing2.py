import tkinter as tk
from tkinter import ttk, Listbox, messagebox
from PIL import Image, ImageTk
import pandas as pd
import random

data = pd.read_csv("D:\\Coding\\PythonVScode\\PokemonProject\\cleanPokeData.csv")

attacker = 49

selected_pokemon_row = data[data['Name']] == "Charmander"
player_attack_value = selected_pokemon_row.iloc[0]["Attack"]
print(player_attack_value)

# def get_attack_value(pokemon_name):
#     selected_pokemon_row = data[data['Name'] == pokemon_name]
#     if not selected_pokemon_row.empty:
#         attack_value = selected_pokemon_row.iloc[0]['Attack']
#         print(attack_value)
#     else:
#         return None
    
# get_attack_value("Squirtle")