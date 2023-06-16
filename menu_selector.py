import file_manager
import parking_spot_manager

def start_process(path):
    spots = parking_spot_manager.str_list_to_class_list(file_manager.read_file(path))
    #firstly I even didn't know how to link the outside file connects by calling functions in this file
    #I referred to many sample code that can link outside file into a programme and I finally made up my mind to create a 'spots' variable to make a role as link function.
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)
            # I'm sorry that I don't know how can I print the whole table without import parking_spot_manager file
            #the import part also refer to the PPT in e-class
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
                # I named the spots as a link ，and by inputing the keword which user want to achieve the requirement like'1:name,2:city,3...4...5...' ,I can turn to the certain calling function。
            elif select == 2:
                print("---filter by---")
                print("[1] name")
                print("[2] city")
                print("[3] district")
                print("[4] ptype")
                print("[5] location")
                select = int(input('type:'))
                if select == 1:
                    keyword = input('type name:')
                    filtered_list = parking_spot_manager.filter_by_name(path, keyword)
                    # as same as above if user input 1,turn to the 'name'
                    # this part from 1-5 in filter almost designed by myself , firstly it had some detail mistakes but referring to sample code that be searched on google and the PPT in e-class I made it.
                elif select == 2:
                    keyword = input('type city:')
                    filtered_list = parking_spot_manager.filter_by_city(path, keyword)
                    # as same as above if user input 2,turn to the 'city'
                elif select == 3:
                    keyword = input('type district:')
                    filtered_list = parking_spot_manager.filter_by_district(path, keyword)
                    # as same as above if user input 3,turn to the 'district'
                elif select == 4:
                    keyword = input('type ptype:')
                    filtered_list = parking_spot_manager.filter_by_ptype(path, keyword)
                    # as same as above if user input 4,turn to the 'ptype'
                elif select == 5:
                    min_lat = float(input('type min lat:'))
                    max_lat = float(input('type max lat:'))
                    min_lon = float(input('type min long:'))
                    max_lon = float(input('type max long:'))
                    filtered_list = parking_spot_manager.filter_by_location(path, min_lat, max_lat, min_lon, max_lon)
                else:
                    print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")  # if I press 4, the programme exited
            break
        else:
            print("invalid input")