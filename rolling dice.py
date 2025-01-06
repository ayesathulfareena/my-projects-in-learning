import random

players=int(input("enter the number of players: "))
score=0
while True:
 if players>=2:
  index=0
  for i in range(players):
    index+=1
    print(index,"player roll the dice")
    break
  break
 else:
  print("morethan 2 players require to play this game")
  break

while   players>=2:


   user=input("enter 'y' to roll a dice: ")
   
   if user=='y':
     while  True:
      roll=random.randint(1,6)
      
      if roll != 1:
       print("dice rolling number",roll)
       score+=roll
       break
      else:
       print("dice rolling number",roll)
       score+=roll
       while True:
        print("score:",score)
        
        if index<players:
         index+=1
         print(index,"player roll a dice")
         break
        while index==players:
         for i in range(2,roll):
          score+=roll
          print("dice rolling number",roll,"\n")
          break
       
        break
    
                  
    
        
      
    
      
    
   
   
 
   
    
      
