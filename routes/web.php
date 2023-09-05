<?php

use App\Http\Controller\AdminController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('index');
});
Route::get('about', function () {
    return view('contact');
});
Route::get('contact', function () {
    return view('contact');
});
Route::get('/doctors', function () {
    return view('doctor');
});
Route::get('/app', function () {
    return view('layouts.app');
});

Route::view('/services', 'services');

Route::middleware(['auth','checksupperadmin'])->group(function () {
    Route::prefix('admin')->group(function (){
        Route::get('settings', App\Http\Livewire\Admins\Settings::class)->name('admin_setting');
        Route::get('nurses', App\Http\Livewire\Admins\Nurses::class)->name('admin_docters');
        Route::get('/doctors', App\Http\Livewire\Admins\Doctor::class)->name('admin_doctors');
        Route::get('/operationreport', App\Http\Livewire\Admin\operationreport::class)->name('admin_operations_report');
        Route::get('/patients', App\Http\Livewire\Admins\Patients::class)->name('admin_patients');
        Route::get('/birthreport', App\Http\Liverware\Admins\Birthreport::class)->name('admin_birth_report');
        Route::get('/pattientBills', App\Http\Liverwire\Admins\Bills::class)->name('patient_bills');
        Route::get('/rooms', App\Http\Livewire\Admins\Rooms::class)->name('Rooms');
        Route::get('/beds', App\Http\Livewire\Admins\Beds::class)->name('patient_beds');
        Route::get('/medicineStore', App\Http\Livewire\Admins\Medicinestore::class)->name('medicineStore');
        Route::get('/department', App\Http\Livewire\Admins\Departments::class)->name('departments');
        Route::get('/employees', App\Http\Livewire\Admins\Employees::class)->name('employees');
        Route::get('/appointment', App\Http\Livewire\Admins\Appointment::class)->name('appointment');
        Route::get('/blocks', App\Http\Livewire\Admins\Blocks::class)->name('blocks');
        Route::get('/admin/hods', App\Http\Livewire\Admis\Hods::class)->name('hods');
        Route::get('/admin/requestedappointments', App\Http\Livewire\Admins\requestedappointments::class)->name('requestedAppointment');
        Route::get('/subscribers', App\Http\Livewire\Admins\Subscribers::class)->name('subscribers');
        Route::get('/contactedus', App\Http\Livewire\Admins\Constactedus::class)->name('contactedus');
    });
});

Auth:: routes();

