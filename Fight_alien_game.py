stamina = 6
alive=False
def report(stamina):
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished! ")
def fight(stamina):
    while stamina > 0:
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run--")
        if "hit" in response or "attack" in response:
            less = report(stamina-1)
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
        stamina-=1
    return False
n=int(input("how many times to want play code--"))
fight(n)
print ("A threatening alien wants to fight you!\n")