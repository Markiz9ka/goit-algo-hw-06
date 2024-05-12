from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.validate_phone(value):
              raise ValueError
        self.value = value

    def __str__(self):
        return str(self.value)
    
    @staticmethod
    def validate_phone(phone):
          return True
        

class Name(Field):
    pass

class Phone(Field):
    @staticmethod
    def validate_phone(phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
         new_phone = Phone(phone)
         self.phones.append(Phone(phone))
         return new_phone
    
    def find_phone(self,phone):
        for p in self.phones:
            if p.value == phone:
               return p
        return None  
    
    def remove_phone(self,phone):
        del_phone = self.find_phone()
        if del_phone:
             self.phones.pop(del_phone)
        return del_phone
    
    def edit_phone(self,old_phone,new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
             raise ValueError

    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p).value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value] = record

    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        if name in self.data:
            self.data.pop(name)
