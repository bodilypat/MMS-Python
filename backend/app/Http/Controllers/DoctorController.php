<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use Illuminate\Http\Request;

class DoctorController extends Controller
{
    // Fetch a list of all doctors
    public function index()
    {
        $doctors = Doctor::all();  // Retrieve all doctor records
        return response()->json($doctors);
    }

    // Show a single doctor by ID
    public function show($id)
    {
        $doctor = Doctor::find($id); // Find the doctor by ID

        if (!$doctor) {
            return response()->json(['message' => 'Doctor not found'], 404);
        }

        return response()->json($doctor);
    }

    // Create a new doctor record
    public function store(Request $request)
    {
        // Validate the input data
        $request->validate([
            'first_name' => 'required|string|max:100',
            'last_name' => 'required|string|max:100',
            'specialization' => 'required|string|max:100',
            'email' => 'required|email|unique:doctors,email',
            'phone_number' => 'required|regex:/^[0-9]{10,15}$/|unique:doctors,phone_number',
            'department' => 'nullable|string|max:100',
            'birthdate' => 'nullable|date',
            'address' => 'nullable|string|max:255',
            'status' => 'nullable|in:active,inactive,retired',
            'notes' => 'nullable|string',
        ]);

        // Create a new doctor record
        $doctor = Doctor::create($request->all());

        return response()->json($doctor, 201);
    }

    // Update an existing doctor record
    public function update(Request $request, $id)
    {
        // Find the doctor by ID
        $doctor = Doctor::find($id);

        if (!$doctor) {
            return response()->json(['message' => 'Doctor not found'], 404);
        }

        // Validate the input data
        $request->validate([
            'first_name' => 'required|string|max:100',
            'last_name' => 'required|string|max:100',
            'specialization' => 'required|string|max:100',
            'email' => 'required|email|unique:doctors,email,' . $id,
            'phone_number' => 'required|regex:/^[0-9]{10,15}$/|unique:doctors,phone_number,' . $id,
            'department' => 'nullable|string|max:100',
            'birthdate' => 'nullable|date',
            'address' => 'nullable|string|max:255',
            'status' => 'nullable|in:active,inactive,retired',
            'notes' => 'nullable|string',
        ]);

        // Update the doctor record
        $doctor->update($request->all());

        return response()->json($doctor);
    }

    // Delete a doctor record
    public function destroy($id)
    {
        // Find the doctor by ID
        $doctor = Doctor::find($id);

        if (!$doctor) {
            return response()->json(['message' => 'Doctor not found'], 404);
        }

        // Delete the doctor record
        $doctor->delete();

        return response()->json(['message' => 'Doctor deleted successfully']);
    }
}
