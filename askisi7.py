def main():
    text=open_file()
    ASCII_list=ASCII(text)
    ASCII_odd_list=odd_numbers(ASCII_list)
    statistics(ASCII_odd_list)
    

def open_file():
        file=input(('Give me the name of the file to open: '))
        infile=open(file,'r')
        lines=infile.read()
        text_list=lines.split()
        infile.close()
        return text_list
    

def ASCII(a_list):
    #FIND THE ASCII NUMBER OF EACH LETTER IN THE TEXT
        ASCII_numbers=[]
        for i in a_list:
            for j in i:
                if ((ord(j)>=65 and ord(j)<=90)or(ord(j)>=97 and ord(j)<=122)): #KEEP ONLY LETTERS, NOT SYMBOLS OR NUMBERS
                    ASCII_numbers.append(ord(j))
        return ASCII_numbers
                                


def odd_numbers(a_list):
    #KEEP ONLY THE ODD NUMBERS IN ASCII LIST
    for number in a_list:
        if number%2==0:
            a_list.remove(number)
    return a_list


def statistics(a_list):
    counted=[]#LIST WITH NUMBERS I COUNTED,TO AVOID MORE COUNTS FOR THE SAME NUMBER
    total=[]#LIST WITH COUNTS OF EACH NUMBER
    for i in a_list:
        if i not in counted:
            counted.append(i)
            total.append(a_list.count(i))
    print_statistics(counted,total,a_list)


def print_statistics(nums_list,stat_list,odd_list):
    print('    STATISTICS   ')
    print('--------------------')
    for index in range(len(nums_list)):
        rate=stat_list[index]/len(odd_list)*100
        #IF RATE IS FLOAT DO UPPER ROUNDING 
        if float(int(rate))!=rate:
            rate=int(rate)+1
        else:
             rate=int(rate)
        print(chr(nums_list[index]),':','*'*rate,end='')
        print(rate,'%',sep='')
        print('\n')
        
main()
