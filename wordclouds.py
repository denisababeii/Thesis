from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import  numpy as np
from PIL import Image
from coursesCleaner import CoursesCleaner

# Read data
df = CoursesCleaner().get_courses()

# Tokenize a sentence and convert each word to lower case
for val in df.CleanDescription: 
    words = '' 
    val = str(val) 
    tokens = val.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    words += " ".join(tokens)+" "

    pic = np.array(Image.open("cloud.png"))
    wordcloud = WordCloud(width = 500, height = 500, 
                    background_color ='white', 
                    mask = pic, 
                    min_font_size = 7).generate(words)

    plt.figure(figsize = (10, 10), facecolor = 'white', edgecolor='blue') 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    
    plt.show()