Full-Stack-Medical-Management-System-Folder-Structure
│
├── backend-MMS using Python                                      # FastAPI Backend (Python)
│   ├── app/  
│   │   ├── main.py                           			# FastAPI app entry
│   │   ├── config.py                                   # ENV setting
│   │   ├── database.py                                 # SQLAlchemy engine/session
│   │   ├── dependancies.py
│   │   ├── auth/    
│   │   │   ├── auth_router.py                                   
│   │   │   ├── auth_service.py
│   │   │   ├── auth_schema.py
│   │   │   └── auth_utils.py
│   │   ├── models/                           			# SQLAlchemy models
│   │   │   ├── user_model.py
│   │   │   ├── patient_model.py
│   │   │   ├── doctor_model.py
│   │   │   ├── appointment_model.py
│   │   │   ├── medical_record_model.py
│   │   │   ├── prescription_model.py
│   │   │   ├── medicine_model.py
│   │   │   ├── lab_test_model.py
│   │   │   ├── lab_report_model.py
│   │   │   ├── invoice_model.py
│   │   │   ├── word_model.py
│   │   │   └── bed_model.py
│   │   ├── routers/                           			
│   │   │   ├── user_router.py
│   │   │   ├── patient_router.py
│   │   │   ├── doctor_router.py
│   │   │   ├── appointment_router.py
│   │   │   ├── medical_record_router.py
│   │   │   ├── prescription_router.py
│   │   │   ├── pharmacy_router.py
│   │   │   ├── lab_router.py
│   │   │   ├── billing_router.py
│   │   │   ├── ward_router.py
│   │   │   └── admin_router.py
│   │   ├── schemas/                                     # Pydantic data validation
│   │   │   ├── user_schema.py
│   │   │   ├── patient_schema.py
│   │   │   ├── doctor_schema.py
│   │   │   ├── appointment_schema.py
│   │   │   ├── medical_record_schema.py
│   │   │   ├── precription_schema.py
│   │   │   ├── medicine_schema.py
│   │   │   ├── lab_test_schema.py
│   │   │   ├── lab_report_schema.py
│   │   │   ├── invoice_schema.py
│   │   │   ├── ward_schema.py
│   │   │   └── bed_schema.py
│   │   ├── services/                                    # Business Logic
│   │   │   ├── user_service.py
│   │   │   ├── patient_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── prescription_service.py
│   │   │   ├── pharmacy_service.py
│   │   │   ├── lab_service.py
│   │   │   ├── billing_service.py
│   │   │   └── ward_service.py
│   │   ├── repositories/                                # Database engine / session/ init
│   │   │   ├── user_repository.py
│   │   │   ├── patient_repository.py
│   │   │   ├── doctor_repository.py
│   │   │   ├── appointment_repository.py
│   │   │   ├── medical_record_repository.py
│   │   │   ├── prescription_repository.py
│   │   │   ├── pharmacy_repository.py
│   │   │   ├── lab_repository.py
│   │   │   ├── billing_repository.py
│   │   │   └── ward_repository.py
│   │   ├── utils/  
│   │   │   ├── jwt_handler.py 
│   │   │   ├── password_hasher.py
│   │   │   ├── email_sender.py
│   │   │   ├── pdf_generator.py                                    
│   │   │   ├── logger.py
│   │   │   └── constants.py
│   │   ├── middleware/      
│   │   │   ├── auth_middleware.py                      
│   │   │   └── error_handler.py
│   │   ├── core/                                       
│   │   │   ├── security.py
│   │   │   ├── settings.py
│   │   │   └── permissions.py
│   │   ├── migrations/  
│   │   │   └── (Alembic auto-generated migration scripts)                         
│   │   ├── tests/                                       
│   │   │   ├── test_auth.py 
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
│   │   ├── api/	
│   │   │ 	├── axiosConfig.js
│   │   │ 	├── authApi.js
│   │   │ 	├── patientApi.js 
│   │   │ 	├── doctorsApi.js    
│   │   │ 	├── appointmentsApi.js
│   │   │ 	├── pharmacyApi.js    
│   │   │ 	├── labApi.js
│   │   │   └── billingApi.js                 
│   │   ├── assets/	
│   │   │ 	├── images/    
│   │   │ 	├── icons/
│   │   │   └── styles/                                
│   │   │   	├── global.css
│   │   │   	└── variables.css 
│   │   ├── components/	
│   │   │ 	├── common/ 
│   │   │   │	├── Navbar.jsx
│   │   │   │	├── Sidebar.jsx
│   │   │   │	├── Footer.jsx
│   │   │   │	├── Loader.jsx
│   │   │   │	└── ProtectedRoute.jsx 
│   │   │   └── ui/                                
│   │   │   	├── Button.jsx
│   │   │   	├── Input.jsx
│   │   │   	├── Table.jsx
│   │   │   	├── Modal.jsx
│   │   │   	└── Card.jsx 
│   │   ├── context/	
│   │   │ 	├── AuthContext.jsx   
│   │   │ 	├── UserContext.jsx
│   │   │   └── ThemeContext.jsx
│   │   ├── hooks/	
│   │   │ 	├── useAuth.js
│   │   │ 	├── useFetch.js   
│   │   │ 	├── useDebounce.js
│   │   │   └── usePagination.js   
│   │   ├── layouts/	
│   │   │ 	├── AdminLayout.jsx    
│   │   │ 	├── DoctorLayout.jsx
│   │   │ 	├── ReceptionistLayout.jsx
│   │   │   └── AuthLayout.jsx
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
│   │   │   │	├── EditPatiet.jsx
│   │   │   │	└── PatientDetail.jsx 
│   │   │ 	├── Doctors/
│   │   │   │	├── DoctorList.jsx
│   │   │   │	├── AddDoctor.jsx
│   │   │   │	├── EditDoctor.jsx
│   │   │   │	└── DoctorProfile.jsx 
│   │   │ 	├── Appointments/
│   │   │   │	├── AppointmentList.jsx
│   │   │   │	└── BookAppointment.jsx 
│   │   │ 	├── Pharmacy/
│   │   │   │	├── MedicineList.jsx
│   │   │   │	├── AddMedicine.jsx
│   │   │   │	└── IssueMedicine.jsx 
│   │   │ 	├── Laboratory/
│   │   │   │	├── TestList.jsx
│   │   │   │	├── AddTest.jsx
│   │   │   │	└── TestReports.jsx 
│   │   │ 	├── Billing/
│   │   │   │	├── InvoiceList.jsx
│   │   │   │	└── GenerateInvoice.jsx 
│   │   │ 	├── Wards/
│   │   │   │	├── WardList.jsx
│   │   │   │	├── BedList.jsx
│   │   │   │	└── AssignBed.jsx 
│   │   │   └── Error/  
│   │   │   	├── NotFound.jsx
│   │   │   	└── Unautorized.jsx  
│   │   ├── routes/	
│   │   │ 	├── AppRoutes.jsx
│   │   │   └── RoleBaseRoutes.jsx
│   │   ├── services/	
│   │   │ 	├── images/    
│   │   │ 	├── icons/
│   │   │   └── styles/   
│   │   └── utils/
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
