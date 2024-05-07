class hospital:
    def_init_(self, patient_name, patient_id, doctor_name, addmision_term,
    mobile_number, branch):
    self.patient_id = patient_id
    self.doctor_name = docter_name
    self.admission_term = admission_term
    self.mobile_number = mobile_number
    self.branch = branch

  def print_patient(self):
    line='{<14:}{<15:}{<20:}{<11:}{25:}'.format(self.patient_id=patient_id
    self.doctor_name=docter_name
    self.admission_term=admission_term
    self.mobile_number=mobile_number
    self.branch=branch)

    print(line)
   p1=patient("021","john luther","cancer ","9094534765","neurology")
   p2=patient("022","martin luther","survical cord","8880008398","neurology")
   print('{<14:}{<15:}{<20:}{<11:}{25:}'.format("patient_id",
    "docter_name","admission_term","mobile_number","branch"))
print("___________________________________________________________")
p1.print_patient()
p2.print_patient()