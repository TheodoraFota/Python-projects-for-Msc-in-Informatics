def main():
    text=open_file()
    ASCII_list=ASCII(text)
    reverse_list=reverse_text(ASCII_list)
    print_text(reverse_list)
    
    
def open_file():
    file=input('Give me the name of the file to open: ')
    infile=open(file,'r')
    lines=infile.read()
    text_list=lines.split()
    infile.close()
    return text_list
    

def ASCII(a_list):
    #FIND THE ASCII NUMBER OF EACH LETTER IN TEXT
    mirror_ASCII=[]
    for i in a_list:
        list_to_append=[] #LIST OF ASCII NUMBERS OF EACH WORD
        for j in i:
            list_to_append.append(chr(128-ord(j)))
        mirror_ASCII.append(list_to_append)
    return mirror_ASCII


def reverse_text(a_list):
    #REVERSE THE ELEMENTS OF EACH LIST
    for i in a_list:
        i.reverse()
    return(a_list)


def print_text(a_list):
    print('The mirror text is:')
    for i in a_list:
            for j in i:
                print (j,end='')

main()
