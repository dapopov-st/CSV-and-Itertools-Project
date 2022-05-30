# ##### Goal 1

# Your first task is to create iterators for each of the four files that contained cleaned up data,
# of the correct type (e.g. string, int, date, etc), and represented by a named tuple.
# For now these four iterators are just separate, independent iterators.

from itertools import islice
import csv
from collections import namedtuple
from datetime import datetime


from constants import files,  data_types, tuple_names


def explore_files():
    """Simple function for 'peeking' into files if these are particularly large"""
    for file in files:
        with open(file, 'r') as file:
            print(f"Printing contents of file {file.name}")
            for row in islice(csv.reader(file), 5):
                print(row)


# explore_files()


def validate_int(data, default=None):
    """Validates integer"""
    try:
        data = int(data)
    except ValueError as er:
        data = default
        print(
            f"Input is not of the format that can be converted to integer, returning default {default}")
    finally:
        return data


def validate_str(data, default=None):
    """Validates cleaned string"""
    try:
        data = str(data).strip()
        if len(data) == 0:
            data = default
    except:
        data = default
    finally:
        return data


def validate_dt(data, fmt='%Y-%m-%dT%H:%M:%SZ', default=None):
    """Validates datetime"""
    try:
        #data = datetime.fromisoformat(data[:-1])
        data = datetime.strptime(data, fmt=fmt)
    except ValueError:
        print(
            f"Input is not of the format that can be converted to datetime, returning default {default}")
        data = default
    finally:
        return data


def type_caster(val, type_):
    """Casts strings into ints and datetimes where appropriate"""
    if type_ == 'INT':
        return validate_int(val)
    elif type_ == 'DATETIME':
        return validate_dt(val, '%m/%d/%Y')
    return validate_str(val)  # don't change if it's a string already


def get_names(header, tuple_name='DefaultNt'):
    """Gets proper field names for a namedtuple"""
    headers = header.strip('\n').split(',')
    headers = (elt.replace(" ", "_").lower() for elt in headers)
    nt = namedtuple(tuple_name, headers)
    return nt


def csv_reader(file, delimiter=',', quotechar='"'):
    """Returns csv reader with the given delimiter and quotechar"""
    return csv.reader(file, delimiter=delimiter, quotechar=quotechar)


def file_iterator(file, data_types, tuple_name):
    """File iterator over csv_reader"""
    with open(file) as f:
        reader = csv_reader(f)
        nt = get_names(next(f), tuple_name=tuple_name)
        for r in reader:
            r = (type_caster(elt[0], elt[1]) for elt in zip(r, data_types))
            yield nt(*r)


def display_first_rows(num_rows=5):
    contents = [[] for _ in range(len(files))]
    for i in range(len(files)):
        print(f"File {files[i]}")
        contents[i] = file_iterator(
            files[i], data_types=data_types[i], tuple_name=tuple_names[i])
        for ticket in islice(contents[i], num_rows):
            print(ticket)


if __name__ == "__main__":
    display_first_rows(5)

    # #OUTPUT
    # File personal_info.csv
    # PersonalInfo(ssn='100-53-9824', first_name='Sebastiano', last_name='Tester', gender='Male', language='Icelandic')
    # PersonalInfo(ssn='101-71-4702', first_name='Cayla', last_name='MacDonagh', gender='Female', language='Lao')
    # PersonalInfo(ssn='101-84-0356', first_name='Nomi', last_name='Lipprose', gender='Female', language='Yiddish')
    # PersonalInfo(ssn='104-22-0928', first_name='Justinian', last_name='Kunzelmann', gender='Male', language='Dhivehi')
    # PersonalInfo(ssn='104-84-7144', first_name='Claudianus', last_name='Brixey', gender='Male', language='Afrikaans')
    # File vehicles.csv
    # Vehicles(ssn='100-53-9824', vehicle_make='Oldsmobile', vehicle_model='Bravada', model_year=1993)
    # Vehicles(ssn='101-71-4702', vehicle_make='Ford', vehicle_model='Mustang', model_year=1997)
    # Vehicles(ssn='101-84-0356', vehicle_make='GMC', vehicle_model='Yukon', model_year=2005)
    # Vehicles(ssn='104-22-0928', vehicle_make='Oldsmobile', vehicle_model='Intrigue', model_year=2000)
    # Vehicles(ssn='104-84-7144', vehicle_make='Ford', vehicle_model='Crown Victoria', model_year=2008)
    # File employment.csv
    # Employment(employer='Stiedemann-Bailey', department='Research and Development', employee_id='29-0890771', ssn='100-53-9824')
    # Employment(employer='Nicolas and Sons', department='Sales', employee_id='41-6841359', ssn='101-71-4702')
    # Employment(employer='Connelly Group', department='Research and Development', employee_id='98-7952860', ssn='101-84-0356')
    # Employment(employer='Upton LLC', department='Marketing', employee_id='56-9817552', ssn='104-22-0928')
    # Employment(employer='Zemlak-Olson', department='Business Development', employee_id='46-2886707', ssn='104-84-7144')
    # File update_status.csv
    # UpdateStatus(ssn='100-53-9824', last_updated='2017-10-07T00:14:42Z', created='2016-01-24T21:19:30Z')
    # UpdateStatus(ssn='101-71-4702', last_updated='2017-01-23T11:23:17Z', created='2016-01-27T04:32:57Z')
    # UpdateStatus(ssn='101-84-0356', last_updated='2017-10-04T11:21:30Z', created='2016-09-21T23:04:07Z')
    # UpdateStatus(ssn='104-22-0928', last_updated='2017-03-28T12:38:29Z', created='2016-04-15T11:37:17Z')
    # UpdateStatus(ssn='104-84-7144', last_updated='2018-02-19T01:34:33Z', created='2016-03-15T14:07:57Z')
