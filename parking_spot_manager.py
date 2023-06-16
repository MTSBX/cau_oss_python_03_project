import file_manager


class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': longitude, 'latitude': latitude}
    #the elements are put into a dictionary
    def get(self, keyword='name'):
        return self.__item[keyword]

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list():
    path = './input/free_parking_spot_seoul.csv'
    lines = file_manager.read_file(path)
    return lines   #refer to the oss_python-week12-v2 PPT in e-class.

def print_spots():
    lines = str_list_to_class_list()
    for line in lines:
        print(line) #fetch each line in the file so that we can generate it

def filter_by_name(spots, name):
    if type(spots) is dict:
        return [spot for spot in spots if name in spot.get('name')]
    # the instruction which should be in the '[]',I asked the chatgpt and through refering to the basic structure of it ,I create this code
def filter_by_city(spots, city):
    if type(spots) is dict:
        return [spot for spot in spots if city in spot.get('city')]
    # the instruction which should be in the '[]',I asked the chatgpt and through refering to the basic structure of it ,I create this code
def filter_by_district(spots, district):
    if type(spots) is dict:
        return [spot for spot in spots if district in spot.get('district')]
    # the instruction which should be in the '[]',I asked the chatgpt and through refering to the basic structure of it ,I create this code
def filter_by_ptype(spots, ptype):
    if type(spots) is dict:
        return [spot for spot in spots if ptype in spot.get('ptype')]
    # the instruction which should be in the '[]',I asked the chatgpt and through refering to the basic structure of it ,I create this code
def filter_by_location(spots, locations):
    if type(spots) is dict:
        min_lat = locations
        max_lat=locations
        min_long=locations
        max_long = locations #conect the data label to the location
        return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_long < spot.get('longitude') < max_long]
    # the instruction which should be in the '[]',I asked the chatgpt and through refering to the basic structure of it ,I create this code
def sort_by_keyword(spots, keyword):
    if type(spots) is dict:
        return sorted(spots, key=lambda spot:spot.get(keyword))
    # this part I search the basic structure of lambda function so that I can use it .

#following the requirements create the print code
while True: # this means that if we not print [4] the programme will keep circulating
    print("--menu--")
    print("--[1]print--")
    print("--[2]filter--")
    print("--[3]sort--")
    print("--[4]exit--")
    user_input = input("type:")
    if user_input == "1":
        print("type:1")
        print("---print elements(477)---")
        print(print_spots()) # call out the print_spots function
    if user_input=="4":
        print("exit")
        break
    if user_input == "2": # if we press 2 ,trun into the filter part
        print("---filter by---")
        print("[1] name")
        print("[2] city")
        print("[3] district")
        print("[4] ptype")
        print("[5] location")
        user_input_2 = input("type:")
        if user_input_2 == "1":
            print("type:1")
            search_name=str(input("input the name:"))
            spots = str_list_to_class_list()
            name_result = filter_by_name(spots, search_name)
            print(name_result)# call out the name_result function
        if user_input_2 == "2":
            print("type:2")
            search_city=str(input("type city:"))
            spots_2 = str_list_to_class_list()
            city_result = filter_by_name(spots_2, search_city)
            print(city_result)# call out the city_result function
        if user_input_2 == "3":
            print("type:3")
            search_district=str(input("type district:"))
            spots_3 = str_list_to_class_list()
            district_result = filter_by_name(spots_3, search_district)
            print(district_result)# call out the district_result function
        if user_input_2 == "4":
            print("type:4")
            search_ptype=str(input("type ptype:"))
            spots_4 = str_list_to_class_list()
            ptype_result = filter_by_name(spots_4, search_ptype)
            print(ptype_result)# call out the ptype_result function
        if user_input_2 == "5":
            print("type:5")
            search_location=str(input("type location:"))
            spots_5 = str_list_to_class_list()
            location_result = filter_by_name(spots_5, search_location)
            print(location_result)# call out the location_result function
    if user_input == "3":
        print("type:3")
        print("---sort by---")
        print(['name', 'city', 'district', 'ptype', 'latitude', 'longitude'])
        spots = str_list_to_class_list()
        user_input_3=str(input("input the keyword"))
        sorted_spots = sort_by_keyword(spots, user_input_3)
        print(spots)
        print(f"keyword:{user_input_3}")