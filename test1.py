import sys
# this is a sample python file
""" print(sys.version)
if 5>2:
    print("5 is greater than 2") """

currentPlayer = ""
finnian = "Finnian[PC]"
john = "John[PC]"
aubrey = "Aubrey[PS5]"
""" on = True    
off = False
if on == True:
    print("true")
if off != True:
    print("false")
for x in [finnian, john, aubrey]: """
 #   print("PLAYER:", x)

def greet(arg1, arg2, arg3):
    global currentPlayer
    print("Hello,", arg1)
    print("RANK:", arg2)
    print("Rocket Pass:", arg3)
    print("")
    currentPlayer = arg1

greet(finnian, "Gold II", "Yes")
greet(aubrey, "Bronze I", "No")
greet(john, "Silver I", "Yes")

if currentPlayer == aubrey:
    print("Welcome Back Aubrey! Do you want to work on your Gamesense?")
elif currentPlayer == finnian:
    print("Welcome Back Finnian! Do you want to work on your Air Dribbling?")
else: currentPlayer == john
print("Welcome Back John! Do you want to work on your Dodges?")
print("Current Player:", currentPlayer)

