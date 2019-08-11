# http://andybromberg.com/sentiment-analysis-python/
# Andy Bromberg's Simple Sentiment Analysis System
# Uses data from Pang & Lee (2005)
# Uses a Naive Bayes Classifier Train the System
#  NB Updated 2016 for package changes around scores

import re, math, collections, os, sys
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import scores
from nltk.collocations import BigramCollocationFinder

#from nltk.corpus import stopwords

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def evaluate_features(feature_select):
    #reading pre-labeled input and splitting into lines
    negSentences = open("D:\\CSNL\\Text_Analysis\\Assignment9\\XLect10.Progs\\rt-polarity-neg.txt", 'r',encoding="utf8")
    posSentences = open("D:\\CSNL\\Text_Analysis\\Assignment9\\XLect10.Progs\\rt-polarity-pos.txt", 'r',encoding="utf8")
    negSentences = re.split(r'\n', negSentences.read())
    posSentences = re.split(r'\n', posSentences.read())
    posSentences = remove_stopwords(posSentences)
    negSentences = remove_stopwords(negSentences)
    #print(posSentences)
    posFeatures = []
    negFeatures = []
    # breaks up the sentences into lists of individual words
    # creates instance structures for classifier
    for i in posSentences:
        posWords = re.findall(r"[\w']+|[.,!?;]", i)
        posWords = [feature_select(posWords), 'pos']
        posFeatures.append(posWords)
    for i in negSentences:
        negWords = re.findall(r"[\w']+|[.,!?;]", i)
        negWords = [feature_select(negWords), 'neg']
        negFeatures.append(negWords)

    #print(posFeatures);
    print("\n")
    print("\n")
    print("\n")
    #print(negFeatures);
    #sys.exit();
    posCutoff = int(math.floor(len(posFeatures)*3/4))
    negCutoff = int(math.floor(len(negFeatures)*3/4))
    trainFeatures = posFeatures[:posCutoff] + negFeatures[:negCutoff]
    testFeatures = posFeatures[posCutoff:] + negFeatures[negCutoff:]

    #Runs the classifier on the testFeatures
    classifier = NaiveBayesClassifier.train(trainFeatures)
    
    #Sets up labels to look at output
    referenceSets = collections.defaultdict(set)
    testSets = collections.defaultdict(set)
    for i, (features, label) in enumerate(testFeatures): # enumerate adds number-count to each item
        referenceSets[label].add(i)               # recorded polarity for these test sentences
        predicted = classifier.classify(features) # classifiers' proposed polarity for tests
        testSets[predicted].add(i)

    #Outputs
    print('train on %s instances, test on %s instances'% (len(trainFeatures), len(testFeatures)))
    print('accuracy:', nltk.classify.util.accuracy(classifier, testFeatures))
    print('pos precision:', scores.precision(referenceSets['pos'], testSets['pos']))
    print('pos recall:', scores.recall(referenceSets['pos'], testSets['pos']))
    print('neg precision:', scores.precision(referenceSets['neg'], testSets['neg']))
    print('neg recall:', scores.recall(referenceSets['neg'], testSets['neg']))
    classifier.show_most_informative_features(10)


def remove_stopwords(tokens):
    stopwords = open("D:\\CSNL\\Text_Analysis\\Assignment9\\XLect10.Progs\\stopwords.txt", 'r', encoding='utf8')
    stopwords = re.split(r'\n', stopwords.read())
    print(stopwords)
    stop = set(stopwords)
    list_of_words = [w.lower() for w in tokens if w.lower() not in stop]
    return list_of_words

def dict_with_bigrams(words):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(1) #Change the frequency here
    scored = finder.score_ngrams(bigram_measures.pmi)
    words.extend(sorted(bigram for bigram, score in scored)[:10])
    return dict([(word, True) for word in words])

def dict_without_stopwords(words):
    temp_words = remove_stopwords(words)
    return dict([(word, True) for word in temp_words])


def make_full_dict(words):
    return dict([(word, True) for word in words])

print('using all words as features')
evaluate_features(make_full_dict)

print('using all words without stopwords as features')
#evaluate_features(dict_without_stopwords)

print('using all words with bigrams as features')
#evaluate_features(dict_with_bigrams)
