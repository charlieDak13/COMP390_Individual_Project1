import meteor_data_class


# from meteor_data_class import MeteorDataEntry
# from meteor_data_class import to_string
print(' ' * 2, 'Name', ' ' * 15, 'Mass', ' ' * 16)
print('=' * 40)
count = 1
year_count = 1


file = open('meteorite_landing_data.txt', 'r')
with file as text_file:
    file.readline()
    for line in file:
        split_list = line.strip('\n').split('\t')
        for i in range(12):
            if len(split_list) < 12:
                split_list.append('')
            else:
                pass
        meteor_object = meteor_data_class.MeteorDataEntry(split_list[0], split_list[1], split_list[2], split_list[3],
                                                          split_list[4],
                                                          split_list[5],
                                                          split_list[6], split_list[7], split_list[8], split_list[9],
                                                          split_list[10],
                                                          split_list[11])
    # meteor_list = []
    # meteor_list.append(meteor_object)
        # meteor_data_class.MeteorDataEntry.print_list(meteor_object, meteor_list)
        # filter_functions.sort_by_mass(meteor_list, split_list[4])
        mass_list = []
        if split_list[4] == '':
            continue
        elif float(split_list[4]) > 2900000:
            mass_list.append(split_list[0] + ' ' + split_list[4])

        for strings in mass_list:
            print(f'{count:2} {meteor_object.name:20} {meteor_object.mass:10}')
            count = count + 1
        # mass_dictionary_list = []
        # for i in range(len(mass_list)):
        #     mass_split = mass_list[i].split()
        #     mass_dict = {
        #         'Name': mass_split[0],
        #         'Mass': mass_split[1]
        #     }
        #     mass_dictionary_list.append(mass_dict)
        # for items in mass_dictionary_list:
        #
        #     print(count, mass_dict['Name'], mass_dict['Mass'])
        #     count = count + 1


# year filter
        year_list = []
        if meteor_object.year == '':
            continue
        elif 2023 > int(meteor_object.year) >= 2013:
            year_list.append(meteor_object.name + meteor_object.year)

        for element in year_list:
            print(f'{year_count:2} {meteor_object.name:25} {meteor_object.year:5}')
            year_count = year_count + 1





