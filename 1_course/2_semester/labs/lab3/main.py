import sys
import json
from builder import Builder
from student import Student
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
        Builder(information, filename_csv, filename_json, encoding_input).load()
        print("OK")

        information.output(filename_output, encoding_output)
        print("OK")
    except InitError:
        print("Catch InitError")
    except OpenCsvError:
        print("Catch OpenCsvError")
    except ReadCsvError as e:
        print("Catch ReadCsvError. " + e._exc)
    except OpenJsonError:
        print("Catch OpenJsonError")
    except ReadJsonError:
        print("Catch ReadJsonError")
    except ConsistentError:
        print("Catch ConsistentError")
    except OutputError:
        print("Catch OutputError")


# Todo: ask about output in load functions
def load_ini(filename):
    print("ini " + filename + ": ", end="")
    try:
        with open(filename) as f:
            ini_dict = json.load(f)
    except OSError:
        raise InitError("Cannot read(open) .ini file")

    ini_keys = ["input", "output"]
    ini_input_keys = ["encoding", "csv", "json"]
    ini_output_keys = ["encoding", "fname"]
    if all(k in ini_dict for k in ini_keys):
        input_dict = ini_dict[ini_keys[0]]
        output_dict = ini_dict[ini_keys[1]]
        if not all(k in input_dict for k in ini_input_keys) or not all(k in output_dict for k in ini_output_keys):
            raise InitError("There are no required keys in the .ini file")
    else:
        raise InitError("There are no required keys in the .ini file")
    return ini_dict


if __name__ == "__main__":
    print_author_info()
    print_task()
    print("*****")
    args = sys.argv
    try:
        if len(args) != 2:
            raise CommandLineError("Invalid numbers of arguments")
    except CommandLineError as e:
        print("***** program aborted *****", repr(e), sep="\n")
        print_help()
    main(args[1])
