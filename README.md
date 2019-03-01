#### for eazy install execute the python Script :
        


# Linux_VirtualBox_Installation

### For Fedora-29/28/27/26 users:
    1) su (Then Enter your password)
    2) cd /etc/yum.repos.d/
    3) wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo
    4) yum update

  #### -- Installing dependency for virtualbox
      a) dnf install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-devel dkms qt5-qtx11extras libxkbcommon     
      b) dnf install VirtualBox-6.0    
      c) /usr/lib/virtualbox/vboxdrv.sh setup
      d) usermod -a -G vboxusers user_name (add your username instead of "user_name")

### CentOS 7.5/6.10 & Red Hat (RHEL) 7/6 users:

    1) su (Then Enter your password)
    2) cd /etc/yum.repos.d/
    3) wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
    4) yum update

  #### -- Installing dependency for virtualbox
  
      a) rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm (for CentOS-7/Rhel-7) 
      
      b) rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm (for CentOS-6/Rhel-6)
      
      c) yum install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-devel dkms
      
      d) ( PAE kernel users install ) 
         yum install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-PAE-devel dkms
         
      e) yum install VirtualBox-6.0
      
      f) /etc/init.d/vboxdrv setup (OR  service vboxdrv setup )
      
      g) usermod -a -G vboxusers user_name (add your username instead of "user_name")
      
      
### For Ubuntu/Mint/Debian users:

    1) wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
    
    2) sudo add-apt-repository “deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian bionic contrib
    (For Ubuntu-18/Mint-19 Users)
    
    3)  sudo add-apt-repository “deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian xenial contrib
    (For Ubuntu-16/Mint-18 Users)
    
    4) sudo apt update && sudo apt install virtualbox-6.0

### For Manjaro/Arch users:

    1) sudo pacman -Syu
    2) sudo pacman -S virtualbox

###### We can manually load the kernel module with the following command:

     sudo modprobe vboxdrv
    
###### make the vboxdrv module autoload on system boot

     1) sudo nano /etc/modules-load.d/virtualbox.conf
     2) type: vboxdrv
     4) Ctl+x
     5) y
  
###### to check module is loaded automatically 
    sudo lsmod | grep vboxdrv



