<?php

namespace App\Http\Controllers;

use App\Models\Patient;
use Illuminate\Http\Request;

class PatientController extends Controller
{
    // Fetch a list of all patients
    public function index()
    {
        $patients = Patient::all();  // Retrieve all patient records
        return response()->json($patients);
    }

    // Show a single patient by ID
    public function show($id)
    {
        $patient = Patient::find($id); // Find the patient by ID

        if (!$patient) {
            return response()->json(['message' => 'Patient not found'], 404);
        }

        return response()->json($patient);
    }

    // Create a new patient record
    public function store(Request $request)
    {
        // Validate the input data
        $request->validate([
            'first_name' => 'required|string|max:100',
            'last_name' => 'required|string|max:100',
            'date_of_birth' => 'required|date',
            'gender' => 'required|in:male,female,other',
            'email' => 'nullable|email|unique:patients,email',
            'phone_number' => 'required|regex:/^[0-9]{10,15}$/|unique:patients,phone_number',
            'address' => 'nullable|string|max:255',
            'insurance_provider' => 'nullable|string|max:100',
            'insurance_policy_number' => 'nullable|string|max:100',
            'primary_care_physician' => 'nullable|string|max:100',
            'medical_history' => 'nullable|string',
            'allergies' => 'nullable|string',
            'status' => 'nullable|in:active,inactive,deceased',
        ]);

        // Create a new patient record
        $patient = Patient::create($request->all());

        return response()->json($patient, 201);
    }

    // Update an existing patient record
    public function update(Request $request, $id)
    {
        // Find the patient by ID
        $patient = Patient::find($id);

        if (!$patient) {
            return response()->json(['message' => 'Patient not found'], 404);
        }

        // Validate the input data
        $request->validate([
            'first_name' => 'required|string|max:100',
            'last_name' => 'required|string|max:100',
            'date_of_birth' => 'required|date',
            'gender' => 'required|in:male,female,other',
            'email' => 'nullable|email|unique:patients,email,' . $id,
            'phone_number' => 'required|regex:/^[0-9]{10,15}$/|unique:patients,phone_number,' . $id,
            'address' => 'nullable|string|max:255',
            'insurance_provider' => 'nullable|string|max:100',
            'insurance_policy_number' => 'nullable|string|max:100',
            'primary_care_physician' => 'nullable|string|max:100',
            'medical_history' => 'nullable|string',
            'allergies' => 'nullable|string',
            'status' => 'nullable|in:active,inactive,deceased',
        ]);

        // Update the patient record
        $patient->update($request->all());

        return response()->json($patient);
    }

    // Delete a patient record
    public function destroy($id)
    {
        // Find the patient by ID
        $patient = Patient::find($id);

        if (!$patient) {
            return response()->json(['message' => 'Patient not found'], 404);
        }

        // Delete the patient record
        $patient->delete();

        return response()->json(['message' => 'Patient deleted successfully']);
    }
}