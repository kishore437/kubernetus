# file handling

a = open('hi.txt', 'w')
b = a.write('this is day28')
print(b)
a.close()

a = open('hi.txt', 'r')
b = a.read()
print(b)
a.close()

class kishore:
    def __init__(self,brand,battery,ram,camera):
        self.Brand=brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
    def display(self):
        print("Brand:",self.Brand)
        print("Battery:",self.battery)
        print("ram:",self.ram)
        print("camera:",self.camera)
obj=kishore("apple",'4000mah','8gb','48mp',)
obj.display()
