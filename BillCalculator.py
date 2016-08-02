bill = float(raw_input("bill amount? "))            

def tip():
	global bill
	user_tip_input=float(raw_input("What percent of bill do you want as your tip? "))
	tip_percentage=user_tip_input/100
	tip_amount =tip_percentage*bill 
	return tip_amount

def total_bill():
	global bill 
	got_tip=tip()
	total_bill=bill + got_tip 
	return total_bill

def split_bill():
	number_of_people = int(raw_input("how many people? "))	
	total_bill_amount = total_bill()
	return total_bill_amount/number_of_people
print split_bill()
