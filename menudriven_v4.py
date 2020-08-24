#=========================================================================#
#Problem Statement: "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."

#version : 3.0
#Owner : Jenitha Rashmi
#=========================================================================#
import os
import webbrowser
import time
while True:
    print()
    print("Description:".upper())
    print("===============================================================================================\n")
    print()
    print("This software opens up an application for you only if you give your input as text.".upper())
    print("You can give in the form of a text like : Please Open Google website".upper())
    print()
    print("For ONLINE Applications: You should have internet working in your PC.\nAnd note that ,the configuration checks for following keywords only:Gmail,Whatsapp,Youtube,Google,LinkedIn.If you want to launch any other website you can go for OPTION 3")

    print()
    print("For OFFLINE Applications (i.e Desktop applications) : You dont require internet at all.But my configuration checks for strings like:Chrome,Firefox,Libreoffice,Postman,VirtualBox,Octave,Rhythmbox,AnyDesk,edge,chromium,explore,windows media player,calculator,about windows,administrative tools,c drive,check disk,command prompt,powershell,contacts,date and time,time,excel,file explorer,file history,outlook,paint,powerpoint,narrator,network connection,dvd player,scanner,services,sound setting,task manager,task scheduler,active connection,volume setting,firewall,wordpad,word,notepad,ip data,disk cleaner,control panel,log out,power off,java web starter,python,step recorder,keyboard,math input,console root,exit,quit. If you want to try with different application names other than these names,you can go for OPTION 4\n")
    print("Press 1 : For Online Applications like email,watsapp web,Google")
    print("Press 2 : For Offline Applications like Firefox,chrome,libreoffice etc")
    print("Press 3 : For Launching particular website if not supported in option 1.You should pass only url : https://cliq.zoho.in")
    print("Press 4 : For launching particular desktop application which is not supported in option 2.You should pass only name of your application like firefox'")

    print("===============================================================================================\n")
    print()
    print("Enter you Option here:")
    i = input()
    if i is not None:    
      if int(i) == 1:
        print("Enter your Online Application Text here :\n Eg: Run <app_name> here")
        online_text = input()
        text1 = online_text.lower().replace("'","").replace('"','')
        if (( "dont" not in text1 ) and ( "didnt" not in text1 ) and ( "not" not in text1 ) and ( "no" not in text1 )) :
            if (("run" in text1 ) or ( "execute" in text1 ) or ( "open" in text1 ) or ("launch" in text1)):
                print("**********************************************************************************************\n")
                print("Going to open online application for you.\nPlease make sure you have good internet connection")
                print("I have configured this program to open a website based on the application name you have given in text")
                print("**********************************************************************************************\n")
                if ( "email" in text1 ) or ( "gmail" in text1 ):
                    webbrowser.open('https://www.gmail.com/',new=1,autoraise=True)
                    print("NOTE:\nPlease check your browser")
                    print("Give your emai id and password to open your account")
                elif ( "whatsapp" in text1):
                    webbrowser.open('https://web.whatsapp.com/',new=1,autoraise=True)
                    print("NOTE:\nPlease check your browser")
                    print("Scan the QR code using your mobile whatsapp web feature after connecting your mobile to internet")
                elif ( "google" in text1):
                    webbrowser.open('https://www.google.com/',new=1,autoraise=True)
                    print("NOTE:\nPlease check your browser")
                    print("Type any text in the search tab to perform search operation")
                elif ( "youtube" in text1 ):
                    webbrowser.open('https://www.youtube.com/',new=1,autoraise=True)
                    print("NOTE:\nPlease check your browser")
                    print("Type any text to see the list of videos.\nClick on the video to watch whichever you want")
                elif ( "linkedin" in text1):
                    webbrowser.open('https://www.linkedin.com/',new=1,autoraise=True)
                    print("NOTE:\nPlease check your browser")
                    print("Give your user name and password if not signed in")
                else:
                    print("NOTE:\nSorry !!! \nNo application found !!\nMight be our configuration won't support your requested application !! \nPlease Try again!!.\n*******************Please Try Option 3 for launching particular website*************************")

            else:
                print("NOTE:\nNo key word like run or open or launch or execute is found.\n So I can't understand what action you want me to take")
        else:
            print("NOTE:\nNo application can be opened as you have not requested")


      elif int(i) == 2:
        print("**********************************************************************************************\n")
        print("Please make sure you have set the path under environment variables in your system for lauching offline applications")
        print("If I have to wait here until you set it up: press y else press n")
        print("**********************************************************************************************\n")
        print("Enter your choice (y or n): ")
        wait_option = input()
        if wait_option.lower() == 'y':
            print()
            print("How long should I wait for you?\n")
            print("Please Enter the time in secs:")
            wait_time = input()

            time.sleep(int(wait_time))
        elif wait_option.lower() == 'n':
            print()
            print("I hope you have set the Path")
            print("Let's continue")
            print()
        else:
            print("NOTE:\nYou choice is invalid.So moving forward without waiting")

        print("Enter your Offline Application Text here .\n Eg : Execute <app_name> here")
        offline_text = input()
        text1 = offline_text.lower().replace("'","").replace('"','')
        if (( "dont" not in text1 ) and ( "didnt" not in text1 ) and ( "not" not in text1 ) and ( "no" not in text1 )) :
            if (("run" in text1 ) or ( "execute" in text1 ) or ( "open" in text1 ) or ("launch" in text1)):
                print()
                print("**********************************************************************************************\n")
                print("Going to open offline application for you.")
                print("I have configured this program to open a application based on the application name you have given in text")
                print("**********************************************************************************************\n")
                print()
                if ( "firefox" in text1):
                      os.system("firefox")
                      print("NOTE:\nYour Firefox browser is ready.\nBrowser alone can be launched without internet connection.\nBut you need internet for browsing")
                elif ("octave" in text1):
                      os.system("octave")
                      print("NOTE:\nYour Octave GUI is ready.Please exit from the Octave window if you want to continue further")
                elif ("postman" in text1):
                      os.system("postman")
                      print("NOTE:\nYour Postman application is ready to use")
                elif ("rhythmbox" in text1):
                      os.system("rhythmbox")
                      print("NOTE:\nYour rhythmbox application is ready to use")
                elif ("chrome" in text1):
                      os.system("chrome")
                      print("NOTE:\nYour Chrome browser is ready.\nBrowser alone can be launched without internet connection.\nBut you need internet for browsing")
                elif ("anydesk" in text1):
                      os.system("anydesk")
                      print("NOTE:\nYour AnyDesk application is ready to use")
                elif ("virtualbox" in text1):
                      os.system("virtualbox")
                      print("NOTE:\nYou Virtual Box is ready to be used")
                ############RAJAN'S CODE FOR WINDOWS OFFLINE APPLICATIONS########################
                elif ("edge" in text1):
                      os.system("start microsoft-edge:")
                elif ("chromium" in text1):
                      os.system("chromium-browser")
                elif ("explore" in text1):
                      os.system("iexplore")
                elif((("media" in text1)and("player" in text1))or("mp3 player"in text1) or (("music" in text1)and("player" in text1))):
                      path=input("Can u say me the path where is should find the mp3 player or i will direcly load the player")
                      if(path!=""):
                        os.system("wmplayer"+path)
                      os.system("wmplayer")
                elif("calculator" in text1):
                      os.system("calc")
                elif("about windows" in text1):
                      os.system("winver")
                elif("administrative tools" in text1):
                      os.system("control admintools")
                elif("c drive" in text1):
                      os.system("c:")
                elif("check disk" in text1):
                      os.system("chkdsk")
                elif("command prompt" in text1):
                      os.system("cmd")
                elif("powershell" in text1):
                      os.system("powershell")
                elif("contacts"in text1):
                      os.system("wab")
                elif("date and time" in text1):
                      os.system("timedate.cpl")
                elif("time" in text1):
                      os.system("time")
                elif("excel"in text1):
                      os.system("excel")
                elif("file explorer"in text1)or("file manager" in text1):
                      os.system("explorer")
                elif("file history" in text1):
                      os.system("filehistory")
                elif("outlook"in text1):
                      os.system("Outlook")
                elif("paint" in text1):
                      os.system("mspaint")
                elif("powerpoint" in text1):
                      os.system("powerpnt")
                elif("narrator" in text1):
                      os.system("narrator")
                elif("network connection" in text1):
                      os.system("control netconnections")
                elif("dvd player"in text1):
                      os.system("dvdplay")
                elif("scanner" in text1):
                      os.system("wiaacmgr")
                elif("services" in text1):
                      os.system("services.msc")
                elif("sound setting"in text1):
                      os.system("mmsys.cpl")
                elif("task manager"in text1):
                      os.system("launchtm")
                elif("task scheduler"in text1):
                      os.system("taskschd.msc")
                elif("active connection"in text1):
                      os.system("netstat")
                elif("volume setting"in text1):         
                      os.system("sndvol")
                elif("firewall"in text1):         
                      os.system("firewall.cpl")
                elif("wordpad" in text1):         
                      os.system("wordpad")
                elif("word"in text1):         
                      os.system("word")
                elif("notepad" in text1):         
                      os.system("notepad")
                elif("ip data"in text1):         
                      os.system("ipconfig")
                elif("disk cleaner" in text1):         
                      os.system("cleanmgr")
                elif("control panel"in text1):         
                      os.system("control")
                elif("log out" in text1):         
                      os.system("logoff")
                elif("power off"in text1):         
                      os.system("shutdown /s")
                elif("java web starter" in text1):         
                      os.system("javaws")
                elif("python"in text1):         
                      os.system("python")
                elif("step recorder"in text1):         
                      os.system("psr")
                elif("keyboard"in text1):         
                      os.system("osk")
                elif("math input"in text1):         
                      os.system("mip")
                elif("console root"in text1):         
                      os.system("mmc")
                elif("exit"in text1)or("quit" in text1):         
                      os.system("break")
                #################################################################################
                else:
                    
                      print("NOTE:\nSorry !!! \nNo application found !!\nMight be our configuration won't support your requested application !! \nPlease Try again!!.\n*******************Please Try Option 4 for launching particular application*************************")

            else:
                print("NOTE:\nNo key word like run or open or launch or execute is found.\n So I can't understand what action you want me to take")
        else:
            print("NOTE:\nNo application can be opened as you have not requested")
                          
      elif int(i) == 3:
        print("Please give your website url")
        url_text = input()
        text1 = url_text.lower()
        if text1 is not None:
            webbrowser.open(url=text1,new=1,autoraise=2)
            print("NOTE:\n URL is ready to be viewed")
        else:
            print("NOTE:\nURL should not be none")
        
      elif int(i) == 4:
                      
        print("Enter your application name")
        app_name = input()
        text1 = app_name.lower().replace("'","").replace('"','').replace(" ",'')
        if text1 is not None:
            os.system('"'+text1+'"')
            print("NOTE:\n Application is ready to be used")
        else:
            print("NOTE:\nApplication Name should not be None")

      else:
        print("NOTE:\nIt is not a valid application option")
    else:
      print("NOTE:\nPlease enter a valid option\n")

    print()
    print("++++++++++++++++++++++!!!! IT IS DONE !!!!++++++++++++++++++++++++++++++\n")
    print()
    print("Next Trial Begins.\nDont forget to read the \"NOTE\" about the previous trial.")
    print()
    print("Do you want to continue:\nPress y or n: ")
    op = input()
    if op.lower() == 'y':
        continue
    else:
        break

    print()
    
