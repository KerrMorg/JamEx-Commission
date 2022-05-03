# Author:       Kerry-Ann Morgan
# Date Created: 04/30/2022
# Course:       ITT103
# Purpose:      Programm to calculate and print JamEX Ltd. commission for thier salespersons.

ans = "Y"
class_code_list = ["1", "2", "3"]

while ans != "n" and ans != "N":
    salesperson_num = input ("Enter the salespeson's number: ") #Accepting user input of salesperson's unique ID
    #Input is stored as type string by default.
    #Sales amount is converted to float and the class code is coverted to int
    while (len(salesperson_num) == 0 or salesperson_num.isspace()):
        print ("Invalid entry. Please enter a valid ID. \n")
        salesperson_num = input ("Enter the salesperson's number: ")
    
    sales_amt = input("Enter the salespeson's total sales: ")
    #isnumeric () checks value and returns True if all characters are numeric
    #while loop is used to account for multiple incorrect entries
    while (sales_amt.isnumeric () == False):
        print("Error. Please enter a valid number.\n")
        sales_amt = input ("Enter the salesperson's total sales: ")

    sales_amt = float (sales_amt)      
              
                                 
    class_code = input ("Enter the salesperson's class code: ")
    while (class_code not in class_code_list):
        print ("Incorrect code entered. Please enter a value of 1,2, or 3\n")
        class_code = input ("Enter the salesperson's class code: ")
        
    #Defining functions to determine commission of reach class code.
    # Each function has logic to determine the commission based on the defined criteria
    def class_1 (sales_amt):
        if sales_amt <= 1000:
            commission = sales_amt * 0.06
        elif sales_amt > 1000 and sales_amt < 2000:
            commission = sales_amt * 0.07
        else:
            commission = sales_amt * 0.1
        return " ".join(['The sales person with number', salesperson_num, 'received a commission of', "${:,.2f}".format(commission)])

    def class_2 (sales_amt):
        if sales_amt < 1000:
            commission = sales_amt * 0.04
        else:
            commission = sales_amt * 0.06
        return " ".join(['The sales person with number', salesperson_num, 'received a commission of', "${:,.2f}".format(commission)])
              
    
    def class_3 (sales_amt):
        commission = sales_amt * 0.045
        return " ".join(['The sales person with number', salesperson_num, 'received a commission of', "${:,.2f}".format(commission)])
        
        #Defining dictionary to emulate switch statement
        #Keys represent the different class code and the values are the fefinied functions
                            
    switch = {"1" : class_1 (sales_amt), "2" : class_2 (sales_amt), "3" : class_3 (sales_amt),}
        
        #Access entered class code (element) by using using the get () method.                        
    
    print (switch.get (class_code))
    
    ans = input ("\nWould you like to continue? Press 'Y' to continue or 'N' to end) ")
                            
print ("Thank you for using our commission calculator. Goodbye!")
    
                             
