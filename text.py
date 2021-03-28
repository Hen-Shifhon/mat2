

def revword(word):
    return word[::-1].lower().strip()
  
def countword():
    counter=1
    file=open('text.txt')
    fileAsList=file.readlines()
    word=fileAsList[0].lower().strip()
    for line in fileAsList[1:]:
        for cur_word in line.split():
            if revword(cur_word).strip()==word:
                counter+=1
    return counter
        