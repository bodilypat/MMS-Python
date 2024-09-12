<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use Illuminate\Http\Request;

class DoctorController extends Controllers
{
    public function store(Request $request)
    {
        $validated = $request->validate([
            'firstName' => 'required|string|max:255',
            'lastName' => 'required|string|max:255',
            'emai' => 'required|string|unique:doctors,email',
            'phone' => 'required|string|max:15',
            'specialty' => 'required|string|max:25',
            'address' => 'nullable|string|max:255',
        ]);
        
        Doctor::create($validated);
        
        return redirect()->route('doctors.index')->with('success', 'Doctor created successfully');
    }
}