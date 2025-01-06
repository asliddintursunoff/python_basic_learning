rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
while(True):
    CPU_chance = random.randint(0, 2)
    
    
    if(CPU_chance==0):
        a = rock
    elif(CPU_chance==1):
        a = paper
    else:
        a = scissors
    
    userChance = int(input("enter \n0 for rock \n1 for paper \n2 for scissors: "))
    
    if(userChance==0):
        b = rock
    elif(userChance==1):
        b = paper
    else:
        b = scissors
    
    print(f"You choose {userChance}\n {b}")
    #CPU win conditionts
    if((userChance==0 and CPU_chance==1) or (userChance==1 and CPU_chance==2) or( userChance==2 and CPU_chance==0)):
        print(f"CPU chose {CPU_chance} \n{a}")
        print("CPU win")
     #User win conditions 
    elif((userChance==0 and CPU_chance==2) or (userChance==2 and CPU_chance==1 )  or  (userChance==1 and CPU_chance==0) ):
        print(f"CPU chose {CPU_chance} \n{a}")
        print("You win")
   
   
    else:
        print(f"CPU chose {CPU_chance} \n{a}")
        print("no body wins")
    