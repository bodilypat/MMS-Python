ERD-diagram

User (1) --(M) Appointments
      |
      └── (M) MedicalRecords

Doctor (1) -- (M) Appointments
        |
        └── (M) MedicalRecords
        |
        └── (M) Prescriptions

Patients (1) -- (M) Appointments
         |
         └── (M) MedicalRecords
         |
         └── (M) Prescriptions
         |
         └── (M) Invoices
         |
         └── (1) Bed (admission)

Prescriptions (1) -- (M) PrescriptionsItems -- (M) Medicines

LabTests (1) -- (M)  LabReports -- (1) Patients

wards (1) -- (M) Beds -- (1) Patients (Optional)

Invoices (1) -- (M) InvoiceItems
