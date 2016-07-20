import random

class Player:
    
    def __init__(self, name, weapon):
        self.name = name
        self.maxPlayerHP = 100
        self.maxPlayerMP = 100
        self.playerHP = 100
        self.playerMP = 100
        self.playerEXP = 0
        self.level = 1
        self.items = []
        self.weapon = weapon
        self.follower = "none"

    
    def playerAttack(self, player, monster):
        playerSuccess = random.randint(1,8)
        if playerSuccess == 1:
            print("You missed...")
        else:
            if monster.monsterHP > 0:
                if player.weapon == "sword":
                    damage = random.randint(12, 15)
                    monster.monsterHP -= damage
                    print("\nYou slash at the", monster.monsterName, "and deal", damage, "damage.")
                if player.weapon == "staff":
                    damage = random.randint(15, 18)
                    if player.playerMP >= damage:
                        player.playerMP -= damage
                        monster.monsterHP -= damage
                        print("\nYou hurl a fireball at the", monster.monsterName, "and deal", damage, "damage.")
                        print("You now have", player.playerMP, "MP.")
                    elif player.playerMP > 0 and player.playerMP - damage < 0:
                        damage = player.playerMP
                        monster.monsterHP -= damage
                        player.playerMP = 0
                        print("\nYou hurl a fireball at the", monster.monsterName, "and deal", damage, "damage.")
                        print("You are out of MP!")
                    elif player.playerMP == 0:
                        damage = random.randint(5, 8)
                        monster.monsterHP -= damage
                        print("\nYou are out of MP, and smack the", monster.monsterName, "with your staff.")
                if player.weapon == "daggers":
                    double = random.randint(1, 5)
                    if double == 1:
                        damage = random.randint(20, 24)
                        print("\nDouble Attack! You stab at the", monster.monsterName, "twice and deal", damage, "damage.")
                    else:
                        damage = random.randint(10, 12)
                        print("\nYou stab at the", monster.monsterName, "and deal", damage, "damage.")
                    monster.monsterHP -= damage
                if monster.monsterHP > 0 :
                    print("The", monster.monsterName, "has", monster.monsterHP, "HP.")
                else:
                    print("The", monster.monsterName, "has no more HP!")
        return monster.monsterHP


    def followerAttack(self, player, monster):
        if player.follower == "Kira":
            kiraAttack = random.randint(1,5)
            if kiraAttack == 1:
                kiraDamage = random.randint(4,6)
                print("\nKira smacks the", monster.monsterName, "with her staff for", kiraDamage, "damage.")
                monster.monsterHP -= kiraDamage
                if monster.monsterHP > 0 :
                    print("The", monster.monsterName, "has", monster.monsterHP, "HP.")
                else:
                    print("The", monster.monsterName, "has no more HP!")
            else:
                kiraHeal = random.randint(10,14)
                player.playerHP = min(player.playerHP + kiraHeal, player.maxPlayerHP)
                print("\nKira heals you for", kiraHeal, "HP!")
                print("You now have", player.playerHP, "HP.")

    def levelUp(self, player):
        newEXP = player.playerEXP - 100
        player.level += 1
        print("\nYou have grown to level", player.level, "!")
        player.playerEXP = newEXP
        upHP = random.randint(5, 10)
        upMP = random.randint(5, 10)
        player.maxPlayerHP += upHP
        player.maxPlayerMP += upMP
        print("\nYour HP increases by", upHP, "to", player.maxPlayerHP)
        print("\nYour MP increases by", upMP, "to", player.maxPlayerMP)
        player.playerHP = player.maxPlayerHP
        player.playerMP = player.maxPlayerMP
        print("\nYour HP and MP have been restored!")


class Monster:

    def __init__(self, monsterName, monsterHP, monsterPower, monsterEXP):
        self.monsterName = monsterName
        self.monsterHP = monsterHP
        self.monsterPower = monsterPower
        self.monsterEXP = monsterEXP


    def monsterAttack(self, player, monster):
        monsterSuccess = random.randint(1,5)
        if monsterSuccess == 1:
            print("\nThe", monster.monsterName, "missed!")
            print("You have", player.playerHP, "HP and", player.playerMP, "MP.")
        else:
            monsterDamage = random.randint(monster.monsterPower, monster.monsterPower + 5)
            player.playerHP -= monsterDamage
            if player.playerHP <= 0:
                print("\nThe", monster.monsterName, "has struck you down...")
                print("\n *** BATTLE END ***")
                return player.playerHP
            else:
                print("You take", monsterDamage, "damage, and have", player.playerHP, "HP and", player.playerMP, "MP.")
                return player.playerHP




