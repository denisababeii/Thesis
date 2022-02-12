from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import  numpy as np
from PIL import Image

# Read data
df = pd.read_csv("COURSES.csv") 

# Filter out specific words without use to the analysis
stopwords = ["case", "weeks", "explanations", "course", "exposition", "concepts", "week", "studies", "interactive", "explanation", "exposure", "example", "examples", "description", "discipline", "demonstration", "presentation", "discussion", "conversation", "dialogue", "debate", "didactical"]
stopwords.extend(STOPWORDS)

# Tokenize a sentence and convert each word to lower case
for val in df.Description: 
    words = '' 
    val = str(val) 
    tokens = val.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    words += " ".join(tokens)+" "

    pic = np.array(Image.open("cloud.png"))
    wordcloud = WordCloud(width = 500, height = 500, 
                    background_color ='white', 
                    stopwords = stopwords, mask = pic, 
                    min_font_size = 7).generate(words)

    plt.figure(figsize = (10, 10), facecolor = 'white', edgecolor='blue') 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    
    plt.show()