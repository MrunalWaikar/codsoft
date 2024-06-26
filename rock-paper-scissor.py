import random
item_list=["Rock", "Paper", "Scissor"]

user_choice=input("Enter your move = Rock , Paper, Scissor=")
comp_choice= random.choice(item_list)

print(" user choice=",user_choice, "Copmputer choice=",comp_choice)

if user_choice == comp_choice:
    print("Both chooses same -Match tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = Computer wins")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the paper= Computer wins")
    else:
        print("Paper covers the rock=You win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts the paper= You wins")
    else:
        print("Rock smashes the scissor=Computer wins")                
    
                    
