# Description: A program for The One Stop Insurance Company needs a program to enter and calculate new insurance policy information for its customers.
# Author: Steve Morrison - SD12
# Date(s): July 18 - , 2024
 
 
# Define required libraries.
import datetime
import sys
import time
 
 
# Define program constants.

f = open("Const.dat", "r")
lines = f.readlines()

POLICY_NUMBER = int((lines[0].strip()))
BASIC_PREMIUM =  float(lines[1].strip())
DISCOUNT_ADDITIONAL_CARS = float(lines[2].strip())
EXTRA_LIABILITY_CHARGE = float(lines[3].strip())
GLASS_COVER_CHARGE = float(lines[4].strip())
LOANER_CAR_CHARGE = float(lines[5].strip())
HST_RATE = float(lines[6].strip())
PROCESSING_FEE =  float(lines[7].strip())

PaymentMethodLst = ["Full", "Monthly", "Down Pay"]
CustProvLst = ["ALBERTA", "AB", "BRITISH COLUMBIA", "BC", "MANITOBA", "MB", "NEW BRUNSWICK", "NB", "NEWFOUNDLAND AND LABRADOR", "NL", "NORTHWEST TERRITORIES", 
               "NWT", "NOVA SCOTIA", "NS", "NUNAVUT", "NU", "ONTARIO", "ON", "PRINCE EDWARD ISLAND", "PEI", "QUEBEC", "QC", "SASKATCHEWAN", "SK", "YUKON", "YT"]


# Define program functions.

# Function for progess bar when writing data to Claims.dat.
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Function to calculate the first payment date.
def CalculatePaymentDate():
    PolicyDate = datetime.datetime.today()
    NextMonth = PolicyDate.month % 12 + 1
    
    if NextMonth == 1:
        NextMonthYear = PolicyDate.year + 1
    else:
        NextMonthYear = PolicyDate.year
    
    FirstPaymentDate = datetime.datetime(NextMonthYear, NextMonth, 1)

    return FirstPaymentDate.strftime('%Y-%m-%d')
  
# Function to calulate the total claim cost.
def CalculateTotalCost(NumCarsFunc, ExtraLiabilityFunc, GlassCoverageFunc, LoanerCarFunc):
    InsurancePremiumFunc = BASIC_PREMIUM + (NumCarsFunc - 1) * BASIC_PREMIUM * (1 - DISCOUNT_ADDITIONAL_CARS)
    
    ExtraLiabilityCosts = 0
    ExtraGlassCosts = 0
    ExtraLoanerCosts = 0

    if ExtraLiabilityFunc == 'Y':
        ExtraLiabilityCosts = EXTRA_LIABILITY_CHARGE * NumCarsFunc
    if GlassCoverageFunc == 'Y':
        ExtraGlassCosts = GLASS_COVER_CHARGE * NumCarsFunc
    if LoanerCarFunc == 'Y':
        ExtraLoanerCosts = LOANER_CAR_CHARGE * NumCarsFunc
        
    ExtraCostsFunc = ExtraLiabilityCosts + ExtraGlassCosts + ExtraLoanerCosts

    TotalPremiumFunc = InsurancePremiumFunc + ExtraCostsFunc
    HSTFunc = TotalPremiumFunc * HST_RATE

    TotalCostFunc = TotalPremiumFunc + HSTFunc
    return InsurancePremiumFunc, TotalPremiumFunc, HSTFunc, TotalCostFunc, ExtraLiabilityCosts, ExtraGlassCosts, ExtraLoanerCosts, ExtraCostsFunc

# Function to calculate the monthly payment of the claim.
def CalculateMonthlyPayment(TotalCostFunc, PaymentMethodFunc, DownPaymentFunc):
    if PaymentMethodFunc == 'Full':
        MonthlyPay = 0
    elif PaymentMethodFunc == 'Monthly':
        MonthlyPay = (TotalCostFunc + PROCESSING_FEE) / 8
    else: 
        RemainingAmount = TotalCostFunc - DownPaymentFunc
        MonthlyPay = (RemainingAmount + PROCESSING_FEE) / 8
    return MonthlyPay


