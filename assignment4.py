acc_bal =(int(input ("Enter your acc balance")))

if (int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal=acc_bal -25000
    print("we have deducted KSH 25000 from your account balance. thankyou for coosing us")
elif (int(acc_bal)==200000) or (int(acc_bal)< 500000):
    acc_bal=acc_bal-(0.3*acc_bal)
    print("We have deducted KSH " +str(0.3*acc_bal) + ". Thank you for choosing us")