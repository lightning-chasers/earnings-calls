#!/usr/bin/env python

import csv
import json
import os
import re
import sys
import traceback
from string import ascii_uppercase
from collections import OrderedDict
from glob import glob
from pprint import pprint

def subdivide(lines, regex):
    '''
    Subdivides a collection of lines based on the delimiting regular expression.
    example_string ='=============================
                    asdfasdfasdf
                    sdfasdfdfsdfsdf
                    =============================
                    asdfsdfasdfasd
                    ============================='
    
    subdivide(example_string, "={29}")
    >>> ['asdfasdfasdf\nsdfasdfdfsdfsdf\n', 'asdfsdfasdfasd\n']
    '''
    equ_pattern = re.compile(regex, re.MULTILINE)
    sections = equ_pattern.split(lines)
    sections = [section.strip() for section in sections]
    return sections

def process_dashed_sections(section):
    '''
    for processing sections with dashes in them, 
    returns the heading of the section along with a dictionary 
        where each key is the subsection's header, 
        and each value is the text in the subsection.
    '''
    
    subsections = subdivide(section, "-{80}")
    heading = subsections[0]  # header of the section.
    d = {key: value for key, value in zip(subsections[1::2], subsections[2::2])}
    
#     print(json.dumps(d, indent=4))
    
    index_pattern = re.compile("\[(\d+)\]", re.MULTILINE)
    def cmp(d):
        '''
        sort the dictionary by first capturing the pattern '[x]' 
        extract 'x' number.
        Then pass this as a key to 'sorted' to sort based on 'x'.
        '''
        mat = index_pattern.findall(d[0])
        if mat:
#             print(mat[0])
            return int(mat[0])
        else:
            # To deale with subsections containing '-'s but not containing '[x]'
            return 0

    o_d = OrderedDict(sorted(d.items(), key=cmp))
    return heading, o_d

def parse(txtFile):
    with open(txtFile, 'r') as tf:
        lines = tf.read()

        # regex pattern for matching headers of each section
        header_pattern = re.compile("^.*[^\n]", re.MULTILINE)

        # regex pattern for matching the sections that contains
        # the list of attendee's (those that start with asterisks )
        ppl_pattern = re.compile("^(\s*\*)(.+)(\s.*)", re.MULTILINE)

        # regex pattern for matching sections with subsections in them.
        dash_pattern = re.compile("-{80}", re.MULTILINE)

        talks_d = dict()
        # Step1. Divide document into sections by the '=' delimiter
        sections = subdivide(lines, "={80}")
        # print(sections)
        
        # Step2. Handle each section like a switch case
        header = []
        for section in sections:
            # Handle headers
            if len(section.split('\n')) == 1:  # likely to match only a header
                header = header_pattern.match(section).string.strip()

            # Handle attendees/authors
            elif ppl_pattern.match(section):
                ppls = ppl_pattern.findall(section)
                # print(ppls)
                
                ppl_d = dict()
                ppl_d = {key.strip(): value.strip() for asterisk, key, value in ppls}
                
                if header:
                    talks_d.update({header: ppl_d})

            # Divide sections into subsections by the '-' delimiter
            elif dash_pattern.findall(section):
                heading, d = process_dashed_sections(section)

                talks_d.update({heading: d})

            # Else its just some random text.
            else:
                # assuming that if the previous section was detected as a header, 
                # then this section will relate to that header
                if header:
                    talks_d.update({header: section})
                    
#         print(json.dumps(talks_d, indent=4))
        return talks_d
        
baseDir = '../'
fileType = '*.txt'

ceoList = [['ticker','calldate',
             'ceoName','ceoFullTitle',
             'ceoQATxt_wc']]

title_pattern = ['Chief Executive Officer','CEO','C.E.O.']

no_corp_participant = []
no_ceotxt = []
no_presentation = []
no_qa = []
totalTxtFiles = 0

