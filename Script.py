class script(object):
    START_TXT = """👋𝖧𝖾𝗅𝗅𝗈 {}!!🎉

𝖨𝗆 <b>𝖠𝗎𝗍𝗈-𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍</b> 𝖨 𝖼𝖺𝗇 𝖲𝖾𝗇𝖽 𝗒𝗈𝗎 𝖬𝗈𝗏𝗂𝖾 𝗂𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌.!!

𝖨 𝖼𝖺𝗇 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝗆𝗈𝗏𝗂𝖾𝗌 𝖺𝗇𝖽 𝗐𝖾𝖻-𝗌𝖾𝗋𝗂𝖾𝗌 𝗂𝗇 𝖸𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌. 𝖨𝗍𝗌 𝖤𝖺𝗌𝗒 𝗍𝗈 𝖴𝗌𝖾 𝗆𝖾 𝖩𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝖺𝗌 𝖺𝖽𝗆𝗂𝗇 𝗍𝗁𝖺𝗍𝗌 𝖺𝗅𝗅 𝗂 𝗐𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾.!!"""
    HELP_TXT = """<b><u>𝖧𝖾𝗒 {}</u></b>
𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝗁𝖾𝗅𝗉 𝖿𝗈𝗋 𝗆𝗒 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌.!🎉"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    OWNER_TXT = """<b>○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=https://t.me/TG_x_filter>🇮🇳❍ 𝖒𝖆𝖓𝖙𝖎𝖘 ❍™◢ ◤</a></b>"""
    
    HOWTOUES_TXT ="""<b>‼️ <u>𝖨𝗇𝗌𝗍𝗋𝗎𝖼𝗍𝗂𝗈𝗇𝗌</u> ‼️</b>

<b>𝖧𝗈𝗐 𝗍𝗈 𝖺𝖽𝖽 𝗆𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉?</b>

• 𝖢𝗈𝗉𝗒 𝗆𝗒 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝗈𝗋 𝖢𝗅𝗂𝖼𝗄 𝗈𝗇 𝖺𝖽𝖽 𝖦𝗋𝗈𝗎𝗉 » 𝖦𝗈 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖺𝖽𝗆𝗂𝗇𝗂𝗌𝗍𝗋𝖺𝗍𝗈𝗋 𝗌𝖾𝗍𝗍𝗂𝗇𝗀𝗌 » 𝖢𝗅𝗂𝖼𝗄 𝖠𝖽𝖽 𝖺𝖽𝗆𝗂𝗇 » 𝖦𝗂𝗏𝖾 𝖺𝗅𝗅 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇𝗌 » 𝖢𝗅𝗂𝖼𝗄 𝗍𝗂𝖼𝗄 𝗆𝖺𝗋𝗄 » 𝖣𝗈𝗇𝖾
• 𝖳𝗁𝖾𝗇 𝗎𝗌𝖾 /connect 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉
• 𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖨 𝖶𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖥𝗂𝗅𝗆𝗌 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉

<b>‼️ <u>നിർദ്ദേശങ്ങൾ</u> ‼️</b>

<b>നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ എങ്ങനെ ചേർക്കാം?</b>

• എന്റെ ഉപയോക്തൃനാമം പകർത്തുക അല്ലെങ്കിൽ ആഡ് ഗ്രൂപ്പ് ക്ലിക്ക് ചെയ്യുക » നിങ്ങളുടെ ഗ്രൂപ്പ് അഡ്മിനിസ്ട്രേറ്റർ ക്രമീകരണങ്ങളിലേക്ക് പോകുക » അഡ്മിനെ ചേർക്കുക ക്ലിക്ക് ചെയ്യുക » എല്ലാ അനുമതികളും നൽകുക » ടിക്ക് മാർക്ക് ക്ലിക്ക് ചെയ്യുക » പൂർത്തിയായി
• തുടർന്ന് നിങ്ങളുടെ ഗ്രൂപ്പിൽ /connect കമാൻഡ് ഉപയോഗിക്കുക
• വിജയകരം നിങ്ങളുടെ ഗ്രൂപ്പ് അംഗങ്ങൾക്കായി ഞാൻ സിനിമകൾ നൽകുന്നതാണ്"""
    REQINFO = """• 𝖬𝗈𝗏𝗂𝖾𝗌 - 𝖫𝗎𝖼𝗂𝖿𝖾𝗋 2019 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆 
    
• 𝖲𝖾𝗋𝗂𝖾𝗌 - 𝖫𝗎𝖼𝗂𝖿𝖾𝗋 𝖲01𝖤01

• 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗂𝗇 𝖤𝗇𝗀𝗅𝗂𝗌𝗁 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖮𝗇𝗅𝗒 𝖠𝗇𝖽 ❎ 𝖣𝗈𝗇'𝗍 𝖴𝗌𝖾 𝖲𝗍𝗒𝗅𝗂𝗌𝗁 𝖥𝗈𝗇𝗍 

• 𝖭𝗈𝗍 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖳𝗁𝖾𝖺𝗍𝖾𝗋 𝖯𝗋𝗂𝗇𝗍 𝖥𝗂𝗅𝖾𝗌.!"""
    
    CAPTION = """<b><code>{file_name}</code></b>
    
<b>╔═══ 𝖩𝗈𝗂𝗇 𝖶𝗂𝗍𝗁 𝖴𝗌 ═══╗
▣ 𝖩𝗈𝗂𝗇 : [𝖦𝗋𝗈𝗎𝗉 1️⃣](https://t.me/Mallu_Movie_Hub_Group)
▣ 𝖩𝗈𝗂𝗇 : [𝖦𝗋𝗈𝗎𝗉 2️⃣](https://t.me/+iEbhY7mM4oE1OTVl)
╚═══ 𝖩𝗈𝗂𝗇 𝖶𝗂𝗍𝗁 𝖴𝗌 ═══╝</b>"""
