def hospital():
    r = int(input("enter number of patients::\n"))
    name = []
    id = []
    ph = []
    doc = []
    re = []
    for i in range(0, r):
        patient=(input("enter patient name::"))
        number = (input("enter phone number::"))
        patient_id = (input("enter id::"))
        doctor = (input("enter doctor name::"))
        reason = (input("enter the reason::"))
        try:
            print(" ")
            print("try part executed")
            raise
        except:
            print("execution raised")
        finally:
            print("always executed")
            print(" ")       
        name.append(patient)
        id.append(patient_id)
        ph.append(number)
        doc.append(doctor)
        re.append(reason)

    print("name\tid\tphone\tdoctor\tcause\t")

    for i in range(0, r):
        print(f'{ name[i]}   {id[i]}   { ph[i]}   {doc[i]}   {re[i]}')
hospital()
