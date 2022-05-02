import requests
from bs4 import BeautifulSoup
import io
import configparser
import pandas as pd
import fitz

def info(pdf_path):
    path = "https://www.cs.ubbcluj.ro" + pdf_path
    response = requests.get(path)

    filestream = io.BytesIO(response.content)
    pdf = fitz.open(stream=filestream, filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    ' '.join(text.split()) # remove multiple whitespace
    return text

def parse_pdf():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "compulsory_courses").split(",")
    courses.extend(parser.get("config", "elective_courses").split(","))
    file = parser.get("config", "courses")

    url = "https://www.cs.ubbcluj.ro/apps/fise/viewSyllabi.php?an=2021&lang=en&specializare=IE"
    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")

    list_of_pdf = []
    p = soup.find_all('a')

    for link in p:
        pdf_link = link.get('href')
        if link.contents[0] in courses and "MLR" not in pdf_link: # avoid Romanian taught class
            list_of_pdf.append([link.contents[0], pdf_link])

    df = pd.read_excel(file)
    for course, link in list_of_pdf:
        content = info(link)
        df.at[df["Name"] == course, "Description"] = content
        df.to_excel(file, index=False)

parse_pdf()