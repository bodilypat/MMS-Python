<?php

namespace App\Http\Controllers;

use App\Models\Pharmacy;
use Illuminate\Http\Request;

class PharmacyController extends Controller
{
    // Fetch all pharmacies
    public function index()
    {
        $pharmacies = Pharmacy::all();
        return response()->json($pharmacies);
    }

    // Show a specific pharmacy by ID
    public function show($id)
    {
        $pharmacy = Pharmacy::find($id);

        if (!$pharmacy) {
            return response()->json(['message' => 'Pharmacy not found'], 404);
        }

        return response()->json($pharmacy);
    }

    // Create a new pharmacy
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'name' => 'required|string|max:255',
            'address' => 'required|string|unique:pharmacies,address|max:255',
            'phone_number' => 'required|string|unique:pharmacies,phone_number|regex:/^[0-9]+$/',
            'email' => 'required|email|unique:pharmacies,email|max:255',
        ]);

        // Create the pharmacy
        $pharmacy = Pharmacy::create($request->all());

        return response()->json($pharmacy, 201);
    }

    // Update an existing pharmacy
    public function update(Request $request, $id)
    {
        $pharmacy = Pharmacy::find($id);

        if (!$pharmacy) {
            return response()->json(['message' => 'Pharmacy not found'], 404);
        }

        // Validate the input
        $request->validate([
            'name' => 'sometimes|required|string|max:255',
            'address' => 'sometimes|required|string|unique:pharmacies,address|max:255',
            'phone_number' => 'sometimes|required|string|unique:pharmacies,phone_number|regex:/^[0-9]+$/',
            'email' => 'sometimes|required|email|unique:pharmacies,email|max:255',
        ]);

        // Update the pharmacy
        $pharmacy->update($request->all());

        return response()->json($pharmacy);
    }

    // Delete a pharmacy
    public function destroy($id)
    {
        $pharmacy = Pharmacy::find($id);

        if (!$pharmacy) {
            return response()->json(['message' => 'Pharmacy not found'], 404);
        }

        // Delete the pharmacy
        $pharmacy->delete();

        return response()->json(['message' => 'Pharmacy deleted successfully']);
    }
}