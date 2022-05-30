# Goal 2

# Create a single iterable that combines all the columns from all the iterators.

# The iterable should yield named tuples containing all the columns.
# Make sure that the SSN's across the files match!
# All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
# Make sure the SSN is not repeated 4 times - one time per row is enough!

from operator import add
from itertools import chain, islice
from functools import reduce
from collections import namedtuple
from goal1_iterators import file_iterator
from constants import data_types, files, tuple_names


def files_iterator(files, data_types):
    """My solution to goal2.  It is not efficient since it does not use the fact that
    namedtuples should be created once and reused.  It would thus be better to return the
    joined dictionary"""
    with open(files[0]) as f0, open(files[1]) as f1, open(files[2]) as f2, open(files[3]) as f3:
        file0_iterator = file_iterator(files[0], data_types[0], tuple_names[0])
        file1_iterator = file_iterator(files[1], data_types[1], tuple_names[1])
        file2_iterator = file_iterator(files[2], data_types[2], tuple_names[2])
        file3_iterator = file_iterator(files[3], data_types[3], tuple_names[3])

        iterators = list(zip(file0_iterator, file1_iterator,
                         file2_iterator, file3_iterator))

        # RESET THE ITERATORS if use get_joined_nt_names in improved post-study code
        f0.seek(0), f1.seek(0), f2.seek(0), f3.seek(0)
        return iterators


def print_n_rows_joint(num_rows_to_display=5):
    """Print n rows of the joint namedtuple"""
    iterators = files_iterator(files, data_types,)
    for row in islice(iterators, num_rows_to_display):
        dict0, dict1, dict2, dict3 = row[0]._asdict(
        ), row[1]._asdict(), row[2]._asdict(), row[3]._asdict()
        if dict0['ssn'] == dict1['ssn'] == dict2['ssn'] == dict3['ssn']:
            print("Next joined nametuple: ")
            joined_dict = {**dict0, **dict1, **dict2, **dict3}
            joined_nt = namedtuple('JoinedNT', joined_dict.keys())(
                *joined_dict.values())
            print("Joined NT: ", joined_nt)


if __name__ == "__main__":
    print_n_rows_joint(10)
    # OUTPUT
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='100-53-9824', first_name='Sebastiano', last_name='Tester', gender='Male', language='Icelandic', vehicle_make='Oldsmobile', vehicle_model='Bravada', model_year=1993, employer='Stiedemann-Bailey', department='Research and Development', employee_id='29-0890771', last_updated='2017-10-07T00:14:42Z', created='2016-01-24T21:19:30Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='101-71-4702', first_name='Cayla', last_name='MacDonagh', gender='Female', language='Lao', vehicle_make='Ford', vehicle_model='Mustang', model_year=1997, employer='Nicolas and Sons', department='Sales', employee_id='41-6841359', last_updated='2017-01-23T11:23:17Z', created='2016-01-27T04:32:57Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='101-84-0356', first_name='Nomi', last_name='Lipprose', gender='Female', language='Yiddish', vehicle_make='GMC', vehicle_model='Yukon', model_year=2005, employer='Connelly Group', department='Research and Development', employee_id='98-7952860', last_updated='2017-10-04T11:21:30Z', created='2016-09-21T23:04:07Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='104-22-0928', first_name='Justinian', last_name='Kunzelmann', gender='Male', language='Dhivehi', vehicle_make='Oldsmobile', vehicle_model='Intrigue', model_year=2000, employer='Upton LLC', department='Marketing', employee_id='56-9817552', last_updated='2017-03-28T12:38:29Z', created='2016-04-15T11:37:17Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='104-84-7144', first_name='Claudianus', last_name='Brixey', gender='Male', language='Afrikaans', vehicle_make='Ford', vehicle_model='Crown Victoria', model_year=2008, employer='Zemlak-Olson', department='Business Development', employee_id='46-2886707', last_updated='2018-02-19T01:34:33Z', created='2016-03-15T14:07:57Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='105-27-5541', first_name='Federico', last_name='Aggett', gender='Male', language='Chinese', vehicle_make='Ford', vehicle_model='Mustang', model_year=2001, employer='Kohler, Bradtke and Davis', department='Support', employee_id='80-0975518', last_updated='2017-07-24T08:58:52Z', created='2016-07-23T17:58:35Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='105-85-7486', first_name='Angelina', last_name='McAvey', gender='Female', language='Punjabi', vehicle_make='Chrysler', vehicle_model='300', model_year=2008, employer='Roberts, Torphy and Dach', department='Human Resources', employee_id='77-4895332', last_updated='2018-02-14T11:32:39Z', created='2016-12-15T05:46:43Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='105-91-5022', first_name='Moselle', last_name='Apfel', gender='Female', language='Latvian', vehicle_make='Isuzu', vehicle_model='Hombre Space', model_year=2000, employer='Lind-Jast', department='Marketing', employee_id='79-6418731', last_updated='2018-03-24T14:29:33Z', created='2016-03-24T03:43:03Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='105-91-7777', first_name='Audi', last_name='Roach', gender='Female', language='Estonian', vehicle_make='Chevrolet', vehicle_model='Silverado 3500', model_year=2004, employer='Bashirian-Lueilwitz', department='Engineering', employee_id='44-3328799', last_updated='2017-05-11T01:48:32Z', created='2016-05-31T00:38:13Z')
    # Next joined nametuple:
    # Joined NT:  JoinedNT(ssn='106-35-1938', first_name='Mackenzie', last_name='Nussey', gender='Male', language='Swedish', vehicle_make='GMC', vehicle_model='Sonoma Club', model_year=1992, employer='Windler, Marks and Haley', department='Services', employee_id='54-6271885', last_updated='2017-10-21T01:07:28Z', created='2016-09-08T04:02:12Z')


