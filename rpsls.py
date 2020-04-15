#coding:gbk
import random

def name_to_number(name):
	if name=="石头":
		return(0)
	elif name=="史波克":
		return(1)
	elif name=="布":
		return(2)
	elif name=="蜥蜴":
		return(3)
	else:
		return(4)
	
	
def number_to_name(number):
	if number==0:
		return("石头")
	elif number==1:
		return("史波克")
	elif number==2:
		return("布")
	elif number==3:
		return("蜥蜴")
	else:
		return("剪刀")
	

def rpsls(num1,num2):
	if num1-num2==-4 or num1- num2==-3 or num1-num2==1 or num1-num2==2:
		print("您赢了!") 
	elif num1==num2:
		print("平局!")
	else:
		print("机器赢了!")


player_choice=input("请输入您的选择:")
while  player_choice in ["石头","剪刀","布","蜥蜴","史波克"]:
	print("----------------")
	player_choice_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("您的选择为:",player_choice)
	print("计算机的选择为:",comp_choice)
	rpsls(player_choice_number,comp_number)
	break
else:
	print("Error: No Correct Name")
	

