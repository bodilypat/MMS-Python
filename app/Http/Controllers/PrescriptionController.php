<?php

namespace App\Http\Controllers;

use App\Models\Prescription;
use App\Models\Patient;
use App\Models\Doctor;
use Illuminate\Http\Request;

class PrescriptionController extends Controllers
{

    /* Display a listing of prescription */
    public function index()
    {

        // Fetch all presccriptions with related doctor and patient
        $prescriptions = Prescription::with(['doctor','patient'])->get();

        // Return the view with the list of prescriptions
        return view('prescriptions.index', compact('prescriptions'));
    }

    /* Show the form for creating a new prescription. */
    public function create()
    {

        // Fetch all patients and doctors
        $patients = Patient::all();
        $doctors = Doctor::all();

        // Return the form view to create a new prescription
        return view('prescripts.create', compact('patients', 'doctors'));
    }

    /* Store a newly creately prescription in storage. */
    public function store(Request $request)
    {

        // Validate the request data
        $validate = $request->validate([
            'patient_id'        => 'required|exists:patient,id',
            'doctor_id'         => 'required|exists:doctors,id',
            'medical_record_id' => 'required|exists:medical_record,id',
            'medication_name'   => 'required|string|max:255',
            'dosage'            => 'required|string|max:255',
            'frequency'         => 'required|string|max:255',
            'notes'             => 'nullable|string|max:500',
        ]);

        // Update the prescription in the database
        Prescription::create($validated);

        // Redirect to the prescriptions list with a success message
        return redirect()->route('prescriptions.index')->with('success','Prescription created successfully.');
    }

    /* Display the specified prescription. */
    public function show(Prescription $prescription)
    {

        // Return the view to display a specific prescription's details
        return view('Prescriptions.show', compact('prescription'));
    }

    /* Show the form editing the specified prescription */
    public function edit(Prescription $presscription)
    {

        // Fetch all patients and doctors for selection in the form
        $patients = Patient::all();
        $doctors = Doctor::all();

        // Return the form to edit an existing prescription
        return view('prescriptions.edit', compact('prescription', 'patients','doctors'));
    }

    /* Update the specfied prescription in storage */
    public function update(Request $request, Prescription $prescription)
    {

        // Validate the request data
        $validated = $request->validate([
            'patient_id'        => 'required|exists:patient,id',
            'doctor_id'         => 'required|exists:doctors,id',
            'medical_record_id' => 'required|exists:medical_record,id',
            'medication_name'   => 'required|string|max:255',
            'dosage'            => 'required|string|max:255',
            'frequency'         => 'required|string|max:255',
            'notes'             => 'nullable|string|max:500',
        ]);

        // Update the prescription in the database
        $prescription->update($validated);

        // Redirect to the prescriptions list with a success message
        return redirect()->route('prescriptions.index')->with('success','Prescription updated successfully.');
    }

    /* Remove the specified prescription from storage. */
    public function destroy(Prescription $prescription)
    {

        // Delete the prescription from the database
        $prescription->delete();

        // Redirect to the prescriptions list with a success message
        return redirect()->route('prescriptions.index')->with('success', 'Prescription deleted successfully.');
    }
}