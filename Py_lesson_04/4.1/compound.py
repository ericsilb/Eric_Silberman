
def total(r,P,n,t):
    return float((P*((1+(r/n))**(n*t)))/(t*12))


ra = float(input("Enter the intrest rate: "))
pe = float(input("Enter the principal: "))
nu = float(input("Number of times the loan is compounded per year: "))
ti = float(input("Life of the loan: "))

print("Your total payment is ", total(ra,pe,nu,ti))
