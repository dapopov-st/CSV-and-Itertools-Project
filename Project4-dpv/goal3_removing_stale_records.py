# Goal 3

# Next, you want to identify any stale records, where stale simply means
# the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017).
# Create an iterator that only contains current records (i.e. not stale) based on the
#  `last_updated` field from the `status_update` file.
import datetime
import itertools
from goal2_combining_iterators_fb import iter_combined, fnames, class_names, parsers, compress_fields


def filter_records(data_iter):
    recent_records = filter(lambda x: x.last_updated >=
                            datetime.datetime(2017, 3, 1), list(data_iter))
    return recent_records


def filter_records_generic(fnames, class_names, parsers, compress_fields, key=None):
    """Keep only the data satisfying the criterion given in the key"""
    data_iter = iter_combined(fnames, class_names,
                              parsers, compress_fields)
    yield from filter(key, data_iter)


if __name__ == "__main__":
    recent_records = filter_records_generic(fnames, class_names, parsers, compress_fields,
                                            key=lambda x: x.last_updated >=
                                            datetime.datetime(2017, 3, 1))
    for row in itertools.islice(recent_records, 10):
        print(row)
        print()

    # OUTPUT:
    # Data(ssn='100-53-9824', first_name='Sebastiano', last_name='Tester', gender='Male', language='Icelandic', employer='Stiedemann-Bailey', department='Research and Development', employee_id='29-0890771', vehicle_make='Oldsmobile', vehicle_model='Bravada', model_year=1993, last_updated=datetime.datetime(2017, 10, 7, 0, 14, 42), created=datetime.datetime(2016, 1, 24, 21, 19, 30))

    # Data(ssn='101-84-0356', first_name='Nomi', last_name='Lipprose', gender='Female', language='Yiddish', employer='Connelly Group', department='Research and Development', employee_id='98-7952860', vehicle_make='GMC', vehicle_model='Yukon', model_year=2005, last_updated=datetime.datetime(2017, 10, 4, 11, 21, 30), created=datetime.datetime(2016, 9, 21, 23, 4, 7))

    # Data(ssn='104-22-0928', first_name='Justinian', last_name='Kunzelmann', gender='Male', language='Dhivehi', employer='Upton LLC', department='Marketing', employee_id='56-9817552', vehicle_make='Oldsmobile', vehicle_model='Intrigue', model_year=2000, last_updated=datetime.datetime(2017, 3, 28, 12, 38, 29), created=datetime.datetime(2016, 4, 15, 11, 37, 17))

    # Data(ssn='104-84-7144', first_name='Claudianus', last_name='Brixey', gender='Male', language='Afrikaans', employer='Zemlak-Olson', department='Business Development', employee_id='46-2886707', vehicle_make='Ford', vehicle_model='Crown Victoria', model_year=2008, last_updated=datetime.datetime(2018, 2, 19, 1, 34, 33), created=datetime.datetime(2016, 3, 15, 14, 7, 57))

    # Data(ssn='105-27-5541', first_name='Federico', last_name='Aggett', gender='Male', language='Chinese', employer='Kohler, Bradtke and Davis', department='Support', employee_id='80-0975518', vehicle_make='Ford', vehicle_model='Mustang', model_year=2001, last_updated=datetime.datetime(2017, 7, 24, 8, 58, 52), created=datetime.datetime(2016, 7, 23, 17, 58, 35))

    # Data(ssn='105-85-7486', first_name='Angelina', last_name='McAvey', gender='Female', language='Punjabi', employer='Roberts, Torphy and Dach', department='Human Resources', employee_id='77-4895332', vehicle_make='Chrysler', vehicle_model='300', model_year=2008, last_updated=datetime.datetime(2018, 2, 14, 11, 32, 39), created=datetime.datetime(2016, 12, 15, 5, 46, 43))

    # Data(ssn='105-91-5022', first_name='Moselle', last_name='Apfel', gender='Female', language='Latvian', employer='Lind-Jast', department='Marketing', employee_id='79-6418731', vehicle_make='Isuzu', vehicle_model='Hombre Space', model_year=2000, last_updated=datetime.datetime(2018, 3, 24, 14, 29, 33), created=datetime.datetime(2016, 3, 24, 3, 43, 3))

    # Data(ssn='105-91-7777', first_name='Audi', last_name='Roach', gender='Female', language='Estonian', employer='Bashirian-Lueilwitz', department='Engineering', employee_id='44-3328799', vehicle_make='Chevrolet', vehicle_model='Silverado 3500', model_year=2004, last_updated=datetime.datetime(2017, 5, 11, 1, 48, 32), created=datetime.datetime(2016, 5, 31, 0, 38, 13))

    # Data(ssn='106-35-1938', first_name='Mackenzie', last_name='Nussey', gender='Male', language='Swedish', employer='Windler, Marks and Haley', department='Services', employee_id='54-6271885', vehicle_make='GMC', vehicle_model='Sonoma Club', model_year=1992, last_updated=datetime.datetime(2017, 10, 21, 1, 7, 28), created=datetime.datetime(2016, 9, 8, 4, 2, 12))

    # Data(ssn='106-36-3293', first_name='Martino', last_name='Tregoning', gender='Male', language='Tok Pisin', employer='Leffler-Hahn', department='Accounting', employee_id='31-5735282', vehicle_make='Volkswagen', vehicle_model='Touareg', model_year=2008, last_updated=datetime.datetime(2017, 3, 18, 18, 24, 17), created=datetime.datetime(2016, 5, 16, 21, 21, 36))
