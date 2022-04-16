import nltk
import string
import pandas as pd
import configparser

# nltk.download('stopwords')
# nltk.download('words')
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download('wordnet')

class CoursesCleaner:
    def __init__(self):
        self.courses = pd.read_csv(self.get_file(), encoding='cp1252')
        self.ps = nltk.PorterStemmer()
        self.wn = nltk.WordNetLemmatizer()
        self.words = set(nltk.corpus.words.words())
        self.stopwords = self.define_stopwords()
        self.courses["CleanDescription"] = self.courses['Description'].apply(lambda x: self.process_description(x))

    def get_courses(self):
        return self.courses

    def get_file(self):
        parser = configparser.ConfigParser()
        parser.read("config.txt")
        return parser.get("config", "courses")

    @staticmethod
    def define_stopwords():
        stopwords = ["understand", "program", "student", "case", "week", "explanation", "course", "exposition",
                     "concept", "study", "interactive", "exposure", "example", "description", "discipline",
                     "demonstration", "presentation", "discussion", "conversation", "dialogue", "debate", "didactical"]
        stopwords.extend(nltk.corpus.stopwords.words('english'))
        return stopwords

    def process_description(self, description):
        description = description.split()
        clean_description = []
        for desc in description:
            d = "".join([char for char in desc if char not in string.punctuation])  # remove punctuations
            d = d.lower()  # converting to lowercase letters
            d = ' '.join([word for word in d.split() if word not in self.stopwords])  # remove stopwords
            d = ' '.join([word for word in d.split() if len(word) >= 2])
            clean_description.append(d)

        clean_description = ' '.join(clean_description)

        # Tokenization
        processed_description = nltk.word_tokenize(clean_description)

        # Stemming
        processed_description = [self.ps.stem(word) for word in processed_description]

        # Lemmatization
        processed_description = [self.wn.lemmatize(word) for word in processed_description]

        processed_description = [word for word in processed_description if len(word) >= 2]

        processed_description = ' '.join(w for w in processed_description if w in self.words)

        return processed_description