fileNum = 0
for char in ascii_uppercase:
    txtFiles = sorted(glob(baseDir + char + fileType))
    totalFiles = len(txtFiles)
    totalTxtFiles += totalFiles
    
    for txtFile in txtFiles:
        fileNum += 1
        print('Processing {} of {}'.format(fileNum,totalTxtFiles))
        
        fileName = txtFile.rsplit('/',1)[1]
        pieces = fileName.split('_')
        coName = pieces[0]
        callDate = pieces[1]
        
        talks_dic = parse(txtFile) # parse the entire txt file
        
        # print(fileName)    
        # print(talks_dic.keys())
        # print(json.dumps(talks_dic, indent=4))
        # print(talks_dic['Corporate Participants'])
        # print('\n')
        # print(talks_dic['Conference Call Participiants'])
        # print(json.dumps(talks_dic['Presentation'], indent=4))
        # print(json.dumps(talks_dic['Questions and Answers'], indent=4))
        
        
        # Look for CEO among Corporate Participants of the given file
        if 'Corporate Participants' in talks_dic.keys():
            ppl = talks_dic['Corporate Participants']
            # print(ppl)
            
        elif 'Conference Call Participiants' in talks_dic.keys():
            ppl = talks_dic['Conference Call Participiants']
            
            with open('../tr-meta/no_corp_participant.csv','a') as f:
                writer = csv.writer(f)
                writer.writerow([fileName])
        else:
            ppl = {'No Person':'No Title'}
            with open('../tr-meta/no_people.csv','a') as f:
                writer = csv.writer(f)
                writer.writerow([fileName])
                
        ceos = []
        ceoQATxt = []
        ceoFound = ''
        ceoName = ''
        ceoTitle = ''
        lines = ''
        for name, title in ppl.items():
            if any(pattern in title for pattern in title_pattern):
                ceoFound = name
                ceoName = name.strip().replace('--','-').replace(' ','-').replace('/','-').replace('"','').translate(None, ".,'()")
                ceoTitle = title.strip().translate(None, ".,'()")
                ceos.append([ceoName,ceoTitle])
                
                if 'Questions and Answers' in talks_dic.keys():
                    for speaker, text in talks_dic['Questions and Answers'].items():
                        if ceoFound in speaker:
                            ceoQATxt = text.replace('\n','').replace('\r','').replace('  ',' ')
                            
                            with open('../tr-ceo-qatxt/{}_{}_{}_qa.txt'.format(coName,ceoName,callDate),'a') as f:
                                f.writelines(ceoQATxt + ' ')
                
                        # else: no ceo qa, do nothing
                
                else: # QA section not found in file
                    ceoQATxt_wc = 0
                    with open('../tr-meta/no_qa.csv','a') as f:
                        writer = csv.writer(f)
                        writer.writerow([ceoName,fileName])
                
                # # collect ceo txt across files in coName for each ceo in coName, 
                # # PTxt may include QA becasue QA section wasn't indicated in file 
                # try:
                #     with open('../tr-ceo-alltxt/{}_{}_all.txt'.format(coName,ceoName),'a') as f:
                #         f.writelines(' '.join(ceoPTxt) + ' '.join(ceoQATxt))
                # except:
                #     traceback.print_exc()
                    
            else: # no ceo found in current title in ppl dictionary
                pass
        
        # collect meta data from each file
        if ceoName == '': # no ceo found in txtFile
            ceoName = 'NA'
            ceoTitle = 'NA'
            ceoQATxt_wc = 0
            
            with open('../tr-meta/no_ceo.csv','a') as f:
                writer = csv.writer(f)
                writer.writerow([coName,fileName])
        else:
            for ceoName, ceoTitle in ceos:
                try:
                    with open('../tr-ceo-qatxt/{}_{}_{}_qa.txt'.format(coName,ceoName,callDate),'r') as f:
                        lines = f.read()
                        ceoQATxt_wc = len(lines)
                except IOError: # no *_qa.txt file available
                    ceoQATxt_wc = 0
            
                with open('../tr-meta/ceoList.csv','a') as f:
                    writer = csv.writer(f)
                    writer.writerow([coName,callDate,ceoName,ceoTitle,ceoQATxt_wc])

print('Total txt files: {}'.format(totalTxtFiles))

# end for char in charset
    # end travarsal across txtFiles start with char
        # end travarsal across kyes in talks_dic in txtFile