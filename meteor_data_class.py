class MeteorDataEntry:

    def __init__(self, name, id, nameType, recClass, mass, fall, year, recLat, recLong, geoLocation, states, countries):
        self.name = name
        self.id = id
        self.nameType = nameType
        self.recClass = recClass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.recLat = recLat
        self.recLong = recLong
        self.geoLocation = geoLocation
        self.states = states
        self.countries = countries

    def print_mass_list(self, lst):

        for items in lst:
            print(self.name, self.id, self.nameType, self.recClass, self.mass, self.fall, self.year, self.recLat,
                  self.recLong, self.geoLocation, self.states, self.countries)


