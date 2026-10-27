
'''


*  *  *  *  *  *  *

   *  *  *  *  *

      *  *  *

         *

'''


column = 7
row = 4
space= 0

for i in range(1, row+1):

    for z in range(1, space+1): 
        print("   ", end=" ")
        
    for j in range(1, column+1):
        print(" * ", end=" ")  

    column=column-2 
    space=space+1
    print("\n")
