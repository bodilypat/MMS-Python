Full-Stack-Medical-Management-System-Folder-Structure
│
backend-MMS with Python                             # FastAPI Backend (Python)
├── app/  
│   ├── main.py                           			# FastAPI app entry
│   ├── database.py                                 # DB connection & session
│   │
│   ├── core/                                       # Core system configuration
│   │   ├── config.py                               # Environment variables       
│   │   ├── security.py                             # JWT, password hashing
│   │   ├── dependencies.py                         # Auth & role dependencies
│   │   ├── logging.py                              # Audit & system logs 
│   │   └── constants.py                            # Enum & Constants
│   ├── models/                           			# SQLAlchemy models
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── permission.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   ├── doctor.py
│   │   ├── medical_record.py
│   │   └── billing.py
│   ├── schemas/                                     # Pydantic data validation
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   ├── doctor.py
│   │   ├── medical_record.py
│   │   └── billing.py
│   │
│   ├── services/                                    # Business Logic
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── role_service.py
│   │   ├── patient_service.py
│   │   ├── appointment_service.py
│   │   ├── doctor_service.py
│   │   ├── medical_record_service.py
│   │   └── billing_service.py
│   ├── api/	                                    # Reusable API files grouped by feature
│   │ 	├── v1/
│   │   │	├── routes/
│   │ 	│   │   ├── auth.py                         # Login, logout, refresh
│   │ 	│   │   ├── users.py                        # User Management                  # RBAC
│   │ 	│   │   ├── patients.py                     # Patient APIs
│   │ 	│   │   ├── doctors.py                      # Doctor APIs
│   │ 	│   │   ├── appointments.py                 # Scheduling
│   │ 	│   │   ├── medical_records.py              # Records
│   │ 	│   │   ├── Prescriptions.py
│   │ 	│   │   ├── billing.py                      # Payments
│   │   │   │   └── reports.py                      # Reports
│   │   │	└── api_router.py
│   │   └── __init__.py       
│   │
│   ├── utils/                                      # Reusable utitlities
│   │   ├── jwt.py 
│   │   ├── password.py
│   │   ├── email.py
│   │   ├── pdf_generator.py                                    
│   │   ├── validators.py
│   │   ├── time_utils.py
│   │   └── logger.py
│   │
│   ├── tests/                                       `
│   │   ├── test_auth.py 
│   │   ├── test_roles.py
│   │   ├── test_permission.py
│   │   ├── test_patient.py
│   │   ├── test_doctors.py
│   │   ├── test_appointments.py
│   │   └── test_billing.py
│   └── static/   
│       ├── uploads/
│       └── reports/                                                                                                             
├── alemblic/     
├── requirements.txt                               
└── README.m                                               
│ 
├── database/                                            # SQL files and seeders
│   ├── init.sql                                         # Create tables
│   ├── seed.sql                                         # Seed sample data
│   └── README.md   
│ 
Frontend-MMS using-React/                                                  
│                                                        # Global Layout, Route Rendering
├── src/   
│   ├── app/	
│   │ 	├── App.jsx                                      # App Shell
│   │ 	├── store.js                                     # Redux store
│   │   └── routes.jsx                                   # Route composition
│   ├── pages/	                                         # Route-level pages
│   │ 	├── auth/
│   │   │	├── Login.jsx
│   │   │	├── Register.jsx
│   │   │	├── ForgotPassword.jsx
│   │   │	└── ResetPassword.jsx
│   │ 	├── admin/   
│   │   │	├── Dashboard.jsx
│   │   │	├── Users.jsx
│   │   │	├── Doctors.jsx
│   │   │	├── Patients.jsx
│   │   │	├── Appointments.jsx
│   │   │	└── Queries.jsx                       
│   │   │	                                              # Page (layout + composition only)
│   │ 	├── doctor/
│   │   │	├── DoctorDashboard.jsx
│   │   │	├── Profile.jsx
│   │   │	├── Appointments.jsx
│   │   │	├── MedicalRecord.jsx
│   │   │	└── PatientHistory.jsx
│   │   │	 
│   │   └── patient/  
│   │   	├── PatientDashboard.jsx                      # Route-level page
│   │   	├── Profile.jsx
│   │   	├── Appointments.jsx  
│   │   	├── BookAppointment.jsx            
│   │   	└── MedicalHistory.jsx   
│   ├── features/	                                      # Business Logic (core)
│   │ 	├── auth/
│   │   │	├── LoginForm.jsx
│   │   │	├── RegisterForm.jsx
│   │   │	├── ForgotPassword.jsx
│   │   │	└── ResetPassword.jsx
│   │ 	├── admin/
│   │   │	├── AdminDashboard.jsx                        # Container / smart / component
│   │   │	├── DashboardStats.jsx                        # Stats grid
│   │   │	├── DashboardCard.jsx                         # Single stat card
│   │   │	├── useDashboard.js                           # Custom hook (data fetching
│   │   │	└── dasboard.constants.js                     
│   │ 	├── doctor/
│   │   │	├── 
│   │   │ 	├── dashboard/   
│   │   │   │	├── DoctorDashboard.jsx                   # Container / smart component
│   │   │   │	├── DoctorCard.jsx                        # Reusable card 
│   │   │   │	├── dashboardConstants.js                 # Static UI data 
│   │   │   │	└── useDoctorDashboard.js                 # Data fetching hook 
│   │   │	├── profile/ 
│   │   │   │	├── DoctorProfilex.jsx                              
│   │   │   │	├── EditProfileFrom.jsx                       
│   │   │   │	└── useDoctorProfile.js                                
│   │   │	├── appointments/ 
│   │   │   │	├── DoctorProfile.jsx
│   │   │   │	├── AppointmentTable.jsx                              
│   │   │   │	├── AppointmentFilters.jsx                 
│   │   │   │	└── useDoctorAppointments.js            
│   │   │	├── medical-records/
│   │   │   │	├── MedicalRecords.jsx                        
│   │   │   │	├── RecordCard.jsx                      
│   │   │   │	└── useMedicalRecords.js    
│   │   │	└── patient-history/
│   │   │   	├── PatientHistory.jsx                      
│   │   │   	├── HistoryTable.jsx                    
│   │   │   	└── usePatientHistory.js
│   │ 	├── patient/
│   │   │ 	├── dashboard/  
│   │   │   │	├── PatientDashboard.jsx                        
│   │   │   │	├── DashboardCard.jsx                            
│   │   │   │	├── dashboardConstants.js                      
│   │   │   │	└── usePatientDashboard.js                      
│   │   │	├── profile/ 
│   │   │   │	├── PatientProfile.jsx                              
│   │   │   │	├── EditProfileFrom.jsx                       
│   │   │   │	└── usePatientProfile.js                                
│   │   │ 	├── appointments/ 
│   │   │   │	├── PatientAppointments.jsx
│   │   │   │	├── AppointmentTable.jsx                              
│   │   │   │	├── AppointmentStatusBadge.jsx                 
│   │   │   │	└── usePatientAppointments.js            
│   │   │	├── book-appointment/
│   │   │   │	├── BookAppointment.jsx                        
│   │   │   │	├── DoctorSelector.jsx            
│   │   │   │	├── TimeSlotPicker.jsx                 
│   │   │   │	└── useBookAppointment.js    
│   │   │ 	└── medical-history/
│   │   │    	├── MedicalHistory.jsx                      
│   │   │    	├── RecordCard.jsx                    
│   │   │    	└── useMedicalHistory.js    
│   │   └── index.js                                    # Barrel exports                         
│   ├── components/	                                    
│   │ 	├── layout/ 
│   │   │	├── AdminLayout.jsx
│   │   │	├── DoctorLayout.jsx
│   │   │	├── PatientLayout.jsx
│   │   │	├── AuthLayout.jsx
│   │   │	├── Sidebar.jsx
│   │   │	├── Header.jsx
│   │   │	├── Footer.jsx
│   │   │	└── ProtectedRoute.jsx
│   │   └── ui/
│   │   	├── Button.jsx
│   │   	├── Input.jsx
│   │   	├── Select.jsx
│   │   	├── TextArea.jsx
│   │   	├── CheckBox.jsx
│   │   	├── Modal.jsx
│   │   	├── Loader.jsx
│   │   	├── Badge.jsx
│   │   	└── Card.jsx 
│   │ 	
│   ├── services/	                                  
│   │ 	├── api.js
│   │ 	├── authService.js                                  
│   │ 	├── adminService.js                                 
│   │ 	├── doctorService.js
│   │   └── patientService.js                          
│   ├── hooks/	                                  
│   │ 	├── useFetch.js
│   │ 	├── useRole.js
│   │   └── useAuth.js
│   ├── context/	                                  
│   │   └── AuthContext.jsx   
│   ├── routes/                                 
│   │ 	├── AuthRoutes.jsx
│   │ 	├── AdminRoutes.jsx                    
│   │ 	├── doctorRoutes.jsx                 
│   │ 	├── PatientRoutes.jsx
│   │   └── index.jsx   
│   ├── config/	 
│   │ 	├── env.js  
│   │ 	├── roles.js                                 
│   │   └── permissions.js       
│   ├── utils/	                                           
│   │ 	├── helpers.js                                     
│   │ 	├── token.js
│   │   └── validators.js                                               
│   └── assets/  
│    	├── images/    
│    	├── icons/
│       └── styles/                                
│   	   	├── bootstrap.min.css
│   	   	└── global.css                                               
└── main.jsx

                  
