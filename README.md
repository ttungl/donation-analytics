# Donation Analytics
---
InsightDataScience
---

### 1. Files Location

In this challenge, our program will do the following steps:

+ Read input files: `itcont.txt` and `percentile.txt`, which are stored in the input folder (`\donation-analytics\input\`)

+ Write output file: `repeat_donors.txt`, which is stored in the output folder (`\donation-analytics\output\`)

+ Source codes in `\donation-analytics\src\` contain the following files:
    
    + `donation-analytics.py`: this is the main file to run the program.
    
    + `donation_info.py`: to manage methods usage.
    
    + `checkInputValid.py`: to check the inputs validation.
    
    + `read_dataset.py` and `write_dataset.py`: to read from files and write to file.
    
### 2. Run the program

To run the program, using `./run.sh` under the `donation-analytics` directory.

The expected result will be written in the `repeat_donors.txt` as follows.

      C00384516|02895|2018|333|333|1
      C00384516|02895|2018|333|717|2

### 3. Testing

To run the test, go to the `insight_testsuite` directory, then using `./run_tests.sh`.
      
      Tungs-MBP:insight_testsuite tungthanhle$ ./run_tests.sh 
      
The expected result will be displayed on the terminal as follows.

      [PASS]: my-own-test repeat_donors.txt
      [PASS]: test_1 repeat_donors.txt
      [Tue Feb 13 00:47:29 CST 2018] 2 of 2 tests passed

Note, the log of the tests is saved in the `results.txt` in `insight_testsuite` directory.

---


