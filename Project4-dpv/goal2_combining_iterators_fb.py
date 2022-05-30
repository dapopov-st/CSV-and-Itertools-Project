# # Disclaimer: This follows Fred Baptiste's solution.
# # This allows for a better starting point going forward.
# # My solution (goal2_combining_iterators_inefficient.py
# # is less efficient since it involves first creating dictionaries, then making a joined
# # namedtuple from every one of those dictionaries. With my solution, just outputting joined
# # dictionaries would be better
# # Goal 2

########################################################################################
# From Fred Baptiste's constants.py
import itertools
from collections import namedtuple
import csv
from datetime import datetime


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


# Files
fname_personal = 'data/personal_info.csv'
fname_employment = 'data/employment.csv'
fname_vehicles = 'data/vehicles.csv'
fname_update_status = 'data/update_status.csv'
fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicle_parser = (str, str, str, int)
update_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Named Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

# Field Inclusion/Exclusion
personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = (personal_fields_compress, employment_fields_compress,
                   vehicle_fields_compress, update_status_fields_compress)


########################################################################################
# From Fred Baptiste's parse_utils.py

def csv_parser(fname, *, delimiter=',', quotechar='"', include_header=False):
    with open(fname) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not include_header:
            next(f)
        yield from reader


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


def extract_field_names(fname):
    reader = csv_parser(fname, include_header=True)
    return next(reader)


def create_named_tuple_class(fname, class_name):
    fields = extract_field_names(fname)
    return namedtuple(class_name, fields)


def create_combo_named_tuple_class(fnames, compress_fields):
    compress_fields = itertools.chain.from_iterable(compress_fields)
    field_names = itertools.chain.from_iterable(
        extract_field_names(fname) for fname in fnames)
    compressed_field_names = itertools.compress(field_names, compress_fields)
    return namedtuple('Data', compressed_field_names)


def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_parser(fname)
    for row in reader:
        parsed_data = (parse_fn(value)for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)


def iter_combined_plain_tuple(fnames, class_names, parsers, compress_fields):
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(fname, class_name, parser)
                          for fname, class_name, parser in zip(fnames, class_names, parsers)))

    merged_iter = (itertools.chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield tuple(compressed_row)


def iter_combined(fnames, class_names, parsers, compress_fields):
    combo_nt = create_combo_named_tuple_class(fnames, compress_fields)
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(fname, class_name, parser)
                          for fname, class_name, parser in zip(fnames, class_names, parsers)))

    merged_iter = (itertools.chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield combo_nt(*compressed_row)


data_iter = iter_combined(fnames, class_names,
                          parsers, compress_fields)

if __name__ == "__main__":
    for row in itertools.islice(data_iter, 5):
        print(row)
