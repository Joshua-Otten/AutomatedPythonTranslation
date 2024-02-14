requirements:
	- googletrans Python libraray
	- stanza Python library
	- openai_cost_tracker Python library
	- API key for ChatGPT

Usage Steps for translating Python terms in pipeline:

1. add terms to 'make_lists.py' file, according to commented specifications
2. run make_lists.py
3. run expand_with_GPT.py
4. If there is a message indicating an error, run 'fix_turbo_expansion.py'
5. run 'formatting.py' with 2 arguments: arg1 = 'to_translate.txt', arg2 = yourModuleName.txt
6. run 'translate.py' with 2 args: arg1 = yourModuleName.txt, arg2 = language code to translate into
7. the new translated library will be in /Formatted/Translations/
