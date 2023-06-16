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