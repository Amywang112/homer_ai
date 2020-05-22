'''pick sentences with syllable count between 12-18 and write them to an output file.'''

from big_phoney import BigPhoney
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'
###fix issue OMP: Error #15: Initializing libiomp5.dylib, but found libiomp5.dylib already initialized.

# Initialization
phoney = BigPhoney()
output_file = open("dactylic.txt", "a")

# Recognize and write lines with right syllables
def meter (input_file, output_file):
    for line in input_file.readlines():
        syllables = phoney.count_syllables(line)
        if syllables >= 12 and syllables <=18:
            output_file.write(line)

# Loop through output files and write results to dactylic.txt
for filename in os.listdir(os.getcwd()+"/outputs"):
    if filename == ".DS_Store":
        continue
    input_file = open("outputs/"+filename, "r")
    meter(input_file, output_file)
    print("Done with " + filename + ". Moving onto the next one.")
    input_file.close()
