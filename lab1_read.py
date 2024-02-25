import sys

###1.IO and sentences########
class Sentence:
    def __init__(self,sentences,num):  #root node index: 0 .
                # sentences:[ [sentence1 [token1[0-9],token2...], sentence2[[ ] ],... ]
        self.sentence_num = num #The number of the sentence in the corpus
        self.sentence = sentences[self.sentence_num] #sentence: [token1[0-9],token2...]
        self.tokens = []  # Tokens[1]= first word
        self.tokens_pos = []
        self.tokens_head = []
        self.tokens_morph=[]
        self.tokens_num = []  #[0,1,...len(sentence)]
        self.tokens_lemma=[]
        for snum in range(len(self.sentence)): # how many tokens
            self.tokens.append(self.sentence[snum][1])
            self.tokens_lemma.append(self.sentence[snum][2])
            self.tokens_pos.append(self.sentence[snum][3])
            self.tokens_morph.append(self.sentence[snum][5])
            self.tokens_head.append(self.sentence[snum][6])

def read(filename):
    f = open(filename, 'r',encoding="utf8") #,encoding="utf8"
    sentences = []
    sentence = []
    sentence.append([0,'Root','__NULL__','root_POS','_','_',-1,'__NULL__','_','_'])
    for i in f.readlines():
        if i=='\n':
            sentences.append(sentence)
            sentence = []
            sentence.append([0,'Root','__NULL__','root_POS','_','_',-1,'__NULL__','_','_'])
            continue
        word=[]
        j=i.split('\t')
        word.append(int(j[0])) #num
        [word.append(j[k]) for k in range(1,6)]
        try:
            word.append(int(j[6]))  #head num
        except ValueError:
            word.append(j[6])  #read blind file, head = '_'
        else:
            pass
        [word.append(j[k]) for k in range(7,10)]
        sentence.append(word)
    f.close()
    return sentences #sentences: [sentence[ token[0-9] ] ]

### 2.evaluation UAS ########
def UAS(pred,gold):  # heads list of a sentence
    total_num=len(gold)
    correct=0
    for i in range(total_num):
        if pred[i]==gold[i]:
            correct+=1
    return correct/total_num

#### 3.write ########
def write(filename, sents ,heads): #sents:list. #filename=sys.path[0] + '\\treebank\english\my_pred\\test.txt'
    print('Begin writing')
    temp = sys.stdout
    f = open(filename, 'w', encoding="utf8")
    sys.stdout = f

    for i in range(len(sents)):
        for j in range(1, len(sents[i])):
            if j == 1 and i != 0:
                print()
            k = sents[i][j]
            print(k[0], '\t', k[1], '\t', k[2], '\t', k[3], '\t','_','\t', k[5],'\t', heads[i][j], '\t',k[7],'\t', '_','\t', '_')

    sys.stdout = temp
    print('End writing.')
    f.close()

if __name__ == '__main__':
    #check test result file format
    filename_train = sys.path[0] + '\\Li_Lin_eng_test_pred.txt'
    sents_train = read(filename_train)
    for i in range(2):   # go through all sentences in corpus
        print('english,',i)
        s_train = Sentence(sents_train, i)  # a sentence in all sentences
        print(s_train.tokens,s_train.tokens_pos,s_train.tokens_lemma,s_train.tokens_morph,s_train.tokens_head)

    filename_train = sys.path[0] + '\\Li_Lin_ger_test_pred.txt'
    sents_train = read(filename_train)
    for i in range(10):   # go through all sentences in corpus
        print('germany,',i)
        s_train = Sentence(sents_train, i)  # a sentence in all sentences
        print(s_train.tokens,s_train.tokens_pos,s_train.tokens_lemma,s_train.tokens_head)
        #print(s_train.tokens_morph)