# OTHER SCRATCHWORK AND EXPERIMENTS

# SNIFF OUT THE NAME: MAKE THIS INTO A FUNCTION
# for row in islice(iterators, 1):
#     print("ROW 0 FIELDS: ", row[0]._fields)
#     print("ROW 1 FIELDS: ", row[1]._fields)
#     all_fields = row[0]._fields + row[1]._fields + \
#         row[2]._fields+row[3]._fields
#     all_fields = ('ssn',) + \
#         tuple(elt for elt in all_fields if elt != 'ssn')
#     joined_nt = namedtuple('JoinedNT', all_fields)
#     print(all_fields)


# You've pretty much nailed it as far as vanilla Python is concerned, but there's an extra simplification you can do if you're using Python 3.5+.

A = namedtuple("A", "a b c")
B = namedtuple("B", "d e")
a = A(10, 20, 30)
b = B(40, 50)
C = namedtuple("C", A._fields + B._fields)
# print(C(*(a + b)))
# C(a=10, b=20, c=30, d=40, e=50)
# Available in Python 3.5+
#print(C(*a, *b))
# C(a=10, b=20, c=30, d=40, e=50)
# print(A._fields)


def namedtuplemerge(*args):
    cls = namedtuple('_'.join(arg.__class__.__name__ for arg in args), reduce(
        add, (arg._fields for arg in args)))
    return cls(*chain(*args))


contents = [[] for _ in range(4)]
for i in range(4):
    #print(f"File {files[i]}")
    # contents[i] = list(chain(file_iterator(
    #     files[i], data_types=data_types[i], tuple_name=tuple_names[i])))
    contents[i] = file_iterator(
        files[i], data_types=data_types[i], tuple_name=tuple_names[i])
# print(contents)
#args = files
#all_names = list(nt[0]._fields for nt in contents)
# reduced = reduce(add, list(nt[0]._fields for nt in contents))
# # make 'ssn' appear as the first field
# fields_ = ('ssn',) + tuple(set(reduced)-{'ssn'})

# fields_ = ('ssn',)+tuple(set(contents[0][0]._fields + contents[1]
# [0]._fields+contents[2][0]._fields+contents[3][0]._fields)-{'ssn'})
# print(fields_)

# C = namedtuple("C", contents[0][0]._fields + contents[1][0]._fields)
# print(C(*a, *b))

# print(namedtuplemerge(contents[0], contents[1]))


# Loop through rows
# for each row, chain across row (ie, apply merge to each row) if ssn == for each arg


# print(len(contents))
#print(list(nt._fields for nt in contents))
#print(list((nt[0] for nt in contents)))
#print(list((nt[0] for nt in contents if not nt.ssn)))
def joined_fieldnames(contents):
    # To make this function self-contained, consider placing the import inside the function
    #from functools import reduce
    reduced = reduce(
        add, (nt[0]._fields for nt in contents))
    #print('REDUCED', reduced)
    reduced_ = ('ssn',)+tuple(elt for elt in reduced if elt != 'ssn')
    # print(reduced_)
    nt_joint = namedtuple("Joined", reduced_)
    #print("FIELDS: ", nt_joint._fields)
    return nt_joint


# joined_nt = joined_fieldnames(contents)
# count = 0
# for row in joined_nt(*chain(*files)):
#     print(joined_nt(row))
# # print(count)


# print(joined_nt(*chain(*files)))


# def files_iterator(files, data_types):
#     #FILES NOT OPENING CORRECTLY
#     with open(files[0]) as f0, open(files[1]) as f1, open(files[2]) as f2, open(files[3]) as f3:
#         reader0, reader1, reader2, reader3 = csv.reader(
#             f0), csv.reader(f1), csv.reader(f2), csv.reader(f3)
#         readers = reader0, reader1, reader2, reader3
#         nts = get_names(next(f0)), get_names(
#             next(f1)), get_names(next(f2)), get_names(next(f3))
#         yield from reader0


# print(files_iterator(files, data_types))


# def display_first_rows(num_rows=5):
#     contents = [[] for _ in range(len(files))]
#     for i in range(len(files)):
#         print(f"File {files[i]}")
#         contents[i] = files_iterator(
#             files[i], data_types=data_types[i])  # , tuple_name=tuple_names[i])
#         for ticket in islice(contents[i], num_rows):
#             print(ticket)


