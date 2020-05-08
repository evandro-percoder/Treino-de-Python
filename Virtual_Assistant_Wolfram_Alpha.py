#!/usr/bin/env python
# coding: utf-8

# In[ ]:

"""
get_ipython().system(' pip install wolframalpha')
get_ipython().system(' pip install wikipedia')

"""


# In[ ]:


import wolframalpha
import wikipedia
import requests

app_id = "virtu@l_@ssitent"
client = wolframalpha.Client(app_id)

while True:
    raw_input = input("\nFaça sua Pesquisa: ")
    wikipedia.set_lang("pt")
    print('\n=========>>> Resposta <<<=========\n')
    print(wikipedia.summary(raw_input, sentences=2))

