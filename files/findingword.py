x= input("Word you want to find: ")
count =0
with open('files/findword.txt','r') as file: 
    # reading each line     
    for line in file: 
        # reading each word         
        for word in line.split(): 
            #print(word)
            if(x in word):
            # displaying the words 
                count+=1
                print("The Word exists and it is:",word)           
    print("The number of occurances are" ,count)