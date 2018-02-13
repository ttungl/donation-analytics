from checkInputValid import *

class Donation:
    
    dict_unique_donors = {}

    def __init__(self, cmte_id, donor_name, zip_code, transaction_dt, transaction_amt, other_id):
        self.cmte_id = cmte_id
        self.donor_name = donor_name
        self.zip_code = zip_code
        self.year = int(transaction_dt[4:])
        self.transaction_dt = transaction_dt
        self.transaction_amt = int(transaction_amt)
        self.other_id = other_id

        self.number_of_repeat_donors = 1
        self.percentile_calculation = self.transaction_amt
        self.repeat_amount = self.transaction_amt
        
        self.array_percentile = []
        
    def increase_number(self):
        self.number_of_repeat_donors +=1

    def increase_amount(self, val):
        self.repeat_amount += val
        
    def update_percentile(self, percentile):
        self.array_percentile.append(self.transaction_amt)
        nth = (percentile/100)*len(self.array_percentile) # nearest-rank method
        self.percentile_calculation = self.array_percentile[int(nth)]
        
    def has_other_id(self):
        return checkDataLimitationForOtherID(self.other_id)

    def has_valid_date(self):
        return checkTransactionDate(self.transaction_dt)

    def has_valid_zip(self):
        return checkZipcode(self.zip_code)

    def is_valid_to_check(self):
        return checkCMTEID_and_TransactionAmount(self.cmte_id, self.transaction_amt)

    def is_repeat_donors(self):
        return checkRepeatDonors(self.dict_unique_donors, self.donor_name, self.zip_code, self.transaction_dt)
        
    def is_valid_donor_name(self):
        return checkDonorName(self.donor_name)

    def copy(self):
        ret = Donation(self.cmte_id, self.donor_name, self.zip_code, self.transaction_dt, self.transaction_amt, self.other_id)
        ret.__dict__.update(self.__dict__)
        return ret

    def __eq__(self, other):
        return self.cmte_id == other.cmte_id and self.zip_code == other.zip_code and self.year == other.year
        
    def __str__(self):
        return '{}|{}|{}|{}|{}|{}'.format(self.cmte_id, self.zip_code, self.year, self.percentile_calculation, self.repeat_amount, self.number_of_repeat_donors)
        
    def __repr__(self):
        return str(self)
