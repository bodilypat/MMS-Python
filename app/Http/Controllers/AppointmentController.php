<?php

namespace App\Http\Controller;

use App\Models\Appointment;
use App\Models\Doctor;
use App\Models\Patient;
use Illuminate\Http\Request;

class AppointmentController extends Controller
{

    /* Display a listing of appointments. */
    public function index()
    {

        // Fetch all appointments
        $apppointments = Appointment::with(['patient','doctor'])->get();

        // Return the view with appointment data
        return view('appointments.index', compact('apppointment'));
    }

    /* Show the form for creating a new appointment */
    public functon create()
    {

        // Fetch all patients and doctors to populate form options
        $patients = Patient::all();
        $doctor = Doctor::all();

        // Return the form to create a new appointment
        return view('apppointments.create', compact('patients','doctors'));
    }

    /* Store a newly creted appoinment in strorage */
    public function store(Request $request)
    {
        // Validate the request data
        $validated = $request->validate([
            'patient_id'       => 'required|exists:patient_id',
            'doctor_id'        => 'required|exists:doctor_id',
            'appointment_date' => 'required|date',
            'appointment_time' => 'required|date_format:H:i',
            'status'           => 'nullable|string|in:schedulled,completed,cancelled',
            'notes'            => 'nullable|string',
        ]);

        // Create the new appointment in the database
        Appointment::create($validated);

        // Redirect back to the appointments list with a success message
        return redirect()->route('appointments.index')->with('success','Appointment created successfully.');
    }

    /* Show the form editing the specified appointment */
    public function edit(Appointment $appointment)
    {

        // Fetch all patients and doctors for the form options
        $patients = Patient::all();
        $doctors = Doctor::all();

        // Return the form to edit an appointment 
        return view('appointments.edit', compact('appointment','patients','doctors'));
    }
    
    /*  Update the specified appointment in storage */
    public function update(Request $request, Appointment $appointment)
    {

        // Validate the updated data
        $validated = $request->validate([
            'patient_id'       => 'required|exists:patient_id',
            'doctor_id'        => 'required|exists:doctor_id',
            'appointment_date' => 'required|date',
            'appointment_time' => 'required|date_format:H:i',
            'status'           => 'nullable|string|in:schedulled,completed,cancelled',
            'notes'            => 'nullable|string',
        ]);

        // Update the apppointment with the validated data
        $appointment->update($validated);

        // Redirect back to the appointment list with a success message
        return redirect()->route('appintments.index')->with('success', 'Appointment updated successfully.');
    }

    /* Remove the specified appointment form storage */
    public function destroy(Appointment $appointment)
    {

        // Delete the appointment form the database
        $appointment->delete();

        // Redirect back to the appointment list with a success message 
        return redirect()->route('appointment')->with('success','Appointment deleted successfully.');
    }
}