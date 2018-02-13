from donation_info import Donation

output_repeat_donors = None

def set_output(output):
    global output_repeat_donors
    output_repeat_donors = output
    return

def WriteToFile(final_result_for_repeat_donors):
    file = open(output_repeat_donors, "w")
    for i in range(len(final_result_for_repeat_donors)):
        file.write(str(final_result_for_repeat_donors[i]))
        file.write("\n")
    file.close()
    
    
    