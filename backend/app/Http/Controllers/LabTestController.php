<?php

namespace App\Http\Controllers;

use App\Models\LabTest;
use App\Models\Patient;
use App\Models\Appointment;
use Illuminate\Http\Request;

class LabTestController extends Controller
{
    // Fetch all lab tests
    public function index()
    {
        $labTests = LabTest::with(['patient', 'appointment'])->get();
        return response()->json($labTests);
    }

    // Show a specific lab test by ID
    public function show($id)
    {
        $labTest = LabTest::with(['patient', 'appointment'])->find($id);

        if (!$labTest) {
            return response()->json(['message' => 'Lab test not found'], 404);
        }

        return response()->json($labTest);
    }

    // Create a new lab test
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'test_name' => 'required|string|max:255',
            'test_date' => 'required|date',
            'results' => 'nullable|string',
            'test_status' => 'nullable|in:Pending,Completed,Failed,In Progress',
        ]);

        // Check if a test for the patient and appointment already exists with the same test name
        $existingTest = LabTest::where('patient_id', $request->patient_id)
            ->where('appointment_id', $request->appointment_id)
            ->where('test_name', $request->test_name)
            ->first();

        if ($existingTest) {
            return response()->json(['message' => 'Test already exists for the patient and appointment'], 400);
        }

        // Create the lab test
        $labTest = LabTest::create($request->all());

        return response()->json($labTest, 201);
    }

    // Update an existing lab test
    public function update(Request $request, $id)
    {
        $labTest = LabTest::find($id);

        if (!$labTest) {
            return response()->json(['message' => 'Lab test not found'], 404);
        }

        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'test_name' => 'required|string|max:255',
            'test_date' => 'required|date',
            'results' => 'nullable|string',
            'test_status' => 'nullable|in:Pending,Completed,Failed,In Progress',
        ]);

        // Update the lab test
        $labTest->update($request->all());

        return response()->json($labTest);
    }

    // Delete a lab test
    public function destroy($id)
    {
        $labTest = LabTest::find($id);

        if (!$labTest) {
            return response()->json(['message' => 'Lab test not found'], 404);
        }

        // Delete the lab test
        $labTest->delete();

        return response()->json(['message' => 'Lab test deleted successfully']);
    }
}