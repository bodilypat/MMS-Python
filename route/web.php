<?php 

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\PatientController;
use App\Http\Controllers\AppointmentController;
use App\Http\Controllers\DoctorController;
use App\Http\Controllers\MedicalRecordController;
use App\Http\Controllers\PrescriptionController;
use App\Http\Controllers\BillingController;

    Route::resource('patients', PatientController::class);
    /* GET /patients(index) -list all patients
       GET/patients/create (create) -show a form to create a patient
       POST/patients(store) -save a new patient
       GET/patients/{patients} (show) -show a specific patient
       GET/patients/{patients}/edit (edit) -show a form to edit a patient
       PUT/patients/{patients} (update) -update a patient
       DELETE/patients/{patient} (destroy) -delete a patient
     */
    Route::resource('appointements',AppointmentController::class);
    /* GET/appointments/ -list all appointments.
       GET/appointments/create  -show a form to create a new appointment 
       POST/appointments/ -store a new appointment 
       GET/appointments/{appointment} -show details of a specific appointment 
       GET/appointments/{appointment}/edit -show a form to edit an appointment
       PUT/appointments/{appointment} -update an appointment
       DELETE/appointments/{appointment} -delete an appointment */
    Route::resource('doctors', DoctorController::class);

    /* GET/doctors -List all doctors.
       GET/doctors/create -Show a form to create a new doctor. 
       POST/doctors -Store a new doctor.
       GET/doctors/{doctor} -Show a specific doctor.
       GET/doctors/{doctor}/edit -Show a form to edit a doctor.
       PUT /doctors/{doctor} -Update a doctor.
       DELETE/doctors/{doctor} -Delete a doctor. 
   */ 

    Route::resource('medical-record',MedicalRecordController::class);

    /* GET/medical-records -L all medicalRecord.
       GET/medical-records/create -Show a form to create a new medicalRecord
       POST/medical-records -Store a new medicalRecord.
       GET/medical-records/{midicalRecord} -Show a specific MedicalRecord.
       GET/medical-records/{midicalRecord}/edit -Show a form to edit a MedicalRecord.
       PUT/medical-records/{medicalRecord} -Update a MedicalRecord.
       DELETE/medical-records/{medicalRecord} -Delete a MedicalRecord
       */

    Route::resource('prescriptions', PrescriptionController::class);

    /* GET/prescriptions -List all prescriptions.
       GET/prescriptions/create -Show a form to create a new prescription.
       POST/prescriptions -Store a new prescription.
       GET/prescriptions/{prescription} -Show a specific prescription.
       GET/prescription/{prescription}/edit -Show a form to edit a prescription
       PUT/prescriptions/{prescription} -Update a prescription.
       DELETE/prescriptions/{prescription} -Delete a prescription.
       */

    route::resource('prescription', BillingController::class);
    
