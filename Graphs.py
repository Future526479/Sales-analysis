import numpy as np
import matplotlib.pyplot as plt

# Customer_type
# Females
Member = 19
Normal = 10
# Males
Member = 14
Normal = 17
x = np.array(["Female(Member)", "Male(Member)", "Female(Normal)", "Male(Normal)"])
y = np.array([19, 10, 14, 17])
plt.bar(x,y)
plt.title("Customer_type")
plt.grid(axis = 'y')
plt.tight_layout()
plt.savefig('Customer_type_Graph')

# Branch
# Females
a = 10
b = 10
c = 8
x = np.array(["A","B","C"])
y = np.array([10, 10, 8])
plt.bar(x,y)
plt.title("Branch")
plt.grid(axis = 'y')
plt.tight_layout()
plt.savefig('Branch(Female)_Graph')
# Males
a = 13
b = 11
c = 7
x = np.array(["A","B","C"])
y = np.array([13, 11, 7])
plt.bar(x,y)
plt.title("Branch")
plt.grid(axis = 'y')
plt.tight_layout()
plt.savefig('Branch(Male)_Graph')

# Product_line
# Males
Health_&_beauty = 7
Electronic_accessories = 6 
Home_&_lifestyle = 6
Sports_&_travel = 6
x = np.array(["Health_&_beauty","Electronic_accessories","Home_&_lifestyle","Sports_&_travel"])
y = np.array([7, 6, 6, 6])
plt.bar(x,y)
plt.title("Product Line (Male)")
plt.grid(axis = 'y')
plt.tight_layout()
plt.savefig('Product_line(Male)_Graph')
# Females
Health_&_beauty = 5
Electronic_accessories = 6 
Home_&_lifestyle = 5
Sports_&_travel = 3
x = np.array(["Health_&_beauty","Electronic_accessories","Home_&_lifestyle","Sports_&_travel"])
y = np.array([5, 6, 5, 3])
plt.bar(x,y)
plt.title("Product Line (Female)")
plt.grid(axis = 'y')
plt.tight_layout()
plt.savefig('Product_line(Female)_Graph')

# Gender
Female = 29
male  = 31
x = np.array(["Female","Male"])
y = np.array([29, 31])
plt.bar(x,y)
plt.title("Gender")
plt.grid(axis = 'y')
plt.savefig('Gender_Graph')

# Payment
Ewallet = 25
Cash = 21
Credit_card = 14 
x = np.array(["Ewallet","Cash","Credit card"])
y = np.array([25, 21, 14])
plt.bar(x,y)
plt.grid(axis = 'y')
plt.title("Payment")
plt.savefig('Payment_Graph')