from lab1_read import Sentence,read, write
from lab2_decorder import State, not_terminal,apply_tran
from lab3_features_extraction import FeatureMapping
from lab5_test import turn_features,get_best_transition

import sys
import copy
import _pickle as cPickle
import gzip

###1.read a model
file_read_model = '/german_model.txt'
filepath_read_model = sys.path[0] + file_read_model
stream=gzip.open(filepath_read_model, 'rb')
features_map=cPickle.load(stream)
weights=cPickle.load(stream)
stream.close()

###2.testing
#1).read test file:
filename_blind=sys.path[0]+'/treebank/german/test/tiger-2.2.test.conll06.blind'
sents_test = read(filename_blind)

#2).parse
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

#3)write
file_write_conll06 = '/result_ger_test_pred.txt'
filepath_write_conll06= sys.path[0] + file_write_conll06

write(filepath_write_conll06,sents_test,heads_list_all)


