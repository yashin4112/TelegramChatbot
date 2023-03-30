from datetime import date
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
from googlesearch import search
import telegram
from today_special import today_is
chatbot = ChatBot("KKWP Help Bot",trainer='chatterbot.trainers.ChatterBotCorpusTrainer')


conversation = [
 'Hi',
'Hello',
'I have a complaint.',
'Please elaborate, your concern',
'Okay Thanks',
'No Problem! Have a Good Day!',
'how are you?',
'Fine, What about you?',
'do you know about programming languages ?',
'Yes, I know about Java, C, CPP and python, and fun fact is my program is written in python!'
]

trainer = ListTrainer(chatbot)
trainer.train(conversation) 

today = date.today()

sem1text='''Semester 1 Lab Manual\n1) 22001-Fundamentals of ICT : <a href ='https://drive.google.com/uc?id=1drQ694_uxGet1oCJAiqpseGAThDDApWi&export=download'>Download</a>
2) 22101-English : <a href ='https://drive.google.com/file/d/1-N_RPbY4xbri0tSHtUBIJRk3q7PLIPDU/view?usp=sharing'>Download</a>
3) 22101-English Work Book : <a href='https://drive.google.com/file/d/1K98pZXzG5K7L9KYeDCnQCmudRQe1zuRM/view'>Download</a>
4) 22102-Basic science(chemistry) : <a href='https://drive.google.com/file/d/18_47S-VSQSpj9HIC1gCMm1t6il1ETdMn/view'>Download</a>
5) 22102-Basic science(physics) : <a href='https://drive.google.com/file/d/1Z53BjXf8VCUCCkycRgQFFxB0yBZFlkja/view'>Download</a>
6) 22057-Guidelines & Assessment Micro Projects & Industrial Training : <a href='https://drive.google.com/file/d/1F8CqYsigjqjh8ZqNcZxhbC3MHNkOhn7v/view'>Download</a>'''

sem2text='''Semester 2 Lab Manual\n1) 22226 - Programming in C : <a href='https://drive.google.com/file/d/1MnWShIThcbvmxyAjbi6cduYoia5x9Oid/view'>Download</a>
2) 22225 - Basic Electronics : <a href='https://drive.google.com/file/d/1DjZ-ZK0H5XNwREC6bhBL9Jts4NPnnz1q/view?usp=sharing'>Download</a>
3) 22215 - Elements of Electrical Engineering : <a href='https://drive.google.com/file/d/1zQFxIB1u8t1wH5KwEp84a7ywcP6Bo2P9/view'>Download</a>
4) 22014 - Web Page Designing with HTML : <a href='https://drive.google.com/file/d/1YghUTFGZgF5Wp0-XqZAB1A6qYRqMt_p9/view'>Download</a>
5) 22013 - Computer Peripheral and Hardware Maintenance : <a href='https://drive.google.com/file/d/1WNuDjTcuWsCfbT1eqC_Ta3k9VIlTk556/view'>Download</a>
6) 22009 - Business Communication Using Computers : <a href='https://drive.google.com/file/d/1WdlOh6UAS46yuoX5ZVHJF7m2eCEujm0J/view'>Download</a>'''

sem3text='''<b>Semester 3 Lab Manual</b>\n1) 22318 - Computer Graphics : <a href='https://drive.google.com/file/d/1y2IccyHSAiX_GWa2pqoskKxmC9OrOuUW/view'>Download</a>
2) 22319 - Database Management : <a href='https://drive.google.com/file/d/1vgBI8t9mUnVUzglxVS_bRNse_pCngMqa/view'>Download</a>
3) 22320 - Digital Techniques : <a href='https://drive.google.com/file/d/1booINyjuBbQpNrIEAz-rtdAi1XvTwMjI/view'>Download</a>
4) 22316 - Object Oriented Programming using C++ : <a href='https://drive.google.com/file/d/1xh1VnpyM8N4F_XTqmbpBPvBGyEnKEQeE/view?usp=sharing'>Download</a> 
5) 22317 - Data Structure using 'C': <a href='https://drive.google.com/file/d/1KVLYhzrQEU__gCB1iqZBUt3b3U_saI1C/view'>Download</a>'''

