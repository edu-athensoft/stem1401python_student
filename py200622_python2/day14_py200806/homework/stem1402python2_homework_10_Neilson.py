"""
Homework
normal						0.638
magic				1/4		0.25
rare				1/10		0.1
legendary			1/100		0.01
ancient legendary		1/500		0.002
"""
import random

determined_crate = random.randint(1, 1000)
chosen_crate = ""

if 1 <= determined_crate <= 638:
    chosen_crate = "normal"
elif 639 <= determined_crate <= 888:
    chosen_crate = "magic"
elif 889 <= determined_crate <= 988:
    chosen_crate = "rare"
elif 989 <= determined_crate <= 998:
    chosen_crate = "legendary"
elif 999 <= determined_crate <= 1000:
    chosen_crate = "ancient legendary"

print("=== Loot Crate ===")
print("Obtainable Items:")
print("normal 63.8.%")
print("magic 25%.")
print("rare 10%.")
print("legendary 1%.")
print("ancient legendary 0.2.%")
print(f"You got a {chosen_crate} item.")