def monsterBattle(player, monster):
    print("\n *** BATTLE START ***")
    print("\nA", monster.monsterName, "appeared!")
    print("You have", player.playerHP, "HP, and", player.playerMP, "MP.")
    print("The", monster.monsterName, " has", monster.monsterHP, "HP.")
    while player.playerHP > 0 :
        while True:
            option = input("\nDo you want to attack, defend, use an item or run?\n(Type attack, defend, item, or run)")
            if option == "run":
                print("\nYou ran away from the", monster.monsterName, ".")
                print("\n *** BATTLE END ***")
                print("You have", player.playerHP, "HP,", player.playerMP, "MP, and ", player.playerEXP, "EXP.")
                return "run"
            if option == "attack":
                player.playerAttack(player, monster)
                if monster.monsterHP <= 0:
                    print("\nYou defeated the", monster.monsterName,"!")
                    gainedEXP = random.randint(monster.monsterEXP, monster.monsterEXP + 5)
                    player.playerEXP += gainedEXP
                    print("You have", player.playerHP, "HP,", player.playerMP, "MP, and gain", gainedEXP, "EXP.")
                    if player.playerEXP >= 100:
                        player.levelUp(player)
                    print("\n *** BATTLE END ***")
                    return "victory"
                else:
                    if player.follower != "none":
                        player.followerAttack(player,monster)
                    print("\nThe", monster.monsterName, "strikes!")
                    monster.monsterAttack(player, monster)
                    if player.playerHP <= 0:
                        return "defeat"
            if option == "defend":
                print("\nYou brace yourself for the", monster.monsterName,"'s attack.")
                if player.follower != "none":
                    player.followerAttack(player,monster)
                print("\nThe", monster.monsterName, "strikes!")
                monster.monsterPower -= 5
                monster.monsterAttack(player,monster)
                monster.monsterPower += 5
                print("The", monster.monsterName, " has", monster.monsterHP, "HP.")
                if player.playerHP <= 0:
                    return "defeat"
            if option == "item" and player.items == []:
                print("\nYou search your pack but find nothing!")
            if option == "item" and player.items != []:
                print("\nYou have", player.items, ". What would you like to use?")
                itemUse = input("(Type the name of an item from your pack)")
                if itemUse not in player.items:
                    print("\nYou don't seem to have any of those...")
                elif itemUse in player.items:
                    if itemUse == "potion":
                        player.playerHP = min(player.playerHP + 40, player.maxPlayerHP)
                        print("\nThe potion restores your HP to", player.playerHP, ".")
                        player.items.remove("potion")
                    elif itemUse == "herb":
                        player.playerMP = min(player.playerMP + 40, player.maxPlayerMP)
                        print("\nThe herb restores your MP to", player.playerMP, ".")
                        player.items.remove("herb")
                    print("The", monster.monsterName, " has", monster.monsterHP, "HP.")
                    if player.follower != "none":
                        player.followerAttack(player,monster)
                    print("\nThe", monster.monsterName, "strikes!")
                    monster.monsterAttack(player, monster)
                    if player.playerHP <= 0 :
                        return "defeat"

                
                
                


