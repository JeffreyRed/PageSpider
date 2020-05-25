import os
import argparse


def main(database: str, url_list_file:str):
    print("We are going to work with " + database)
    print("We are going to scan " + url_list_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQlite file name")
    parser.add_argument("-i", "--input", help="file containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_fie = args.input
    main(database=database_file, url_list_file=input_fie)