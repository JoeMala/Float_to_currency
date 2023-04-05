def float_to_currency():    
    #runs function check_input() created at the bottom that ensures input is numeric.
    user_Input = check_input()

    #negative is a boolean that notes if input is a negative number so to output properly (like in Excel with the minus sign before the currency symbol) 
    negative = False
    if user_Input[0] == "-":
        amtToString = user_Input[1:]
        negative = True

    else:
        amtToString = user_Input

    #declaration of lists to breakdown input to dollars and cents
    dollars = []
    cents = []
    has_cents = False
    
    #find index of decimal if one is present and add all numbers left of it to dollars[]
    cents_start_index = 0
    for i in amtToString:
        if i == ".":
            cents_start_index += 1
            has_cents = True
            break
        else:
            dollars.append(i)
        cents_start_index += 1

    #create cents and round up if necessary
    if has_cents:
        for i in range(cents_start_index, len(amtToString)):
            cents.append(amtToString[i])

        if (len(cents) >= 3):
            thousandth_of_cent = int(amtToString[cents_start_index + 2])
            cents = int(''.join(amtToString[cents_start_index : cents_start_index + 2]))
            if thousandth_of_cent >=5:
                cents += 1
                if cents > 99:
                    cents = ['0','0']
                    tempDollars = int(''.join(dollars))
                    tempDollars += 1
                    dollars = str(tempDollars)

                else:
                    cents = str(cents)
            else:
                cents = amtToString[cents_start_index : cents_start_index + 2]
        
        if (len(cents) == 1):
            cents.append('0')

    else:
        cents = ['0', '0']

    #add commas to dollars[]
    dollars_with_commas = []
    counter1 = 1
    if len(dollars) % 3 == 0:
        for i in dollars:
            if counter1 % 3 == 1 and len(dollars) > 3 and counter1 > 1:
                dollars_with_commas.append(",")
                dollars_with_commas.append(i)
                
            else:
                dollars_with_commas.append(i)

            counter1 +=1

    counter2 = 0
    if len(dollars) % 3 == 1:
        dollars_with_commas.append(dollars[0])
        counter2 += 1
        for i in range(1,len(dollars)):
            if counter2 % 3 == 1:
                dollars_with_commas.append(",")
                dollars_with_commas.append(dollars[i])
            
            else:
                dollars_with_commas.append(dollars[i])

            counter2 += 1

    counter3 = 0        
    if len(dollars) % 3 == 2:
        dollars_with_commas.append(dollars[0])
        dollars_with_commas.append(dollars[1])
        counter3 += 1
        for i in range(2,len(dollars)):
            if counter3 % 3 == 1:
                dollars_with_commas.append(",")
                dollars_with_commas.append(dollars[i])
            
            else:
                dollars_with_commas.append(dollars[i])

            counter3 += 1

    #runs function created at the bottom that produces a currency selection based on user selection. 
    currency_type = which_currency()
    if negative:
        print('-' + currency_type + ''.join(dollars_with_commas) + "." + ''.join(cents))

    if not negative:
        print(currency_type + ''.join(dollars_with_commas) + "." + ''.join(cents))


#checks the user input is a number
def check_input():
    while True:
        try:
            print("Please enter a valid number to be formatted to a currency.")
            number = input()
            amt = float(number)
            return number

        except ValueError:
            print( "\'" + number + "\'" + " is invalid. Try again.\n")

#allows user to choose from five currencies
def which_currency():
    print("""Please enter the number of the currency from the list below.\n
        \t1. U.S. Dollar (USD)
        \t2. European Euro (EUR)
        \t3. Japanese Yen (JPY)
        \t4. British Pound (GBP)
        \t5. Chinese Yuan (CNY)
            """)
    
    not_ok = True
    while not_ok:
        try:
            currency = int(input())
            if currency in (1,2,3,4,5):
                not_ok = False
                if currency == 1:
                    return '$'
                if currency == 2:
                    return '€'
                if currency == 3:
                    return '¥'
                if currency == 4:
                    return '£'
                if currency == 5:
                    return '¥'
                """
                 For Python 10 and later the commented out block below can be replaced with all the if statements preceding this comment.
                 
                 match currency:
                    case 1:
                        return '$'
                    case 2:
                        return '€'
                    case 3:
                        return '¥'
                    case 4:
                        return '£'
                    case 5:
                        return '¥'
                  """
                         
            else:
                print('Please enter a number one through five.')
            
        except ValueError:
            print("Please enter a number one through five.")
                       
   
if __name__== "__main__":
    float_to_currency()
