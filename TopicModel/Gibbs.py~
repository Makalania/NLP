import sys
import random
import math
file = sys.argv[1]
inputs = open(file)
alpha = 0.5
theta = 5
Dtw = {}
Ddt = {}
Ddw = {}
Dto = [0]*50
Dw = {}
Ndo = 1000
N = 50
def main():
    wordNumber = 0
    articleNumber = -1
    for line in inputs:
        array = line.split()
        if line[0] != " " and line!="\n":
            number = array[0]
            wordNumber += int(number)
            articleNumber +=1

        elif len(array) >= 1:
            for i in range(len(array)):
                word = array[i]
                topic = random.randint(0,49)

                if Dw.has_key(word):
                    Dw[word]+=1
                else:
                    Dw[word]=1
                
                if Dtw.has_key(word):
                    Dtw[word][topic]+=1
                else:
                    Dtw[word] = [0]*50
                    Dtw[word][topic] = 1

                Dto[topic]+=1
                    
                if Ddt.has_key(articleNumber):
                    Ddt[articleNumber][topic]=Ddt[articleNumber][topic]+1
                    Ddt[articleNumber][50]+=1
                else:
                    Ddt[articleNumber]=[0]*51
                    Ddt[articleNumber][topic]=1
                    Ddt[articleNumber][50]+=1
                    
                if Ddw.has_key(articleNumber):
                    Ddw[articleNumber].append((word,topic))
                else:
                    Ddw[articleNumber]=[(word,topic)]
    score0 = 1.0
    score1 = 1000.0
    
   # while(abs((score1-score0)/score0)>0.001):
    for i in range(0,10):
        score0 = score1
        score1 = process(len(Dw))
    print score1

    prob = probArticle(16)
    print prob

    words = probWords(15)
    print words

    
def process(wordNum):
    for i in range(0,1000):
        for j in range(0,len(Ddw[i])):
            word = Ddw[i][j][0]
            article = i
            oldTopic = Ddw[article][j][1]
            Dtw[word][oldTopic]-=1
            Dto[oldTopic]-=1
            Ddt[article][oldTopic]-=1
            Ddt[article][50]-=1
            prob = [0]*50
            for t in range(0,50):
                topic = t
                ntw = Dtw[word][topic]
                nto = Dto[topic]
                ndt = Ddt[article][topic]
                ndo = Ddt[article][50]
                ptd = (ndt+alpha)/(ndo+N*alpha)
                pwt = (ntw+alpha)/(nto+wordNum*alpha)
                pwd = ptd*pwt
                prob[topic]=pwd
            for n in range(1,50):
                prob[n] +=prob[n-1]
            for n in range(0,50):
                prob[n] = prob[n]*10000000
            newRan = random.randint(0,int(prob[-1]))
            newTopic = 49
            for n in range(0,50):
                if newRan <= prob[n]:
                    newTopic = n
                    break                
            Ddw[article][j]=(word,newTopic)
            Dtw[word][newTopic]+=1
            Dto[newTopic]+=1
            Ddt[article][newTopic]+=1
            Ddt[article][50]+=1
            
    ###calcuate convergence                
    pc = 0.0
    for d in range(0,1000):

        pwL = 0.0        
        for i in range(0,len(Ddw[d])):
            
            ptdpwt = 0.0
            for t in range(0,50):
                ndt = Ddt[d][t]
                ndo = Ddt[d][50]
                ele = Ddw[d][i]
                word = ele[0]
                ntw = Dtw[word][t]
                nto = Dto[t]
                ptd = (ndt+alpha)/(ndo+N*alpha)
                pwt = (ntw+alpha)/(nto+wordNum*alpha)
                ptdpwt = ptdpwt + (ptd*pwt)

            pwL = pwL + math.log(ptdpwt)
        pc = pc + (pwL)
            
        
    return pc            

def probArticle(article):
    ndo = Ddt[article][50]
    result = []
    for i in range(0,50):
        topic = i
        ndt = Ddt[article][topic]
        ptd = (ndt+alpha)/(ndo+N*alpha)
        result.append(ptd)
    return result


def probWords(number):
    
    result = [0 for j in range(50)]
    for i in range(0,50):
        topic = i
        temp = []
        for word in Dtw:
            ntw = Dtw[word][topic]
            now = Dw[word]
            ptw = float((ntw+theta))/float((now+N*theta))
            temp.append((ptw,word))
        temp.sort(key=lambda x:x[0], reverse=True)
        temp = temp[:15]
        result[i]=temp
    return result
        
if __name__ == '__main__':
	main()
