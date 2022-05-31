import nltk
import string
import pandas as pd

class CoursesCleaner:
    def __init__(self, database):
        self.courses = database.get_courses()
        self.ps = nltk.PorterStemmer()
        self.wn = nltk.WordNetLemmatizer()
        self.stopwords = self.define_stopwords()
        self.courses["CleanDescription"] = self.courses['Description'].apply(lambda x: self.process_description(x))

    def get_courses(self):
        return self.courses

    @staticmethod
    def define_stopwords():
        stopwords = ["understand", "program", "student", "case", "week", "explanation", "course", "exposition",
                     "concept", "study", "interactive", "exposure", "example", "description", "discipline",
                     "demonstration", "presentation", "discussion", "conversation", "dialogue", "debate", "didactical"]
        stopwords.extend(nltk.corpus.stopwords.words('english'))
        return stopwords

    def process_description(self, description):
        # Tokenization
        description = description.split()

        processed_description = []
        for element in description:
            # Remove punctuation
            word = "".join([char for char in element if char not in string.punctuation])

            # Convert to lowercase letters
            word = word.lower()

            # Remove predefined stopwords and words with less than two characters
            if word not in self.stopwords and len(word) >= 2:
                processed_description.append(word)

        # Stemming
        processed_description = [self.ps.stem(word) for word in processed_description]

        # Lemmatization
        processed_description = [self.wn.lemmatize(word) for word in processed_description]

        # Create a string of the filtered words separated by space
        processed_description = ' '.join(processed_description)

        return processed_description
