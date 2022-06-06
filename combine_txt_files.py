"""Script to combine all text files in a directory into a single file."""

import sys
import pandas as pd


def combine_txt_files(txt_files, output_file):
    """
    Combine multiple text files into one.

    :param txt_files: List of text files to combine.
    :param output_file: Output file name.
    """

    # Read all text files into a single dataframe.
    df = pd.concat([pd.read_csv(f, sep='\t') for f in txt_files])

    # Write combined dataframe to output file.
    df.to_csv(output_file, index=False)


def main(txt_files):
    """
    Combine multiple text files into one.
    """

    # Combine all text files into one.
    combine_txt_files(txt_files, 'combined.csv')


if __name__ == '__main__':
    txt_files = sys.argv[1:]
    main(txt_files)
