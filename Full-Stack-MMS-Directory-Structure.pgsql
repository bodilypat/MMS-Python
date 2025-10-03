Full-Stack-Medical-Management-System-Directory-Structure
├── backend/
│   ├── app/  
│   │   ├── main.py                           			# FastAPI app startup
│   │   ├── api_router.py
│   │   ├── auth/
│   │   ├── middleware/
│   │   ├── api/                              			# Route handler (controllers)
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── patient_router.py
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
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── schemas/                                    # Pydantic data validation
│   │   │   ├── __init__.py
│   │   │   ├── patient.py
│   │   │   ├── doctor.py
│   │   │   ├── appointment.py
│   │   │   ├── prescription.py
│   │   │   ├── medical_record.py
│   │   │   ├── inventory.py
│   │   │   └── billing.py
│   │   ├── services/                                   # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── patient_service.py
│   │   │   ├── doctor_service.py
│   │   │   ├── appointment_service.py
│   │   │   ├── prescription_service.py
│   │   │   ├── medical_record_service.py
│   │   │   ├── inventory_service.py
│   │   │   └── billing_service.py
│   │   ├── db/                                         # Database engine / session/ init
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── init_db.py
│   │   ├── middleware/                                 # Custom middleware
│   │   │   ├── __init__.py
│   │   │   └── auth_middleware.py
│   │   ├── utils/                                      # Utility functions
│   │   │   ├── __init__.py
│   │   │   └── auth_utils.py
│   │   ├── core/                                       # Configs, security, exceptions
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── exceptions.py
│   │   └── main.py                                                                                                                 
│   ├── tests/                                          # Unit & integration test
│   │   ├── __init__.py  
│   │   ├── conftest.py
│   │   ├── api/
│   │   │   ├── test_auth.py
│   │   │   ├── test_patients.py
│   │   │   ├── test_doctors.py
│   │   │   └── test_appointments.py    
│   │   └── services/     
│   │       ├── test_doctors.py
│   │       └── test_appointments.py                             
├── .env                                      
├── README.md                                
├── requirements.txt
├── run.py                              
│
├── frontend/                         # Front-end static app       
│   ├── public                        # Static entry point for deployment  
│   │   └── index.html                # Entry login/landing page
│   ├── pages/                        # Pages routed via hash or history 
│   │   ├── dasdboard/                # Dashboard & layout-specific views    
│   │   │   ├── home.html                    
│   │   │   └── overview.html    
│   │   └── modules/  
│   │ 		├── patients/
│   │   	│   ├── list.html                    
│   │  		│   ├── add.html                     
│   │   	│   ├── view.html                    
│   │   	│   └── edit.html 
│   │   	├── doctors/
│   │   	│   ├── list.html                    
│   │   	│   ├── add.html                     
│   │   	│   ├── profile.html                    
│   │   	│   └── schedule.html  
│   │   	├── appointments/                
│   │   	│   ├── list.html                     
│   │   	│   ├── book.html                    
│   │   	│   └── calendor.html      
│   │   	├── prescriptions/
│   │   	│   ├── list.html                                 
│   │   	│   └── add.html 
│   │   	├── lab-tests/
│   │   	│   ├── list.html                                
│   │   	│   └── results.html     
│   │   	├── payments/
│   │   	│   ├── invoices.html                                   
│   │   	│   └── receipt.html          
│   │   	├── insurance/
│   │   	│   ├── polices.html                                      
│   │   	│   └── claim.html  
│   │   	├── pharmacies/
│   │   	│   ├── list.html                                    
│   │   	│   └── orders.html  
│   │   	└── reports/ 
│   │       	├── summary.html                   
│   │       	└── charts.html                
│   ├── components/							# Reusable UI parts
│   │   ├── layout/  
│   │   │   ├── navbar.html 
│   │   │   ├── sidebar.html 
│   │   │   └── footer.html            
│   │   └── modals/ 
│   │       └── confirm-delete.html
│   ├── assets/                              
│   │   ├── css/
│   │   │   ├── main.css                    # Global styles
│   │   │   ├── layout.css                  # Layout-specific styles 
│   │   │   └── module/                     # Module-specific styles 
│   │   │       ├── patients.css
│   │   │       ├── doctors.css
│   │   │       └── appointments.css
│   │   │ 
│   │   ├── js/
│   │   │   ├── main.js                      # Bootstrap/init script
│   │   │   ├── auth.js                      # Auth logic
│   │   │   ├── api.js                       # API service (XHR/fetch)
│   │   │   └── module/                      # Module-specific JS
│   │   │       ├── patients.js
│   │   │       ├── doctors.js
│   │   │       └── appointments.js
│   │   └── images/
│   │       └── Logo.png
│   │ 
│   │ 
│   ├── utils/                               # Utility scripts/helpers
│   │   ├── form-validation.js
│   │   └── date-utils.js 
│   ├── store/                               # (optional) Shared data/state (local/session/user)
│   │   └── session.js 
│   │ 
│   ├── README.md 
│   └── LICENSE                    
│