# display_first_rows(5)

def get_joined_nt_names():
    with open(files[0]) as f0, open(files[1]) as f1, open(files[2]) as f2, open(files[3]) as f3:
        file0_iterator = file_iterator(files[0], data_types[0], tuple_names[0])
        file1_iterator = file_iterator(files[1], data_types[1], tuple_names[1])
        file2_iterator = file_iterator(files[2], data_types[2], tuple_names[2])
        file3_iterator = file_iterator(files[3], data_types[3], tuple_names[3])

        iterators = list(zip(file0_iterator, file1_iterator,
                         file2_iterator, file3_iterator))

        # SNIFF OUT THE NAME: MAKE THIS INTO A FUNCTION
        for row in islice(iterators, 1):
            #print("ROW 0 FIELDS: ", row[0]._fields)
            #print("ROW 1 FIELDS: ", row[1]._fields)
            all_fields = row[0]._fields + row[1]._fields + \
                row[2]._fields+row[3]._fields
            all_fields = ('ssn',) + \
                tuple(elt for elt in all_fields if elt != 'ssn')
            joined_nt = namedtuple('JoinedNT', all_fields)
            # print(all_fields)
            return joined_nt


# def files_iterator(files, data_types):
#     with open(files[0]) as f0, open(files[1]) as f1, open(files[2]) as f2, open(files[3]) as f3:
#         reader0, reader1, reader2, reader3 = csv.reader(
#             f0), csv.reader(f1), csv.reader(f2), csv.reader(f3)
#         readers = zip(reader0, reader1, reader2, reader3)
#         #print("READERS: ", list(readers))
#         nt0, nt1, nt2, nt3 = get_names(next(f0), tuple_names[0]), get_names(
#             next(f1), tuple_names[1]), get_names(next(f2), tuple_names[2]), get_names(next(f3), tuple_names[3])
#         # print(nt0)
#         # print(nt1)
#         #print("LEN READERS: ", len(readers))

#         # for r0 in readers:
#         #     r0 = (type_caster(elt[0], elt[1])
#         #           for elt in zip(r0, data_types[0]))

#         #     print("NEXT", nt0(*r0).ssn)

#         for (r0, r1, r2, r3) in readers:
#             r0 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r0, data_types[0]))
#             r1 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r1, data_types[1]))
#             r2 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r2, data_types[2]))
#             r3 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r3, data_types[3]))
#             # yield list(chain(nt0(*r0), nt1(*r1), nt2(*r2), nt3(*r3)))
#             # yield list(chain(nt0(*r0), nt1(*r1), nt2(*r2), nt3(*r3)))
#             # print(nt0(*r0).ssn)
#             # print(nt1(*r1).ssn)
#             if nt0(*r0).ssn == nt1(*r1).ssn == nt2(*r2).ssn == nt3(*r3).ssn:
#                 print(list(zip(nt0(*r0), nt1(*r1), nt2(*r2), nt3(*r3))))


#             # print("R0", nt0(*r0))
#             # yield r0
#             # yield r1
#             # yield r2
#             # yield r3
# print("FILES ITERATOR: ", files_iterator(files, data_types=data_types))


# BACKUP
# def files_iterator(files, data_types):
#     with open(files[0]) as f0, open(files[1]) as f1, open(files[2]) as f2, open(files[3]) as f3:
#         reader0, reader1, reader2, reader3 = csv.reader(
#             f0), csv.reader(f1), csv.reader(f2), csv.reader(f3)
#         readers = reader0, reader1, reader2, reader3
#         nt0, nt1, nt2, nt3 = get_names(next(f0)), get_names(
#             next(f1)), get_names(next(f2)), get_names(next(f3))
#         print("LEN READERS: ", len(readers))
#         for r0, r1, r2, r3 in readers:
#             r0 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r0, data_types[0]))
#             r1 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r0, data_types[0]))
#             r2 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r0, data_types[0]))
#             r3 = (type_caster(elt[0], elt[1])
#                   for elt in zip(r0, data_types[0]))
#             # yield list(chain(nt0(*r0), nt1(*r1), nt2(*r2), nt3(*r3)))
#             # yield list(chain(nt0(*r0), nt1(*r1), nt2(*r2), nt3(*r3)))
#             print("R0", nt0(*r0))
#             yield r0
#             yield r1
#             yield r2
#             yield r3


# print("FILES ITERATOR: ", files_iterator(files, data_types=data_types))

# for i in range(len(contents[0])):
#     print("NEXT: ")
#     if contents[0][i].ssn == contents[1][i].ssn == contents[2][i].ssn == contents[3][i].ssn:
#         print(joined_nt(contents[0][i], contents[1]
#               [i], contents[2][i], contents[3][i]))

# for j in range(len(files)):
#     # for k in range(len(contents[0][]))
#     # if contents[0]
#     #print(i, j)
#     elt = contents[j][i]
#     print(elt)
#     if
#     print(elt.ssn)
#print(f"File {files[i]}")
#contents[i] = file_iterator(files[i], data_types=filetypes[i])
# print(contents)