sem4text='''<b>Semester 4 Lab Manual</b>
1) 22412 - Java Programming : <a href='https://drive.google.com/file/d/1WfsbdcY_0RxkwQDGb87245LTs7NOYKBj/view'>Download</a>
2) 22415 - Microprocessor : <a href='https://drive.google.com/file/d/1-Whn17XI1HFJtcG-xuOp21oTu_CGWufg/view'>Download</a>
3) 22416 - Database Management : <a href='https://drive.google.com/file/d/1ubq8fd6876ChmMN-bF4xJ-SQfZKu3vGk/view'>Download</a>
4) 22034 - GUI Apllication Development using vb.net : <a href='https://drive.google.com/file/d/1ZSoPRFUWK1YR2m8WJMSzJ4DPxoN2D3BD/view'>Download</a>'''

sem5text='''<b>Semester 5 Lab Manual</b>
1) 22516 - Operating Systems : <a href='https://drive.google.com/file/d/1meFSp3Gl6edCtf4mANcWd6jIJfFvl_hg/view'>Download</a>
2) 22517 - Advanced Java Programming : <a href='https://drive.google.com/file/d/12NoAgo0Qdr4FocQ4VHOeCswFtdNy-5uW/view'>Download</a>
3) 22518 - Software Testing : <a href='https://drive.google.com/file/d/1pcXjlwJgjddse02EHEn_GXZMLKIo_01l/view'>Download</a>'''

sem6text='''<b>Semester 6 Lab Manual</b>
1) 22616 - Programmig with Python : <a href='https://drive.google.com/file/d/1p7AoHylEAIvIvCXb6MStzd2PFvgin1-1/view'>Download</a>
2) 22617 - Mobile Application Development : <a href='https://drive.google.com/file/d/1Nv24p2U9xAUP-s2A0glH6w6IMei1ZvvP/view'>Download</a>'''


def chat_res(user_msg,up,cont):
    typing_act=cont.bot.send_chat_action(chat_id=up.message.chat_id, action=telegram.ChatAction.TYPING,timeout=2)
    user_msg_edited=str(user_msg).lower()
    ans="Don't Understand you."
    if user_msg_edited in ('hey','hii','sup','hi','hie','hello'):
        ans= random.choice(['Hey!','Hii!','sup','Hi!','Hie!'])
    elif user_msg_edited in ('who are you?','who are you',):
        ans= "It's KKWP Help Bot."
    elif user_msg_edited in ('time','time?'):
        d2 = today.strftime("%B %d, %Y")
        ans='''Today's Date: {0}'''.format(d2)
    elif user_msg_edited in ('who is your father','who is your father?'):
        ans="Ritesh Mahale Gave birth to me."
    elif user_msg_edited =='ritesh':
        ans="Hey..! It's my developer !"
    elif user_msg_edited in ('fine','good',):
        ans="Woow! that's cool!"
    elif user_msg_edited[0]=='/':
        list_msg=user_msg_edited.split(' ',1)
        if len(list_msg)==1:
            ans="Please insert parameter after command."
        elif list_msg[0]=='/manual':
            if list_msg[1] in ('s1','1','sem1'):
                ans=sem1text
            if list_msg[1] in ('s2','2','sem2'):
                ans=sem2text
            if list_msg[1] in ('s3','3','sem3'):
                ans=sem3text
            if list_msg[1] in ('s4','4','sem4'):
                ans=sem4text
            if list_msg[1] in ('s5','5','sem5'):
                ans=sem5text
            if list_msg[1] in ('s6','6','sem6'):
                ans=sem6text
        elif list_msg[0]=='/search':
            search_result=[]
            for i in search(list_msg[1],stop=5):
                search_result.append(i)
                return search_result
        elif list_msg[0]=='/youtube':
            search_result=[]
            for i in search(list_msg[1]+' youtube',stop=5):
                search_result.append(i)
            return search_result
        elif list_msg[0]=='/calculate':
            ans=eval(list_msg[1])
    else:
        ans=chatbot.get_response(user_msg.lower()).text
    
    return ans