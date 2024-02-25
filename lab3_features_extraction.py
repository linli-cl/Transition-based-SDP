
class FeatureMapping:  #one state
    def __init__(self):   #<c_set,seq>:all <c,t> pairs. #sentence: list of its tokens,pos,heads.
        self.features_dic={}

    def add_feature(self,str):
        if str not in self.features_dic:
            self.features_dic[str] = len(self.features_dic) + 1
        else:
            pass

    def get_right_most_pos(self,int,arcs,pos_list):
        if int in arcs:
            num=arcs.index(int)
            if num > int and num!= -1:
                ld_num=num
                return pos_list[ld_num]
            else:
                return '__NULL__'
        else:
            return '__NULL__'

    def get_left_most_pos(self,int,arcs,pos_list):
        if int in arcs:
            num=arcs[::-1].index(int) #reverse arcs list
            if num < int and num!= -1:
                rd_num=num
                return pos_list[rd_num]
            else:
                return '__NULL__'
        else:
            return '__NULL__'

    def extract_feature(self,a_state, token_list, lemma_list,pos_list,morph_list): #one sentence
        features=[]
        stack=a_state[0] #[stack]
        buffer=a_state[1] #[buffer]
        arcs=a_state[2]  #[prediced arcs]

        if stack == []:
            str1_s = 'S[-1]-form=__NULL__'
            str2_s = 'S[-1]-pos=__NULL__'
            lemma_s = 'S[-1]-lemma=__NULL__'
            morph_s= 'S[-1]-morph=__NULL__'
            str3_s = 'S[-2]-form=__NULL__'
            str4_s = 'S[-2]-pos=__NULL__'
        elif len(stack) == 1:
            int1_s = stack[0]
            str1_s = 'S[-1]-form=' + token_list[int1_s]
            str2_s = 'S[-1]-pos=' + pos_list[int1_s]
            lemma_s = 'S[-1]-lemma=' + lemma_list[int1_s]
            morph_s = 'S[-1]-morph='+ morph_list[int1_s]
            str3_s = 'S[-2]-form=__NULL__'
            str4_s = 'S[-2]-pos=__NULL__'
        else:
            int1_s = stack[-1]
            str1_s = 'S[-1]-form=' + token_list[int1_s]
            str2_s = 'S[-1]-pos=' + pos_list[int1_s]
            lemma_s = 'S[-1]-lemma=' + lemma_list[int1_s]
            morph_s = 'S[-1]-morph=' + morph_list[int1_s]
            int2_s = stack[-2]
            str3_s = 'S[-2]-form=' + token_list[int2_s]
            str4_s = 'S[-2]-pos=' + pos_list[int2_s]
        #str5_s = str1_s + str2_s #x
        str6_s = str3_s + str4_s

        if buffer == []:
            str1 = 'B[0]-form=__NULL__'
            str2 = 'B[0]-pos=__NULL__'
            lemma = 'B[0]-lemma=__NULL__'
            morph = 'B[0]-morph=__NULL__'
            str3 = 'B[1]-form=__NULL__'
            str4 = 'B[1]-pos=__NULL__'
            str5 = 'B[2]-form=__NULL__'
            str6 = 'B[2]-pos=__NULL__'
            str7 = 'B[3]-form=__NULL__'
            str8 = 'B[3]-pos=__NULL__'
        elif len(buffer) == 1:
            int1 = buffer[0]
            str1 = 'B[0]-form=' + token_list[int1]
            str2 = 'B[0]-pos=' + pos_list[int1]
            lemma = 'B[0]-lemma=' + lemma_list[int1]
            morph = 'B[0]-morph='+morph_list[int1]
            str3 = 'B[1]-form=__NULL__'
            str4 = 'B[1]-pos=__NULL__'
            str5 = 'B[2]-form=__NULL__'
            str6 = 'B[2]-pos=__NULL__'
            str7 = 'B[3]-form=__NULL__'
            str8 = 'B[3]-pos=__NULL__'
        elif len(buffer) == 2:
            int1 = buffer[0]
            str1 = 'B[0]-form=' + token_list[int1]
            str2 = 'B[0]-pos=' + pos_list[int1]
            lemma = 'B[0]-lemma=' + lemma_list[int1]
            morph = 'B[0]-morph='+morph_list[int1]
            int2 = buffer[1]
            str3 = 'B[1]-form=' + token_list[int2]
            str4 = 'B[1]-pos=' + pos_list[int2]
            str5 = 'B[2]-form=__NULL__'
            str6 = 'B[2]-pos=__NULL__'
            str7 = 'B[3]-form=__NULL__'
            str8 = 'B[3]-pos=__NULL__'
        elif len(buffer) == 3:
            int1 = buffer[0]
            str1 = 'B[0]-form=' + token_list[int1]
            str2 = 'B[0]-pos=' + pos_list[int1]
            lemma = 'B[0]-lemma=' + lemma_list[int1]
            morph = 'B[0]-morph='+morph_list[int1]
            int2 = buffer[1]
            str3 = 'B[1]-form=' + token_list[int2]
            str4 = 'B[1]-pos=' + pos_list[int2]
            int3 = buffer[2]
            str5 = 'B[2]-form=' + token_list[int3]
            str6 = 'B[2]-pos=' + token_list[int3]
            str7 = 'B[3]-form=__NULL__'
            str8 = 'B[3]-pos=__NULL__'
        else:
            int1 = buffer[0]
            str1 = 'B[0]-form=' + token_list[int1]
            str2 = 'B[0]-pos=' + pos_list[int1]
            lemma = 'B[0]-lemma=' + lemma_list[int1]
            morph = 'B[0]-morph='+morph_list[int1]
            int2 = buffer[1]
            str3 = 'B[1]-form=' + token_list[int2]
            str4 = 'B[1]-pos=' + pos_list[int2]
            int3 = buffer[2]
            str5 = 'B[2]-form=' + token_list[int3] #x
            str6 = 'B[2]-pos=' + token_list[int3]
            int4 = buffer[3]
            str7 = 'B[3]-form=' + token_list[int4] #x
            str8 = 'B[3]-pos=' + pos_list[int4]
        #str9 = str1 + str2  #x
        #str10 = str3 + str4 #x
        for f in [str1_s,str2_s,str3_s,str4_s,str1,str2,str3,str4,str5,str6,str7,str8]: #,str9,str10
            features.append(f)
            self.add_feature(f)
        for f in [lemma_s,morph_s,morph,lemma]: #lemma
            features.append(f)
            self.add_feature(f)

        # #bigram: two words pairs:
        str1_bi= str1_s+str2_s+str1+str2
        str2_bi= str1_s+str2_s+str1
        str3_bi= str1_s+str2_s+str2
        str4_bi= str1_s+str1+str2
        str5_bi= str2_s+str1
        str6_bi = str1_s + str1
        str7_bi= str2_s+str2
        str8_bi = str4_s + str2_s
        str10_bi = str1_s + str3_s
        str9_bi = str1 + str3
        for f in [str1_bi,str2_bi,str3_bi,str4_bi,str5_bi,str6_bi,str7_bi,str8_bi,str10_bi,str9_bi]:
            features.append(f)
            self.add_feature(f)

        #rd,ld:
        if stack!=[]:
            int1_s=stack[-1]
            stack_top_ld_pos=self.get_left_most_pos(int1_s,arcs,pos_list)
            stack_top_rd_pos = self.get_right_most_pos(int1_s, arcs,pos_list)
            str4_tri = str2_s + 'ld(S[-1]-pos)' + stack_top_ld_pos + str2 # x
            str5_tri = str2_s + 'rd(S[-1]-pos)' + stack_top_rd_pos + str2 # x
            for f in [str4_tri,str5_tri]: #[str4_tri,str5_tri] ld_s_pos,rd_s_pos,s1,
                features.append(f)
                self.add_feature(f)
        if buffer!=[]:
            int1=buffer[0]
            buffer_front_ld_pos=self.get_left_most_pos(int1,arcs,pos_list)
            buffer_front_rd_pos = self.get_right_most_pos(int1, arcs, pos_list)
            str6_tri= str2_s + str2 + 'ld(B[0]-pos)'+buffer_front_ld_pos
            for f in [str6_tri]:
                features.append(f)
                self.add_feature(f)
        if stack != [] and buffer!=[]:
            int1_s = stack[-1]
            b0 = buffer[0]
            distance='B[0]-S[-1]='+str(b0-int1_s)
            s2= str2_s + distance +str2
            s3 = str1_s + distance + str1
            s4 = str2_s + distance
            s5 = distance + str2
            s6 = str1_s + distance
            s7 = distance + str1
            for f in [s2,s3,s4,s7]: #s5,s6,
                features.append(f)
                self.add_feature(f)
        #trigram:
        str1_tri = str1_s + str1 + str3
        str2_tri = str2 +str4 + str6
        str3_tri = str4_s + str2_s + str2
        str4_tri = str6_s + str4_s +str2_s
        for f in [str1_tri,str2_tri,str3_tri,str4_tri]: #
            features.append(f)
            self.add_feature(f)

        return features


