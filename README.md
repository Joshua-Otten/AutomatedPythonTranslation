# AutomatedPythonTranslation
Pipeline and evaluations for automatic Python library/term translation

Requirements:
	- googletrans Python libraray
	- stanza Python library
	- openai_cost_tracker Python library
	- API key for ChatGPT
	- spacy Python library

The csv 'pipeline_translations_corrections' includes all translations and corrections from the pipeline in French, Greek, Hindi, and Bengali.  Note that these are also automatically processed (replace spaces with underscores and eliminate determiners) in order to be compatible with UniPy.    

Usage Steps for translating Python terms in pipeline:
1. add terms to translate within the 'make_lists.py' file, according to commented specifications
2. run make_lists.py
ALTERNATIVELY:
	- write Python terms to the file 'to_expand.txt,' each on one line
3. run expand_with_GPT.py
4. If there is a message indicating an error, you can try running 'fix_turbo_expansion.py'
	- check that the new file, 'Fixed_to_translate.txt', is not missing very many terms
	- if it is, you may need to manually inspect the 'to_translate.txt' file for errors in ChatGPT's outputs/formatting
5. run 'formatting.py' with 2 arguments: arg1 = 'to_translate.txt', arg2 = yourModuleName.txt
6. run 'translate.py' with 2 args: arg1 = yourModuleName.txt, arg2 = language code(s) to translate into
   - Note: may need to uncomment line 17 for stanza download if this is the first time using this language code
   - Once terms are expanded from steps 1-5, you can run this multiple times to translate to additional languages
8. the new translated library will be in /Formatted/Translations/
9. optionally, run 'process_terms.py' with 2 args: arg1 = yourModuleName.txt, arg2 = language code
   - This will process translations so they are more "Pythonic"
   - Note that stanza does not currently work for Bengali
Note that files in the Pipeline/Translated/ directory are not corrected
10. optionally, run 'abbreviator.py' with the path to the translations file as an argument
	- ensure that all spaces between words are replaced with underscores first
	- you may need to download the particular spacy model with 'python -m space download [model]'