
def checkDataLimitationForOtherID(Other_ID):
    # input: str type
    # output: bool type
    if not Other_ID:
        return True # if input has no Other_ID
    else:
        return False # if input has Other_ID

def checkDonorName(donor_name):
    new_donor_name = donor_name.replace(", ","")
    new_donor_name = new_donor_name.replace(" ","")
    if new_donor_name.isalpha(): 
        return True
    else: 
        return False

def checkTransactionDate(Transaction_date):
    if Transaction_date.isdigit() == False:  # check for digit
        return False
    elif len(Transaction_date) == 8 and int(Transaction_date[:2])<=12 and int(Transaction_date[2:4])<=31: # No. should be 8 tran.date should be less than 13 , 32 
        return True
    else:
        return False

def checkZipcode(Zipcode): # check for zipcode
    if 4 < len(Zipcode) <10:
        return True
    else:
        return False

def checkRepeatDonors(dict_unique_donors, donor_name, zip_code, transaction_dt):
    current_key = donor_name.replace(", ","")+zip_code # unique ID for a donor
    if current_key not in dict_unique_donors:
        dict_unique_donors[str(current_key)] = str(transaction_dt)
        return False
    else: # repeat donor
        prev_value = dict_unique_donors.get(current_key)
        if (int(prev_value[:4]) == int(transaction_dt[:4])) and (int(transaction_dt[4:]) == int(prev_value[4:])+1):
            dict_unique_donors[str(current_key)] = str(transaction_dt) # update
            return True
        else: 
            return False
    
def checkCMTEID_and_TransactionAmount(CMTE_ID,Transaction_AMT):
    if  CMTE_ID and Transaction_AMT:
        return True
    else:
        return False

# def RoundingPercentile(percentile_calculation):
#     intput: float type
#     output: int type
#     tem = str(int(percentile_calculation*100))
#     if int(tem[-2:]) <= 50:
#         return int(percentile_calculation)
#     else:
#         return int(percentile_calculation+1)