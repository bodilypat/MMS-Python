Full-Stack-MMS-Directory-Structure(no framework)/
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
├── backend/
│   ├── app/                              
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── router.py
│   │   │   │   ├── endpoints/
│   │   │   │	│	├── __int__.py
│   │   │   │	│	├── auth.py
│   │   │   │	│	├── patients.py
│   │   │   │	│	├── doctors.py
│   │   │   │	│	├── appointments.py
│   │   │   │   │   └── billing.py
│   │   │   │   └── deps.py                       
│   │   ├── core/   
│   │   │   ├── __int__.py 
│   │   │   ├── config.py                             
│   │   │   ├── security.py
│   │   │   ├── logging.py 
│   │   │   ├── models/
│   │   │   │  	├── __int__.py
│   │   │   │  	├── user.py
│   │   │   │  	├── patient.py
│   │   │   │ 	├── doctor.py
│   │   │   │  	├── appointment.py
│   │   │   │ 	└── billing.py 
│   │   │   ├── schemas/
│   │   │   │  	├── __init__.py
│   │   │   │  	├── user.py					          # Common user-related schemas (Auth, Base user)
│   │   │   │  	├── patient.py                        # Patient request/response models
│   │   │   │ 	├── doctor.py                         # Doctor request/response models
│   │   │   │  	├── appointment.py                    # Appointment creation/view/update
│   │   │   │ 	└── billing.py                        # Invoice, Payment, billing schemas
│   │   │   ├── services/
│   │   │   │  	├── __init__.py
│   │   │   │  	├── auth.py
│   │   │   │  	├── patient.py
│   │   │   │ 	├── doctor.py
│   │   │   │  	├── appointment.py
│   │   │   │ 	└── billings.py   
│   │   │   ├── db/
│   │   │   │  	├── __init.py
│   │   │   │  	├── base.py
│   │   │   │  	├── session.py
│   │   │   │ 	└── main.py         
│   │   │   ├── middleware/
│   │   │   │  	├── __init.py
│   │   │   │ 	└── main.py   
│   │   │   ├── utils/
│   │   │   │  	├── __init.py
│   │   │   │ 	└── helper.py   
│   │   │   └── main.py                       # Entry point (FastAPI app)                           
│   ├── alembics/ 
│   │   ├── versions/  
│   │   └── env.py                   
│   ├── tests/  
│   │   ├── __int__.py  
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
├── .htaccess                                 
├── composer.json                             
└── README.md
