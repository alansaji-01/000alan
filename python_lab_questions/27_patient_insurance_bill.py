# Calculate a patient's bill after a 10 percent insurance deduction.
class Patient:
    def __init__(self, patient_id, name, disease, bill):
        self.patient_id, self.name, self.disease, self.bill = patient_id, name, disease, bill
    def final_bill(self):
        return self.bill * 0.90

if __name__ == '__main__':
    patient = Patient(101, 'Alan', 'Fever', 5000)
    print('Patient:', patient.name)
    print('Disease:', patient.disease)
    print('Original bill:', patient.bill)
    print('Final bill:', round(patient.final_bill(), 2))
