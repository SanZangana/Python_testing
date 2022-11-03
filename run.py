# user presses 's' and the game will ask for their name. once they type their name, the game begins with questions and different choices which leads to different paths
start = input("Hello and welcome to Amazing Adventures. To start, please press enter key ")
print(start)

# user enters name and game proceeds...

name = input("Before we start, type in your name: ")
print("Get ready", name , "the Amazing Adventure starts now!")


# so here the user has to make a choice betweem twp different roads/paths- ofc they lead to different paths and end goals/adventures.
question = input("You open your eyes, and see two roads a head in a mystical wood. The road to the right leads to a big castle while the road to the left leads to a UFO. Now, which path will you choose? Press enter 'R' for the castle or 'L' for the UFO. ")
# Right path
if question.lower() == 'r':
    question = input("On the way to the castle... a wizard appears. The wizard asks 'You can ask me to craft a weapon, what will you choose?' Press 'R' for a raygun or 'L' for a Lightsaber ")
    if question.lower() == 'r':
        print("There you go, but keep in mind, save the ammunition for the villains a head")
        # Left path 
if question.lower() == 'l':
    question == input("While on your way to the UFO a foreign green creature with one eye appears! 'Hello human, would you like to taste soda from Jupiter?' Press 'Y' for yes and 'N' for no ")
    if question.lower() == 'y':
        # when user "fails" the game they can press 'R' for a chance to pick another path
        print("You drink the soda but your vision starts to get blurry... you pass out. GAME OVER. Press 'R' to restart the game ")
    if question.lower() == 'n':
        print("Phew... good choice. That was the evil alien 'Duhok', he is known for giving travelers fake soda to rob them! ")