# Main body of program.
while True:

    # Gather user inputs.

    CustFirstName = input("Enter customer first name: ").title()
    CustLastName = input("Enter customer last name: ").title()
    CustAddress = input("Enter the street address of the customer: ")
    CustCity = input("Enter the city the customer lives: ").title()
    
    while True:
        CustProv = input("Enter the province of residency of the customer: ").upper()
        if CustProv == "ALBERTA" or CustProv == "AB":
            CustProv = "AB"
            break
        elif CustProv == "BRITISH COLUMBIA" or CustProv == "BC":
            CustProv = "BC"
            break
        elif CustProv == "MANITOBA" or CustProv == "MB":
            CustProv = "MB"
            break
        elif CustProv == "NEW BRUNSWICK" or CustProv == "NB":
            CustProv = "NB"
            break
        elif CustProv == "NEWFOUNDLAND AND LABRADOR" or CustProv == "NL" or CustProv == "NFLD":
            CustProv = "NL"
            break
        elif CustProv == "NORTHWEST TERRITORIES" or CustProv == "NWT":
            CustProv = "NWT"
            break
        elif CustProv == "NOVA SCOTIA" or CustProv == "NS":
            CustProv = "NS"
            break
        elif CustProv == "NUNAVUT" or CustProv == "NU":
            CustProv = "NU"
            break
        elif CustProv == "ONTARIO" or CustProv == "ON":
            CustProv = "ON"
            break
        elif CustProv == "PRINCE EDWARD ISLAND" or CustProv == "PEI":
            CustProv = "PEI"
            break
        elif CustProv == "QUEBEC" or CustProv == "QC":
            CustProv = "QC"
            break
        elif CustProv == "SASKATCHEWAN" or CustProv == "SK":
            CustProv = "SK"
            break
        elif CustProv == "YUKON" or CustProv == "YT":
            CustProv = "YT"
            break
        else:
            print("Data Entry Error - please input valid province name")
            
    
    CustPostal = input("Enter the postal code of the customer(X9X9X9)): ")

    while True:
        CustPhone = input("Enter the member's phone number (9999999999): ") 
        if CustPhone == "":
            print("Data Entry Error - Phone Number cannot be blank.")
        elif len(CustPhone) != 10:
            print("Data Entry Error - Phone Number must be 10 digits.")
        elif CustPhone.isdigit() == False:
            print("Data Entry Error - Phone Number contains invalid characters.")
        else: 
            break
    
    NumCars = int(input("Enter the number of cars being insured: "))

    while True:
        ExtraLiability = input("Does the customer want extra liability up to $1,000,000? (Y / N): ").upper()
        if ExtraLiability != "Y" and ExtraLiability != "N":
            print("Data Entry Error - prompt to continue must be a Y or an N.")
        else:
            break

    while True:
        GlassCoverage = input("Does the customer want glass coverage? (Y / N): ").upper()
        if GlassCoverage != "Y" and GlassCoverage != "N":
            print("Data Entry Error - prompt to continue must be a Y or an N.")
        else:
            break
    
    while True:
        LoanerCar = input("Does the customer want a loaner car? (Y / N): ").upper()
        if LoanerCar != "Y" and LoanerCar != "N":
            print("Data Entry Error - prompt to continue must be a Y or an N.")
        else:
            break

    while True:
        PaymentMethod = input("How does the customer want to pay? (Full/Monthy/Down Pay): ").title()
        if PaymentMethod not in PaymentMethodLst:
            print("Data Entry Error - Input correct payment type")
        else:
            break
    
    DownPayment = 0
    if PaymentMethod == "Down Pay":
        DownPayment = float(input("Enter the down payment amount: "))
    
    while True:
        ClaimNum = input("Enter the customer's previous claim number: ")
        ClaimDate = input("Enter the customer's previous claim date (YYYY-MM-DD): ")
        ClaimAmt = float(input("Enter the customer's previous claim amount: "))
        
        with open('Claims.dat', 'a') as file:
            file.write(f"{ClaimNum},{ClaimDate},{ClaimAmt}\n")
        
        Continue = input("Do you want to enter another previous claim (Y / N): ").upper()
        if Continue == "N":
            break
 

    # Perform required calculations.

    InvoiceDate = datetime.datetime.today().date()

    FirstPaymentDate = CalculatePaymentDate()

    InsurancePremium, TotalPremium, HST, TotalCost, ExtraLiabilityAmt, ExtraGlassAmt, ExtraLoanerAmt, ExtraCosts = CalculateTotalCost(NumCars, ExtraLiability, GlassCoverage, LoanerCar)

    MonthyPayment = CalculateMonthlyPayment(TotalCost, PaymentMethod, DownPayment)


    # print results

    CustNameDsp = f"{CustFirstName} {CustLastName}"
    CustPhoneDsp = "(" + CustPhone[0:3] + ") " + CustPhone[3:6] + "-" + CustPhone[6:]
    DownPaymentDsp = "${:,.2f}".format(DownPayment)
    InsurancePremiumDsp = "${:,.2f}".format(InsurancePremium)
    TotalPremiumDsp = "${:,.2f}".format(TotalPremium)
    HSTDsp = "${:,.2f}".format(HST)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    ExtraLiabilityAmtDsp = "${:,.2f}".format(ExtraLiabilityAmt)
    GlassCoverageAmtDsp = "${:,.2f}".format(ExtraGlassAmt)
    LoanerCarAmttDsp = "${:,.2f}".format(ExtraLoanerAmt)
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    AddressDsp = f"{CustAddress}, {CustCity}, {CustProv}"
    MonthlyPaymentDsp = "${:,.2f}".format(MonthyPayment)

    print(f"+----------------------------------------------------------+")
    print(f"|               One Stop Insurance Company                 |")
    print(f"|                                                          |")
    print(f"| Policy Number:                                     {POLICY_NUMBER:>5} |")
    print(f"| Policy Date:                                  {InvoiceDate} |")
    print(f"| First Payment Date:                           {FirstPaymentDate:>10} |")
    print(f"|                                                          |")
    print(f"| Customer Name: {CustNameDsp:>41} |")
    print(f"| Customer Phone Number:                    {CustPhoneDsp:>14} |")
    print(f"| Customer Address:{AddressDsp:>39} |")
    print(f"| Customer Postal Code:                            {CustPostal:>7} |")
    print(f"|                                                          |")
    print(f"| Extra Liability?:                                      {ExtraLiability:>1} |")
    print(f"| Extra Liability Cost:                          {ExtraLiabilityAmtDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Glass Coverage?:                                       {GlassCoverage:>1} |")
    print(f"| Glass Coverage Cost:                           {GlassCoverageAmtDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Number of Cars:                                       {NumCars:>2} |")
    print(f"| Insurance Premium:                             {GlassCoverageAmtDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Loaner Car?:                                           {LoanerCar:>1} |")
    print(f"| Loaner Car Cost:                               {LoanerCarAmttDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Total Extra Costs:                             {ExtraCostsDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Total Premium:                                 {TotalPremiumDsp:>9} |")
    print(f"| HST:                                           {HSTDsp:>9} |")
    print(f"| Total Cost:                                    {TotalCostDsp:>9} |")
    print(f"|                                                          |")
    print(f"| Monthly Payment:                               {MonthlyPaymentDsp:>9} |")
    print(f"+----------------------------------------------------------+")
    print(f"|                     Previous Claims                      |")
    print(f"|                                                          |")
    print(f"|        Claim #         Claim Date          Amount        |")
    print(f"+----------------------------------------------------------+")
    print(f"|                                                          |")
    claims = []
    with open('Claims.dat', 'r') as file:
        for line in file:
            ClaimNum, ClaimDate, ClaimAmt = line.strip().split(',')
            claims.append((ClaimNum, ClaimDate, float(ClaimAmt)))

    for claim in claims:
        print(f"|        {claim[0]:<15} {claim[1]:<15}    ${claim[2]:>10,.2f}     |")
    print(f"+----------------------------------------------------------+")
    
    
    # write data to Policy.dat
    
    with open("Policy.dat", "a") as f:
        f.write(f"{POLICY_NUMBER}, {CustNameDsp}, {CustAddress}, {CustCity}, {CustProv}, {CustPhone}, {NumCars}, {ExtraLiability}, {GlassCoverage}, {LoanerCar}, {PaymentMethod}, {DownPayment}, {TotalPremiumDsp}\n")
    
    print()
 
    TotalIterations = 30 
    Message = "Saving Claim Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1) 
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print("Policy data has been successfully saved to Policy.dat ...")

    # Update counters and accumulators.
    POLICY_NUMBER += 1

    Continue = input("Do you want to process another claim (Y / N): ").upper()
    if Continue == "N":
        break