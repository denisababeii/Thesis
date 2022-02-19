import nltk
nltk.download('stopwords')
nltk.download('words')
nltk.download('omw-1.4')
import string
import pandas as pd

class CoursesCleaner:
    def __init__(self, file='COURSES.csv'):
        self.courses = pd.read_csv(file)
        self.ps = nltk.PorterStemmer()
        self.wn = nltk.WordNetLemmatizer()
        self.words = set(nltk.corpus.words.words())
        self.stopwords = self.define_stopwords()
        self.courses["CleanDescription"] = self.courses['Description'].apply(lambda x: self.process_description(x))

    def get_courses(self):
        return self.courses

    def define_stopwords(self):
        stopwords = ["understand", "program", "student", "case", "week", "explanation", "course", "exposition", "concept", "study", "interactive", "exposure", "example", "description", "discipline", "demonstration", "presentation", "discussion", "conversation", "dialogue", "debate", "didactical"]
        stopwords.extend(nltk.corpus.stopwords.words('english'))
        return stopwords

    def process_description(self, description):
        description = description.split()
        cleanDescription = []
        for desc in description:
            d = "".join([char for char in desc if char not in string.punctuation]) # remove punctuations
            d = d.lower() #converting to lowercase letters
            d = ' '.join([word for word in d.split() if word not in (self.stopwords)]) # remove stopwords
            d = ' '.join([word for word in d.split() if len(word) >= 2])
            cleanDescription.append(d)

        cleanDescription = ' '.join(cleanDescription)

        # Tokenization
        ProcessedDescription = nltk.word_tokenize(cleanDescription)
        
        # Stemming
        ProcessedDescription = [self.ps.stem(word) for word in ProcessedDescription]
        
        # lemmatization
        ProcessedDescription = [self.wn.lemmatize(word) for word in ProcessedDescription]
        
        ProcessedDescription = [word for word in ProcessedDescription if len(word) >= 2]

        ProcessedDescription = ' '.join(w for w in ProcessedDescription if w in self.words)
        
        return ProcessedDescription