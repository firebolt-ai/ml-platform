class signup():
    def __init__(self, firstname, lastname, email, password, confirmPassword, hidden):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword
        self.hiddenInput = hidden
    
    def formBuilder(self, input):
        input.add(self.firstname)
        input.add(self.lastname)
        input.add(self.email)
        input.add(self.password, self.hiddenInput)
        input.add(self.confirmPassword, self.hiddenInput)
        input.save('signup/output/formBuilder.app.out')