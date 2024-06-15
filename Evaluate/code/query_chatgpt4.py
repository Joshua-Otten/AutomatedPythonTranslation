# -*- coding: utf-8 -*-

import openai
from openai_cost_tracker import query_openai

openai.api_key = ''
model_engine = "gpt-4-0125-preview"
path = '../GPT-4/'


# acquire the English list to translate
eng = open('EnglishKey.txt','r')
eng_terms = eng.readlines()
eng.close()
for i in range(len(eng_terms)):
    eng_terms[i] = eng_terms[i].strip()
'''
# Spanish
language = 'Spanish'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => valor absoluto.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => valor absoluto\nmemory view => vista de la memoria\npower => elevar\nprint => imprimir\nSyntax Error => Error de sintaxis.  Please translate these terms into "+language+": "

# give entire set for one language (French), translate to all the others
French_set_file = open('trans_examples_French.txt','r')
French_set = French_set_file.readline()
French_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to French, you have these translations: " + French_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language, '0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
'''
##################################
print('NOW ON TO FRENCH')
# French
language = 'French'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => valeur absolue.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => valeur absolue\nmemory view => mémoire visuelle\npower => puissance\nprint => imprimer\nSyntax Error => Erreur de syntaxe.  Please translate these terms into "+language+": "
# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
    
    
##################################
# Greek
print('NOW ON TO GREEK')
language = 'Greek'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => απόλ.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => απόλ\nmemory view => προβολή μνήμης\npower => δύναμη\nprint => τύπωσε\nSyntax Error => Συντακτικό λάθος.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j = 0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
    
 
##################################
# Mandarin
print('NOW ON TO MANDARIN')
language = 'Mandarin'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => 绝对值.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => 绝对值\nmemory view => 内存视图\npower => 次方\nprint => 打印\nSyntax Error => 语法错误.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j = 0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
 

##################################
# Hindi
print('NOW ON TO HINDI')
language = 'Hindi'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => निरपेक्ष मान.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => निरपेक्ष मान\nmemory view => स्मृति_दर्शन\npower => घात\nprint => प्रिंट\nSyntax Error => वाक्यविन्यास त्रुटि.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j=0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    #sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
    
##################################
# Bengali
print('NOW ON TO BENGALI')
language = 'Bengali'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]'). Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => পরম মান.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => পরম মান\nmemory view => মেমরি ভিউ\npower => ক্ষমতা\nprint => ছাপা\nSyntax Error => বাক্যগঠন ত্রুটি.  Please translate these terms into "+language+": "
# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j = 0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1
    

##################################
# Sorani Kurdish
print('NOW ON TO SORANI KURDISH')
language = 'Sorani Kurdish'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => بەهای ڕەها.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => بەهای ڕەها\nmemory view => دیمەنی بیرگە\npower => هێز\nprint => چاپکردن\nSyntax Error => هەڵەی ڕستەسازی.  Please translate these terms into "+language+": "


# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j=0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1

##################################
# Arabic
print('NOW ON TO ARABIC')
language = 'Arabic'

zero_shot_prompt = "Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in "+language+".  Please help me with this by translating each of the following terms into "+language+". Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => قيمة مطلقة.  Please translate these terms into "+language+": "

few_shot = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  For example: absolute value => قيمة مطلقة\nmemory view => عرض الذاكرة\npower => قوة\nprint => طباعة\nSyntax Error => خطأ لغوي.  Please translate these terms into "+language+": "

# give entire set for one language (Spanish), translate to all the others
Spanish_set_file = open('trans_examples_Spanish.txt','r')
Spanish_set = Spanish_set_file.readline()
Spanish_set_file.close()

