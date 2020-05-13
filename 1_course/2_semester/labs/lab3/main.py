"""
Author: Maxym Koval (Group K-12)
"""

import sys
import json
from loader import load
from info import Information
from errors import *


def print_author_info():
    about_author = f"\
            Author: Koval\n\
                    Maxym\n\
            Group:  K-12\n"
    print(about_author)


def print_task():
    task = f"Two files are input (main .csv and additional .json).\n\
             Files contains information about student performance.\n\
             The program processes the data and output... and some info about task\n"
    print(task)


def print_help():
    help_info = "To run the program you should type the next line: \n\
           program_name.py init... and some help instructions\n"
    print(help_info)


def main(init_filename):
    try:
        print("ini " + init_filename + ": ", end="")
        ini_dict = load_ini(init_filename)
        print("OK")

        ini_input_dict = ini_dict["input"]
        ini_output_dict = ini_dict["output"]

        encoding_input = ini_input_dict["encoding"]
        filename_csv = ini_input_dict["csv"]
        filename_json = ini_input_dict["json"]
        encoding_output = ini_output_dict["encoding"]
        filename_output = ini_output_dict["fname"]

        information = Information()

        load(information, filename_csv, filename_json, encoding_input)

        if not filename_output:
            print("output stdout:", end="\n")
            information.output(filename_output, encoding_output)
        else:
            print("output " + filename_output + ": ", end="")
            information.output(filename_output, encoding_output)
            print("OK")
    except InitError:
        print("Catch InitError")
    except ReadCsvError:
        print("Catch OpenCsvError")
    except LoadCsvError:
        print("Catch LoadCsvError")
    except ReadJsonError:
        print("Catch OpenJsonError")
    except LoadJsonError:
        print("Catch LoadJsonError")
    except ConsistentError:
        print("Catch ConsistentError")
    except OutputError:
        print("Catch OutputError")


def load_ini(filename):
    try:
        with open(filename) as f:
            ini_dict = json.load(f)

        ini_keys = ["input", "output"]
        ini_input_keys = ["encoding", "csv", "json"]
        ini_output_keys = ["encoding", "fname"]
        if all(k in ini_dict for k in ini_keys):
            input_dict = ini_dict[ini_keys[0]]
            output_dict = ini_dict[ini_keys[1]]
            if not all(k in input_dict for k in ini_input_keys) or not all(k in output_dict for k in ini_output_keys):
                raise InitError(f"There are no required keys in the {filename}")
        else:
            raise InitError(f"There are no required keys in the {filename}")
        return ini_dict
    except OSError:
        raise InitError(f"Cannot open or read {filename}")


# Todo: 1) doc all the function, 2) implement info function, 3) handle all the exceptions, 4) check limits (mark, ...)
if __name__ == "__main__":
    print_author_info()
    print_task()
    print("*****")
    args = sys.argv
    try:
        if len(args) != 2:
            raise CommandLineError("Invalid numbers of arguments")
        main(args[1])
    except CommandLineError as e:
        print("***** program aborted *****", repr(e), sep="\n")
        print_help()
