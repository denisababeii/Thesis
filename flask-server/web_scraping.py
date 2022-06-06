import requests
from bs4 import BeautifulSoup
import io
import configparser
import pandas as pd
import fitz

def info(path):
    # Access the PDF through an HTTP request
    response = requests.get(path)
    # Save the content of the PDF as a byte stream
    filestream = io.BytesIO(response.content)
    # Use the PyMuPDF library (with the import name ’fitz’) to transform the byte stream to text
    pdf = fitz.open(stream=filestream, filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    # Remove multiple white spaces
    ' '.join(text.split())
    return text

def parse_pdf():
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    courses = parser.get("config", "compulsory_courses").split(",")
    courses.extend(parser.get("config", "elective_courses").split(","))
    file = parser.get("config", "courses")

    # Extract the information from the syllabi web page and transform it into a tree of Python objects using Beautiful Soup
    url = "https://www.cs.ubbcluj.ro/apps/fise/viewSyllabi.php?an=2021&lang=en&specializare=IE"
    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the URLs in the page by extracting the ’a’ tagged objects
    list_of_pdf = []
    p = soup.find_all('a')

    for link in p:
        pdf_link = link.get('href')
        # Select only the relevant URLs
        if link.contents[0] in courses and "MLR" not in pdf_link: # avoid Romanian taught class
            list_of_pdf.append([link.contents[0], pdf_link])

    # Store Excel data in a Dataframe object
    df = pd.read_excel(file)
    for course, link in list_of_pdf:
        path = "https://www.cs.ubbcluj.ro" + link
        # Extract text from PDF file
        content = info(path)
        # Insert the text content of the PDF in the DataFrame object
        df.at[df["Name"] == course, "Description"] = content
        # Insert the link of the PDF in the DataFrame object
        df.at[df["Name"] == course, "Link"] = path
        # Write the modified DataFrame object to the Excel file
        df.to_excel(file, index=False)

parse_pdf()