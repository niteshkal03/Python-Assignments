# 5. Task: Salary Calculation 
# ● Objective: You have to calculate an employee's salary by computing the gross 
# salary tax and net salary based on the given parameters. 
# ● Hints: 
# ○ Base Salary = ₹50000 
# ○ Bonus = ₹5000 
# ○ Tax Rate = 10%  
# ○ Other Charges = ₹2000 
# Display the Gross Salary Tax and Net Salary.

base_Salary = 50000
bonus = 5000 
tax_rate = 10 
other_charges = 2000

print(f"Base Salary (Rs.): {base_Salary}")
print(f"Bonus (Rs.): {bonus}")
print(f"Tax Rate (%): {tax_rate}")
print(f"Other Charges (Rs.): {other_charges}")
print()

gross_salary = base_Salary + bonus
print(f"Gross Salary (Rs.): {gross_salary}")
print("="*30)

gross_salary_tax = gross_salary / tax_rate
print(f"Gross Salary Tax (Rs.): {int(gross_salary_tax)}")

net_salary = gross_salary - gross_salary_tax - other_charges
print(f"Net Salary (Rs.): {int(net_salary)}")
