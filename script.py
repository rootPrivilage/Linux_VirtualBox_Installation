import os
import sys, traceback
def mainWindow():
    try :


        def mainMenu():
            while True:
                os.system("clear")
                os.system("clear")

                print("\033[1;36m ****************** Main Menu ********************\033[1;32m")

                print('''
1) Fedora
2) CentOS/Rhel
3) Ubuntu/Mint/Debian
4) Manjaro/Arch 

''')

                mMenu=input("\033[1;31mMain-Menu >>\033[1;32m")

                if mMenu=="1":

                    while mMenu=="1" :
                        os.system("sudo cd /etc/yum.repos.d/")
                        os.system("sudo wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo")
                        os.system("sudo yum update")
                        os.system("sudo dnf install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-devel dkms qt5-qtx11extras libxkbcommon")
                        os.system("sudo dnf install VirtualBox-6.0")                        
                        os.system("sudo /usr/lib/virtualbox/vboxdrv.sh setup")
                        cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m")


                elif mMenu=="2":
                    while mMenu=="2" :
                        os.system("clear")
                        os.system("clear")
                        print("\033[1;36m ****************** CentOS/RHEL ********************\033[1;32m")
                        print("\033[1;36m  home --> Home Menu    back--->Previous Menu \033[1;32m")
                        print('''

1)CentOs-6/RHEL-6
2)CentOs-7/RHEL-7
                           ''')

                        mMenu1=input("\033[1;31mCentOs/Rhel >>\033[1;32m")
                        if mMenu1=="1":
                            os.system("sudo cd /etc/yum.repos.d/")
                            os.system("sudo wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo")
                            os.system("sudo yum update")
                            os.system("sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm")
                            os.system("sudo yum install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-PAE-devel dkms")
                            os.system("sudo yum install VirtualBox-6.0")
                            os.system("sudo /etc/init.d/vboxdrv setup")
                            os.system("sudo service vboxdrv setup")
                            cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m")
                            

                        elif mMenu1=="2":
                            os.system("sudo cd /etc/yum.repos.d/")
                            os.system("sudo wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo")
                            os.system("sudo yum update")
                            os.system("sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm")
                            os.system("sudo yum install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-PAE-devel dkms")
                            os.system("sudo yum install VirtualBox-6.0")
                            os.system("sudo /etc/init.d/vboxdrv setup")
                            os.system("sudo service vboxdrv setup")
                            cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m")  

                        elif mMenu1=="home":
                            mainMenu()

                        elif mMenu1=="back":
                            mainMenu()

                        else:
                            cont=input("\033[1;33m Invalid Input Press Enter To continue \033[1;32m")



                elif mMenu=="3":
                    while mMenu=="3" :
                        os.system("clear")
                        os.system("clear")
                        print("\033[1;36m ****************** Ubuntu/Mint/Debian ********************\033[1;32m")
                        print("\033[1;36m  home --> Home Menu    back--->Previous Menu \033[1;32m")
                        print('''  

1) Ubuntu-16/Mint-18
2) Ubuntu-18/Mint-19/Debian-10

                            ''')
                        mMenu1=input("\033[1;31mUbuntu/Mint/Debain >>\033[1;32m")

                        if mMenu1=="1":
                            os.system("sudo wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
                            os.system('''sudo add-apt-repository “deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian xenial contrib''')
                            os.system("sudo yum update")
                            os.system("sudo apt install virtualbox-6.0")
                            cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m")
                            

                        elif mMenu1=="2":
                            os.system("sudo wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
                            os.system('''sudo add-apt-repository “deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian bionic contrib''')
                            os.system("sudo yum update")
                            os.system("sudo apt install virtualbox-6.0")
                            os.system("sudo service vboxdrv setup")
                            cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m") 

                        elif mMenu1=="home":
                            mainMenu()

                        elif mMenu1=="back":
                            mainMenu()


                elif mMenu=="4":
                    while mMenu=="4" :
                        os.system("sudo pacman -Syu")
                        os.system("sudo pacman -S virtualbox")
                        os.system("sudo echo ""type: vboxdrv"" >> /etc/modules-load.d/virtualbox.conf")
                        os.system("sudo lsmod | grep vboxdrv")
                        cont=input("\033[1;36m \n\n Press Enter to continue \033[1;32m")


                else:
                    cont=input("\033[1;33m Invalid Input Press Enter To continue \033[1;32m")
        

        mainMenu()
        

    



    except KeyboardInterrupt:
        print ("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    mainWindow()
