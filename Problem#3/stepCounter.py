def feet_to_steps(user_feet):
   #write your code here
   #Emily Burke Lab time friday at 3
   return user_feet/2.5
if __name__ == '__main__':
 #take input feet steps here
 #store it into the function
   user_feet = float(input())
   #print your steps here
   print(f'{feet_to_steps(float(user_feet)):.0f}')