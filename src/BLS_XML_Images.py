# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import re as regexp

# function to remove html tags and extract the text content
def return_text(html_string):
    regex = regexp.compile('src\s*=\s*"(.+?)"')
    text_string = regexp.search(regex,html_string)
    return ("https://www.bls.gov" + str(text_string[1]))

# function to remove html tags and extract the text content
def return_text1(html_string):
    regex = regexp.compile('<.*?>')
    text_string = regexp.sub(regex, '', html_string)
    return text_string

# function takes v6 xml file and outputs a pipe delimited flat file
def parse_xml(xml_file):
    # Parses XML section into an element tree incrementally
    # Parameters are filename or file object containing XML data. sequence of events
    doc = ET.iterparse(xml_file)#, events=('start', 'end'))

    # create header and open text file to write the data elements in pipe delimited format
    header = 'Title|Image_1|Image_2|Image_3|Image_4|Cap_2|Cap_3|Cap_4\n'
    
    with open('OOH_Image_Data_Captions.txt', 'w') as f:
        f.write(header)    
    newline = ''

    # Loop thru the elements along with the event (start or end)
    for event, element in doc:
        title = ''
        img1 = ''
        img2 = ''
        img3 = ''
        img4 = ''
        caption_2 = ''
        caption_3 = ''
        caption_4 = ''
        
        # For getting a fully populated element, check for “end” event
        if event == 'end' and element.tag == "occupation": # Total 324 occupations
            for records in element:
                #Summary (Median Pay, Number of Jobs, Job Outlook)\
                #print(records.tag+': ', records.text)
                if records.tag == 'title':
                    title = records.text
                
                if records.tag == 'image':
                    img1 = return_text(records.text)
                
                if records.tag == 'what_they_do':
                    for subrecs1 in records:
                        #print(subrecs1.tag) # section_title, section_image, section_body
                        if subrecs1.tag == 'section_image':
                            img2 = return_text(subrecs1.text)
                            caption_2 = return_text1(subrecs1.text).strip()

                if records.tag == 'work_environment':
                    for subrecs2 in records:
                        #print(subrecs2.tag) # section_title, section_image, section_body
                        if subrecs2.tag == 'section_image':
                            img3 = return_text(subrecs2.text)
                            caption_3 = return_text1(subrecs2.text).strip()

                if records.tag == 'how_to_become_one':
                    for subrecs3 in records:
                        #print(subrecs3.tag) # section_title, section_image, section_body
                        if subrecs3.tag == 'section_image':
                            img4 = return_text(subrecs3.text)
                            caption_4 = return_text1(subrecs3.text).strip()
                            
            newline = title + '|' + img1 + '|' + img2 + '|' + img3 + '|' + img4 + '|' + caption_2 + '|' + caption_3 + '|' + caption_4 + '\n'
            
            with open('OOH_Image_Data_Captions.txt', 'a', encoding="utf-8") as f:
                f.write(newline)
#=============================================================================================

path = r"C:\5_UMSI_MADS\SIADS 697 & 698 Capstone"
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    parse_xml(fullname)
    print(fullname)






















