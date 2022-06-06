"""
Python script to combine multiple CSV files into one."""

import sys
import pandas as pd
    

def combine_csv_files(csv_files, output_file):
    """
    Combine multiple CSV files into one.

    :param csv_files: List of CSV files to combine.
    :param output_file: Output file name.
    """


    # Read all CSV files into a single dataframe.
    df = pd.concat([pd.read_csv(f) for f in csv_files])

    # Write combined dataframe to output file.
    df.to_csv(output_file, index=False)


def main(csv_files):
    """
    Combine multiple CSV files into one.
    """

    # Combine all CSV files into one.
    combine_csv_files(csv_files, 'combined.csv')


if __name__ == '__main__':
    csv_files = sys.argv[1:]
    main(csv_files) 