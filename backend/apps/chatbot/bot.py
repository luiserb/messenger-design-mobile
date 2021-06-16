from django.conf import settings

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

path = settings.DIALOGS_CHATBOT

chatbot = ChatBot(
        'Robot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
        ],
    )
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(path)