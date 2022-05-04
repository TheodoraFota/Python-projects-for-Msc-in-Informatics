import random
def main():
    print('SCORE 4')
    print('---------')
    dim=int(input('Give me the dimension of the tables for score4: '))\

    #PLAY THE GAME ONLY IF DIMENSION >=4
    while dim<4:
        print('Dimension of table must be bigger than 4')
        dim=int(input('Give me the dimension of the tables for score4: '))

    #PLAY THE GAME 100 TIMES
    total_count=0
    for i in range(100):
        score4_array=create_array(dim)
        total_count+=count_of_fours_in_rows(dim,score4_array)+ count_of_fours_in_cols(dim,score4_array)+count_of_fours_in_diagonals1(dim,score4_array)+\
            count_of_fours_in_diagonals2(dim,score4_array)
    print('The average of fours of 1 is:',format(total_count/100,'.2f'))




def create_array(N):
    
    #INITIALIZATION OF ROWS,COLUMS AND ARRAY
    ROWS=N
    COLS=N
    array=[]

    
    #INITIALIZATION OF ARRAY WITH 0
    for r in range(ROWS):
        row=[]
        for c in range(COLS):
            row.append(0)
        array.append(row)



    #HOW MANY POSITIONS I WILL FILL WITH 1
    if (N*N)%2==0:
        MaxNum=(N*N)/2
    else:
        MaxNum=(N*N)//2+1
    

   
    #FILL HALF OF THE POSITIONS WITH 1
    CountOf1=0
    while CountOf1!=MaxNum:
        r=random.randint(0,ROWS-1)
        c=random.randint(0,COLS-1)
        if array[r][c]!=1:
            array[r][c]=1
            CountOf1+=1
    return array




def count_of_fours_in_rows(N,an_array):
    count1_in_rows=0
    for i in range(N):
        for j in range(N-3):
            if an_array[i][j]+an_array[i][j+1]+an_array[i][j+2]+an_array[i][j+3]==4:
                count1_in_rows+=1
    return count1_in_rows


    
def count_of_fours_in_cols(N,an_array):
    count1_in_cols=0
    for j in range(N):
        for i in range(N-3):
            if an_array[i][j]+an_array[i+1][j]+an_array[i+2][j]+an_array[i+3][j]==4:
                count1_in_cols+=1
    return count1_in_cols


def count_of_fours_in_diagonals1(N,an_array):
    #COUNT FOURS OF 1 IN DIAGONALS STARTING FROM THE MAIN DIAGONAL
    count1_in_diagonals1=0
    for i in range(N-3):
       for j in range(N-3):
           if an_array[i][j]+an_array[i+1][j+1]+an_array[i+2][j+2]+an_array[i+3][j+3]==4:
               count1_in_diagonals1+=1
    return count1_in_diagonals1

def count_of_fours_in_diagonals2(N,an_array):               
    #COUNT FOURS OF 1 IN DIAGONALS STARTING FROM THE SECONDARY DIAGONAL
    count1_in_diagonals2=0
    for i in range(N-3):
        for j in range(N-1,2,-1):
            if an_array[i][j]+an_array[i+1][j-1]+an_array[i+2][j-2]+an_array[i+3][j-3]==4:
                count1_in_diagonals2+=1
    return count1_in_diagonals2
    
               
   
                
        
main()

    
        
        

