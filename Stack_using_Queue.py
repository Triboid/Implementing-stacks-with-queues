q1 = []
q2 = []
size = int(input("Enter the size of your stack: "))
def isempty(item):
    if len(item) == 0:
        return True
    else:
        return False

def enqueue(item,val):    
    if len(item) < size:        
        item.append(val)

def dequeue(item):
    if isempty(item) == False:
        a = item[0]
        item.pop(0)
        return a

def push(val):
    enqueue(q1,val)   

def pop(q1,q2):        
    while len(q1) > 1:
        enqueue(q2,dequeue(q1))    
    a = q1[0] 
    q1.pop()

    return (a)     


print("Menu:")
print("What operation would you like to perform: Push or Pop")
print("Enter 1 for push")
print('Enter 2 for pop')
print("Enter 3 for exiting the program")

choice = 1
while choice == 1 or choice == 2:
    choice = int(input("Enter your choice here: "))
    
    if choice == 1:
        if len(q1) < size:
            val = int(input("Enter the value you would like to push in the stack: "))
            push(val)
            print(f"Your stack: {q1}")
        else:
            print("Error! Stack is full!\nYou can either pop it or exit the program.")

               
    if choice == 2:

        if isempty(q1) == False:
            print(f"The popped put value is: {pop(q1,q2)}")
            print(f"Your stack: {q2}")
            q2,q1 = q1,q2
        else:
            print("Error! Stack is empty!\nYou can either fill the stack or exit the program.")
            
    if choice == 3:
        print("Exiting...")
        break
            



