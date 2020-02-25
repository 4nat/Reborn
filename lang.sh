toilet -f mono12 -F border 4NAT
echo -e "\e[4;34m 1- continue with english. \e[0m"
echo -e "\e[4;34m 2- türkce devam et. \e[0m"
read numb
if [ $numb = "1" ]
then
clear
python sms.py
echo en >.en
if [ $numb = "2" ]
then
clear
python .tr.py
echo TR >.tr

	else
		echo "Inavlid İnput!!!"
	fi
fi
