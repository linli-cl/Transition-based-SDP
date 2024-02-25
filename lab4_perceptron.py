import sys

def train_perceptron(epochs,instances,f_len):
    w=[[0]*f_len,[0]*f_len,[0]*f_len]  #shift, la, ta
    for i in range(epochs):
        total=0
        correct=0
        for inst in instances:  #a sentence
            for xy in inst:  #a configuration
                total += 1
                y_correct=xy[-1]
                x=xy[0:-1]
                score0,score1,score2=0,0,0
                if x != []:
                    for value_f in x:  # the value of the feature in all features{}
                        num_f = value_f - 1  #need minus 1, because the index of first feature is 0 in list
                        score0 += w[0][num_f]  # shift
                        score1 += w[1][num_f]  # la
                        score2 += w[2][num_f]  # ra
                else:
                    pass
                score_list=[score0,score1,score2]
                m=max(score_list)
                #print(score_list,m,y_correct)
                y_pred=score_list.index(m)  #pred transition
                if y_pred==y_correct:
                    correct += 1
                else:
                    for value_f in x:
                        numf = value_f - 1  #need minus 1, because the index of first feature is 0 in list
                        w[y_correct][numf] += 1
                        w[y_pred][numf] -= 1
            # if total % 500 == 0:
            #     accuracy= correct/total
            #     print('total:',total,'accuracy:',accuracy)
        accuracy= correct/total
        print('epoches:', i, 'total:', total, 'accuracy:', accuracy)
    return w


class Instance:
    #label: int  #correct label transitions
    #feats: dict[int, int]  #sparse representation
    def __init__(self,features,):
        self.features_all=features  #dict {}
        #self.ins_f_t_pairs_all=feature_tran_pairs_all_sentences
        self.instances=[] #<vec,t> of all configurations of a sentences of all sentences


    def get_instances(self,feature_tran_pairs_all_sentences):  #all sentences
        for pairs in feature_tran_pairs_all_sentences: # a sentences
            vector_one_sentence=[]
            for a_pair in pairs: # a configuration
                vector_one_c=[]
                #1. map features to value
                fs = a_pair[0:-1] #features of this configuration
                if fs!=[]:
                    for f in fs:  # a feature in a configuration
                        if f in self.features_all:
                            f_val= self.features_all[f]  #the num of this feature in all features
                            vector_one_c.append(f_val)
                        else:
                            pass
                else:
                    pass
                # 2. map transition label to integer  [shift:0, la:1, ra:2]
                t_str=a_pair[-1]  #tran of this configuration
                if t_str=='SHIFT':
                    t=0
                elif t_str=='LA':
                    t=1
                else:  #t_str=='RA'
                    t=2
                vector_one_c.append(t)
                vector_one_sentence.append(vector_one_c)
            self.instances.append(vector_one_sentence)