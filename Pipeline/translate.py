# this translates a given file to a given language
# args: arg1 = filename, arg2 = language code to translate into

import googletrans
from googletrans import Translator
import sys
from httpcore import ReadTimeout

lang = sys.argv[2]
filename = sys.argv[1]
file = open('Formatted/'+filename,'r')
lines = file.readlines()
file.close()

def beginning_download(lang_id):
    import stanza
    #stanza.download(lang_id) # only needs to be done once per lang
    nlp = stanza.Pipeline(lang_id)
    print('completed initializations')
    return nlp
    
    
    
new = open('Translated/'+lang+'_'+filename,'w')

translator = Translator()


#nlp = beginning_download(lang)


for line in lines:
    #print('translating:',line.strip())
    try_again = True
    to_write = ''
    while try_again:
        try:
            output = translator.translate(line.strip(), src='en', dest=lang)
            print(output.text)
            to_write = output.text.strip()
            try_again = False
        except TypeError:
            print('unable to translate:',line.strip())
            to_write = line.strip()
            try_again = False
        except ReadTimeout:
            print('read operation timed out, trying again')
        
        
    # additional formatting/processing
    '''
    processed = ''
    doc = nlp(to_write)
    for sentence in doc.sentences:
        for word in sentence.words:
            if not str(word.pos) == 'DET':
                processed += word.text + '_'
            else:
                print('discarding:',word.text)
    processed = processed[:len(processed)-1]
    #print('writing:',processed)
    new.write(processed+'\n')
    '''
    
    new.write(to_write+'\n')

new.close()

