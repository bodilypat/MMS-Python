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

    Route::get('patietns', [PatientController::class,'index']);
    Route::get('patients/{id}', [PatientController::class,'show']);
    Route::get('patients/create', [PatientController::class,'create']);
    Route::post('patients', [PatientController::class,'store']);
    Route::get('patients/{id}/edit', [PatientControll::class,'edit']);
    Route::put('patients/{id}', [patientController::class,'update']);
    Route::delete('patient/{id}', [PatientController::class,'destroy']);
    
    Route::resource('appointements',AppointmentController::class);

    Route::get('appointments', [AppointmentController::class,'index']);
    Route::get('appointments/{id}', [AppointmentController::class,'show']);
    Route::get('appointments/create', [AppointmentController::class,'create']);
    Route::post('appointmnets', [AppointmentController::class,'store']);
    Route::get('appointments/{id}/edit', [AppointmentControll::class,'edit']);
    Route::put('appointments/{id}', [AppointmentController::class,'update']);
    Route::delete('appointments/{id}', [AppointmentController::class,'destroy']);
    
    Route::resource('doctors', DoctorController::class);

    Route::get('doctors', [DoctorController::class,'index']);
    Route::get('doctors/{id}', [DoctorController::class,'show']);
    Route::get('doctors/create', [DoctorController::class,'create']);
    Route::post('doctors', [DoctorController::class,'store']);
    Route::get('doctors/{id}/edit', [DoctorControll::class,'edit']);
    Route::put('doctors/{id}', [DoctorController::class,'update']);
    Route::delete('doctors/{id}', [DoctorController::class,'destroy']);
    
    Route::resource('medical-record',MedicalRecordController::class);

    Route::get('medical-records', [MedicalRecordController::class,'index']);
    Route::get('medical-records/{id}', [MedicalRecordController::class,'show']);
    Route::get('medical-records/create', [MedicalRecordController::class,'create']);
    Route::post('medical-records', [MedicalRecordController::class,'store']);
    Route::get('medical-recordss/{id}/edit', [MedicalRecordControll::class,'edit']);
    Route::put('medical-records/{id}', [MedicalRecordController::class,'update']);
    Route::delete('medical-records/{id}', [MedicalRecordController::class,'destroy']);
    
    Route::resource('prescriptions', PrescriptionController::class);

    Route::get('prescriptions', [PrescriptionController::class,'index']);
    Route::get('Prescriptions/{id}', [PrescriptionController::class,'show']);
    Route::get('Prescriptions/create', [PrescriptionController::class,'create']);
    Route::post('Prescriptions', [PrescriptionController::class,'store']);
    Route::get('Prescriptions/{id}/edit', [PrescriptionControll::class,'edit']);
    Route::put('Prescriptions/{id}', [PrescriptionController::class,'update']);
    Route::delete('Prescriptions/{id}', [PrescriptionController::class,'destroy']);

    
    