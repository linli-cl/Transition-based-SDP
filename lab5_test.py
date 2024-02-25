
def turn_features(features_all,a_features): #a_features:a list
    features_vector=[]
    for i in a_features:
        if i in features_all:
            num=features_all[i]
            features_vector.append(num-1)
    return features_vector

def get_best_transition(features_vector,w):
    scores=[0,0,0]
    for i in features_vector:
        scores[0] += w[0][i] #shift
        scores[1] += w[1][i] #la
        scores[2] += w[2][i] #ra
    m=max(scores)
    t=scores.index(m)
    return t

