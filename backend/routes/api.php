<?php

	use App\Http\Controllers\DoctorController;

	// Fetch all doctors
	Route::get('doctors', [DoctorController::class, 'index']);

	// Fetch a single doctor by ID
	Route::get('doctors/{id}', [DoctorController::class, 'show']);

	// Create a new doctor
	Route::post('doctors', [DoctorController::class, 'store']);

	// Update an existing doctor by ID
	Route::put('doctors/{id}', [DoctorController::class, 'update']);

	// Delete a doctor by ID
	Route::delete('doctors/{id}', [DoctorController::class, 'destroy']);
	
	use App\Http\Controllers\PatientController;

	// Fetch all patients
	Route::get('patients', [PatientController::class, 'index']);

	// Fetch a single patient by ID
	Route::get('patients/{id}', [PatientController::class, 'show']);

	// Create a new patient
	Route::post('patients', [PatientController::class, 'store']);

	// Update an existing patient by ID
	Route::put('patients/{id}', [PatientController::class, 'update']);

	// Delete a patient by ID
	Route::delete('patients/{id}', [PatientController::class, 'destroy']);
	
	use App\Http\Controllers\AppointmentController;

	// Fetch all appointments
	Route::get('appointments', [AppointmentController::class, 'index']);

	// Fetch a single appointment by ID
	Route::get('appointments/{id}', [AppointmentController::class, 'show']);

	// Create a new appointment
	Route::post('appointments', [AppointmentController::class, 'store']);

	// Update an existing appointment by ID
	Route::put('appointments/{id}', [AppointmentController::class, 'update']);

	// Delete an appointment by ID
	Route::delete('appointments/{id}', [AppointmentController::class, 'destroy']);
	
	use App\Http\Controllers\MedicalRecordController;

	// Fetch all medical records
	Route::get('medical-records', [MedicalRecordController::class, 'index']);

	// Fetch a specific medical record by ID
	Route::get('medical-records/{id}', [MedicalRecordController::class, 'show']);

	// Create a new medical record
	Route::post('medical-records', [MedicalRecordController::class, 'store']);

	// Update a medical record by ID
	Route::put('medical-records/{id}', [MedicalRecordController::class, 'update']);

	// Delete a medical record by ID
	Route::delete('medical-records/{id}', [MedicalRecordController::class, 'destroy']);
	
	use App\Http\Controllers\PrescriptionController;

	// Fetch all prescriptions
	Route::get('prescriptions', [PrescriptionController::class, 'index']);

	// Fetch a specific prescription by ID
	Route::get('prescriptions/{id}', [PrescriptionController::class, 'show']);

	// Create a new prescription
	Route::post('prescriptions', [PrescriptionController::class, 'store']);

	// Update an existing prescription
	Route::put('prescriptions/{id}', [PrescriptionController::class, 'update']);

	// Delete a prescription
	Route::delete('prescriptions/{id}', [PrescriptionController::class, 'destroy']);
	
	use App\Http\Controllers\LabTestController;

	// Fetch all lab tests
	Route::get('lab-tests', [LabTestController::class, 'index']);

	// Fetch a specific lab test by ID
	Route::get('lab-tests/{id}', [LabTestController::class, 'show']);

	// Create a new lab test
	Route::post('lab-tests', [LabTestController::class, 'store']);

	// Update an existing lab test
	Route::put('lab-tests/{id}', [LabTestController::class, 'update']);

	// Delete a lab test
	Route::delete('lab-tests/{id}', [LabTestController::class, 'destroy']);
	
	use App\Http\Controllers\PaymentController;

	// Fetch all payments
	Route::get('payments', [PaymentController::class, 'index']);

	// Fetch a specific payment by ID
	Route::get('payments/{id}', [PaymentController::class, 'show']);

	// Create a new payment
	Route::post('payments', [PaymentController::class, 'store']);

	// Update an existing payment
	Route::put('payments/{id}', [PaymentController::class, 'update']);

	// Delete a payment
	Route::delete('payments/{id}', [PaymentController::class, 'destroy']);
	
	use App\Http\Controllers\PharmacyController;

	// Fetch all pharmacies
	Route::get('pharmacies', [PharmacyController::class, 'index']);

	// Fetch a specific pharmacy by ID
	Route::get('pharmacies/{id}', [PharmacyController::class, 'show']);

	// Create a new pharmacy
	Route::post('pharmacies', [PharmacyController::class, 'store']);

	// Update an existing pharmacy
	Route::put('pharmacies/{id}', [PharmacyController::class, 'update']);

	// Delete a pharmacy
	Route::delete('pharmacies/{id}', [PharmacyController::class, 'destroy']);
	
	use App\Http\Controllers\InsuranceController;

	// Fetch all insurance records
	Route::get('insurances', [InsuranceController::class, 'index']);

	// Fetch a specific insurance record by ID
	Route::get('insurances/{id}', [InsuranceController::class, 'show']);

	// Create a new insurance record
	Route::post('insurances', [InsuranceController::class, 'store']);

	// Update an existing insurance record
	Route::put('insurances/{id}', [InsuranceController::class, 'update']);

	// Delete an insurance record
	Route::delete('insurances/{id}', [InsuranceController::class, 'destroy']);
	
?>
