
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
while True:
    choice1 = input("You\'re at a crossroad, way do you want to go? Left or right?").lower()
    if choice1.count('left'):
        choice2 = input('You find yourself staring before a body of water. Would you like to wait or do something else?').lower()
        if choice2.count('wait'):
            choice3 = input('Amazingly a castle begins to rise from the waters. Before you now stands 3 doors: Red, Blue, and Yellow. What do you want to do next?').lower()
            if choice3.count('red'):
                print("As you enter the red door, fire begins to exhume the room and you burn to death.\nGame Over")
                break
            if choice3.count('blue'):
                print("Creeping into the blue door, you begin to hear growls and screeches from unkjown beasts. They soon maul you to death.\nGame Over")
                break
            if choice3.count('yellow'):
                print('Opening the yellow door, light begins to glisten from inside. The room is filled with treasure from floor to ceiling.\n You Win!')
                break
            print('Before you could do so, the castle senses a disturbance from your very soul. As it has risen from the waters, it now descends back into it. You have lost the treasure...\nGame Over!')     
        if choice2.count('swim'):
            print('As you you traverse the body of water, using every ounce of strength to swim, trout begins to surround and attack you. You drown to death\Game Over!')
            break
        print("As you do, other treasure hunters hear the commotion. They find and capture you.\nGame Over.")
        break
    print("You fall into a trap hole.\nGameOver, try again.")
    break