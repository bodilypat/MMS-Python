<?php

namespace App\Http\Controllers;

use App\Models\Patient;
use Illuminate\Http\Request;

class PatientController extends Controllers
{
    
    public function store(Request $request)
    {
        $validated = $request->validate([
            'firstName' => 'required|string|max:255',
            'lastName' => 'required|string|max:255',
            'email' => 'required|email|unique:patients,email',
            'dob' => 'required|date',
            'gender' => 'required|in:male,female,other',
            'phone' => 'required|string|max:15',
            'address' => 'nullable|string|max:255',
        ]);

        patient::create($validated);

        return redirect()->route('patients.index')->with('success', 'Patient created successfully.');
    }
}