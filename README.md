# AutomatedPythonTranslation
Pipeline and evaluations for automatic Python library/term translation

Requirements:
	- googletrans Python libraray
	- stanza Python library
	- openai_cost_tracker Python library
	- API key for ChatGPT

Usage Steps for translating Python terms in pipeline:
1. add terms to translate within the 'make_lists.py' file, according to commented specifications
2. run make_lists.py
3. run expand_with_GPT.py
4. If there is a message indicating an error, you can try running 'fix_turbo_expansion.py'
5. run 'formatting.py' with 2 arguments: arg1 = 'to_translate.txt', arg2 = yourModuleName.txt
6. run 'translate.py' with 2 args: arg1 = yourModuleName.txt, arg2 = language code to translate into
   - Note: may need to uncomment line 17 for stanza download if this is the first time using this language code
   - Once terms are expanded from steps 1-5, you can run this multiple times to translate to additional languages
8. the new translated library will be in /Formatted/Translations/
