# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:52:38 2020

@author: Raj Tagore
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

Bot1 = ChatBot('Bot')
trainer1 = ChatterBotCorpusTrainer(Bot1)
trainer1.train('D:\Padhai\AI/BankBot.yml')
while True:
    q = input('You: ')
    if q == 'exit':
        break
    else:
        a = Bot1.get_response(q)
        print('Bankbot: ', a)
        