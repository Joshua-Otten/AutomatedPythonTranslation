# processes translations so that they are more "Pythonic"
# replaces spaces with underscores, removes determiners
# Note that stanza does not work for Bengali
# arguments: [filename] [lang code]
import sys

lang_id = sys.argv[2]
filename = sys.argv[1]

path = 'Translated/'
f = open(path+filename,'r')
lines = f.readlines()
f.close()
n = open(path+'PROCESSED_'+filename,'w')

def beginning_download(lang_id):
    import stanza
    #stanza.download(lang_id) # only needs to be done once per lang
    nlp = stanza.Pipeline(lang_id)
    print('completed initializations')
    return nlp

nlp = beginning_download(lang_id)

for line in lines:
    to_write = ''
    for i in line:
        if i == '_':
            to_write += ' '
        else:
            to_write += i
            
    processed = ''
    doc = nlp(to_write.strip())
    for sentence in doc.sentences:
        for word in sentence.words:
            if not str(word.pos) == 'DET':
                processed += word.text + '_'
            else:
                print('discarding:',word.text)
    processed = processed[:len(processed)-1]
    n.write(processed+'\n')

n.close()
