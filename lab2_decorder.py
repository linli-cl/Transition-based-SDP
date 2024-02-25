import copy

class State:
    def __init__(self, c):  # c=[stack,buffer,arcs]
        self.state=c
        self.stack=c[0]
        self.buffer=c[1]
        self.heads=c[2]

#1. apply t
def apply_tran(state, t ): #state: c=[stack,buffer,arcs]
    if state[0]!=[]:
        i = state[0][-1]  # stack top
        j = state[1][0]  # buffer front
        if t=='LA' or t==1:
            del(state[0][-1])  #delete stack top
            state[2][i]=j  #j->i
        elif t=='RA' or t==2:
            del (state[0][-1]) #delete stack top
            state[1][0]=i  #buffer front change to i
            state[2][j] = i #i->j
        else:  #t=='SHIFT' or t==0
            state[0].append(j)
            del state[1][0]
    else:  # t=='SHIFT'
        state[0].append(state[1][0])
        del state[1][0]
    #print('apply_tran: ',t,state[0],' ',state[1],' ',state[2])
    return state


#2.oracle
def not_terminal(c):  #c=[stack,buffer,arcs]
    #print('terminal: ', c[1])
    if c[1]==[]:  #buffer is empty
        return False
    else:
        return True

def should_leftarc(c, arcs):  #c=[stack,buffer,arcs] # c: so far configuration state, arcs: correct_arcs
    if c[0]!=[]:
        i = c[0][-1]  # stack top
        j = c[1][0]  # buffer front
        if arcs[i]==j and i!=0:  # i is not root and stack is not empty
            return True
        else:
            return False
    else:
        return False

def should_rightarc(c, arcs):  # c: so far configuration state, arcs: correct_arcs
    if c[0]!=[]:
        i = c[0][-1]  # stack top
        j = c[1][0]  # buffer front
        if arcs[j]==i and has_all_children(j, c[2], arcs) and c[0][0]!=[]: #c[2]: a:set of so far predicted arcs
            return True
        else:
            return False
    else:
        return False

def has_all_children(buffer_front, a, arcs):  #a: set of so far predicted arcs
    arc_remain=arcs
    for i in range(1,len(arcs)):
        if a[i]==arcs[i]:  #Remove the heads of all the predicted words
            arc_remain[i] = -1
    if buffer_front not in arc_remain:  #If not as the head of the unpredicted word
        return True  #That means it has all children
    else:
        return False

def get_oracle_transitions(state,correct_arcs):
    if should_leftarc(state, correct_arcs):
        t = 'LA'
    elif should_rightarc(state, correct_arcs):
        t = 'RA'
    else:
        t = 'SHIFT'
    return t

def oracle_parse(start_state, correct_arcs): #c=[stack,buffer,arcs]  correct_arcs: list of heads sequence
    seq=[]
    c=start_state #start_state=[ [0],[1,2,...],[-1]*len ]
    c_set=[]
    c_set.append(copy.deepcopy(start_state) )
    while not_terminal(c): #c=[stack,buffer,arc]
        t=get_oracle_transitions(c,correct_arcs)
        c = apply_tran( c, t )
        temp_c=copy.deepcopy(c)
        c_set.append(temp_c)
        seq.append(t)
    return seq, c_set  # seq is the transitions sequences

def parse_seq_gettree(start_state, seq):
    c=start_state
    for t in seq:
        c=apply_tran(c,t)
    return c[2] #c[2] is c.A is the tree

