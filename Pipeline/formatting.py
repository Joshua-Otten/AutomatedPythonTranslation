# this formats files so that only the translations appear, line by line.
# arg 1 is the file to format, arg 2 is new filename

# assumes no issues with formatting

import sys

filename = sys.argv[1]

file = filename
f = open(file,'r')
gpt_lines = f.readlines()
f.close()

new = open('Formatted/'+sys.argv[2],'w')

to_expand = open('to_expand.txt','r')
to_expand_len = len(to_expand.readlines())
to_expand.close()

# quick sanity check
if len(gpt_lines) != to_expand_len:
    print('File error:',filename,' has',len(gpt_lines),'lines')

else:
    for line in gpt_lines:
        if line.strip() == '-':
            new.write('-\n')
            #print('-')
        else:
            parts = line.strip().split()
            #print(parts)
            #print(language)
            index = parts.index('=>') + 1
            to_write = ' '.join(parts[index:])
            if to_write == '':
                #print('Nothing after =>')
                to_write = ' '.join(parts[:index-1])
            #print(to_write)
            new.write(to_write+'\n')
        
new.close()
