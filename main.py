# Project: Honest Harry's Used Car Lot - Sprint Week 1
# Programmers: Ashley Fillmore & Michael O'Reilly
# Date: June 10, 2021

# Create constants
TAX_RATE = 0.15
LICENSE_FEE = 75
LICENSE_FEE2 = 165
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
FINANCE_FEE = 39.99

# Create initial while loop
while True:
    # Create input and while loop for customer first name
    while True:
        FirstName = input("Enter First Name (Type END to Stop Program): ").title()

        if FirstName == "":
            print("Cannot Be Blank. Please Re-Enter: ")
        else:
            break
    if FirstName.upper() == "END":
        break

    # Create input and while loop for customer last name
    while True:
        LastName = input("Enter Last Name: ").title()

        if LastName == "":
            print("Cannot Be Blank. Please Re-Enter: ")
        else:
            break

    # Create while loop for phone number
    while True:
        PhoneNum = input("Enter Phone Number (1234567890): ")

        if PhoneNum == "":
            print("Phone Number Cannot Be Blank. Please Re-Enter: ")
        elif len(PhoneNum) != 10:
            print("Phone Number Must Be Ten Digits. Please Re-Enter: ")
        else:
            break

    # Create variable and input for purchase date
    PurchaseDate = input("Enter Purchase Date: ").title()

    # Create while loop and if statements for plate number
    while True:
        PlateNum = input("Enter Plate Number (XXX999): ").upper()

        if PlateNum == "":
            print("Cannot Be Blank. Please Re-Enter: ")
        elif len(PlateNum) != 6:
            print("Must Be 6 Characters. Please Re-Enter: ")
        elif not (PlateNum[0:3].isalpha() and PlateNum[3:6].isdigit()):
            print("Plate Number Not Valid. Please Re-Enter: ")
        else:
            break




    # Create variables and inputs for car year, car make and car model
    CarYear = input("Enter Year of Car: ")
    CarMake = input("Enter Make of Car: ").title()
    CarModel = input("Enter Model of Car: ").title()

    # Create while loop and if statements for sell price
    while True:
        SellPrice = float(input("Enter Price of Car: "))

        if SellPrice > 20000:
            print("Price of Car Cannot Exceed $20,000. Please Re-Enter: ")
        elif SellPrice <= 0:
            print("Price of Car Cannot Be Less Than $0. Please Re-Enter: ")
        else:
            break

    if SellPrice < 5000:
        LICENSE_FEE = 75
    elif SellPrice >= 5000:
        LICENSE_FEE = LICENSE_FEE2
    else:
        break

    if SellPrice < 10000:
        TransferFee = SellPrice * TRANSFER_FEE_RATE
    else:
        TransferFee = SellPrice * (TRANSFER_FEE_RATE + 1.00) * LUXURY_TAX_RATE


    # Create while loop and if statements for trade in
    while True:
        TradeIn = float(input("Enter Trade In Value: "))

        if TradeIn > SellPrice:
            print("Trade In Value of Car Cannot Exceed Sale Price. Please Re-Enter: ")
        else:
            break

    # Create variables and inputs for sales persons name, credit card # and exp date
    SalesPersonName = input("Enter Sales Person's Name: ").title()
    CredCardNum = input("Enter Credit Card Number: ")
    ExpDate = input("Enter Expiry Date: ")
    CustName = FirstName[:1] + ". " + LastName
    ReceiptID = FirstName[:1] + LastName[:1] + "-" + PlateNum[3:6] + "-" + PhoneNum[6:11]

    # Write calculations
    PriceAfterTrade = SellPrice - TradeIn
    Tax = (SellPrice - TradeIn) * TAX_RATE
    TotSalesPrice = PriceAfterTrade + Tax + TransferFee

    # Print statements
    print()
    print("         1         2         3         4         5         6         7")
    print("12345678901234567890123456789012345678901234567890123456789012345678901")
    print("# Years    # Payments    Financing Fee   Total Price    Monthly Payment")
    print("-" * 71)

    # Write 'for' statement for years 1-4
    for Year in range(0, 4):
        Year = Year + 1
        YearlyFinanceFee = Year * 39.99
        Months = Year * 12
        TotSalesPrice = TotSalesPrice + YearlyFinanceFee
        TotMonthPmt = TotSalesPrice / Months

        # Format int/float variables into str/pad
        YearlyFinanceFeeStr = "${:,.2f}".format(YearlyFinanceFee)
        YearlyFinanceFeePad = "{:>10}".format(YearlyFinanceFeeStr)

        TotSalesPriceStr = "${:,.2f}".format(TotSalesPrice)
        TotSalesPricePad = "{:>10}".format(TotSalesPriceStr)

        TotMonthPmtStr = "${:,.2f}".format(TotMonthPmt)
        TotMonthPmtPad = "{:>10}".format(TotMonthPmtStr)

        SellPriceStr = "${:,.2f}".format(SellPrice)
        SellPricePad = "{:>10}".format(SellPriceStr)

        TradeInStr = "${:,.2f}".format(TradeIn)
        TradeInPad = "{:>10}".format(TradeInStr)

        PriceAfterTradeStr = "${:,.2f}".format(PriceAfterTrade)
        PriceAfterTradePad = "{:>10}".format(PriceAfterTradeStr)

        TaxStr = "${:,.2f}".format(Tax)
        TaxPad = "{:>10}".format(TaxStr)

        LICENSE_FEEStr = "${:,.2f}".format(LICENSE_FEE)
        LICENSE_FEEPad = "{:>10}".format(LICENSE_FEEStr)

        TransferFeeStr = "${:,.2f}".format(TransferFee)
        TransferFeePad = "{:>10}".format(TransferFeeStr)

        TotSalesPriceStr = "${:,.2f}".format(TotSalesPrice)
        TotSalesPricePad = "{:>10}".format(TotSalesPriceStr)


        print("   {}           {}       {}        {}       {}".format(Year, Months, YearlyFinanceFeePad, TotSalesPricePad, TotMonthPmtPad))
    print()

    CurrentDate = "2021-06-11"
    import datetime
    Current_Date = datetime.date.today()
    print("Date: {}".format(CurrentDate))
    print("First Payment Date: {}".format(Current_Date + datetime.timedelta(days=30)))
    print()

    # Create while loop and if statements for payment schedule
    while True:
        try:
            PmtPlan = input("Enter the payment schedule you want to follow (1-4): ")
        except:
            print("Invalid Payment Schedule. Please Enter 1-4: ")
        if PmtPlan == "":
            print("Cannot Be Blank. Please Enter 1-4: ")
        elif PmtPlan < "1" or PmtPlan > "4":
            print("Invalid Payment Schedule. Please Enter 1-4: ")
        else:
            if PmtPlan == "1":
                Year = 1
                Payments = 12
                break
            elif PmtPlan == "2":
                Year = 2
                Payments = 24
                break
            elif PmtPlan == "3":
                Year = 3
                Payments = 36
                break
            elif PmtPlan == "4":
                Year = 4
                Payments = 48
                break

    # Write print statements
    print()
    print("         1         2         3         4         5         6         7")
    print("123456789012345678901234567890123456789012345678901234567890123456789012345")
    print("Honest Harry Car Sales                           Invoice Date: {}".format(PurchaseDate))
    print("Used Car Sale and Receipt                        Receipt No: {}".format(ReceiptID))
    print()
    print("Sold To:                            Car Details: ")
    print("     " + CustName + "                           {} {} {}".format(CarYear, CarMake, CarModel))
    print()
    print("                                    Sale Price:                  {}".format(SellPricePad))
    print("                                    Trade Allowance:             {}".format(TradeInPad))
    print("                                    Price After Trade:           {}".format(PriceAfterTradePad))
    print("                                                                 ----------")
    print("                                    HST:                         {}".format(TaxPad))
    print("                                    License Fee:                 {}".format(LICENSE_FEEPad))
    print("                                    Transfer Fee:                {}".format(TransferFeePad))
    print("                                                                 ----------")
    print("                                    Total Sales Cost:            {}".format(TotSalesPricePad))
    print()
    print("Terms: {}                                             Total Payments:     {}".format(Year, Year * 12))
    print()
    print("    Honest Harry Car Sales – Best Used Cars At The Best Price!")
    print()






























