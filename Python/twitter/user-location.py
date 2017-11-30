#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "WmaaU1DLmJa3UG8cN7BUaHPoU"
consumer_secret = "RGl2IZPh6vi4GsG2tXIbWKlgo9siK3tFB6ozVbo2KWZSlbCDWS"
access_key = "48714232-gBXGnc3aXBi1dQBzIeaQ56BDi1mR2d7vUi5329bOJ"
access_secret = "3PaOtlyFroigW8bKsqQURCKbnNTJtecqlaHNtNtc1BwRn"

users = ["SjSrwillis06","SKComputing","smatheny80","smgllc1312","smgrobsmith","Smithcalvind","SmithSailruner","smithsj1","SMOORE2o18","smoothdelicious","smoothdelicious","SnoopFog2377","SnowflakeDruid","snowwolf1313","snowwolf1313","Soapfangh50","Soapfangh50","Soapfangh50","SoCalLeonardo","SoCalSuzanna","sodajunkie","sodajunkie","sodajunkie","songlibah","Sorrells2Don","SoSofieFatale","sotokai","Southpaw253","Spiderhaze22766","Steele_McQuaid","stephens_ben","Steve50G","stevemincer","stillsalty_12","Stlelaine","StormFrontWX","Stormy60","Subachef","Sujube","surfnjohn","SusanKuta2","Suthen_boy","SuzanGregory2","sw_dad","SwordfishParm","SwordfishParm","swtimogenation","t_m_f_rd","t_m_f_rd","Tadache","tamraakanana","Tani98245","Tatoskins","taxwiz12","Taylor_A_Wiens","TBrondolo","tcentric","TeaPartyAussie","techyheads","ted_karman","TedRizen","TedRizen","TedschwartzJGRE","tejana1234","tekker44","TEmiliusen","Teressastone4","Teressastone4","terryr610","TexasFatAss","thakingDini","thankyouDonald1","thankyouDonald1","thankyouDonald1","thankyouDonald1","the1ladycham","the1ladycham","theanayeli","TheDayTrade","TheDonnnieSharp","thegarshow","TheGoodGuy2016","themostmitsos","TheOath","theoliviafaas","therealbradg","TheRealDonald4","TheRealSlimDon1","therealsmw512","TheRightShift","TheUrbanEntity","TheXpozer1","thorton311","thugsRbadMK","thumper911911","tierneymichele","timmie4reel","TimTward004","tinkymoo4","tm00123","TMoneyLu","toddstarnes","toftheangels","tolovana66","tolovana66","TomDono82526643","TonyaBr04239217","TrafficAdPays","travisjlewallen","travisjlewallen","travisjlewallen","tressairis","trigtrader","trish_bradshaw","Troybaker56","TRUMP_IS_WINNER","Trump45_","Trumps_Cowgirls","TrumpStayTrue","TRUMPTexas123","TRUMPTexas123","TrumpTrain4444","TrumpTrain4444","TrumpTrain4444","TrumpTrain4444","TrumpTrain4444","TrumpTrain4444","TrumpTrain4444","trustthetruth16","truth_american","truthbrulee","truthteller213","truthteller213","truthteller213","truthvsthelies","ttreakle1","ttreakle1","ttreakle1","ttreakle1","TurtsBlues","TVsAndyDaly","TwaddictsRUs","tweet4snowden","TwoCrows59","txfinest13","txlady706","TylerBaniak","UF2","UgglaD","uhatemebro","ultprivacy","umpire43","UndyingCunt","unfilteredguy1","Ureagletz","USAsweetheart30","USAsweetheart30","USfullofAs","USfullofAs","vadtrav62","Vascoaztec","VeeVee","Versailles56","Veteren1971","virgosiempre1","virgosiempre1","virgosiempre1","virgosiempre1","virgosiempre1","visionary831","vntgplgrnd","vntgplgrnd","voiceofforex","vol4life999","vonehmsen57","Wadinator1","wakey1160","WalshFreedom","WalshFreedom","wambamdrebel","WarrenTrammell","WarrenTrammell","wayjones","wayjones","We3forDemocracy","whistletune65","whitt_rob","WikiTrumps1776","wildauburnrebel","WildManRan","williambussie","williambussie","Willief25525906","WillisAthGA","WillisAthGA","WillisAthGA","wiseones1nj24","Wishchild87","wkemp138","WomenSupermoto","woofeous","woofeous","WordJulia","wuxeter","wv7771946","wyatt1983","WyattAmazing","xcaliber12345","xxxboston","y0mamasec","y0mamasec","Y1pkhb","YahooDanny","YefimPodokshik","yipper_merry","yourcluelessnow","yreme_jensen","zemantoni","zenstitcher","zionfanatic","ZJabotinsky","ZzeonBlue"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

for loc in users:
    print(api.get_user(screen_name=loc).profile_location)
    print(loc)
