f = open('French_libraries.txt','r')
lines = f.readlines()
f.close()
n = open('French_libraries_formatted.txt','w')

def beginning_download(lang_id):
    import stanza
    #stanza.download(lang_id) # only needs to be done once per lang
    nlp = stanza.Pipeline(lang_id)
    print('completed initializations')
    return nlp

nlp = beginning_download('fr')

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
