<?php

namespace App\Http\Controller;

use App\Models\Appointment;
use App\Models\Doctor;
use App\Models\Patient;
use Illuminate\Http\Request;

class AppointmentController extends Controller
{
    public function store(Request $request)
    {
        $validated = $request->validate([
            'patient_id' => 'required|exists:patient_id',
            'doctor_id' =>  'required|exists:doctor_id',
            'appointment_time' => 'required|date',
            'status' => 'nullable|string|in:schedulled,completed,cancelled',
            'notes' => 'nullable|string',
        ]);

        Appointment::create($validated);

        return redirect()->route('appointments.index')->with('success','Appointment created successfully.');
    }
    
}