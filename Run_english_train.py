from lab1_read import Sentence,read,UAS,write
from lab2_decorder import State,oracle_parse,not_terminal,apply_tran
from lab3_features_extraction import FeatureMapping
from lab4_perceptron import Instance,train_perceptron
from lab5_test import turn_features,get_best_transition

import sys
import copy
import _pickle as cPickle
import gzip

###----- PART 1: read file-----
#1.train dates:
filename_train = sys.path[0] + '/treebank/english/train/wsj_train.only-projective.conll06'
sents_train = read(filename_train)


###----- PART 2: Decoder and Extract Features( use train dates ) -----
num_sentences = len(sents_train)
train_data_all_f = FeatureMapping() #get the corpus's features dic
features_tran_pairs_all_sentences = []  #get all sentences' <features, trans> list in the corpus

#1.get the corpus's  features dic &  <features,tran> of all sentences
flag=num_sentences  #print and show the extraction progress
for i in range(len(sents_train)):   # go through all sentences in corpus
    s_train = Sentence(sents_train, i)  # a sentence in all sentences
    start = [[0], list(range(1, len(s_train.tokens))), [-1] * len(s_train.tokens)]  #initialize
    start_c = State(start)
    start_c_oracle = copy.deepcopy(start_c.state)
    sentence_gold_head_oracle = copy.deepcopy(s_train.tokens_head)
    s_gold_seq, s_gold_c_set = oracle_parse(start_c_oracle, sentence_gold_head_oracle)
                                #get a sentence's  transitions sequence list & all configurations

    features_tran_pairs_one_sentence = []
    for each_c in range(len(s_gold_seq)):  # each configuration # len(seq)+1 = len(configurations)
        features_tran_pairs_str_list=train_data_all_f.extract_feature(s_gold_c_set[each_c],
                                s_train.tokens,s_train.tokens_lemma,s_train.tokens_pos,s_train.tokens_morph)
        features_tran_pairs_str_list.append(s_gold_seq[each_c]) #s_gold_seq[each_c]: a transition
        features_tran_pairs_one_sentence.append(features_tran_pairs_str_list)  #all configurations in one sentences
    features_tran_pairs_all_sentences.append(features_tran_pairs_one_sentence) #all sentences in train corpus
    flag -= 1
    print('features extraction progress:',flag) #print and show the extraction progress

###----- PART 3: Perceptron training -----
#1.instance
train_instances_features_all=Instance(train_data_all_f.features_dic)
train_instances_features_all.get_instances(features_tran_pairs_all_sentences)
#2.perceptron
f_len=len(train_data_all_f.features_dic) #to initialize weight
weights=train_perceptron(10,train_instances_features_all.instances,f_len) #perceptron train
#3.save a model
file_write_model = '/english_model.txt'
filepath_write_model = sys.path[0]  + file_write_model
stream=gzip.open(filepath_write_model,'wb')
cPickle.dump(train_data_all_f.features_dic, stream, -1)
cPickle.dump(weights, stream, -1)
stream.close()


###----- PART 4: Testing and Evaluate ( use dev dates )-----
#1.read a model
file_read_model = '/english_model.txt'
filepath_read_model = sys.path[0]  + file_write_model
stream=gzip.open(filepath_read_model, 'rb')
features_map=cPickle.load(stream)
weights=cPickle.load(stream)
stream.close()

#2.testing
#1).read test dates:
filename_blind=sys.path[0]+'/treebank/english/dev/wsj_dev.conll06.blind'
sents_test = read(filename_blind)
#2).read evaluate dates:
filename_gold = sys.path[0] + '/treebank/english/dev/wsj_dev.conll06.gold'
sents_gold = read(filename_gold)
#3).parse
num_sentences=len(sents_test)
heads_list_all=[]  #all the heads list got from test result, len=num_sentences
for i in range(num_sentences): #range(len(sents_gold)):  # a sentence in all sentences   #input: all sentences
    s_test = Sentence(sents_test, i)
    start = [[0], list(range(1, len(s_test.tokens))), [-1] * len(s_test.tokens)]
    start_c = State(start)
    the_state = copy.deepcopy(start_c.state)
    while not_terminal(the_state):
        extractd_state=FeatureMapping()
        state_features_str_list =extractd_state.extract_feature(
                        the_state,s_test.tokens,s_test.tokens_lemma,s_test.tokens_pos,s_test.tokens_morph)
        state_features_vector=turn_features(features_map,state_features_str_list)  #
        best_tran=get_best_transition(state_features_vector,weights)  #
        the_state=apply_tran(the_state,best_tran)
    heads_list_all.append(the_state[2]) #get test dates all sentences' head sequences
#4).UAS score:
uas = 0
for i in range(num_sentences):
    s_gold = Sentence(sents_gold, i)
    print(heads_list_all[i],s_gold.tokens_head)
    uas += UAS(heads_list_all[i],s_gold.tokens_head)
uas_result = "%.2f%%" % ( uas/num_sentences * 100)
print(uas_result)

#5).write
file_write_conll06 = '/result_english_dev_pred.txt'
filepath_write_conll06= sys.path[0] + file_write_conll06
write(filepath_write_conll06,sents_test,heads_list_all)
