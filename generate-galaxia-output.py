import sys
import os
import subprocess
import time

def generateOutput(parameterfilepath):

    try:
        # time.sleep(15)
        dirname = os.path.dirname(parameterfilepath)
        # parameterfilepath = os.path.join(path, parameterfilename)
        with open(parameterfilepath, 'r') as parameterfile:
            lines = parameterfile.readlines()
            if lines:
                outputfilename = f'galaxia_{os.path.basename(parameterfilepath)}.ebf'
                print(f'output file name": {outputfilename}')
                outputfilepath = os.path.join(dirname, outputfilename)
                print(f'output file path: {outputfilepath}')
                outputfile = open(outputfilepath, 'w+')
                outputfile.writelines(lines)
                outputfile.close()
    except Exception as e:
        print(e)
        raise(e)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        generateOutput(sys.argv[1])
    else:
        print('No parameter file path provided')
