from colorama import Fore
import program_guests
import program_hosts
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return


def print_header():
    snake = \
        """
             ~8I?? OM               
            M..I?Z 7O?M             
            ?   ?8   ?I8            
           MOM???I?ZO??IZ           
          M:??O??????MII            
          OIIII$NI7??I$             
               IIID?IIZ             
  +$       ,IM ,~7??I7$             
I?        MM   ?:::?7$              
??              7,::?778+=~+??8       
??Z             ?,:,:I7$I??????+~~+    
??D          N==7,::,I77??????????=~$  
~???        I~~I?,::,77$Z?????????????  
???+~M   $+~+???? :::II7$II777II??????N 
OI??????????I$$M=,:+7??I$7I??????????? 
 N$$$ZDI      =++:$???????????II78  
               =~~:~~7II777$$Z      
                     ~ZMM~ """

    print(Fore.WHITE + '****************  SNAKE BnB  ****************')
    print(Fore.GREEN + snake)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Snake BnB!")
    print("Why are you here?")
    print()


def find_user_intent():
    print("[g] Book a cage for your snake")
    print("[h] Offer extra cage space")
    print()
    choice = input("Are you a [g]uest or [h]ost? ")
    if choice == 'h':
        return 'offer'

    return 'book'


if __name__ == '__main__':
    main()
