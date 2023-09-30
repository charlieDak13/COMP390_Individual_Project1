import meteor_data_class

# makes empty lists to hold filtered values
mass_list = []
year_list = []

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
                                                          split_list[4], split_list[5], split_list[6], split_list[7],
                                                          split_list[8], split_list[9], split_list[10], split_list[11])
# mass filter
        if meteor_object.mass == '':
            continue
        elif float(meteor_object.mass) > 2900000:
            mass_list.append(meteor_object.name + ', ' + meteor_object.mass)
# year filter
        if meteor_object.year == '':
            continue
        elif 2023 > int(meteor_object.year) >= 2013:
            year_list.append(meteor_object.name + ',' + meteor_object.year)

print(' ' * 2, 'Name', ' ' * 21, 'Mass (g)', ' ' * 16)
print('=' * 40)
count = 1
for i in range(len(mass_list)):
    splitMass = mass_list[i].split(',')
    print(f'{count:2} {splitMass[0]:25} {splitMass[1]:10}')
    count = count + 1
# year table
year_count = 1
print('=' * 40)
print(' ' * 2, 'Name', ' ' * 20, 'Year', ' ' * 16)
print('=' * 40)
for i in range(len(year_list)):
    splitYear = year_list[i].split(',')
    print(f'{year_count:2} {splitYear[0]:25} {splitYear[1]:5}')
    year_count = year_count + 1




