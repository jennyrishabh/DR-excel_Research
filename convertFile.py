from pandas import DataFrame, read_excel
from argparse import ArgumentParser
from os import remove


def change_file_format_to_csv(filename):
    filename = filename.split(".")
    filename[-1] = 'csv'


if __name__ == "__main__":
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", default="", required=False,
                        help="Input file to be converted")
    args = parser.parse_args()

    # Load input
    print(args.input)
    content = read_excel(args.input)

    # Change filename to csv
    filename_output = args.input.split(".")
    filename_output[-1] = "csv"
    filename_output = '.'.join(filename_output)

    # Store input as CSV
    content.to_csv(filename_output)

    # Cat output to command line
    with open(filename_output, 'r') as f:
        print(f.read())

    # Remove temporary file
    remove(filename_output)