entire_set_prompt = "I am trying to translate Python's key terms into "+language+", so that people can code in "+language+".  For example, when translating Python to Spanish, you have these translations: " + Spanish_set + ".  Please translate the following terms into "+language+".  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding translation (as in '[term] => [translation]').  Here are the terms, separated by commas:  "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot, entire_set_prompt]
files = ['0-shot/'+language,'0+Motive/'+language, '1-shot/'+language, '5-shot/'+language, 'all-other/'+language]

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    j=0
    # for every 10 terms, ask model to translate
    for i in range(j,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1




############################################
##### Splitting / Expanding Experiment #####
############################################
print('NOW Splitting/Unabbreviating Testing')

# acquire the original English Python terms to expand
eng = open('EnglishOriginalTerms.txt','r')
eng_terms = eng.readlines()
eng.close()
for i in range(len(eng_terms)):
    eng_terms[i] = eng_terms[i].strip()



zero_shot_prompt = "Please expand (i.e. split and unabbreviate) these Python terms into the word or phrase that they are intended to represent.  If no abbreviation or splitting into separate words is necessary, then the expanded form will be the same as the original term.  Do not provide any other response; simply list each term (each on a separate line) followed by => and its corresonding expansion (as in '[term] => [expansion]').  Here are the terms, separated by commas:  "

zero_shot_motivation = "I am trying to translate Python's key terms into other languages, so that people can code in their native language.  However, I first need to know the expanded form of the abbreviations.  Please help me with this by expanding (i.e. splitting and unabbreviating) each of the following terms into the word or phrase that they are intended to represent. If no abbreviation or splitting into separate words is necessary, then the expanded form will be the same as the original term.  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding expansion (as in '[term] => [expansion]').  Here are the terms, separated by commas:  "

one_example = "I am trying to translate Python's key terms into other languages, so that people can code in their native language.  However, I first need to know the expanded form of the abbreviations.  Please help me with this by expanding (i.e. splitting and unabbreviating) each of the following terms into the word or phrase that they are intended to represent. If no abbreviation or splitting into separate words is necessary, then the expanded form will be the same as the original term.  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding expansion (as in '[term] => [expansion]').  For example: abs => absolute value.  Please expand these terms: "

few_shot = "I am trying to translate Python's key terms into other languages, so that people can code in their native language.  However, I first need to know the expanded form of the abbreviations.  Please help me with this by expanding (i.e. splitting and unabbreviating) each of the following terms into the word or phrase that they are intended to represent. If no abbreviation or splitting into separate words is necessary, then the expanded form will be the same as the original term.  Do not provide any other response or translations; simply list each term (each on a separate line) followed by => and its corresonding expansion (as in '[term] => [expansion]').  For example: abs => absolute value\nmemoryview => memory view\npow => power\nprint => print\nSyntaxError => Syntax Error.  Please expand these terms: "

prompts = [zero_shot_prompt, zero_shot_motivation, one_example, few_shot]
files = ['expansion/0-shot','expansion/0+Motive', 'expansion/1-shot', 'expansion/5-shot']

k=0
for prompt in prompts:
    f = open(path+files[k]+'.txt','w')
    # for every 10 terms, ask model to translate
    for i in range(0,len(eng_terms),10):
        terms = ', '.join(eng_terms[i:i+10])
        output = ''
        ### QUERY HERE ###
        response = query_openai(
            model=model_engine,
            messages=[{'role': 'user','content': prompt+terms}],
            max_tokens=1024,
            simulation=False,
            print_cost=True,
        )
        print('"'+prompt+terms+'"')
        print(response["choices"][0]["message"]["content"])
        f.write(response["choices"][0]["message"]["content"]+'\n')
        
    f.close()
    # sanity check:
    f = open(path+files[k]+'.txt','r')
    l = f.readlines()
    if len(l) != 222:
        print('##############################')
        print('Error with file '+files[k]+'!  Lines:',str(len(l)))
        print('##############################')
        count_bad_lines = 0
        for line in l:
            if line.count('=>') > 1:
                count_bad_lines += line.count('=>')-1
        print('newline issues:',count_bad_lines)
            
    f.close()
    
    k += 1

