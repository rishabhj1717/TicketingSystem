
class Ticket():
    number_slots = 0
    parking_slot = 0
    parking_list = []

    def __init__(self,number_slot):
        self.number_slots = number_slot
        print("Created a parking slot with " + str(self.number_slots) + " slots")

    def display_slots(self):
        print(self.number_slots, self.parking_slot, self.parking_list)
    

    def get_empty_slot(self):
        if(self.parking_slot < self.number_slots and self.number_slots != 0):
            empty_list = [index for index,obj in enumerate(self.parking_list,start=1) if not bool(obj)]
            val = self.parking_slot
            if(val==0 or len(empty_list)<=0 or (len(empty_list)>0 and empty_list[0]>val)):
                self.parking_slot += 1
                return self.parking_slot
            elif(len(empty_list)>0 and empty_list[0]<val):
                return empty_list[0]
        elif(self.parking_slot > self.number_slots and self.number_slots!=0):
            empty_list = [index for index,obj in enumerate(self.parking_list,start=1) if not bool(obj)]
            if(len(empty_list)>0):
                return empty_list[0]
            else:
                return -1
            
    
    def register_details(self, number_plate, car_color):
        if(self.parking_slot < self.number_slots or self.get_empty_slot()!=-1):
            slot_val = self.get_empty_slot()
            if(slot_val>self.number_slots or self.number_slots == -1):
                print("Parking is full, Sorry")
                return
            elif(slot_val>=len(self.parking_list)):    
                reg_dict = {}
                reg_dict['numberPlate'] = number_plate
                reg_dict['carColor'] = car_color
                reg_dict['parkingSlot'] = slot_val
                self.parking_list.append(reg_dict)
            elif(slot_val<=len(self.parking_list)):
                reg_dict = {}
                reg_dict['numberPlate'] = number_plate
                reg_dict['carColor'] = car_color
                reg_dict['parkingSlot'] = slot_val
                self.parking_list[slot_val-1] = reg_dict
            print("Allocated slot number: "+ str(slot_val))
        else:
            print("Parking is full")
    
    def vacate_slot(self, car_slot):
        if(len(self.parking_list)>0):
            self.parking_list[car_slot - 1] = {}
        else:
            print("No data as no one has parked their vehicles")

    def display_status(self):
        if(len(self.parking_list)>0):
            formatted_row = '{:<10} {:<20} {:<10}'
            print(formatted_row.format("Slot No.", "Registration Number", "Car Colour"))
            for obj in self.parking_list:
                if(bool(obj)):
                    print(formatted_row.format(obj['parkingSlot'],obj['numberPlate'],obj['carColor']))
        else:
            print("No data as no one has parked their vehicles")

    def get_registration_numb(self, data):
        if(len(self.parking_list)>0):
            reg_list = [obj['numberPlate'] for obj in self.parking_list if bool(obj) and obj['carColor'] == data]
            if(len(reg_list)>0):
                print(reg_list)
            else:
                print("No registration number for car colour as "+data)
        else:
            print("No data as no one has parked their vehicles")
    
    def get_slot_number(self, data,flag):
        '''0 -> Slot numbers of all slots where a car of a particular colour is parked.
            1 -> Slot number in which a car with a given registration number is parked. '''
        if(len(self.parking_list)>0):
            if(flag==0):
                slot_list = [obj['parkingSlot'] for obj in self.parking_list if bool(obj) and obj['carColor'] == data]
                if(len(slot_list)>0):
                    print(slot_list)
                else:
                    print("No slot number for car colour as "+data)
            
            elif(flag==1):
                slot_list = [obj['parkingSlot'] for obj in self.parking_list if bool(obj) and obj['numberPlate'] == data]
                if(len(slot_list)>0):
                    print(slot_list)
                else:
                    print("No slot number for car registration number as "+ data)
        else:
            print("No data as no one has parked their vehicles")
            


    def exit_system(self):
        print("Bye")
        quit()

# t = Ticket(6)
# t.register_details("123","White")
# t.register_details("124","Red")
# t.register_details("125","Black")
# t.register_details("126","Black")
# t.display_slots()
# t.display_status()
# t.vacate_slot(2)
# t.display_slots()
# t.display_status()
# t.register_details("127","Blue")
# t.display_slots()
# t.display_status()

    

while(True):
    command = raw_input("Welcome to the ticketing console. Hope it works fine for you.\n")
    # t = Ticket(0)
    if(command.split()[0] == 'create_parking_lot'):
        park_slots_total = command.split()[1]
        t = Ticket(int(park_slots_total))
    if(command.split()[0] == 'park'):
        reg_number = command.split()[1]
        car_colour = command.split()[2]
        t.register_details(reg_number,car_colour)
    if(command.split()[0] == 'leave'):
        slot_to_vacate = command.split()[1]
        t.vacate_slot(int(slot_to_vacate))
    if(command.split()[0] == 'status'):
        t.display_status()
    if(command.split()[0] == 'registration_numbers_for_cars_with_colour'):
        colour_of_car = command.split()[1]
        t.get_registration_numb(colour_of_car)
    if(command.split()[0] == 'slot_numbers_for_cars_with_colour'):
        colour_of_car = command.split()[1]
        t.get_slot_number(colour_of_car,0)
    if(command.split()[0] == 'slot_number_for_registration_number'):
        registr_number = command.split()[1]
        t.get_slot_number(registr_number,1)
    if(command.split()[0] == 'exit'):
        t.exit_system()

