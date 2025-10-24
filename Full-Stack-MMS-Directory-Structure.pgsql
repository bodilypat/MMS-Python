Full-Stack-Medical-Management-System-Directory-Structure
├── backend-Python
│   ├── app/  
│   │   ├── main.py                           			# FastAPI app startup
│   │   ├── api_router.py
│   │   ├── api/                              			# Route handler (controllers)
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── patient_router.py
│   │   │       ├── department_router.py
│   │   │       ├── doctor_router.py
│   │   │       ├── appointment_router.py
│   │   │       ├── prescription_router.py
│   │   │       ├── medical_record_router.py
│   │   │       ├── billing_router.py
│   │   │       ├── inventory_router.py
│   │   │       └── lab_api.py
│   │   ├── models/                           			# SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── department.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── billing.py
│   │   │   └── inventory.py
│   │   ├── schemas/                                    # Pydantic data validation
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── department.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── billing.py
│   │   │   └── inventory.py
│   │   ├── services/                                   # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── patient_service.py
│   │   │   ├── department_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── prescription_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── billing_service.py
│   │   │   └── inventory_service.py
│   │   ├── db/                                         # Database engine / session/ init
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── init_db.py
│   │   ├── auth/    
│   │   │   ├── __init__.py                                   
│   │   │   ├── auth_handler.py
│   │   │   ├── auth_bearer.py
│   │   │   └── permission.py
│   │   ├── middleware/    
│   │   │   ├── __init__.py           
│   │   │   ├── auth_middleware.py                      
│   │   │   └── logging_middleware.py
│   │   ├── auth/    
│   │   │   ├── __init__.py                                   
│   │   │   ├── auth_handler.py
│   │   │   └── auth_bearer.py
│   │   ├── core/                                       # Configs, security, exceptions
│   │   │   ├── __init__.py 
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── exceptions.py
│   │   │   └── constants.py
│   │   ├── utils/  
│   │   │   ├── __init__.py 
│   │   │   ├── auth_utils.py
│   │   │   ├── date_utils.py
│   │   │   ├── response_utils.py                                    # Utility functions
│   │   │   └── file_utils.py
│   │   └── __main.py                                                                                                                 
│   ├── tests/                                          # Unit & integration test
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py
│   │   │   ├── test_patients.py
│   │   │   ├── test_doctors.py
│   │   │   ├── test_appointments.py
│   │   │   └── test_billing.py    
│   │   └── services/     
│   │       ├── test_doctors_service.py
│   │       ├── test_patient_service.py
│   │       └── test_appointment_service.py                                                        
│   │ 
├── frontend-react/                      
│   ├── public                                        # Static entry point for deployment  
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   ├── manifest.json
│   │   └── robots.txt                                 
│   │     
│   ├── src/                              
│   │   ├── assets/
│   │   │   ├── images/ 
│   │   │   │   └── logo.png
│   │   │   └── styles/                     
│   │   │       ├── main.css
│   │   │       ├── layout.css
│   │   │       ├── theme.css
│   │   │       └── variables.css
│   │   │
│   │ 	├── components/							                 # Reusable UI components
│   │   │   ├── common/   
│   │   │   │	├── Accordion/  
│   │   │   │	│   ├── Accordion.jsx
│   │   │   │	│   ├── AccordionItem.jsx
│   │   │   │	│   └── Accordion.css                            # Shared small components
│   │   │   │	├── Button.jsx
│   │   │   │	├── InputField.jsx
│   │   │   │	├── Spinner.jsx
│   │   │   │	└── Table.jsx
│   │   │   │
│   │   │ 	├── layout/                                             # Layout-level components
│   │   │   │	├── Navbar.jsx
│   │   │   │	├── Sidebar.jsx
│   │   │   │	├── Footer.jsx
│   │   │   │	└── ProtectRoute.jsx                                      # Role-based route guard
│   │   │ 	├── models/                                             # Layout-level components
│   │   │   │	├── ModelDelete.jsx
│   │   │   │	├── ModalConfirm.jsx
│   │   │   │	└── ModalForm.jsx     
│   │   │ 	├── charts/                                             # Layout-level components
│   │   │   │	├── ModelDelete.jsx
│   │   │   │	├── ModalConfirm.jsx
│   │   │   │	└── ModalForm.jsx     
│   │   │   └── Notifications/                     
│   │   │       ├── Toast.jsx
│   │   │       └── NotificationBell.jsx    
│   │   │   
│   ├── pages/	
│   │ 	├── Auth/                                              # Page-level components
│   │   │   ├── Login.jsx                    
│   │  	│   ├── Register.jsx                     
│   │   │   ├── login.schema.js                 
│   │   │   └── register.schema.js
│   │ 	├── Patients/
│   │   │   ├── PatientList.jsx                    
│   │  	│   ├── PatientFrom.jsx                               # Fixed spelling "Form"
│   │   │   ├── patient.api.js           
│   │   │   └── patient.schema.js
│   │   ├── Doctors/
│   │   │   ├── DoctorList.jsx                    
│   │  	│   ├── DoctorFrom.jsx                        
│   │   │   └── doctor.api.js
│   │   ├── Appointments/   
│   │   │   ├── AppointmentList.jsx                    
│   │  	│   ├── AppointmentFrom.jsx                            
│   │   │   └── appointment.api.js                 
│   │   ├── Billings/
│   │   │   ├── BillingList.jsx                    
│   │  	│   ├── BillingReceipt.jsx                               
│   │   │   └── billing.api.js           
│   │   ├── Reports/           
│   │  	│   ├── Summary.jsx                               
│   │   │   └── Chart.jsx           
│   │   ├── Dashboard/                               
│   │   │   └── Dashboard.jsx           
│   │   └── NotFound.jsx                              # 404 page          
│   │ 
│   ├── routes/                                       # App Routing
│   │   ├── AppRoutes.jsx                             # Main route map   
│   │   └── routeConfix.js                            # Centralized route definitions 
│   ├── context/							
│   │   ├── AuthContext.jsx                           # Global state or auth context
│   │   └── ThemeContext.jsx 
│   │
│   ├── hooks/				                          # Custom React hooks			
│   │   ├── useAuth.js                     
│   │   ├── useApi.js     
│   │   ├── useForm.js                   
│   │   └── useTheme.js        
│   │    
│   ├── services/				                      # API and service layers			
│   │   ├── apiClient.js                              # Axios or Fetch wrapper
│   │   ├── authService.js                            # Login/Register
│   │   ├── patientService.js   
│   │   ├── doctorService.js            
│   │   ├── appointmentService.js      
│   │   ├── billingService.js          
│   │   └── session.js                                # Session/localStorage helpers
│   │ 
│   ├── utils/                                        # Utility helpers
│   │   ├── formValidation.js
│   │   ├── dateUtils.js
│   │   ├── formatters.js                             # For currency, name, phone
│   │   └── constants.js                              # Frontend constants (roles, URLS)
│   │
│   ├── App.jsx                                       # Root component
│   ├── index.js                                      # React entry point
│   ├── setupTests.js                                 # Jest / RTL stup (Optional)
│   └── vite.config.js / webpack.config.js            # Depending n bundler                
│
├── .env 
├── package.json
├── REMDME.md
└── requirements.txt                        # Python dependancies
