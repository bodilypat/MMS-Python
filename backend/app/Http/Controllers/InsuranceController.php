<?php

namespace App\Http\Controllers;

use App\Models\Insurance;
use Illuminate\Http\Request;

class InsuranceController extends Controller
{
    // Fetch all insurance records
    public function index()
    {
        $insurances = Insurance::with('patient')->get(); // Include patient data
        return response()->json($insurances);
    }

    // Show a specific insurance record by ID
    public function show($id)
    {
        $insurance = Insurance::with('patient')->find($id);

        if (!$insurance) {
            return response()->json(['message' => 'Insurance record not found'], 404);
        }

        return response()->json($insurance);
    }

    // Create a new insurance record
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'provider_name' => 'required|string|max:255',
            'policy_number' => 'required|string|unique:insurance,policy_number|max:50',
            'coverage_type' => 'required|in:Full,Partial',
            'coverage_amount' => 'required|numeric|min:0',
            'patient_id' => 'required|exists:patients,patient_id',
            'start_date' => 'required|date|before_or_equal:end_date',
            'end_date' => 'required|date|after_or_equal:start_date',
        ]);

        // Create the insurance record
        $insurance = Insurance::create($request->all());

        return response()->json($insurance, 201);
    }

    // Update an existing insurance record
    public function update(Request $request, $id)
    {
        $insurance = Insurance::find($id);

        if (!$insurance) {
            return response()->json(['message' => 'Insurance record not found'], 404);
        }

        // Validate the input
        $request->validate([
            'provider_name' => 'sometimes|required|string|max:255',
            'policy_number' => 'sometimes|required|string|unique:insurance,policy_number|max:50',
            'coverage_type' => 'sometimes|required|in:Full,Partial',
            'coverage_amount' => 'sometimes|required|numeric|min:0',
            'patient_id' => 'sometimes|required|exists:patients,patient_id',
            'start_date' => 'sometimes|required|date|before_or_equal:end_date',
            'end_date' => 'sometimes|required|date|after_or_equal:start_date',
        ]);

        // Update the insurance record
        $insurance->update($request->all());

        return response()->json($insurance);
    }

    // Delete an insurance record
    public function destroy($id)
    {
        $insurance = Insurance::find($id);

        if (!$insurance) {
            return response()->json(['message' => 'Insurance record not found'], 404);
        }

        // Delete the insurance record
        $insurance->delete();

        return response()->json(['message' => 'Insurance record deleted successfully']);
    }
}