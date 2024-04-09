# Alexander Tran
# 2/29/24
# An online shopping app that sells digital and physical merchandise

def main():
	#ask the user for information
		#ask the user for the physical items
	name1 = input("What is the name of your first physical item?")
	price1 = float(input("What is the price of your first physical item?"))
	name2 = input("What is the name of your second physical item?")
	price2 = float(input("What is the price of your second physical item?"))
	name3 = input("What is the name of your third physical item?")
	price3 = float(input("What is the price of your third physical item?"))
		#ask the user for the digital items
	name4 = input("What is the name of your first digital item?")
	price4 = float(input("What is the price of your first digital item?"))
	name5 = input("What is the name of your second digital item?")
	price5 = float(input("What is the price of your second digital item?"))
	
	#calculate the subtotals and totals
		#physical items
	subtotalPhys = (price1 + price2 + price3)
	totalPhys = ((subtotalPhys) + 5.99) * 1.065
		#digital items
	subtotalDig = (price4 + price5)
	totalDig = (subtotalDig * 1.065)
		#find the total and subtotal of the entire order
	finalSubtotal = subtotalDig + subtotalPhys
	finalTotal = totalDig + totalPhys
	
	#create receipt
	print("=======================================")
	print("				WALMAZON")
	print("=======================================")
	print("Thank you for shopping at Walmazon! Here is a recap of your purchase!")
	print("_____________________________________")
	print("Physical Items:")
	print(name1 + ": $" + str(price1))
	print(name2 + ": $" + str(price2))
	print(name3 + ": $" + str(price3))
	print("Physical Subtotal: " + str(subtotalPhys))
	print("Physical Total: " + str(totalPhys))
	print("_____________________________________")
	print("Digital Items:")
	print(name4 + ": $" + str(price4))
	print(name5 + ": $" + str(price5))
	print("Digital Subtotal: " + str(subtotalDig))
	print("Digital Total: " + str(totalDig))
	print("_____________________________________")
	print("Tax: 6.5%")
	print("Shipping Rate: $5.99")
	print("Subtotal: $" + str(finalSubtotal))
	print("Total: $" + str(finalTotal))
	print(" ")
	print("We hope you've had a great time shopping at Walmazon!")
main()
