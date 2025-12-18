Full-Stack-Medical-Management-System-Folder-Structure
│
├── backend-MMS using Python                            # FastAPI Backend (Python)
│   ├── app/  
│   │   ├── main.py                           			# FastAPI app entry
│   │   ├── database.py                                 # DB connection & session
│   │   │
│   │   ├── core/                                       # Core system configuration
│   │   │   ├── config.py                               # Environment variables       
│   │   │   ├── security.py                             # JWT, password hashing
│   │   │   ├── dependencies.py                         # Auth & role dependencies
│   │   │   └── logging.py                              # Audit & system logs 
│   │   ├── auth/    
│   │   │   ├── auth_router.py                                   
│   │   │   ├── auth_service.py
│   │   │   ├── auth_schema.py
│   │   │   ├── auth_utils.py
│   │   │   └── oauth2_handler.py
│   │   ├── models/                           			# SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── patient.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── medical_record.py
│   │   │   ├── prescription.py
│   │   │   └── billing.py
│   │   ├── schemas/                                     # Pydantic data validation
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── patient.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── medical_record.py
│   │   │   ├── prescription.py
│   │   │   └── billing.py
│   │   │
│   │   ├── services/                                                # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── patient_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── prescription_service.py
│   │   │   └── billing_service.py
│   │   │
│   │   ├── routers/                           			             # FastAPI endpoints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── patients.py
│   │   │   ├── doctors.py
│   │   │   ├── appointments.py
│   │   │   ├── medical_records.py
│   │   │   ├── prescriptions.py
│   │   │   └── billings.py
│   │   │
│   │   ├── utils/                                                    # Reusable utitlities
│   │   │   ├── jwt_handler.py 
│   │   │   ├── password_hasher.py
│   │   │   ├── email_sender.py
│   │   │   ├── pdf_generator.py                                    
│   │   │   ├── logger.py
│   │   │   └── constants.py
│   │   │
│   │   ├── tests/                                       
│   │   │   ├── test_auth.py 
│   │   │   ├── test_user.py
│   │   │   ├── test_patient.py
│   │   │   ├── test_doctor.py
│   │   │   ├── test_appointments.py
│   │   │   └── test_billing.py
│   │   └── static/   
│   │       ├── reports/
│   │       └── uploads/                                                                                                             
│   ├── requirements.txt                                          
│   └── lembic.ini                                                     
│ 
├── database/                                                 # SQL files and seeders
│   ├── init.sql                                              # Create tables
│   ├── seed.sql                                              # Seed sample data
│   └── README.md   
│ 
├── Frontend-MMS using-React/                      
│   ├── public                                        
│   │   ├── favicon.ico
│   │   ├── manifest.json
│   │   └── hospital-logo.png                                 
│   │     
│   ├── src/                              
│   │   │
│   │   ├── api/	                                         # Reusable API files grouped by feature
│   │   │ 	├── authApi.js
│   │   │ 	├── patientApi.js
│   │   │ 	├── doctorApi.js 
│   │   │ 	├── appointmentApi.js    
│   │   │ 	├── billingApi.js
│   │   │ 	├── prescriptionApi.js    
│   │   │   └── settingApi.js                 
│   │   ├── assets/	
│   │   │ 	├── images/    
│   │   │ 	├── icons/
│   │   │   └── styles/                                
│   │   │   	├── global.css
│   │   │   	└── variables.css 
│   │   ├── components/	                                    # Common UI & reusable components
│   │   │ 	├── layout/ 
│   │   │   │	├── Header.jsx
│   │   │   │	├── Sidebar.jsx
│   │   │   │	├── Footer.jsx
│   │   │   │	├── Loader.jsx
│   │   │   │	└── ProtectedRoute.jsx 
│   │   │ 	├── forms/ 
│   │   │   │	├── PatientForm.jsx
│   │   │   │	├── DoctorForm.jsx
│   │   │   │	├── AppointmentForm.jsx
│   │   │   │	├── BillingForm.jsx
│   │   │   │	├── PrescriptionForm.jsx
│   │   │   │	├── ProfileForm.jsx
│   │   │   │	└── AppConfigForm.jsx 
│   │   │ 	├── tables/ 
│   │   │   │	├── PatientTable.jsx
│   │   │   │	├── DoctorTable.jsx
│   │   │   │	├── AppointmentTable.jsx
│   │   │   │	├── BillingTable.jsx
│   │   │   │	└── Prescription.jsx 
│   │   │ 	├── ui/ 
│   │   │   │	├── SearchBar.jsx
│   │   │   │	└── Pagination.jsx 
│   │   │   └── common/                                
│   │   │   	├── Button.jsx
│   │   │   	├── Modal.jsx
│   │   │   	└── Card.jsx 
│   │   ├── pages/	
│   │   │ 	├── Auth/   
│   │   │   │	├── Login.jsx
│   │   │   │	├── Register.jsx
│   │   │   │	└── ForgotPassword.jsx  
│   │   │ 	├── Dashboard/
│   │   │   │	├── AdminDasboard.jsx
│   │   │   │	├── DoctorDashboard.jsx
│   │   │   │	└── ReceptionDashboard.jsx 
│   │   │ 	├── Patients/
│   │   │   │	├── PatientList.jsx
│   │   │   │	├── AddPatient.jsx
│   │   │   │	├── EditPatient.jsx
│   │   │   │	└── PatientDetail.jsx 
│   │   │ 	├── Doctors/
│   │   │   │	├── DoctorList.jsx
│   │   │   │	├── AddDoctor.jsx
│   │   │   │	├── EditDoctor.jsx
│   │   │   │	└── DoctorProfile.jsx 
│   │   │ 	├── Appointments/
│   │   │   │	├── AppointmentList.jsx
│   │   │   │	├── BookAppointment.jsx
│   │   │   │	├── EditAppointment.jsx
│   │   │   │	└── ViewAppointment.jsx 
│   │   │ 	├── Billing/
│   │   │   │	├── BillingList.jsx
│   │   │   │	├── AddBilling.jsx
│   │   │   │	├── EditBillnig.jsx
│   │   │   │	└── ViewBilling.jsx 
│   │   │ 	├── Pharmacy/
│   │   │   │	├── MedicineList.jsx
│   │   │   │	├── AddMedicine.jsx
│   │   │   │	└── IssueMedicine.jsx 
│   │   │ 	├── Laboratory/
│   │   │   │	├── TestList.jsx
│   │   │   │	├── AddTest.jsx
│   │   │   │	└── TestReports.jsx 
│   │   │ 	├── Wards/
│   │   │   │	├── WardList.jsx
│   │   │   │	├── BedList.jsx
│   │   │   │	└── AssignBed.jsx 
│   │   │   └── Error/  
│   │   │   	├── NotFound.jsx
│   │   │   	└── Unautorized.jsx  
│   │   ├── context/	                                   # Global State (Authentication, Theme, User role)
│   │   │ 	├── AuthContext.jsx   
│   │   │ 	├── UserContext.jsx
│   │   │   └── ThemeContext.jsx
│   │   ├── hooks/	
│   │   │ 	├── useAuth.js
│   │   │ 	├── useFetch.js   
│   │   │ 	├── useDebounce.js
│   │   │   └── usePagination.js   
│   │   ├── layouts/	                                   # Different role-layouts
│   │   │ 	├── AdminLayout.jsx    
│   │   │ 	├── DoctorLayout.jsx
│   │   │ 	├── ReceptionistLayout.jsx
│   │   │   └── AuthLayout.jsx
│   │   ├── routes/	                                      # Centralized routing including 
│   │   │ 	├── AppRoutes.jsx                             # Protected Routes
│   │   │   └── RoleBaseRoutes.jsx                        # Role-Based Routes
│   │   ├── services/	
│   │   │ 	├── images/    
│   │   │ 	├── icons/
│   │   │   └── styles/   
│   │   ├── types/	
│   │   │ 	├── PatientTypes.js    
│   │   │ 	├── doctorType.js
│   │   │   └── AppointmentType.js  
│   │   ├── config/	
│   │   │ 	├── env.js  
│   │   │ 	├── routeConfig.js
│   │   │   └── theme.js
│   │   └── utils/                                        # Helper functions, constants, dte utitlities, validators 
│   │    	├── formatDate.js    
│   │    	├── validators.js
│   │    	├── constants.js
│   │       └── roles.js 
│   ├── App.jsx                                    
│   ├── main.jsx                                                                 
│   └── index.css        
│
├── docker/                                                 # Container configurations
│   ├── frontend.DockerFile 
│   ├── backend.DockerFile
│   ├── nginx/  
│   │   └── nginx.conf                                      # Reverse proxy
│   └── docker-compose.yml                                  # Multi-Container setup
│
├── docs/                                                   
│   ├── ERD.png                                             # Entity Relationship Diagram
│   ├── API_Documentation.md
│   ├── Architecture.md                             
│   └── requirements.md
│
├── scripts/                                                # Utility scripts 
│   ├── backup_db.sh
│   ├── restore_db.sh                                
│   └── deploy.sh
│
├── .env                                                    # Root environment variable
├── package.json
├── REMDME.md
└── requirements.txt                                  
