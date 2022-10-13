class Otentikasi:
  def __init__(self):
    self.email = "renaldy12"
    self.password = "12"
    
  def login(self, input_email, input_password):
    if input_email == self.email:
      if input_password == self.password:
        print("Login Berhasil")