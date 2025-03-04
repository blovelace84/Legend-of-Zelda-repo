#input a file into the story
#write an input for the user to begin the story
#create a function called CurseFunc
#loop that file so each letter will display
#import time to loop file so each letter will display a typing effect
#Add multiple lines for each sentence
#print content after writing

import time

lines = [

    "The Legend of Zelda: Python’s Curse\n",
    "\n",
    "Long ago in the kingdom of Hyurule, \n"
    "\n"
    "there was peace surrounding the land.\n"
    "\n"
    "While the citizens of Hyrule are living their lives,\n"
    "\n"
    "Darkness engulfs Hyrule as an ancient curse left by Python spreads venom across the land. ",
    "Monsters known as Errors emerge, twisting reality. Princess Zelda is imprisoned, fully consumed by the black venom, ",
    "while Hyrule Castle falls into ruin.\n",
    "\n",
    "Only a sacred sword, forged to purify corruption, can break the curse. Link, the kingdom’s last hope, ",
    "embarks on a journey to restore Hyrule and free Zelda.\n",
    "\n",
    "Final Battle: Python’s Last Stand\n",
    "\n",
    "Deep within Hyrule Castle, in a venom-filled arena, Python’s dragon-like form strikes with deadly attacks. ",
    "Link must purify the land as Errors attempt to stop him. As the battle intensifies, Zelda’s voice momentarily ",
    "breaks through the curse, strengthening the sword.\n",
    "\n",
    "In a final clash, Link lands a purifying blow, shattering Python and dissolving the venom. ",
    "Zelda is freed, and Hyrule begins to heal. The curse is lifted, and balance is restored.\n"
]


zeldaFile  = open('zeldaFile.txt', 'w')
with open('zeldaFile.txt', 'w') as file:
    file.writelines(lines)
with open('zeldaFile.txt', 'r') as file:
    content = file.read()

for letter in content:
    print(letter, end="", flush=True)
    time.sleep(0.08)