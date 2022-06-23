class Client:
    all = []

    def __init__(self, name: str, idd_client: int, address: str, phone: str, email: str = None):

        assert len(name) >= 8, f"Name should be greater than 8 characters"
        assert len(name) <= 16, f"Name should be lesser than 16 characters"
        assert idd_client > 0, f"Id should be greater than 0"
        assert len(phone) > 0, f"Phone be greater than 0"

        self.__name = name
        self.__idd_client = idd_client
        self.__address = address
        self.__phone = phone
        self.__email = email

        Client.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def idd(self):
        return self.__idd_client

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.__name}', " \
               f"{self.__idd_client}, {self.__address}, {self.__phone}, {self.__email} )"



