import datetime 
from today_special import today_is


today=datetime.datetime.now()
d2 = today.strftime("%B %d, %Y")

helptext='''
    &#127979 <b>I can help you to get Educational help Related to KKWP and much more, 
you can visit<a href='https://poly.kkwagh.edu.in/'> Official KKWP website</a></b>&#127979
    \n\n<b>You can Control me with these commands</b>
    \n/start - Starts KKWP chat bot\n/help - Get detailed information about commands
    \n<b>General Commands</b>\n/today - Returns current Day info\n/website - Returns KKWP Official Website\n/msbte - Returns MSBTE Official Website\n/search [parameters] - Returns search result (eg. /search kkwp)
    \n<b>Educational Commands</b>
/manual - Get Manuals of all sem (eg. /manual sem1)
/search - Search information on google (eg. /search query)
/calculate - Calculation for genral purpose (eg. /calculate 2+3)
/compile - Compiles python code just tag the code message or file
'''


msbte_cmd='''MSBTE Home : <a href='http://msbte.org.in/'>Website</a>
Online Activities : <a href='https://msbte.org.in/online_activities.html'>Website</a>
Curriculum Search : <a href='https://msbte.org.in/portal/curriculum-search/'>Website</a>
Results : <a href='https://msbte.org.in/DISRESLIVE2021CRSLDSEP/frmALYSUM21PBDisplay.aspx'>Website</a>
'''

todaytext='''Today's Date: {0}
Today's Day : {1}
Today's events: 
<b>1 : {2}</b>
<b>2 : {3}</b>
<b>3 : {4}</b>
<b>4 : {5}</b>
<b>5 : {6}</b>
'''.format(d2,
datetime.datetime.today().strftime('%A'),today_is()[0],
today_is()[1],today_is()[2],today_is()[3],
today_is()[4])