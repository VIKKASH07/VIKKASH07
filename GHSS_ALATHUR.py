import time
import sys
import os
import signal



def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.005)
#exit("hi")


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
zzz="\003[01;32;40m"
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
os.system('date')
delay_print(f'''
{bbb} ######   ##     ##  ######   ######  
{bbb}##    ##  ##     ## ##    ## ##    ## 
{aaa}##        ##     ## ##       ##       
{aaa}##   #### #########  ######   ######  
{ddd}##    ##  ##     ##       ##       ## 
{ddd}##    ##  ##     ## ##    ## ##    ## 
{ddd} ######   ##     ##  ######   ######{hhh}
_______________________________________________

          {jjj}    πΌππΌππππ     {hhh}  
_______________________________________________


                  [{ccc}ππ   {ddd}α΄ Ιͺα΄α΄α΄sΚ  π°ππ]
 ''')
 
delay_print(f'''
{eee}[{ccc}β’{aaa}]PYTHON --->> 1


{eee}[{ccc}β’{aaa}]C++   --->>> 2


{eee}[{ccc}β’{aaa}]ABOUT --->>> 3


{eee}[{ccc}β’{aaa} EXIT  --->>> 0


''') 
a=input(f'{ddd} ENTER number= ') 

if a=='1'or a=='01':
    i=0
    while True:
        os.system('clear')
        os.system('date')
        delay_print(f'''
{bbb} ######   ##     ##  ######   ######  
{bbb}##    ##  ##     ## ##    ## ##    ## 
{aaa}##        ##     ## ##       ##       
{aaa}##   #### #########  ######   ######  
{ddd}##    ##  ##     ##       ##       ## 
{ddd}##    ##  ##     ## ##    ## ##    ## 
{ddd} ######   ##     ##  ######   ######{hhh}
_______________________________________________

          {jjj}    πΌππΌππππ     {hhh}  
_______________________________________________


                  [{ccc}ππ   {ddd}α΄ Ιͺα΄α΄α΄sΚ  π°ππ] ''') 
        delay_print(f'''
{eee}[{ccc}β’{aaa}]PYTHON RUN      --->> 1


{eee}[{ccc}β’{aaa}] PYTHON SETUP ---->>> 2


{eee}[{ccc}β’{aaa}] BACK          --->>>95





          ''')
          
        b=input (f'ENTER number = ')
        if b=='1' or b=='01':
             os.system('''cd Desktop 
             python  python3.py''')
             break
        elif b =='2' or b=='02':
            os.system('''cd Desktop 
                  touch python3.py
                  ''')
            
            os.system('python  python3.py')
            break
        elif b == '95':
            delay_print('\033[1;92mComing back')
            os.system('sleep 1.0')
            os.system('python GHSS_ALATHUR.py')
            
     
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

          {jjj}    πΌππΌππππ     {hhh}  
_______________________________________________


            [{ccc}ππ   {ddd}α΄ Ιͺα΄α΄α΄sΚ  π°ππ] ''') 
        delay_print(f'''
{eee}[{ccc}β’{aaa}] C ++ RUN      --->> 1


{eee}[{ccc}β’{aaa}] C ++ SETUP  ---->>> 2


{eee}[{ccc}β’{aaa}] BACK         --->>> 95


{eee}[{ccc}β’{aaa}]EXIT          --->>> 00



          ''')
        c=input (f'{jjj}ENTER number  = ')
        if c=='1' or c=='01':
            os.system('''cd Desktop 
                g++ c++.cpp
./a.out  ''')
            break

        elif c =='2' or c=='02':
            os.system('''cd Desktop 
                  touch c++.cpp
                  ''')
            break
        elif c == '95':
            delay_print('\033[1;92mComing back')
            os.system('sleep 1.0')
            os.system('python GHSS_ALATHUR.py')
            
        elif c ==00 or c==0:
            delay_print(f"""
 {jjj}   THANK YOU....
    
 {ccc}  NOW Exiting....""")
            
            exit()
        else:
           delay_print('\n\033[1;92mInvalid input\n')
           os.system('sleep 1.0')
    

elif a=='3' or a=='03':
    while True:
        delay_print(f"""
     ('''γπ¦γγπγγπ©γγπγγπ‘γγπγγπ¦γγπγγπ‘γ


ππ’π₯π‘ π’π¦  π«πΉ-π©πΉπΉ-π π π©πΉ (π­π­.π¬π³.π?π¬π¬π²) 

    π π
__________________________________________________________________________     
{eee}[{ccc}β’{aaa}] BACK          --->>>95


{eee}[{ccc}β’{aaa}]EXIT           --->>>00




    """)
        f=input(f"{jjj}ENTER number :")
        
        if f=='95':
            delay_print('\033[1;92mComing back')
            os.system('sleep 1.0')
            os.system('python GHSS_ALATHUR.py')
        elif f=='00' or f=='0':
            delay_print(f"""
{jjj}    THANK YOU.... 
    
    
{ccc}    NOW Exiting....""")
            os.system('sleep 1.0')
            exit()
    
        else:
	        delay_print('\n\033[1;92mInvalid Input\n')
	        os.system('sleep 1.0')
	        

elif a== 'q' or a== 'Q'or a==00 or a==0:
    delay_print(f"""
{jjj}    THANK YOU.... 
    
    
{ccc}    NOW Exiting....""")
    os.system('sleep 1.0')
    exit()
else:
	delay_print('\n\033[1;92mInvalid Input\n')
	os.system('sleep 1.0')
	os.system('python GHSS_ALATHUR.py')
