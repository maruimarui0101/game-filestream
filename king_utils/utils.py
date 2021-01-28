import hashlib

game_dict = {
    "1": "Flying Sweets"
    , "2": "Circus Builder"
    , "3": "Zoom Racer"
}


def isFloat(value):
    """
    Verifies a single item from a log file and verifies if the item can be confirmed to be of 
    Number (integer) type

    :param value: Number field to be verified
    :return: Boolean
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

def write_to_invalid_log(OUTPUT_DIR, line):
    """
    Provided that line_check returns False, the line is written to the invalid.log file within the output directory

    :param line: line from log file being read
    :param OUTPUT_DIR: directory for output files
    :return: None
    """

    invalid_log_dir = OUTPUT_DIR + "\\invalid.log"

    with open(invalid_log_dir, "a+") as f:
        f.write(line + "\n")

def write_valid_log(OUTPUT_DIR, line):
    """
    Provided that line_check returns True, the line is outputted to the appropiate csv file

    :param line: line from log file being read
    :param OUTPUT_DIR: directory for output files
    :return: None
    """

    line_item = line.split("|")

    valid_file_dir = OUTPUT_DIR + "\\" + line_item[0] + ".csv"

    with open(valid_file_dir, "a+") as f:
        # hash the user ID 
        line_item[1] = hashlib.sha256(line_item[1].encode('utf-8')).hexdigest()
        hhh = ','.join('"' + str(x) + '"' for x in line_item[1:])
        f.write(hhh + "\n")

def line_check(line):
    """
    Checks an individual line from a log file with the following checks:
    - if the tracking event is acknowledged via the case statements
    - depending on the tracking event, if the amount of fields are correct 
    - verifying integer field types
    - verifying that the game id checks out with the game_dict object

    :param line: line from log file being read
    :return: Boolean
    """

    log_line = line.split("|")

    tracking_event = log_line[0]

    check_event = False
    check_length = False
    check_types = False
    check_game = False

    if  tracking_event == "gameinstallation":
        check_event = True
        length_expected = 4
        check_length = len(log_line) == length_expected
        if check_length:
            check_types = isFloat(log_line[2]) and isFloat(log_line[3])
            check_game = log_line[2] in game_dict.keys()

    elif tracking_event == "gamestart":
        check_event = True
        length_expected = 4
        check_length = len(log_line) == length_expected
        if check_length:
            check_types = isFloat(log_line[2]) and isFloat(log_line[3])
            check_game = log_line[2] in game_dict.keys()

    elif tracking_event == "gamepurchase":
        check_event = True
        length_expected = 5
        check_length = len(log_line) == length_expected
        if check_length:
            check_types = isFloat(log_line[2]) and isFloat(log_line[4])
            check_game = log_line[2] in game_dict.keys()

    return check_event and check_length and check_types and check_game

def process_file(INPUT_FILE, OUTPUT_DIR):
    """
    Takes in a file to process before delegating to the 
    line_check function

    :param INPUT_FILE: full directory of log file to process
    :param OUTPUT_DIR: directory for output files
    :return: None
    """
    with open(INPUT_FILE) as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip() # removing whitespace from lines 
            if line_check(line):
                write_valid_log(OUTPUT_DIR, line)
            else: 
                write_to_invalid_log(OUTPUT_DIR, line)
            
