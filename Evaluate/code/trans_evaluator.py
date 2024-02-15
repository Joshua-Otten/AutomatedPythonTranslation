# This code evaluates both a file of outputs, and a file of correct translations
# each file is formatted the same way a LanguageKey is formatted (each term on one line), but we don't have underscores, etc.  Formatting subject to change depending on how translators write output, etc
# We compare the lemmatized versions of the expanded terms
# if stanza does not support a particular language, we will have to evaluate that some other way
from torchmetrics.text import CHRFScore

def beginning_download(lang_id):
    import stanza
    #stanza.download(lang_id) # only needs to be done once per lang
    nlp = stanza.Pipeline(lang_id)
    print('completed initializations')
    return nlp

# creates a new file where all words are lemmatized
def lemmatize(file, nlp):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    
    docs = [stanza.Document([], text=line.strip()) for line in lines]
    
    out_docs = nlp(docs) # out_docs is a list
    
    # now write this to new files
    new = open('lemmatized_'+file,'w')
    for line in out_docs:
        for sentence in line.sentences:
            to_write = list()
            for word in sentence.words:
                to_write.append(word.lemma)
            new.write(' '.join(to_write).lower()+'\n')
            
    print('lemmatized:',file)



# this function compares two lemmatized files
def raw_accuracy(gold_trans, test_trans):
    # open and read the files
    gold_trans = open(gold_trans,'r')
    gold = gold_trans.readlines()
    gold_trans.close()
    test_trans = open(test_trans,'r')
    test = test_trans.readlines()
    test_trans.close()
    if len(gold) != len(test):
        print("Error: lengths of the two sets do not match")
        print("Length of golden set:",len(gold))
        print("Length of test:",len(test))
    correct = 0
    total = len(gold)
    for i in range(len(gold)):
        if gold[i].lower().strip() == test[i].lower().strip():
            correct += 1
    #print(f"\t{correct} correct out of {total}")
    print(f"\tRaw: {100*correct/total:.2f}%")



def CHRF_score(gold_trans, test_trans):
    chrf = CHRFScore()
    gold_trans = open(gold_trans,'r')
    gold = gold_trans.readlines()
    gold_trans.close()
    test_trans = open(test_trans,'r')
    test = test_trans.readlines()
    test_trans.close()
    if len(gold) != len(test):
        print("Error: lengths of the two sets do not match")
        print("Length of golden set:",len(gold))
        print("Length of test:",len(test))
    total = len(gold)
    all_scores = 0
    for i in range(len(gold)):
        target = [gold[i].lower().strip()]
        pred = [test[i].lower().strip()]
        score = chrf(pred, target).item()
        all_scores += score
    #print("Avg CHRF score is:",all_scores/total)
    print(f"\tCHRF: {100*all_scores/total:.2f}%")
        
def print_llm_scores(language, prompt):
    print('"'+language+'"')
    print('ChatGPT text-davinci')
    raw_accuracy('../Gold/'+language+'Key.txt','../ChatGPT-Dav/'+prompt+'/'+language+'.txt')
    CHRF_score('../Gold/'+language+'Key.txt','../ChatGPT-Dav/'+prompt+'/'+language+'.txt')
    print('GPT-turbo')
    raw_accuracy('../Gold/'+language+'Key.txt','../ChatGPT-Turbo/'+prompt+'/'+language+'.txt')
    CHRF_score('../Gold/'+language+'Key.txt','../ChatGPT-Turbo/'+prompt+'/'+language+'.txt')
    print('Llama2')
    raw_accuracy('../Gold/'+language+'Key.txt','../Llama2/'+prompt+'/'+language+'.txt')
    CHRF_score('../Gold/'+language+'Key.txt','../Llama2/'+prompt+'/'+language+'.txt')

def print_google_scores(language, version):
    print('"'+language+'"')
    raw_accuracy('../Gold/'+language+'Key.txt','../GoogleTranslate/'+version+'/'+language+'.txt')
    CHRF_score('../Gold/'+language+'Key.txt','../GoogleTranslate/'+version+'/'+language+'.txt')

# for testing
#nlp = beginning_download('fr')
#lemmatize('Llama2_zero_French.txt', nlp)
#lemmatize('FrenchKey.txt', nlp)

# in the function -> Gold first, then test file


print('Get silly warning out of the way:')
CHRF_score('../Gold/SpanishKey.txt','../Llama2/0-shot/Spanish.txt')
print('\n')