def main():
    defeatOutcome = "defeat"
    death = "You have fallen..."
    weapon = 0
    name = input("\nWhat is your name?")
    player = Player(name, weapon)
    print("\n **** EXORDIUM ****")
    print("\n...You awaken on the cold floor of a dark room...")
    print("In a pack by your feet you find a potion and an herb.")
    player.items.append("potion")
    player.items.append("herb")
    print("You see a staff, a sword, and two daggers in the corner of the room.")
    while weapon != "staff" or weapon != "sword" or weapon != "daggers":
        weapon = input("\nWhich weapon do you choose?(Type staff, sword, or daggers)")
        if weapon == "staff":
            print("\nYou pick up the staff and feel its power course through you.")
            player.weapon = "staff"
            break
        if weapon == "sword":
            print("\nYou pick up the steel sword and give it a few swings.")
            player.weapon = "sword"
            break
        if weapon == "daggers":
            print("\nYou pick up the iron daggers and sharpen them on each other.")
            player.weapon = "daggers"
            break
    door1 = 0
    while door1 != "left" or door1 != "right":
        door1 = input("There are two doors leading out of the dark room--one to the left, \n and one to the right. \n\nWhich door do you choose to open? (Type left or right)")        
        if door1 == "left" or "right":
            break
    if door1 == "left":
        print("\nYou enter the room to the left, and find a chest containing a potion. You add \n it to your pack and return to the dark room, then enter the door to the right.")
        player.items.append("potion")
        door1 = "right"
    if door1 == "right":
        print("\nYou enter a long hall. A bat swoops down from the ceiling!")
    bat = Monster("bat", 30, 5, 25)
    battle1 = monsterBattle(player, bat)
    if battle1 == defeatOutcome:
        return death
    print("\nYou walk the length of the long hall and come to large door at the end, \nbeyond which you hear a faint rustling. A wooden staircase on your right \nleads up into darkness.")
    choice1 = 0
    while choice1 != "door" or "stairs":
        choice1 = input("\nDo you choose to open the door or climb the staircase? (Type door or stairs)")
        if choice1 == "door" or "stairs":
            break
    if choice1 == "door":
        print("\nYou push open the large door slowly and enter a seemingly storage room. \n\nDo you wish to search the room or return to the staircase outside?")
        choice2 = 0
        while choice2 != "search" or "stairs":
            choice2 = input("(Type search or stairs)")
            if choice2 == "search" or "stairs":
                break
        if choice2 == "search":
            print("\nYou begin pouring over the room, searching the many barrels, sacks, and shelves for anything of use.")
            print("Resting on a box the corner of the room you come across an herb \nand a potion, and place them in your pack.")
            player.items.append("herb")
            player.items.append("potion")
            print("Suddenly from under the box you hear a screech and a giant rat jumps out!")
            rat = Monster("giant rat", 35, 8, 30)
            battle2 = monsterBattle(player, rat)
            if battle2 == defeatOutcome:
                return death
            choice2 = "stairs"
        if choice2 == "stairs":
            print("\nYou exit the room and return to the long hallway outside.")
        choice1 = "stairs"
    if choice1 == "stairs":
        print("\nYou begin to ascend the staircase, feeling your way carefully up the steps \ninto the dark. As you climb you begin to hear a faint voice that grows \nlouder with each step.")
    print("\nReaching the landing at the top of the stairway, you realize the voice is \ncalling for help. Atop the landing there is a hallway leading further into \ndarkness, and a door to the immediate right where the voice seems to be coming \nfrom. From under the door, a pale light flickers.")
    choice3 = 0
    while choice3 != "door" or "hall":
        choice3 = input("\nDo you wish to open the door or move past it down the hallway? \n(Type door or hall)")
        if choice3 == "door" or "hall":
            break
    if choice3 == "door":
        print("\nYou cautiously work the door open and step into the light of the room. \nYou see a young girl frantically batting at what appears to be a large blob \nof slime with a staff. As it lunges at her, she makes brief eye contact \nwith you and shrieks for help.")
        choice4 = 0
        while choice4 != "help" or "leave":
            choice4 = input("\nWill you help the girl or leave the room? (Type help or leave)")
            if choice4 == "help" or "leave":
                break
        if choice4 == "help":
            print("You run over to the girl to assist her in fighting the blob of slime!")
            slime = Monster("giant slime", 40, 9, 35)
            battle3 = monsterBattle(player, slime)
            if battle3 == defeatOutcome:
                return death
            print("The girl thanks you for your help. She tells you her name is Kira.")
            print("Kira says she awoke in this room with no memory of how she got here. \nAll she could find was the staff she is wiedling, which seems to have a healing effect, \nbut is not of much use for attacking.")
            print("Kira asks if she can join you as you try to find your way out.")
            kiraFollowChoice = 0
            while kiraFollowChoice != "yes" or "no":
                input("Will you let Kira join you? (Type yes or no)")
                if kiraFollowChoice == "yes" or "no":
                    break
            if kiraFollowChoice == "no":
                print("Kira gives you a cold stare, then storms out of the room and down the hall...")
            if kiraFollowChoice == "yes":
                player.follower = "Kira"
                print("Kira says she will assist you however she can.")
                print("You and Kira leave the room and begin making your way down the long hall.")
        if choice4 == "leave":
            print("You step back out of the room and close the door.") 
            choice3 = "hall"
    if choice3 == "hall":
        print("\nYou start walking down the hallway and the cries for help diminish \nuntil they are stifled altogether...")
    print("\nAt the end of the dark hallway, you reach a wall. It appears to be a dead end, \nuntil you spy a wooden ladder propped up against the right wall. It reaches up \nto the ceiling to what appears to be a port.")
    print("You cautiously ascend the rungs of the ladder until you can reach the port. \nYou try to push it open, but it appears the bolt is locked in place with a rusty pad.")
    choice5 = 0
    while choice5 != "break" or "search":
        choice5 = input("\nWill you try to break the bolt or search back down the hallway for a key? (Type break or search)")
        if choice5 == "break" or "search":
            break
    if choice5 == "break":
        if player.playerHP > 5:
            print("You grab the bolt, steading yourself on the top rung of the ladder, and pull \nwith all your might. The bolt gives slightly but is still firmly in place.")
            print("You wrench the bolt again and again, exhausting yourself in the process, but \nwith a hefty tug the rusty padlock snaps and the bolt flies free.")
            print("\nPushing the port open over your head, you shield your eyes as light pours \nthrough the opening. Climbing up and out of the hallway, you find youself in a \nransacked room in what seems to be a deserted cabin.")
            print("You collapse on the floor, out of breath and muscles aching from breaking the \nlock.")
            player.playerHP -= 5
            print("(You have lost 5 HP in the process, and your HP is now", player.playerHP, ")")
        else:
            print("You are too weary to try and break the bolt of the port open, and decide to search down the hallway for a key to the pad.")
            choice5 == "search"
    if choice5 == "search":
        pass
    print("A giant dragon swoops in and kills you...(cause that's all I got for now)")
    
        



    
        
if __name__ == "__main__": main()