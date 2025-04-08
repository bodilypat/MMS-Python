<?php

namespace App\Http\Controllers;

use App\Models\Appointment;
use App\Models\Patient;
use App\Models\Doctor;
use Illuminate\Http\Request;

class AppointmentController extends Controller
{
    // Fetch all appointments
    public function index()
    {
        $appointments = Appointment::with(['patient', 'doctor'])->get(); // Include patient and doctor relationships
        return response()->json($appointments);
    }

    // Show a single appointment by ID
    public function show($id)
    {
        $appointment = Appointment::with(['patient', 'doctor'])->find($id);

        if (!$appointment) {
            return response()->json(['message' => 'Appointment not found'], 404);
        }

        return response()->json($appointment);
    }

    // Create a new appointment record
    public function store(Request $request)
    {
        // Validate the input data
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'doctor_id' => 'required|exists:doctors,doctor_id',
            'appointment_date' => 'required|date|after:today', // Ensure appointment date is in the future
            'reason_for_visit' => 'nullable|string|max:255',
            'status' => 'nullable|in:Scheduled,Completed,Cancelled,No-Show',
            'duration' => 'nullable|integer',
            'appointment_type' => 'nullable|string|max:100',
            'notes' => 'nullable|string',
        ]);

        // Create a new appointment record
        $appointment = Appointment::create($request->all());

        return response()->json($appointment, 201);
    }

    // Update an existing appointment record
    public function update(Request $request, $id)
    {
        // Find the appointment by ID
        $appointment = Appointment::find($id);

        if (!$appointment) {
            return response()->json(['message' => 'Appointment not found'], 404);
        }

        // Validate the input data
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'doctor_id' => 'required|exists:doctors,doctor_id',
            'appointment_date' => 'required|date|after:today',
            'reason_for_visit' => 'nullable|string|max:255',
            'status' => 'nullable|in:Scheduled,Completed,Cancelled,No-Show',
            'duration' => 'nullable|integer',
            'appointment_type' => 'nullable|string|max:100',
            'notes' => 'nullable|string',
        ]);

        // Update the appointment record
        $appointment->update($request->all());

        return response()->json($appointment);
    }

    // Delete an appointment record
    public function destroy($id)
    {
        // Find the appointment by ID
        $appointment = Appointment::find($id);

        if (!$appointment) {
            return response()->json(['message' => 'Appointment not found'], 404);
        }

        // Delete the appointment record
        $appointment->delete();

        return response()->json(['message' => 'Appointment deleted successfully']);
    }
}