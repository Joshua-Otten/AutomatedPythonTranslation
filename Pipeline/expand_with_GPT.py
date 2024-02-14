# -*- coding: utf-8 -*-

import openai
from openai_cost_tracker import query_openai

openai.api_key = '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' #"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"
model_engine = "gpt-3.5-turbo-1106" #"text-davinci-003" # use turbo

# get list of terms to expand
f = open('to_expand.txt','r')
to_expand = f.readlines()
f.close()
for i in range(len(to_expand)):
    to_expand[i] = to_expand[i].strip()
    
    
# Note that prompt is few shot (best accuracy on std lib)
prompt = "I am trying to translate Python's key terms into other languages, so that people can code in their native language.  However, I first need to know the expanded form of the abbreviations.  Please help me with this by expanding (only splitting and unabbreviating) each of the following terms into the word or phrase that they are intended to represent. If no abbreviation or splitting into separate words is necessary, meaning that the terms are complete words and not concatenating together, then the expanded form should be the same as the original.  This is because while we want to expand the words, we want them to be as brief as possible.  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding expansion (as in '[term] => [expansion]').  For example: abs => absolute value\nmemoryview => memory view\npow => power\nprint => print\nSyntaxError => Syntax Error.  Please expand these terms: "
    
    
f = open('to_translate.txt','w')
# for every 10 terms, ask model to translate
for i in range(0,len(to_expand),10):
    terms = ', '.join(to_expand[i:i+10])
    output = ''
    ### QUERY HERE ###
    response = query_openai(
        model=model_engine,
        messages=[{'role': 'user','content': prompt+terms}],
        max_tokens=100,
        simulation=False,
        print_cost=True,
    )
    print('"'+prompt+terms+'"')
    print(response["choices"][0]["message"]["content"])
    f.write(response["choices"][0]["message"]["content"]+'\n')
    
f.close()

# sanity check, file should have same number of terms:
f = open('to_translate.txt','r')
l = f.readlines()
if len(l) != len(to_expand):
    print('Issue: file length incorrect.',len(to_expand),'terms, but',len(l),'expansions')
    count_bad_lines = 0
    for line in l:
        if line.count('=>') > 1:
            count_bad_lines += line.count('=>')-1
    print('newline issues:',count_bad_lines)
f.close()



