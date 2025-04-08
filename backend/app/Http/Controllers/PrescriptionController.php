<?php

namespace App\Http\Controllers;

use App\Models\Prescription;
use App\Models\MedicalRecord;
use Illuminate\Http\Request;

class PrescriptionController extends Controller
{
    // Fetch all prescriptions
    public function index()
    {
        $prescriptions = Prescription::with('medicalRecord')->get();
        return response()->json($prescriptions);
    }

    // Show a specific prescription by ID
    public function show($id)
    {
        $prescription = Prescription::with('medicalRecord')->find($id);

        if (!$prescription) {
            return response()->json(['message' => 'Prescription not found'], 404);
        }

        return response()->json($prescription);
    }

    // Create a new prescription
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'record_id' => 'required|exists:medical_records,record_id',
            'medication_name' => 'required|string|max:255',
            'dosage' => 'required|string|max:50',
            'frequency' => 'required|string|max:50',
            'start_date' => 'required|date',
            'end_date' => 'nullable|date',
            'instructions' => 'nullable|string',
            'status' => 'nullable|in:Active,Completed,Expired,Cancelled',
            'created_by' => 'required|integer', // Assuming user id
            'updated_by' => 'required|integer', // Assuming user id
        ]);

        // Create the prescription
        $prescription = Prescription::create($request->all());

        return response()->json($prescription, 201);
    }

    // Update an existing prescription
    public function update(Request $request, $id)
    {
        $prescription = Prescription::find($id);

        if (!$prescription) {
            return response()->json(['message' => 'Prescription not found'], 404);
        }

        // Validate the input
        $request->validate([
            'record_id' => 'required|exists:medical_records,record_id',
            'medication_name' => 'required|string|max:255',
            'dosage' => 'required|string|max:50',
            'frequency' => 'required|string|max:50',
            'start_date' => 'required|date',
            'end_date' => 'nullable|date',
            'instructions' => 'nullable|string',
            'status' => 'nullable|in:Active,Completed,Expired,Cancelled',
            'created_by' => 'required|integer',
            'updated_by' => 'required|integer',
        ]);

        // Update the prescription
        $prescription->update($request->all());

        return response()->json($prescription);
    }

    // Delete a prescription
    public function destroy($id)
    {
        $prescription = Prescription::find($id);

        if (!$prescription) {
            return response()->json(['message' => 'Prescription not found'], 404);
        }

        // Delete the prescription
        $prescription->delete();

        return response()->json(['message' => 'Prescription deleted successfully']);
    }
}