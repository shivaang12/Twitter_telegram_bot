#MAIN DECLARATION

import twitter, time, sys
import telegram

#Twitter Authorization key values
CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_TOKEN_KEY=''
ACCESS_TOKEN_SECRET=''

#Telegram Token
TELEGRAM_TOKEN=''

#Generating Api instance
api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

#Generating Bot instance
bot = telegram.Bot(token=TELEGRAM_TOKEN)


id =    #insert chat_id for Telegram. You can also retrive the chat id using Telegram api
twi_id=0    #initial tweet id


#functions

def getMyTimeLine():
    if twi_id == 0:
        return api.GetHomeTimeline(count=1)

    else:
        print twi_id
        return api.GetHomeTimeline(since_id=twi_id)


def textMessage(name, text1):
    Name = "*"+name+"*"
    final = Name+" - "+text1
    bot.sendMessage(chat_id=id, text=final, parse_mode=telegram.ParseMode.MARKDOWN)

NAME_HOLDER = ""
TEXT_HOLDER = ""
NAME_HOLDER_t = ""
TEXT_HOLDER_t = ""


while 1:
    try:
        #to catch a tweet
        ins = getMyTimeLine()

        #There parms will hold out data

        for s in ins:
            print s.user.name
            NAME_HOLDER = s.user.name
            print s.text
            TEXT_HOLDER = s.text
            if s.id > twi_id:
                twi_id=s.id
            textMessage(NAME_HOLDER, TEXT_HOLDER)

        time.sleep(300)

    except:
        print "reloop"
        time.sleep(300)
