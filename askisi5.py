import random
def main():
    print("WELCOME TO MY SOS GAME!LET'S START NOW!")
    print('----------------------------------------')
    length=int(input('Give me the colums of the game: '))
    width=int(input('Give me the rows of the game: '))
    
    #PLAY THE GAME ONLY IF LENGTH OR WIDTH >3
    while length<3 and width<3:
        print('Length or width has to be bigger than 2')
        length=int(input('Give me the colums of the game: '))
        width=int(input('Give me the rows of the game: '))
        
    #PLAY THE GAME 50 TIMES    
    total_count=0
    for i in range(50):
        game_rectangle=create_rectangle(width,length)
        total_count+=count_of_SOS_in_rows(width,length,game_rectangle)+count_of_SOS_in_colums(width,length,game_rectangle)+\
                      count_of_SOS_in_diagonals1(width,length,game_rectangle)+count_of_SOS_in_diagonals2(width,length,game_rectangle)
    print('The average of SOS is: ',format(total_count/50,'.2f'))

          
def create_rectangle(N,M):
    
    #INITIALIZATION OF ROWS,COLS AND ARRAY
    ROWS=N
    COLS=M
    array=[]

    
    #INITIALIZATION OF ARRAY WITH O
    for r in range(ROWS):
        row=[]
        for c in range(COLS):
            row.append('O')
        array.append(row)

        
    #HOW MANY POSITIONS I WILL FILL WITH S
    if (N*M)%2==0:
        positions=(N*M)/2
    else:
        positions=(N*M)//2+1


    #FILL HALF OF THE POSITIONS WITH S
    CountOfS=0
    while CountOfS!=positions:
        r=random .randint(0,ROWS-1)
        c=random.randint(0,COLS-1)
        if array[r][c]!='S':
            array[r][c]='S'
            CountOfS+=1
    return array



def count_of_SOS_in_rows(N,M,an_array):
    countSOS_in_rows=0
    for i in range(N):
        for j in range(M-2):
            if an_array[i][j]+an_array[i][j+1]+an_array[i][j+2]=='SOS':
                countSOS_in_rows+=1
    return countSOS_in_rows

    
def count_of_SOS_in_colums(N,M,an_array):
    countSOS_in_cols=0
    for j in range(M):
        for i in range(N-2):
            if an_array[i][j]+an_array[i+1][j]+an_array[i+2][j]=='SOS':
                countSOS_in_cols+=1
    return countSOS_in_cols

    
    
def count_of_SOS_in_diagonals1(N,M,an_array):
    #COUNT SOS IN DIAGONALS STARTING FROM THE MAIN DIAGONAL
    countSOS_in_diagonals1=0
    for i in range(N-2):
       for j in range(M-2):
           if an_array[i][j]+an_array[i+1][j+1]+an_array[i+2][j+2]=='SOS':
               countSOS_in_diagonals1+=1
    return countSOS_in_diagonals1


    
def count_of_SOS_in_diagonals2(N,M,an_array):
    #COUNT SOS IN DIAGONALS STARTING FROM THE SECONDARY DIAGONAL
     countSOS_in_diagonals2=0 
     for i in range(N-2):
        for j in range(M-1,1,-1):
            if an_array[i][j]+an_array[i+1][j-1]+an_array[i+2][j-2]=='SOS':
                countSOS_in_diagonals2+=1
     return countSOS_in_diagonals2
            
main()
