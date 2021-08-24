# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import os
import re as regexp

# function to extract median pay from a string
def return_pay(input_text):
    curr = regexp.findall('\s([\$]\d+([\.,]\d{3}?))', input_text)
    for items in curr:
        return items[0]

# function to remove html tags and extract the text content
def return_text(html_string):
    regex = regexp.compile('<.*?>')
    text_string = regexp.sub(regex, '', html_string)
    return text_string

# function to process input text data and output a list of words
def process_data(documents, input_data):
    documents = []
    stemmer = WordNetLemmatizer()
    X = input_data
    for sen in X.split("."):
        # Remove special chars
        document = regexp.sub(r'\W', ' ', str(sen))
        # remove single chars
        document = regexp.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove single chars from the start
        document = regexp.sub(r'\^[a-zA-Z]\s+', ' ', document) 
        # replace spaces with single space
        document = regexp.sub(r'\s+', ' ', document, flags=regexp.I)
        # Remove prefixed 'b' for byte data
        document = regexp.sub(r'^b\s+', '', document)
        # Lowercase
        document = document.lower()
        # Lemmatization
        document = document.split()
        document = [stemmer.lemmatize(word) for word in document]
        #document = ' '.join(document)
        documents.extend(document)
        documents = [word for word in documents if word != 'nbsp']
    return documents


# function takes v6 xml file and outputs a pipe delimited flat file
def parse_xml(xml_file):
    # Parses XML section into an element tree incrementally
    # Parameters are filename or file object containing XML data. sequence of events
    doc = ET.iterparse(xml_file)#, events=('start', 'end'))

    # create header and open text file to write the data elements in pipe delimited format
    header = 'Title|Description|Median_Pay|Growth|Decline|What_They_Do|Work_Environment|How_To_Become|Job_Outlook_Tab|'
    header = header + 'Pay1|Entrylevel|Workexp|Onjobtrain|Numjobs|Joboutlook|Trend|Jobopenings\n'
    
    with open('OOH_Job_Data.txt', 'w') as f:
        f.write(header)    
    newline = ''

    # Loop thru the elements along with the event (start or end)
    for event, element in doc:
        title = ''
        descr = ''
        pay = ''
        wtd = ''
        workenv = ''
        htb = ''
        jout = ''
        # For getting a fully populated element, check for “end” event
        if event == 'end' and element.tag == "occupation": # Total 324 occupations
            for records in element:
                #Summary (Median Pay, Number of Jobs, Job Outlook)\
                #print(records.tag+': ', records.text)
                if records.tag == 'title':
                    title = records.text
                
                if records.tag == 'description':
                    descr = (records.text).strip()
                
                if records.tag == 'summary_pay':
                    pay = return_pay(records.text) # median pay
                
                if records.tag == 'summary_outlook':
                    #print('Summary_Outlook: ', return_text(records.text.replace('&nbsp;',' ')))
                    grow = regexp.findall("grow (\d+)", records.text.replace('&nbsp;',' '))
                    decl = regexp.findall(r"decline (\d+)", records.text.replace('&nbsp;',' '))
                    g = 0
                    d = 0
                    for item in grow:
                        g = item
                    for item in decl:
                        d = item
                    
                if records.tag == 'what_they_do':
                    for subrecs1 in records:
                        #print(subrecs1.tag) # section_title, section_image, section_body
                        if subrecs1.tag == 'section_body':
                            wtd = return_text(subrecs1.text)
                            documents = []
                            wtd = process_data(documents, wtd)

                if records.tag == 'work_environment':
                    for subrecs2 in records:
                        #print(subrecs2.tag) # section_title, section_image, section_body
                        if subrecs2.tag == 'section_body':
                            workenv = return_text(subrecs2.text)
                            documents = []
                            workenv = process_data(documents, workenv)

                if records.tag == 'how_to_become_one':
                    for subrecs3 in records:
                        #print(subrecs3.tag) # section_title, section_image, section_body
                        if subrecs3.tag == 'section_body':
                            htb = return_text(subrecs3.text)
                            documents = []
                            htb = process_data(documents, htb)

                if records.tag == 'job_outlook':
                    for subrecs4 in records: 
                        #print(subrecs4.tag) # section_title, section_body, section_chart,section_datatable
                        if subrecs4.tag == 'section_body':
                            jout = return_text(subrecs4.text)
                            documents = []
                            jout = process_data(documents, jout)

                if records.tag == 'quick_facts':
                    for subrecs5 in records:
                        if subrecs5.tag == 'qf_median_pay_annual':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    pay1 = subrecs.text
                        if subrecs5.tag == 'qf_entry_level_education':
                            for subrecs in subrecs5:
                                 if subrecs.tag == 'value':
                                    entrylevel = subrecs.text
                        if subrecs5.tag == 'qf_work_experience':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    workexp = subrecs.text
                        if subrecs5.tag == 'qf_on_the_job_training':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    onjobtrain = subrecs.text
                        if subrecs5.tag == 'qf_number_of_jobs':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    numjobs = subrecs.text
                        if subrecs5.tag == 'qf_employment_outlook':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    joboutlook = subrecs.text
                                elif subrecs.tag == 'description':
                                    trend = subrecs.text
                        if subrecs5.tag == 'qf_employment_openings':
                            for subrecs in subrecs5:
                                if subrecs.tag == 'value':
                                    jobopenings = subrecs.text
                                
            newline = title + '|' + descr + '|' + str(pay) + '|' + str(g) + '|' + str(d) + '|' + str(wtd) + '|' 
            newline = newline + str(workenv) + '|' + str(htb) + '|' + str(jout) + '|' 
            newline = newline + str(pay1) + '|' + str(entrylevel) + '|' + str(workexp) + '|' + str(onjobtrain) + '|' 
            newline = newline + str(numjobs) + '|' + str(joboutlook) + '|' + str(trend) + '|' + str(jobopenings) + '\n'
            
            with open('OOH_Job_Data.txt', 'a', encoding="utf-8") as f:
                f.write(newline)
#=============================================================================================

path = r"C:\5_UMSI_MADS\SIADS 697 & 698 Capstone"
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    parse_xml(fullname)
    print(fullname)






















