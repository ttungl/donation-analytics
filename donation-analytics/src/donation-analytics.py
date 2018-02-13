from read_dataset import readline, readPercentile, split, set_inputs
from write_dataset import WriteToFile, set_output
from donation_info import Donation
from checkInputValid import *

import sys

# variables
lineCounter = 1
final_result_for_repeat_donors = []

set_inputs(sys.argv[1], sys.argv[2])
set_output(sys.argv[3])

percentile = readPercentile(0)

# read itcont.txt until done
while readline(lineCounter) is not None:
    rawLine = readline(lineCounter)
    splittedRawLine = split(rawLine)
    new_donation = Donation(splittedRawLine[0], splittedRawLine[7], splittedRawLine[10][:5], splittedRawLine[13], splittedRawLine[14], splittedRawLine[15])
    
    if new_donation.has_other_id() and new_donation.is_valid_to_check() and new_donation.is_valid_donor_name():
        # repeat donors
        if new_donation.is_repeat_donors(): 
            try:
                index = final_result_for_repeat_donors.index(new_donation)
                old_donation = final_result_for_repeat_donors[index]
                old_donation = old_donation.copy()
                old_donation.update_percentile(percentile)
                old_donation.increase_number()
                old_donation.increase_amount(new_donation.transaction_amt)
                final_result_for_repeat_donors.append(old_donation)

            except:
                final_result_for_repeat_donors.append(new_donation)

    lineCounter += 1

WriteToFile(final_result_for_repeat_donors)





