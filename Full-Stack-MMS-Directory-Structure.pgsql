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
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── schemas/                                    # Pydantic data validation
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── department.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── services/                                   # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── patient_service.py
│   │   │   ├── department_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── prescription_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── inventory_service.py
│   │   │   └── billing_service.py
│   │   ├── db/                                         # Database engine / session/ init
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── init_db.py
│   │   ├── middleware/                                 
│   │   │   └── auth_middleware.py
│   │   ├── auth/                                       
│   │   │   ├── auth_handler.py
│   │   │   └── auth_bearer.py
│   │   ├── utils/                                      # Utility functions
│   │   │   └── auth_utils.py
│   │   ├── core/                                       # Configs, security, exceptions
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── exceptions.py
│   │   └── main.py                                                                                                                 
│   ├── tests/                                          # Unit & integration test
│   │   ├── api/
│   │   │   ├── test_auth.py
│   │   │   ├── test_patients.py
│   │   │   ├── test_doctors.py
│   │   │   └── test_appointments.py    
│   │   └── services/     
│   │       ├── test_doctors.py
│   │       └── test_appointments.py                                                        
│   │ 
├── frontend-react/                      
│   ├── public                                        # Static entry point for deployment  
│   │   └── index.html                                # Entry login/landing page 
│   │     
│   ├── src/                              
│   │   ├── assets/
│   │   │   ├── images/ 
│   │   │   │   └── logo.png
│   │   │   └── styles/                     
│   │   │       ├── main.css
│   │   │       └── layout.css
│   │   │
│   ├── components/							          # Shared Components
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   ├── Footer.jsx     
│   │   └── ModalDelete.jsx
│   ├── pages/	
│   │ 	├── Auth/
│   │   │   ├── Login.jsx                    
│   │  	│   ├── Register.jsx                     
│   │   │   ├── login.schema.js                 
│   │   │   └── register.schema.js
│   │ 	├── patients/
│   │   │   ├── PatientList.jsx                    
│   │  	│   ├── PatientFrom.jsx
│   │   │   ├── patient.api.js           
│   │   │   └── patient.schema.js
│   │   ├── doctors/
│   │   │   ├── DoctorList.jsx                    
│   │  	│   ├── DoctorFrom.jsx                        
│   │   │   └── doctor.api.js
│   │   ├── appointments/   
│   │   │   ├── AppointmentList.jsx                    
│   │  	│   ├── AppointmentFrom.jsx                            
│   │   │   └── appointment.api.js                 
│   │   ├── billings/
│   │   │   ├── BillingList.jsx                    
│   │  	│   ├── BillingReceipt.jsx                               
│   │   │   └── billing.api.js                   
│   │   └── reports/ 
│   │      	├── Summary.jsx            
│   │      	└── Charts.jsx           
│   │ 
│   ├── services/							
│   │   ├── apiClient.js                     # Axios wrapper
│   │   ├── authService.js                   # Login/Register
│   │   └── session.js                       # Session Storage
│   ├── utils/                               
│   │   ├── formValidation.js
│   │   └── dateUtils.js 
│   ├── routes/                               
│   │   └── AppRoutes.jsx 
│   │ 
│   ├── App.jsx
│   ├── index.js
│   └── readme.md                 
│
├── .env 
├── README.md
├── run.py
└── requirements.txt                        # Python dependancies
