<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;
use App\Http\Controllers\DoctorController;
use App\Http\Controllers\PatientController;
use App\Http\Controllers\AppointmentController;
use App\Http\Controllers\PrescriptionController;
use App\Http\Controllers\PaymentController;
use App\Http\Controllers\InsuranceController;

// Home route (Landing page)
Route::get('/', function () {
    return view('welcome');  // Your welcome view (Landing Page)
});

// User routes
Route::get('/users', [UserController::class, 'index'])->name('users.index');  // List all users
Route::get('/users/create', [UserController::class, 'create'])->name('users.create');  // Show the form to create a new user
Route::post('/users', [UserController::class, 'store'])->name('users.store');  // Store the new user in the database
Route::get('/users/{user}/edit', [UserController::class, 'edit'])->name('users.edit');  // Show the form to edit a user
Route::put('/users/{user}', [UserController::class, 'update'])->name('users.update');  // Update the user in the database
Route::delete('/users/{user}', [UserController::class, 'destroy'])->name('users.destroy');  // Delete the user

// Doctor routes
Route::get('/doctors', [DoctorController::class, 'index'])->name('doctors.index');  // List all doctors
Route::get('/doctors/create', [DoctorController::class, 'create'])->name('doctors.create');  // Show form to add new doctor
Route::post('/doctors', [DoctorController::class, 'store'])->name('doctors.store');  // Store the new doctor
Route::get('/doctors/{doctor}/edit', [DoctorController::class, 'edit'])->name('doctors.edit');  // Edit doctor
Route::put('/doctors/{doctor}', [DoctorController::class, 'update'])->name('doctors.update');  // Update doctor
Route::delete('/doctors/{doctor}', [DoctorController::class, 'destroy'])->name('doctors.destroy');  // Delete doctor

// Patient routes
Route::get('/patients', [PatientController::class, 'index'])->name('patients.index');  // List all patients
Route::get('/patients/create', [PatientController::class, 'create'])->name('patients.create');  // Add a new patient
Route::post('/patients', [PatientController::class, 'store'])->name('patients.store');  // Store the new patient
Route::get('/patients/{patient}/edit', [PatientController::class, 'edit'])->name('patients.edit');  // Edit patient
Route::put('/patients/{patient}', [PatientController::class, 'update'])->name('patients.update');  // Update patient
Route::delete('/patients/{patient}', [PatientController::class, 'destroy'])->name('patients.destroy');  // Delete patient

// Appointment routes
Route::get('/appointments', [AppointmentController::class, 'index'])->name('appointments.index');  // List all appointments
Route::get('/appointments/create', [AppointmentController::class, 'create'])->name('appointments.create');  // Show appointment creation form
Route::post('/appointments', [AppointmentController::class, 'store'])->name('appointments.store');  // Store new appointment
Route::get('/appointments/{appointment}/edit', [AppointmentController::class, 'edit'])->name('appointments.edit');  // Edit appointment
Route::put('/appointments/{appointment}', [AppointmentController::class, 'update'])->name('appointments.update');  // Update appointment
Route::delete('/appointments/{appointment}', [AppointmentController::class, 'destroy'])->name('appointments.destroy');  // Delete appointment

// Prescription routes
Route::get('/prescriptions', [PrescriptionController::class, 'index'])->name('prescriptions.index');  // List all prescriptions
Route::get('/prescriptions/create', [PrescriptionController::class, 'create'])->name('prescriptions.create');  // Create prescription form
Route::post('/prescriptions', [PrescriptionController::class, 'store'])->name('prescriptions.store');  // Store prescription
Route::get('/prescriptions/{prescription}/edit', [PrescriptionController::class, 'edit'])->name('prescriptions.edit');  // Edit prescription
Route::put('/prescriptions/{prescription}', [PrescriptionController::class, 'update'])->name('prescriptions.update');  // Update prescription
Route::delete('/prescriptions/{prescription}', [PrescriptionController::class, 'destroy'])->name('prescriptions.destroy');  // Delete prescription

// Payment routes
Route::get('/payments', [PaymentController::class, 'index'])->name('payments.index');  // List all payments
Route::get('/payments/create', [PaymentController::class, 'create'])->name('payments.create');  // Add new payment
Route::post('/payments', [PaymentController::class, 'store'])->name('payments.store');  // Store new payment
Route::get('/payments/{payment}/edit', [PaymentController::class, 'edit'])->name('payments.edit');  // Edit payment
Route::put('/payments/{payment}', [PaymentController::class, 'update'])->name('payments.update');  // Update payment
Route::delete('/payments/{payment}', [PaymentController::class, 'destroy'])->name('payments.destroy');  // Delete payment

// Insurance routes
Route::get('/insurances', [InsuranceController::class, 'index'])->name('insurances.index');  // List all insurance
Route::get('/insurances/create', [InsuranceController::class, 'create'])->name('insurances.create');  // Create new insurance
Route::post('/insurances', [InsuranceController::class, 'store'])->name('insurances.store');  // Store insurance
Route::get('/insurances/{insurance}/edit', [InsuranceController::class, 'edit'])->name('insurances.edit');  // Edit insurance
Route::put('/insurances/{insurance}', [InsuranceController::class, 'update'])->name('insurances.update');  // Update insurance
Route::delete('/insurances/{insurance}', [InsuranceController::class, 'destroy'])->name('insurances.destroy');  // Delete insurance