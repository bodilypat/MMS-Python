<?php

namespace App\Http\Controllers;

use App\Models\MidicalRecord;
use App\Models\Patient;
use Illuminate\Http\Request;

class MedicalRecordController extends Controller
{

    /* Display a listing of medical record */

    public function index()
    {

        // Fetch all medical records with the paitent relationship
        $medicalRecord = MedicalRecord::with('patient')->get();

        // Return the view with the list of medical records
        return view('medical_records.index', compact('medicalRecords'));
    }

    /* show the for creating a new medical record. */
    public function create()
    {

        // Fetch all patient for the medical record form
        $patients = Patient::all();

        // Return the form to create a new medical record
        return view('medical_records.create', compact('patients'));
    }

    /* Store a newly created medical record in storage */
    public function store(Request $request)
    {

        // Validate the request data
        $valdiated = $request->validate([
            'patient_id'   => 'required|exists:patients,id',
            'doctor_id'    => 'nullable|exists:doctor,id',
            'dianosis'     => 'required|string',
            'treatment'    => 'nullable|string',
            'medications'  => 'nullable|string',
            'notes'        => 'nullable|string',
        ]);

        // Create a new medicl record in the database
        MedicalRecord::create($validated);

        // Redirect to the medical records list with a success message
        return redirect()->route('medical_records.index')->with('success', 'Midical record created successfully.');
    }

    /* Display the specified medical record */
    public function show(MedicalRecord $medicalRecord)
    {

        // Return the view to show the details of a specified medical record
        return view('medical_records.show', compact('medicalRecord'));
    }

    /* show the form for editing the specified medical record */
    public function edit(MedicalRecord $medicalRecord)
    {

        // Fetch all patients for the form
        $patients = Patient::all();

        // Return the form to edit an existing medical record 
        return view('medical_records.edit', compact('medicalRecord','patients'));
    }

    /* Update the specified medical record in storage. */
    public function update(Request $request, MedicalRecord $medicalRecord)
    {

        // Validate the update data
        $validated = $request->validate([
            'patient_id'   => 'required|exists:patients,id',
            'doctor_id'    => 'nullable|exists:doctor,id',
            'dianosis'     => 'required|string',
            'treatment'    => 'nullable|string',
            'medications'  => 'nullable|string',
            'notes'        => 'nullable|string',
        ]);

        // Update the medical record in the database
        $medicalRecord->update($validated);

        // Redirect to the medical records list with a success message
        return redirect()->route('medical_records.index')->with('success', 'Medical record updated successfully.');
    }

    /* Romove the specified medical record from storage. */
    public function destroy(MedicalRecord $medicalRecord)
    {

        // Delete the medical record from the database
        $medicalRecord->delete();

        // Redirect to the medical records list with a success message
        return redirect()->route('medical_records.index')->with('success', 'Medical record deleted successfully.');
    }
}