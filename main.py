import logging
from googlesearch import search
from telegram import ParseMode
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import date
from chat_res import chat_res
from today_special import today_is
from constants import helptext,msbte_cmd,todaytext

# website changed
# def today_event():
# 	r = requests.get("https://www.daysoftheyear.com/")
# 	eventinfo=[]
# 	soup = BeautifulSoup(r.content,features='html.parser')
# 	specialday=(soup.find(attrs={'class':'longer'}))
# 	eventinfo.insert(0,specialday)
# 	soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
# 	all_heading=soup.find(attrs={'class':'section__cards even'})
# 	current_day=all_heading.find_all(attrs={'class':'card__title heading'})
# 	links=[' ']
# 	for i in all_heading.find_all('a',href=True):
# 		links.append(i['href'])
# 	for i in current_day:
# 		eventinfo.append((i.text).replace('\n','').replace('\xa0',' '))
# 	templinks=links
# 	links=[]
# 	for x in templinks:
# 		if x not in links:
# 			links.append(x)
	
# 	return [eventinfo,links] 

today=datetime.now()

API_KEY='5227788520:AAGrrw0g2QW2DlKbH2CEofN-vyKSZrD6SKU'

updater = Updater(API_KEY,use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

d2 = today.strftime("%B %d, %Y")

def start(update:Update,context:CallbackContext):
	update.message.reply_photo(photo='https://images.app.goo.gl/gPHnRz9boukaL4i66',caption='☺️Hello , Welcome to KKWP Educational Chatbot☺️\nYou can check out my commands in /help Command')

def help(update:Update,context:CallbackContext):
	update.message.reply_text(text=helptext,parse_mode=ParseMode.HTML)

def timef(update:Update,context:CallbackContext):
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING, timeout=4)
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_DOCUMENT, timeout=2)
	update.message.reply_text(todaytext,parse_mode=ParseMode.HTML)

about_us_link='https://images.app.goo.gl/JR1RnCoXQbmM8NYy5'

def msbte(update:Update,context:CallbackContext):
	update.message.reply_photo(photo=open('./res/msbte_logo.jpg','rb'),caption=msbte_cmd,parse_mode=ParseMode.HTML)

def about_us(update:Update,context:CallbackContext):
	update.message.reply_photo(photo=about_us_link,caption="<b>About Us</b>\n02) Chetna Ahire \n30) Prsni Kanani 36) Ritesh Mahale",parse_mode=ParseMode.HTML)

def compile_it(update:Update,context:CallbackContext):
	b=update.message.reply_to_message
	try:
		file = context.bot.getFile(update.message.reply_to_message.document.file_id)
		file.download('./pr.py')
		import subprocess
		p=subprocess.Popen(['python' ,'pr.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out,err = p.communicate()
		output=out.decode('UTF-8')
		print(output)
		update.message.reply_text(text="Your code output :\n{0}".format(output))
	except:
		try:
			# messageid=update.message.reply_to_message.message_id
			with open('pr.py','w') as f:
				f.write(b['text'])
				f.close()
				
			import subprocess
			p=subprocess.Popen(['python' ,'pr.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			out,err = p.communicate()
			output=out.decode('UTF-8')
			errmsg=err.decode('UTF-8')
			print(output)
			update.message.reply_text(text="Your code output :\n\n\n{0}\n\nError message : \n{1}".format(output,errmsg))
		except:
			update.message.reply_text("Please tag/mention the file or code script of python")


def reply_bot(update:Update,context:CallbackContext):
	
	'reply function'

	text = str(update.message.text).lower()
	answer = chat_res(text,update,context)
	
	if isinstance(answer,list):
		update.message.reply_text(text=answer[0],parse_mode=ParseMode.HTML)
		update.message.reply_text(text=answer[1],parse_mode=ParseMode.HTML)
		update.message.reply_text(text=answer[2],parse_mode=ParseMode.HTML)
		update.message.reply_text(text=answer[3],parse_mode=ParseMode.HTML)
		update.message.reply_text(text=answer[4],parse_mode=ParseMode.HTML)
	else:
		update.message.reply_text(text=answer,parse_mode=ParseMode.HTML)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('today', timef))
updater.dispatcher.add_handler(CommandHandler('msbte', msbte))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('about', about_us))
updater.dispatcher.add_handler(CommandHandler('compile', compile_it))
updater.dispatcher.add_handler(MessageHandler(Filters.text,reply_bot))

updater.start_polling()
updater.idle()