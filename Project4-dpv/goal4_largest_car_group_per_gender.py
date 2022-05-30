# ##### Goal 4

# Start with the filtered data from Goal #3
# Find the largest group of car makes for each gender.

# Possibly more than one such group per gender exists (equal sizes).

# First sort by gender to allow groups to be made in correct order
# Then use groupby
from goal2_combining_iterators_fb import fnames, class_names, parsers, compress_fields
from goal3_removing_stale_records import filter_records_generic
import itertools
import datetime


def group_counts(group, category):
    return ((elt[0][1], len(list(elt[1])))
            for elt in group if elt[0][0] == category)


def group_by_grouping_key(fnames, class_names, parsers, compress_fields, category='Female', filter_key=lambda x: x.last_updated >=
                          datetime.datetime(2017, 3, 1), grouping_key=lambda elt: (elt.gender, elt.vehicle_make)):
    """
    Group data from multiple files, filtered by filter_key,  by grouping key
    """
    filtered_data = filter_records_generic(fnames, class_names, parsers, compress_fields,
                                           key=filter_key)
    sorted_data = sorted(filtered_data, key=grouping_key)

    group = itertools.groupby(sorted_data, key=grouping_key)

    group = ((elt[0][1], len(list(elt[1])))
             for elt in group if elt[0][0] == category)
    return list(sorted(group, key=lambda elt: elt[1], reverse=True))


def display_groups():
    for gender in ['Female', 'Male']:
        print(f"{gender} groups:")
        print(group_by_grouping_key(fnames, class_names,
              parsers, compress_fields, category=gender))


if __name__ == "__main__":
    display_groups()
    # OUTPUT:
    # Female groups:
    # [('Chevrolet', 42), ('Ford', 42), ('GMC', 22), ('Mitsubishi', 22), ('Toyota', 20), ('Dodge', 17), ('Mercedes-Benz', 17), ('Lexus', 15), ('Pontiac', 14), ('Audi', 13), ('Mazda', 13), ('Volvo', 13), ('BMW', 12), ('Nissan', 12), ('Suzuki', 12), ('Buick', 11), ('Volkswagen', 10), ('Acura', 9), ('Infiniti', 9), ('Kia', 9), ('Honda', 8), ('Land Rover', 8), ('Oldsmobile', 8), ('Cadillac', 6), ('Chrysler', 6), ('Subaru', 6), ('Jeep', 5), ('Lotus', 5), ('Mercury', 5), ('Bentley', 4), ('Hyundai', 4), ('Lincoln', 4), ('Isuzu', 3), ('Jaguar', 3), ('Plymouth', 3), ('Porsche', 3), ('Saab', 3), ('Saturn', 3), ('Aston Martin', 2), ('Lamborghini', 2), ('Scion', 2), ('Austin', 1), ('Bugatti', 1), ('Eagle', 1), ('Geo', 1), ('Morgan', 1), ('Panoz', 1), ('Rolls-Royce', 1)]
    # Male groups:
    # [('Ford', 40), ('Chevrolet', 30), ('GMC', 28), ('Mitsubishi', 28), ('Dodge', 22), ('Toyota', 21), ('Mercedes-Benz', 19), ('Volkswagen', 16), ('Audi', 14), ('Buick', 13), ('Mazda', 13), ('BMW', 12), ('Mercury', 11), ('Pontiac', 11), ('Volvo', 10), ('Cadillac', 9), ('Honda', 9), ('Hyundai', 8), ('Saab', 8), ('Subaru', 8), ('Acura', 7), ('Infiniti', 7), ('Jeep', 7), ('Lexus', 6), ('Nissan', 6), ('Kia', 5), ('Lincoln', 5), ('Lotus', 5), ('Oldsmobile', 5), ('Jaguar', 4), ('Lamborghini', 4), ('Plymouth', 4), ('Porsche', 4), ('Aston Martin', 3), ('Bentley', 3), ('Chrysler', 3), ('Isuzu', 3), ('Land Rover', 3), ('Maserati', 3), ('Saturn', 3), ('Geo', 2), ('Maybach', 2), ('Panoz', 2), ('Suzuki', 2), ('Aptera', 1), ('Austin', 1), ('Corbin', 1), ('Daewoo', 1), ('Eagle', 1), ('Jensen', 1), ('Rolls-Royce', 1), ('Scion', 1), ('Smart', 1)]
