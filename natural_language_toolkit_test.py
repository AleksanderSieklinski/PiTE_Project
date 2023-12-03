import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analize(sentence):
    print("\n{0}".format(sentence), end='')
    result = SentimentIntensityAnalyzer().polarity_scores(sentence)
    for k in sorted(result):
        if   k == 'neg':
            print('Negative: {0}, '.format(result[k]), end='')
        elif k == 'neu':
            print('Neutral:  {0}, '.format(result[k]), end='')
        elif k == 'pos':
            print('Positive: {0}  '.format(result[k]), end='')
        else:
            print('{0}: {1}, '.format(k, result[k]), end='')
    print()
    return result['compound'], result['neg'], result['neu'], result['pos']

def open_file(sentences):
    sentences_tab = []
    try:
        with open(sentences) as f:
            for line in f:
                sentences_tab.append(line)
        return sentences_tab
    except FileNotFoundError:
        print("File not found")
        exit(1)

if __name__ == '__main__':
    nltk.download('vader_lexicon')
    sentences = open_file("sentences.txt")
    positive, negative, neutral, compound = [], [], [], []
    for sentence in sentences:
        comp, neg, neu, pos = analize(sentence)
        positive.append(pos)
        negative.append(neg)
        neutral.append(neu)
        compound.append(comp)
    # save results in file
    with open('results.txt', 'w') as file:
        file.write("Positive: {0}\n".format(positive))
        file.write("Negative: {0}\n".format(negative))
        file.write("Neutral: {0}\n".format(neutral))
        file.write("Compound: {0}\n".format(compound))