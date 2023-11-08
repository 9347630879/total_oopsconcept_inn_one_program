class address:
    __address: str = " "

    def __init__(self):
        pass

    def setaddress(self, address: str):
        self.address = address

    def getaddress(self) -> str:
        return self.address


address = address()
address.setaddress("84/176-2,Shareen nagar , Kurnool")
print(address.getaddress())


class Employee(address):
    __fname: str = " "
    __lname: str = " "
    __address: str = " "

    def __init__(self, fname, lname):
        super().__init__()
        self.__fname = fname
        self.__lname = lname

    def getfullname(self) -> str:
        return f'fullname:{self.__fname} {self.__lname}'

    def salcal(self) -> float:
        pass


class permanentemployee(Employee):
    __sal: float = 500

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        pass

    def salcal(self) -> float:
        return self.__sal * 12


class contractemployee(Employee):
    __sal: float = 500

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        pass

    def salcal(self,hrs:int) -> float:
        return self.__sal * hrs





emp = permanentemployee("Sai", "Sundhar")
name = emp.getaddress()
print(name)
emp.setaddress("Kurnool")
a = emp.getaddress()
print(a)
print(emp.salcal())

emp = contractemployee("Dhanunjai","Gokavaram")
name = emp.getaddress()
print(name)
emp.setaddress("Tirupathi")
a = emp.getaddress()
print(a)
print(emp.salcal(24))
