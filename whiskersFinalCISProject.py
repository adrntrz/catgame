import time


brick=" 🧱"
door="🚪"
player="🐈"
tree="🌳"
mrmeowmeow="😸"
mouse="🐁"
catnip="⭐"
dog="🐶"
owner="🧍"
shower="🛀"
kitchen="🍳"
sofa="🛋️"
bed="🛏️"


rooms=[ # Left, Right, Up, Down
       [brick, brick, brick, door], # introScene, index 0
       [sofa, door, brick, door], # livingroom, index 1
       [kitchen,door,door,door], # kitchen, index 2 
       [tree,tree,tree,tree], # outside, index 3
       [brick, brick, mouse, door], # garage, index 4
       [door, brick, door, door], # hallway, index 5
       [catnip, catnip, catnip, catnip], #goodending 6
       [dog, dog, dog, tree], #badending index 7
       [tree, tree, mrmeowmeow, tree], #neighboryard index 8
       [brick, door, door, catnip], #catnip index9
       [owner, door, brick, shower], #bathroom index10
       [brick, brick, door, bed] #bedroom index11
       
      ]

def drawRoom(index):
    global rooms
    
    left=0
    right=1
    up=2
    down=3
    r=rooms[index]
    print("\n")
    print(brick+brick+r[up]+brick+brick)
    print(r[left]+"   "+player+"      "+r[right])
    print(brick+brick+r[down]+brick+brick)
    print("\n")




catnip = False


def introduction():
    drawRoom(0)
    print("\nWelcome to the Cat Adventure Game!")
    time.sleep(1)
    print("You are a curious cat named Whiskers. There are many rooms and outdoors to explore and who knows what you may find. Try not to get a bad ending!")
    time.sleep(1)
    print("Your adventure begins now!\n")
    time.sleep(2)
    global catnip
    catnip = False
    return scene_one()

def scene_one():
    drawRoom(1)
    print("\nScene 1: The Living Room")
    time.sleep(1)
    print("You find yourself in the cozy living room.")
    time.sleep(1)
    print("Do you want to explore the kitchen or go outside?")
    choice = input("Type 'kitchen' or 'outside': ").lower()
    if choice == 'kitchen':
        return "kitchen"
    elif choice == 'outside':
        return "outside"
    else:
        print("Invalid choice, try again.")
        return scene_one()


def scene_two():
    drawRoom(2)
    global catnip
    print("\nScene 2: The Kitchen")
    time.sleep(1)
    print("You discover a bowl of tasty-looking salmon.")
    time.sleep(1)
    print("Do you want to eat the fish, ignore the fish and explore further, or leave the kitchen?")
    choice = input("Type 'eat' or 'ignore or 'leave': ").lower()
    while choice != 'eat' and choice!='ignore' and choice!='leave':
        choice = input("Type 'eat' or 'ignore or 'leave': ").lower()
    if choice == 'eat':
        return good_ending()
    elif choice == 'ignore':
        print("You discover a bag of catnip.")
        drawRoom(9)
        choice = input("Type 'take' or 'leave': ").lower()
        while choice != 'take' and choice != 'leave':
            choice = input("Type 'take with you' or 'leave': ").lower()
        if choice == 'take':
            catnip = True
            print("Explore further inside or go outside?") 
            choice = input("Type 'explore' or 'outside': ").lower()
            if choice == 'explore':
                return "hallway"
            elif choice == 'outside':
                return "outside"
    if choice == 'eat':
        return "good_ending"
    elif choice == 'leave':
        return "scene_one"
    
def scene_three():
    drawRoom(3)
    global catnip
    print("\nScene 3: Outside")
    time.sleep(1)
    print("You see a bird in the backyard.")
    time.sleep(1)
    if catnip == True:
        print("Do you want to use the catnip to get the bird, ignore the bird and explore further, or go back inside?")
        choice = input("Type 'use catnip' or 'ignore' or 'inside': ").lower()
        while choice != 'use catnip' and choice != 'ignore' and choice != 'inside':
            choice = input("Type 'use catnip' or 'ignore' or 'inside': ").lower()
        if choice == 'use catnip':
            print("The catnip enahnced your focus and you caught the bird! You see a garage, would you like to explore or go back inside?")
            choice = input("Type 'explore' or 'inside': ").lower()
            while choice != 'explore' and choice != 'inside':
                choice = input("Type 'explore' or 'inside': ").lower()
            if choice == 'explore':
                return "garage"
            elif choice == 'inside':
                return scene_one()
        elif choice == 'inside':
            return scene_one()
        elif choice == 'ignore':
            return scene_four()
    elif catnip == False:
        print("Do you want to chase the bird or go back inside?")
        choice = input("Type 'chase' or 'inside': ").lower()
        while choice != 'chase' and choice !='inside':
            choice = input("Type 'chase' or 'inside': ").lower()
        if choice == 'chase':
            return "bad_ending"
        elif choice == 'inside':
            return scene_one()
    else:
        print("Invalid choice. Try again.")
        return scene_three()
    
def scene_four():
    drawRoom(4)
    print("\nScene 4: Garage")
    time.sleep(1)
    print("Would you like to enter?")
    choice = input("Type 'yes' or 'no': ")
    if choice == 'yes':
        print("You see mouse droppings, do you investigate?")
        choice = input("Type 'yes' or 'no': ").lower()
        while choice != 'yes' and choice != 'no':
            choice = input("Type 'yes' or 'no': ").lower()
        if choice== 'yes':
            print("You find and catch the mouse, do you eat it?")
            choice = input("Type 'yes' or 'no': ").lower()
            while choice != 'yes' and choice != 'no':
                choice = input("Type 'yes' or 'no: ")
            if choice == 'yes':
                return badending_two()
            elif choice == 'no':
                print("You let the mouse go and explore further.\nYou find a window that leads to the neighbor's yard.")
                return scene_eight()
        elif choice == 'no':
            print("You ignore the mouse droppings and find an exit that takes you to the nieghbor's yard.")
            return scene_eight()
    elif choice == 'no':
        print("You ignore the garage and find an opening in a gate to the neighbor's yard.")
        return scene_eight()
    else:
        print("Invalid choice, try again.")
        return scene_four()

