# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def find_gcf(x,y):
    for num1 in range (x,0,-1):
        if x % num1 == 0 and y % num1 == 0:
            return num1
        
            
        





if __name__ == '__main__':
  
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    print(find_gcf(x,y))

