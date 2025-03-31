class CartePizzeraException(Exception):
    """
    Exception raised for errors in the pizza menu.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)