#input a file into the story
#write an input for the user to begin the story
#create a function called CurseFunc
#loop that file so each letter will display
#write an import that inputs the file text of the story.
#Add multiple lines for each sentence
#print content after writing


lines = ["Long ago, in the Kingdom of Hyrule,\n",
          "lived people of laughter and love\n",
         "While the people of Hyrule enjoyed their day,\n"
         "Darkness engulfs Hyrule as an ancient curse left by Python spreads venom across the land. Monsters known as Errors emerge, twisting reality. Princess Zelda is imprisoned, fully consumed by the black venom, while Hyrule Castle falls into ruin.\n",
         ]

zeldaFile  = open('zeldaFile.txt', 'w')
with open('zeldaFile.txt', 'w'):
    zeldaFile.write(str(lines))
