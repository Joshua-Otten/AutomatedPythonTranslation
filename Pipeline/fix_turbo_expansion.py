# main problem appears to be that gpt-turbo did not add a new line between term translations/expansions
# this script is supposed to fix that formatting issue
## NOTE: this code is not completely without issues.  However, it seems to work in the majority of cases.  In special cases where it fails to fix formatting, I temporarily reformatted parts of ChatGPT's file to make it work--this was more efficient than debugging the code.

import sys

def term_search(s, t):
    string = s.strip()
    term = t.strip()
    index = string.find(term)
    if index < 0:
        # if chatgpt just concatenated two words
        if len(term.split())>1:
            if ''.join(term.split()) in string:
                print('gotcha!!!')
                return string.find(''.join(term.split()))
        else:
            return None
    else:
        return index

file = 'to_translate.txt'
f = open(file,'r')
gpt_lines = f.readlines()
f.close()

new = open('Fixed_'+file,'w')

eng_terms = open('to_expand.txt','r')
eng_key = eng_terms.readlines()
eng_terms.close()

i = 0
k = 0
while i < len(eng_key):
    print('term:',eng_key[i])
    if gpt_lines[k].count('=>') > 1:
        print('more than one => :',gpt_lines[k])
        last = 0
        # write all the => translations on separate lines
        for j in range(gpt_lines[k].count('=>')):
            string = gpt_lines[k][last:len(gpt_lines[k])]
            #print('string ===',string)
            while i < len(eng_key) and term_search(string,eng_key[i]) == None:
                # if term not in line
                print('Skipped in multi-line',eng_key[i])
                #print('string was:',string)
                new.write('-\n')
                i += 1
                #index = term_search(string,eng_key[i]) + last
            if i >= len(eng_key): # in case we're out of terms
                break
            index = term_search(string,eng_key[i])# + last

            # write the stuff before index
            if last != index:
                print('to write:', gpt_lines[k][last:index])#gpt_lines[k][last:index])
                new.write(gpt_lines[k][last:index].strip()+'\n')
            
            last = index
            i += 1
            print('about to look and see, j=',j)
            if j == gpt_lines[k].count('=>')-1:
                # write stuff from after the index
                print('end of line, now write:',gpt_lines[k][index:len(gpt_lines[k])])
                new.write(gpt_lines[k][index:len(gpt_lines[k])].strip()+'\n')
                k += 1
    elif gpt_lines[k] == '\n':
        k += 1
    else:
        term = gpt_lines[k].split()[0]
        print('single =>')
        print(gpt_lines[k])
        if term_search(gpt_lines[k],eng_key[i])==None:#eng_key[i].strip() not in gpt_lines[k]:#term.strip() != eng_key[i].strip():
            print('Skipped',eng_key[i])
            new.write('-\n')
            i += 1
        else:
            # gpt did this one fine, just write the term
            print('everything a-okay\n')
            new.write(gpt_lines[k].strip()+'\n')
            i += 1
            k += 1
        
new.close()
# sanity check
new = open('Fixed_'+file,'r')
lines = new.readlines()
print(len(lines))
new.close()