def scene_five():
    drawRoom(5)
    print("\nScene 5: Hallway")
    time.sleep(1)
    print("You hear a sound coming from the bathroom, do you enter or continue down the hallway?")
    choice = input("Type 'bathroom' or 'continue': ").lower()
    while choice != 'bathroom' and choice !='continue':
        choice = input("Type 'bathroom' or 'continue': ").lower()
    if choice == 'bathroom':
        return scene_six()
    elif choice == 'continue':
        print("You find a set of stairs.. do you go up or go back to the living room?")
        choice = input("Type 'go up' or 'go back': ").lower()
        while choice != 'go up' and choice != 'go back':
            choice = input("Type 'go up' or 'go back': ").lower()
        if choice == 'go up':
            return scene_seven()
        elif choice == 'go back':
            return scene_one()

def scene_six():
    drawRoom(10)
    print("\nScene 6: The Bathroom")
    time.sleep(1)
    print("Your owners try to put you in the bath, do you take the bath or run away?")
    choice = input("Type 'bath' or 'run': ").lower()
    while choice != 'bath' and choice != 'run':
        choice = input("Type 'bath' or 'run': ").lower()
    if choice == 'bath':
        return badending_three()
    elif choice == 'run':
        print("You manage to escape. Do you want to explore the hallway or go outside?")
        choice = input("Type 'hallway' or 'outside': ").lower()
        while choice != 'hallway' and choice != 'outside':
            choice = input("Type 'hallway' or 'outside': ").lower()
        if choice == 'hallway':
            return scene_five()
        elif choice == 'outside':
            return scene_three()

def scene_seven():
    drawRoom(11)
    print("\nScene 7: Owner's Bedroom")
    time.sleep(1)
    print("You enter your owner's bedroom and see fresh laundry on the bed, do you sleep on it or pee on it?")
    choice = input("Type 'sleep' or 'pee': ").lower()
    while choice != 'sleep' and choice != 'pee':
        choice = input("Type 'sleep' or 'pee': ").lower()
    if choice == 'sleep':
        return good_endingtwo()
    elif choice == 'pee':
        return badending_four()

def scene_eight():
    drawRoom(8)
    print("\nScene 8: The Neighbor's Yard")
    time.sleep(1)
    print("You run into your cat neighbor Mr.Meow Meow, he asks if you want to play with him.")
    choice = input("Type 'yes' or 'no': ").lower()
    while choice != 'yes' and choice != 'no':
        choice = input("Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        return goodending_three()
    elif choice == 'no':
        return badending_five()


def good_ending():
    drawRoom(6)
    print("\nCongratulations! You enjoyed a delicious fish and had a good nap.")
    time.sleep(1)
    print("You are a happy cat! Thanks for playing!")
    time.sleep(2)
    return introduction()

def good_endingtwo():
    print("\nCongratulations! You took a long nap and felt refreshed!")
    time.sleep(1)
    print("You are a happy and sleepy cat, Thanks for playing!")
    return introduction()

def bad_ending():
    print("\nOh no! You chased the bird and got lost outside.")
    time.sleep(1)
    print("Your adventure ends here. Better luck next time!")
    time.sleep(2)
    return introduction()

def badending_two():
    print("\nThe mouse was poisoned, you died!")
    time.sleep(1)
    print("Your adventure ends here. Better luck next time!")
    time.sleep(2)
    return introduction()

def badending_three():
    print("\nOh no! You took a bath and now you are soaking wet and upset. No more exploring for you!")
    time.sleep(1)
    print("Your adventure ends here. Better luck next time!")
    time.sleep(2)
    return introduction()

def badending_four():
    print("\nOh no! Your owners caught you and put you in a cage.")
    time.sleep(1)
    print("Your adventure ends here. Better luck next time!")
    time.sleep(2)
    return introduction()

def goodending_three():
    print("\n You and Mr.Meow Meow played tag for hours and had fun.")
    time.sleep(1)
    print("Congratulations! You are a happy fulfilled cat! Thanks for playing.")
    time.sleep(2)
    return introduction()

def badending_five():
    drawRoom(7)
    print("\n Oh no! Mr.Meow Meow left and you got chased by the neighbor's dog.")
    time.sleep(1)
    print("The neighbor's dog caught you and ate you. You died. Better luck next time.")
    time.sleep(2)
    return introduction()

def main():
    scene_map = {
        "introduction": introduction,
        "scene_one": scene_one,
        "kitchen": scene_two,
        "outside": scene_three,
        "garage": scene_four,
        "hallway": scene_five,
        "bathroom": scene_six,
        "bedroom": scene_seven,
        "yard": scene_eight,
        "good_ending": good_ending,
        "good_endingtwo": good_endingtwo,
        "goodending_three": goodending_three,
        "bad_ending": bad_ending,
        "badending_two": badending_two,
        "badending_three": badending_three,
        "badending_four": badending_four,
        "badending_five": badending_five
    }

    current_scene = "introduction"

    while current_scene:
        scene_function = scene_map[current_scene]
        current_scene = scene_function()

if __name__ == "__main__":
    main()
