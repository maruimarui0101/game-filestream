# Short Filestream project

Short project simulating telemtery data from a small gaming company tracking in game events. Log files are read from an input directory with individual lines being appended to particular files depending on the event type that is recorded within a specified output folder. Invalid rows are recorded in a separate folder within the output folder. 



In spite of how crude the implementation is, this is better implemented with a framework such as Spark streaming, a separate repository will be made to attempt this.



## Pre-requisites

Packages that are required to be installed before running this script are provided within the requirements.txt file. The script was developed within a virtual environment with anaconda.

## Running the script 

The script can be run from command line with the following command 

```bash
python main.py [input_directory] [output_directory]
```

where input_directory is where the input files are and where output_directory is where the outputs are to be delivered to e.g.

```
python main.py input output
```

where input and output are folders within the current working directory

In order to successfully run this script, the stated input_directory must exist and the output_directory must not exist. 

## Running automated tests

Tests can be run with the pytest python package, once installed tests can be run with:

```
pytest
```

The tests conducted emulate the expected outputs for each line stated within the briefing document and are contained within the test_document.py file 