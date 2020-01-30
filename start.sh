#!/bin/bash
clear
if [[ -s update.4nat ]];then
echo "All Requirements Found...."
echo -e "\e[1;32m Reborn \e[0m"
echo "Press Enter To Continue"
read a1
clear
else
echo 'Installing Requirements....'
echo .
fi
toilet -f mono12 -F border 4NAT
echo -e "\e[4;34m 1- Termux \e[0m"
echo -e "\e[4;34m 2- Other Linux OS. \e[0m"
read numb
if [ $numb = "1" ]
then

	pkg install python
	pkg install python3
	pkg install python3-pip
	pkg install dos2unix
	pip3 install requests
	pip3 install colorama
        pip3 install -r requirements.txt
	cp ~/Reborn/sms.py /data/data/com.termux/files/usr/bin/Reborn
	dos2unix /data/data/com.termux/files/usr/bin/Reborn
	chmod 777 /data/data/com.termux/files/usr/bin/Reborn


echo Made By 4NAT >update.4nat
echo Requirements Installed....
echo Press Enter To Continue...
read upd
python sms.py
	else
		echo "Inavlid İnput!!!"
	fi
