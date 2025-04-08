<?php

namespace App\Http\Controllers;

use App\Models\MedicalRecord;
use App\Models\Patient;
use App\Models\Appointment;
use Illuminate\Http\Request;

class MedicalRecordController extends Controller
{
    // Fetch all medical records
    public function index()
    {
        $records = MedicalRecord::with(['patient', 'appointment'])->get();
        return response()->json($records);
    }

    // Show a specific medical record by ID
    public function show($id)
    {
        $record = MedicalRecord::with(['patient', 'appointment'])->find($id);

        if (!$record) {
            return response()->json(['message' => 'Medical Record not found'], 404);
        }

        return response()->json($record);
    }

    // Create a new medical record
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'diagnosis' => 'nullable|string|max:500',
            'treatment_plan' => 'nullable|string',
            'note' => 'nullable|string',
            'status' => 'nullable|in:Active,Archived,Inactive',
            'created_by' => 'required|integer', // Assuming user id
            'updated_by' => 'required|integer', // Assuming user id
            'attachments' => 'nullable|string|max:255',
        ]);

        // Create the medical record
        $record = MedicalRecord::create($request->all());

        return response()->json($record, 201);
    }

    // Update an existing medical record
    public function update(Request $request, $id)
    {
        $record = MedicalRecord::find($id);

        if (!$record) {
            return response()->json(['message' => 'Medical Record not found'], 404);
        }

        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'diagnosis' => 'nullable|string|max:500',
            'treatment_plan' => 'nullable|string',
            'note' => 'nullable|string',
            'status' => 'nullable|in:Active,Archived,Inactive',
            'created_by' => 'required|integer',
            'updated_by' => 'required|integer',
            'attachments' => 'nullable|string|max:255',
        ]);

        // Update the medical record
        $record->update($request->all());

        return response()->json($record);
    }

    // Delete a medical record
    public function destroy($id)
    {
        $record = MedicalRecord::find($id);

        if (!$record) {
            return response()->json(['message' => 'Medical Record not found'], 404);
        }

        // Delete the medical record
        $record->delete();

        return response()->json(['message' => 'Medical Record deleted successfully']);
    }
}