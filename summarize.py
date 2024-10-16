import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, summary_ratio=0.2):
    # Tokenize sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Remove stop words and punctuation
    stop_words = set(stopwords.words("english") + list(string.punctuation))
    words_filtered = [word for word in words if word not in stop_words]

    # Calculate word frequencies
    word_frequencies = {}
    for word in words_filtered:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    # Calculate sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_frequencies[word]
                else:
                    sentence_scores[sentence] = word_frequencies[word]

    # Sort sentences by score
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    # Select the top sentences based on the summary ratio
    summary_length = int(len(sentences) * summary_ratio)
    summary = ' '.join(ranked_sentences[:summary_length])

    return summary

if __name__ == "__main__":
    text = input("Enter the text you want to summarize:\n")
    summary = summarize_text(text)
    print("\nSummary:\n", summary)
