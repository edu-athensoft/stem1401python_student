#stem1401_python_final_program1
#Qi Jun

#program has to remove certain punctuations:  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

'''!()-[]{};:'"\,<>./?@#$%^&*_~'''

forbidden_characters = ["''","'","!","(",")","-","[","]","{","}",";",":","'"'"','"',"\\",",","<",">",".","/","?","@","#","$,""&","%","^","*","~","'"]

word = input("insert words and anything you want")

for i in word:
    if i not in forbidden_characters:
        print(i,end="")

#end!
