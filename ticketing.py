class Ticket:
    number_slots = 0
    parking_slot = 0
    parking_list = []

    def __init__(self,number_slot):
        self.number_slots = number_slot

    def display_slots(self):
        print(self.number_slots, self.parking_slot, self.parking_list)
    
    def register_details(self, number_plate, car_color):
        reg_dict = {}
        reg_dict['numberPlate'] = number_plate
        reg_dict['carColor'] = car_color
        self.parking_slot += 1
        reg_dict['parkingSlot'] = self.parking_slot
        self.parking_list.append(reg_dict)
    
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
        quit()

t = Ticket(6)
t.get_slot_number("123",1)
t.display_slots()
t.register_details("123", "White")
t.display_slots()
t.register_details("124", "Black")
t.display_slots()
t.display_status()
t.get_registration_numb("Black")
# t.vacate_slot(1)
t.display_slots()
t.display_status()
t.get_registration_numb("White")
t.get_slot_number("Black",0)
t.get_slot_number("123",1)
t.exit_system()