print('\nEXPANSION with GPT-Turbo\n')
print('Baseline (scores for standard compared with expanded)')
raw_accuracy('../Gold/EnglishKey.txt','../Gold/EnglishOriginalTerms.txt')
CHRF_score('../Gold/EnglishKey.txt','../Gold/EnglishOriginalTerms.txt')
prompts = ['_0-shot','_0+Motive','_1-shot','_5-shot']
for prompt in prompts:
    print('PROMPT:',prompt[1:])
    filename = '../ChatGPT-Turbo/expansion/expansion'+prompt+'.txt'
    raw_accuracy('../Gold/EnglishKey.txt',filename)
    CHRF_score('../Gold/EnglishKey.txt',filename)




# Automatically evaluating all languages over raw accuracy + CHRF
test_languages = ['Spanish','French','Greek','Mandarin','Hindi','Bengali','Arabic','SoraniKurdish']

# ChatGPT and Llama2
print('\nTRANSLATION SCORES for ChatGPT and Llama2\n')
prompts = ['0-shot','0+Motive','1-shot','5-shot','all-other']
for prompt in prompts:
    print('PROMPT:',prompt)
    for language in test_languages:
        print_llm_scores(language,prompt)
        print()

# Google Translate
print('\nGOOGLE TRANSLATE SCORES\n')
versions = ['no-cntxt','def','expl']
for version in versions:
    print('GOOGLE:',version)
    for language in test_languages:
        print_google_scores(language, version)
        print()
    print()


print('\nPipeline Testing French\n')
print('Random module:')
raw_accuracy('../Gold/French_pipeline_random.txt','../Pipeline/French_pipeline_test_random.txt')
CHRF_score('../Gold/French_pipeline_random.txt','../Pipeline/French_pipeline_test_random.txt')
print('Numpy module:')
raw_accuracy('../Gold/French_pipeline_numpy.txt','../Pipeline/French_pipeline_test_numpy.txt')
CHRF_score('../Gold/French_pipeline_numpy.txt','../Pipeline/French_pipeline_test_numpy.txt')
print('Total (both modules):')
raw_accuracy('../Gold/French_pipeline_gold.txt','../Pipeline/French_pipeline_test.txt')
CHRF_score('../Gold/French_pipeline_numpy.txt','../Pipeline/French_pipeline_test_numpy.txt')

print('\nPipeline Testing Greek\n')
print('Random module:')
raw_accuracy('../Gold/Greek_pipeline_random.txt','../Pipeline/Greek_pipeline_test_random.txt')
CHRF_score('../Gold/Greek_pipeline_random.txt','../Pipeline/Greek_pipeline_test_random.txt')
print('Numpy module:')
raw_accuracy('../Gold/Greek_pipeline_numpy.txt','../Pipeline/Greek_pipeline_test_numpy.txt')
CHRF_score('../Gold/Greek_pipeline_numpy.txt','../Pipeline/French_pipeline_test_numpy.txt')
print('Total (both modules):')
raw_accuracy('../Gold/Greek_pipeline_gold.txt','../Pipeline/Greek_pipeline_test.txt')
CHRF_score('../Gold/Greek_pipeline_numpy.txt','../Pipeline/Greek_pipeline_test_numpy.txt')

print('\nPipeline Testing Hindi\n')
print('Random module:')
raw_accuracy('../Gold/Hindi_pipeline_random.txt','../Pipeline/Hindi_pipeline_test_random.txt')
CHRF_score('../Gold/Hindi_pipeline_random.txt','../Pipeline/Hindi_pipeline_test_random.txt')
print('Numpy module:')
raw_accuracy('../Gold/Hindi_pipeline_numpy.txt','../Pipeline/Hindi_pipeline_test_numpy.txt')
CHRF_score('../Gold/Hindi_pipeline_numpy.txt','../Pipeline/Hindi_pipeline_test_numpy.txt')
print('Total (both modules):')
raw_accuracy('../Gold/Hindi_pipeline_gold.txt','../Pipeline/Hindi_pipeline_test.txt')
CHRF_score('../Gold/Hindi_pipeline_numpy.txt','../Pipeline/Hindi_pipeline_test_numpy.txt')


print('\nPipeline Testing Bengali\n')
print('Random module:')
raw_accuracy('../Gold/Bengali_pipeline_random.txt','../Pipeline/Bengali_pipeline_test_random.txt')
CHRF_score('../Gold/Bengali_pipeline_random.txt','../Pipeline/Bengali_pipeline_test_random.txt')
print('Numpy module:')
raw_accuracy('../Gold/Bengali_pipeline_numpy.txt','../Pipeline/Bengali_pipeline_test_numpy.txt')
CHRF_score('../Gold/Bengali_pipeline_numpy.txt','../Pipeline/Bengali_pipeline_test_numpy.txt')
print('Total (both modules):')
raw_accuracy('../Gold/Bengali_pipeline_gold.txt','../Pipeline/Bengali_pipeline_test.txt')
CHRF_score('../Gold/Bengali_pipeline_numpy.txt','../Pipeline/Bengali_pipeline_test_numpy.txt')
