#coding:gbk
import random

def name_to_number(name):
	if name=="ʯͷ":
		return(0)
	elif name=="ʷ����":
		return(1)
	elif name=="��":
		return(2)
	elif name=="����":
		return(3)
	else:
		return(4)
	
	
def number_to_name(number):
	if number==0:
		return("ʯͷ")
	elif number==1:
		return("ʷ����")
	elif number==2:
		return("��")
	elif number==3:
		return("����")
	else:
		return("����")
	

def rpsls(num1,num2):
	if num1-num2==-4 or num1- num2==-3 or num1-num2==1 or num1-num2==2:
		print("��Ӯ��!") 
	elif num1==num2:
		print("ƽ��!")
	else:
		print("����Ӯ��!")


player_choice=input("����������ѡ��:")
while  player_choice in ["ʯͷ","����","��","����","ʷ����"]:
	print("----------------")
	player_choice_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("����ѡ��Ϊ:",player_choice)
	print("�������ѡ��Ϊ:",comp_choice)
	rpsls(player_choice_number,comp_number)
	break
else:
	print("Error: No Correct Name")
	

