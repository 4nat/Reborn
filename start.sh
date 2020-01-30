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
toilet -f mono12 -F border 4NAT
echo -e "\e[4;36m 01- Turkish \e[0m"
echo -e "\e[4;36m 02- English\e[0m"
read numb
if [ $numb = "01" ]
then
echo -e "\e[4;34m Cok Yakinda Türkçe Sürümü Sizlerle ! \e[0m"
python sms.py
if [ $numb = "02" ]
	then
python sms.py
	if [ $numb = "2" ]
	then

		if [ "$(whoami)" != 'root' ]; then
			echo "Non-root!! (sudo sh ~/Reborn/start.sh)"
			exit
		else
			apt install python3 python3-pip dos2unix
			pip3 install requests
			pip3 install colorama
			cp ~/Reborn/sms.py /usr/bin/Reborn
			dos2unix /usr/bin/Reborn
			chmod 777 /usr/bin/
			Reborn
		fi
	else
		echo "Inavlid İnput!!!"
	fi
fi
done
