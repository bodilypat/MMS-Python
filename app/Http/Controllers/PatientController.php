<?php

namespace App\Http\Controllers;

use App\Models\Patient;
use Illuminate\Http\Request;

class PatientController extends Controller
{
    
    public function index()
    {
        /* Get all patient */
        $patients = Patient::all();

        /* Return the view with patients data */
        return view('patients.index', compact('patients'));
    }

    /* Show form creating a new patient */
    public function create()
    {
        /* Return the view to create a new patient */
        return view('patients.create');
    }

    /* Store a newly created patient in storage */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'firstName' => 'required|string|max:255',
            'lastName'  => 'required|string|max:255',
            'email'     => 'required|email|unique:patients,email',
            'dob'       => 'required|date',
            'gender'    => 'required|in:male,female,other',
            'phone'     => 'required|string|max:15',
            'address'   => 'nullable|string|max:255',
        ]);

        patient::create($validated);

        return redirect()->route('patients.index')->with('success', 'Patient created successfully.');
    }

    /* Display the specified patient */
    public function show(Patient $patient)
    {
        //return the view to show a specific patient
        return view('patient.show', compact('patient'));
    }

    /* Show the form for editing the specified patient. */
    public function edit(Patient $patient)
    {
        //Return the view to edit a patient
        return view('patients.edit', compact('patient'));
    }

    /* Update the specified patient in storage*/
    public function update(Request $request, Patient $patient)
    {
        //Validate the request date
        $validated = $request->validate([

            'firstName' => 'required|string|max:255',
            'lastName'  => 'required|string|max:255',
            'email'     => 'required|email|unique:patients,email',
            'dob'       => 'required|date',
            'gender'    => 'required|in:male,female,other',
            'phone'     => 'required|string|max:15',
            'address'   => 'nullable|string|max:255',
            
        ]);

        // Update the patient's information with the validated data
        $patient->update($validate);

        //Redirect back to the patient list with a success message
        return redirect()->route('patient.index')->with('success','patient updated successfully');
    }

    /* Remove the specified patient from storage. */
    public function destroy(Patient $patient)
    {
        $patient->delete();

        //Redirect back to the patients list with a success message
        return redirect()->route('patients.index')->with('success', 'Patient deleted successfull!');
    }
}