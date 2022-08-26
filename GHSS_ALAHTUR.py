import time
import sys
import os
import signal



def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.005)


aaa="\033[0;30m"
bbb="\033[0;31m"
ccc="\033[1;31m"
ddd="\033[0;32m"
eee="\033[1;32m"
fff="\033[0;33m"
ggg="\033[1;33m"
iii="\033[0;34m"
hhh="\033[1;34m"
jjj="\033[0;35m"
kkk="\033[1;35m"
yyy="\033[0;36m"
sss="\033[1;36m"
xxx="\033[0;37m"



# Text Color 
zzz="\003[0;32;40m"
zzz2="\003[0;32m"
print (zzz)
delay_print(f'''
{aaa}  #####  #     #  #####   #####  
{bbb} #     # #     # #     # #     # 
{ccc} #       #     # #       #       
{ddd} #  #### #######  #####   #####  
{eee} #     # #     #       #       # 
{ggg} #     # #     # #     # #     # 
{iii}  #####  #     #  #####   #####  
                                 ''')
                                 
os.system('clear')
delay_print(f'''
{bbb} ######   ##     ##  ######   ######  
{bbb}##    ##  ##     ## ##    ## ##    ## 
{aaa}##        ##     ## ##       ##       
{aaa}##   #### #########  ######   ######  
{ddd}##    ##  ##     ##       ##       ## 
{ddd}##    ##  ##     ## ##    ## ##    ## 
{ddd}######   ##     ##  ######   ######{hhh}
_______________________________________________

          {jjj}    𝘼𝙇𝘼𝙏𝙃𝙐𝙍     {hhh}  
_______________________________________________


                  [{ccc}𝐁𝐘   {ddd}ᴠɪᴋᴋᴀsʜ  𝙰𝚃𝚁]
 ''')
 
delay_print(f'''
{eee}[{ccc}•{aaa}]PYTHON --->> 1


{eee}[{ccc}•{aaa}]C++   --->>> 2


{eee}[{ccc}•{aaa}]ABOUT --->>> 3


{eee}[{ccc}•{aaa}]EXIT  --->>> 0
''') 
a=input(f'{ddd} ENTER number= ') 

if a=='1'or a=='01':
    i=0
    while True:
        os.system('clear')
        delay_print(f'''
{bbb} ######   ##     ##  ######   ######  
{bbb}##    ##  ##     ## ##    ## ##    ## 
{aaa}##        ##     ## ##       ##       
{aaa}##   #### #########  ######   ######  
{ddd}##    ##  ##     ##       ##       ## 
{ddd}##    ##  ##     ## ##    ## ##    ## 
{ddd} ######   ##     ##  ######   ######{hhh}
_______________________________________________

          {jjj}    𝘼𝙇𝘼𝙏𝙃𝙐𝙍     {hhh}  
_______________________________________________


                  [{ccc}𝐁𝐘   {ddd}ᴠɪᴋᴋᴀsʜ  𝙰𝚃𝚁] ''') 
        delay_print(f'''
{eee}[{ccc}•{aaa}]PYTHON RUN      --->> 1


{eee}[{ccc}•{aaa}] PYTHON SETUP ---->>> 2


{eee}[{ccc}•{aaa}] BACK          --->>>95


{eee}[{ccc}•{aaa}]EXIT           --->>>00
          ''')
          
        b=input (f'ENTER number = ')
        if b=='1' or b=='01':
             os.system('''cd Desktop 
             python  python3.py''')
            
        elif b =='2' or b=='02':
            os.system('''cd Desktop 
                  touch python3.py
                  ''')
            
            os.system('python  python3.py')
        elif b == '95':
            delay_print('\033[1;92mComing back')
            os.system('sleep 1.0')
            os.system('python GHSS_ALAHTUR.py')
            
        elif b== 'q' or b == 'Q'or b ==00 or b==0:
            delay_print(f"""
{jjj}    THANK YOU..... 
    
    .. 
{ccc}   NOW Exiting.....""")
            os.system('sleep 1.0')
            exit()
        else:
            delay_print('\n\033[1;92mInvalid input\n')
            os.system('sleep 1.0')
    
elif a=='2' or a=='02':
    
    while True:
        os.system('clear')
        delay_print(f'''
{bbb} ######   ##     ##  ######   ######  
{bbb}##    ##  ##     ## ##    ## ##    ## 
{aaa}##        ##     ## ##       ##       
{aaa}##   #### #########  ######   ######  
{ddd}##    ##  ##     ##       ##       ## 
{ddd}##    ##  ##     ## ##    ## ##    ## 
{ddd}######   ##     ##  ######   ######{hhh}
_______________________________________________

          {jjj}    𝘼𝙇𝘼𝙏𝙃𝙐𝙍     {hhh}  
_______________________________________________


            [{ccc}𝐁𝐘   {ddd}ᴠɪᴋᴋᴀsʜ  𝙰𝚃𝚁] ''') 
        delay_print(f'''
{eee}[{ccc}•{aaa}] C ++ RUN      --->> 1


{eee}[{ccc}•{aaa}] C ++ SETUP  ---->>> 2


{eee}[{ccc}•{aaa}] BACK          --->>>95


{eee}[{ccc}•{aaa}]EXIT           --->>>00
          ''')
        c=input ('ENTER number  = ')
        if c=='1' or c=='01':
            os.system('''cd Desktop 
                g++ c++.cpp
./a.out  ''')


        elif c =='2' or c=='02':
            os.system('''cd Desktop 
                  touch c++.cpp
                  ''')

        elif c == '95':
            delay_print('\033[1;92mComing back')
            os.system('sleep 1.0')
            os.system('python GHSS_ALAHTUR.py')
            break
        elif c== 'q' or c == 'Q'or c ==00 or c==0:
            delay_print(f"""
 {jjj}   THANK YOU....
    
    
 {ccc}  NOW Exiting....""")
            os.system('sleep 1.0')
            exit()
        

elif a=='3' or a=='03':
    delay_print(f"""
     ('''【𝗦】【𝗜】【𝗩】【𝗔】【𝗡】【𝗘】【𝗦】【𝗔】【𝗡】


𝗕𝗢𝗥𝗡 𝗢𝗦  𝗫𝗹-𝗩𝗹𝗹-𝗠𝗠𝗩𝗹 (𝟭𝟭.𝟬𝟳.𝟮𝟬𝟬𝟲) 

    😎 😉
    


    """)
elif c== 'q' or c == 'Q'or c ==00 or c==0:
    delay_print(f"""
{jjj}    THANK YOU.... 
    
    
{ccc}    NOW Exiting....""")
    os.system('sleep 1.0')
    exit()
else:
	delay_print('\n\033[1;92mInvalid Input\n')
	os.system('sleep 1.0')
	os.system('python basicx.py')
