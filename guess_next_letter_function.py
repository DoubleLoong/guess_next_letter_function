def guess_next_letter(partten,used_letters=[],word_list=['abound','apple','about','attack']):
    partten_dict={}
    for index,items in enumerate(tuple(partten)):
        if items !='_':
            partten_dict[index]=items
    wrong_letter=list(set(used_letters).difference(set(partten)))
    probable_words=[]
    for word in word_list:
        if len(word)==len(partten):
            if  used_letters==[]:
                probable_words.append(word)
                continue
            same_letters_count=0
            for index,items in enumerate(tuple(word)):
                if  partten_dict.get(index)==items:
                    same_letters_count+=1
                if items in wrong_letter:
                    same_letters_count-=1
            if same_letters_count == len(partten_dict):        
                probable_words.append(word)
    if len(probable_words) ==0:
        return ''
    probable_letters={}
    for word in probable_words:
        for letter in set(word):
            if letter  in probable_letters.keys():
                probable_letters[letter]+=1
            else:
                probable_letters[letter]=1
    result_list =sorted(probable_letters.items(),key=lambda x:x[1],reverse=True)
    for i in result_list:
        if i[0] not in set(used_letters):
           return i[0]
    
if __name__=='__main__':
    word='attack'
    test1=[['______',list()],['_____k',list('ke')],['_tt__k',list('ket')]]
    for index,items in enumerate(test1):
        print(index+1," next_letter:",guess_next_letter(items[0],items[1]),True if guess_next_letter(items[0],items[1]) in word else False)
