total_cost=1000000
portion_down_payment=.25
current_savings=0
r=.04
annual_salary=float(input("Annual Salary: "))
portion_saved=random.randint(0,10000)
months=0
down=portion_down_payment*total_cost
semi_annual_raise=.07

while(current_savings<down):
	current_savings+=current_savings*r/12
	current_savings+=annual_salary/12*portion_saved
	months+=1
	if(months%6==0):
		savings+=semi_annual_raise
