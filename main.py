import os, sys, glob
from king_utils import utils

numArgs = len(sys.argv)

print ('Number of arguments:', numArgs, 'arguments.')

def main():
    if numArgs == 3:
            # Retrieve the input directory
            INPUT_DIR = sys.argv[1]
            # Retrieve the output file
            OUTPUT_DIR = sys.argv[2]

            print('Valid amount of arguments provided, proceeding')

            # Check input file path exists and is a directory
            if not os.path.exists(INPUT_DIR):
                raise Exception('Input directory does not exist!')
                exit()
            if os.path.exists(OUTPUT_DIR):
                raise Exception('Output directory already exists!')
                exit()
            
            os.mkdir('output')

    else:
        print("Not enough arguments")
        exit()

    for filename in glob.iglob(INPUT_DIR + "/*.log", recursive=False):
        utils.process_file(filename, OUTPUT_DIR)

    print("COMPLETE")

if __name__ == "__main__":
    main()