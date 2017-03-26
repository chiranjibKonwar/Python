

class EMI_CALCULATOR(object):
     # Data attributes
     # Helps to calculate EMI

      Loan_amount = None
      Month_Payment = None
      Interest_rate = None
      Payment_period = None

      def get_loan_amount(self):
     #get the  value of loan amount
          self.Loan_amount = input("Enter The Loan amount(in rupees) :")
          pass

      def get_interest_rate(self):
       # get the value of interest rate
          self.Interest_rate = input("Enter The Interest rate(in percentage(%)) : ")
          pass

      def get_payment_period(self):
       # get the payment period"
          self.Payment_period = input("Enter The Payment period (in month): ")
          pass


      def calc_interest_rate(self):
      # To calculate the  interest rate"
          self.get_interest_rate()

          if self.Interest_rate > 0:
             self.Interest_rate = (self.Interest_rate /100.0) 
         
          else:
             print "You have not entered The interest rate correctly ,please try again "
          pass

      def calc_emi(self):
      # To calculate the EMI"          

          try:

            self.get_loan_amount() #input loan amount 
            self.get_payment_period() #input payment period
            self.calc_interest_rate() #input interest rate and calculate the interest rate
          
          except NameError:
                 print "You have not entered Loan amount (OR) payment period (OR) interest rate  incorrectly,Please enter and try again. "
         
          try:
            self.Month_Payment = (self.Loan_amount*self.Interest_rate/12*pow((self.Interest_rate/12)+1,
                                 (self.Payment_period)))/(pow(self.Interest_rate/12+1,
                                 (self.Payment_period)) - 1)

#EMI = [P x R x (1+R)^N]/[(1+R)^N-1]


          except ZeroDivisionError: 
                        print "ERROR!! ZERO DIVISION ERROR , Please enter The Interest rate correctly and Try again."

          else:
             print "Monthly Payment is : %r"%self.Month_Payment
          pass


if __name__ == '__main__':# main method 
                              
   Init = EMI_CALCULATOR() # creating  instances

                              
   Init.calc_emi() #to calculate EMI



print
   
