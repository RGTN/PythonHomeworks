total_cost=1000000
portion_down_payment=.25
current_savings=0
r=.04
annual_salary=float(input("Annual Salary: "))
portion_saved=float(input("Portion saved every year"))
months=0
down=portion_down_payment*total_cost
semi_annual_raise=.07

while(current_savings<down):
	current_savings+=current_savings*r/12
	current_savings+=annual_salary/12*portion_saved
	months+=1
	if(months%6==0):
	savings+=semi_annual_raise

print("Number of months: "+str(months))
print(str(int(months/12//1))+" Years | "+str(months%12)+" Months")
