<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use Illuminate\Http\Request;

class DoctorController extends Controller
{
    // Display a listing of doctors
    public function index()
    {
        $doctors = Doctor::all(); // You might want to paginate or filter the results
        return view('doctors.index', compact('doctors'));
    }

    // Show the form for creating a new doctor
    public function create()
    {
        return view('doctors.create');
    }

    // Store a newly created doctor in storage
    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:doctors',
            'phone' => 'nullable|string',
            'specialty' => 'nullable|string',
            'availability' => 'nullable|string',
        ]);

        Doctor::create($validatedData);

        return redirect()->route('doctors.index')->with('success', 'Doctor created successfully!');
    }

    // Display the specified doctor
    public function show(Doctor $doctor)
    {
        return view('doctors.show', compact('doctor'));
    }

    // Show the form for editing the specified doctor
    public function edit(Doctor $doctor)
    {
        return view('doctors.edit', compact('doctor'));
    }

    // Update the specified doctor in storage
    public function update(Request $request, Doctor $doctor)
    {
        $validatedData = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:doctors,email,' . $doctor->id,
            'phone' => 'nullable|string',
            'specialty' => 'nullable|string',
            'availability' => 'nullable|string',
        ]);

        $doctor->update($validatedData);

        return redirect()->route('doctors.index')->with('success', 'Doctor updated successfully!');
    }

    // Remove the specified doctor from storage
    public function destroy(Doctor $doctor)
    {
        $doctor->delete();

        return redirect()->route('doctors.index')->with('success', 'Doctor deleted successfully!');
    }
}
