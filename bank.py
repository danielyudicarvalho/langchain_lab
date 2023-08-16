import random

def simulate_bank_loan(client_credit_score):
    loan_approval = "Denied"
    if client_credit_score >= 700:
        loan_approval = "Approved"
        loan_amount = random.randint(5000, 20000)
        interest_rate = random.uniform(0.05, 0.1)
        loan_term = random.randint(12, 60)
        
        
        # Define some constants for our simulation
        MIN_CREDIT_SCORE = 580 # The minimum credit score we'll consider for this simulation
        MAX_LOAN_AMOUNT = 25000.00 # The maximum amount we will lend in this simulation
        APR = 10.0 / 100 # Annual percentage rate for loans (includes fees)
        FEES = 300.0 # Application fee charged to all customers regardless of approval status
        INCOME_PROTECTION_INSURANCE = False # Whether or not to offer income protection insurance as part of the loan
        
        def calculate_monthly_payment(amount, interest_rate):
            """Calculate the monthly payment based on the loan amount, interest rate, and number of months"""
            return ((amount * interest_rate) / 12) + (((amount * interest_rate) / 12) * (1 + .06))**(1/12)-1 
        
        def main():
        
            # Generate random data for our fictional customer
            customer_score = round(random.uniform(MIN_CREDIT_SCORE, 900), 0) 
            print("Customer's credit score:", customer_score)
            
            customer_income = int(input("Enter customer's annual income: "))
            print()
        
            # Determine if the customer qualifies for a loan based on their credit score
            qualified = True if customer_score >= MIN_CREDIT_SCORE else False
            print("Loan qualified" if qualified else "Loan denied")
        
            # Calculate the total loan cost (interest, fees, etc.)
            total_cost = APR * loan_amount + FEES 
        
            # Print out results
            if qualified:
                monthly_payment = calculate_monthly_payment(loan_amount, APR)
        
                print("\nMonthly Payment:", monthly_payment)
                
                if INCOME_PROTECTION_INSURANCE:
                    ipi_premium = .2 * monthly_payment
                    print("Income Protection Insurance Premium:", ipi_premium)
        
                    monthly_payment += ipi_premium
            
                print("Total Cost:", total_cost)
                print("Remaining Balance After Payments:", loan_amount - total_cost)
        
            else: 
                print("Reason For Denial:")
                if customer_score < MIN_CREDIT_SCORE: 
                    print("- Insufficient Credit Score")
                elif customer_income <= 40*12*2000: 
                    print("- Low Income")
                else: 
                    print("- Other reasons...")
        
            
            
        if __name__ == "__main__":
            loan_amount = float(input("Enter desired loan amount ($):"))
            main()
        print(f"Client loan is approved. Loan amount: , Interest rate: {interest_rate*100}%, Loan term: {loan_term} months, Monthly payment: .2f")
    else:
        print(f"Client loan is denied. Credit score: {client_credit_score}")
    return loan_approval

client_credit_score = int(input("Enter client credit score: "))
loan_approval = simulate_bank_loan(client_credit_score)