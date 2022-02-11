import telebot, wikipedia, re

bot = telebot.TeleBot('1063681375:AAH9Lt7gl25J1tkJCsS_qPkV1_USntJI2ms')
wikipedia.set_lang("ru, en")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitexts = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitexts=wikitexts+x+'.'
            else:
                break
        wikitexts=re.sub('\([^()]*\)', '', wikitexts)
        wikitexts=re.sub('\([^()]*\)', '', wikitexts)
        wikitexts=re.sub('\{[^\{\}]*\}', '', wikitexts)
        return wikitexts
    except Exception as e:
        return 'В Wikipedia нет информации об этом'
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне слово, и я найду его на Wikipedia')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
bot.polling(none_stop=True, interval=0)
