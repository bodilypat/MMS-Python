<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use Illuminate\Http\Request;

class DoctorController extends Controllers
{

    /* Display a listing of the Doctors. */
    public function index()
    {

        // Retrieve all doctors 
        $doctors = Doctor::all();

        // Return the view with doctor data
        return view('doctors.index', compact('doctors'));
    }

    /* Show the form form creating a new doctor */
    public function create()
    {

        // Return the view to create a new doctor
        return view('doctors.create');
    }

    /* Store a newly created doctor in storage */
    public function store(Request $request)
    {

        // Validate the request data
        $validated = $request->validate([
            'firstName' => 'required|string|max:255',
            'lastName'  => 'required|string|max:255',
            'email'     => 'required|string|unique:doctors,email',
            'phone'     => 'required|string|max:15',
            'specialty' => 'required|string|max:25',
            'address'   => 'nullable|string|max:255',
        ]);
        
        // Create a new doctor with the validated data
        Doctor::create($validated);
        
        // Redirect back to the doctors list with a success message
        return redirect()->route('doctors.index')->with('success', 'Doctor created successfully');
    }

    /* Display the specified doctor. */
    public function show(Doctor $doctor)
    {

        // Return the view to show a specific doctor
        return view('doctors.show', compact('doctor'));
    }

    /* Show the form for editing the specified doctor */
    public function edit(Doctor $doctor)
    {

        // Return the view to edit a doctor
        return view('doctors.edit', compact('doctor'));
    }

    /* update the specified doctor in storage */
    public function update(Request $request, Doctor $doctor)
    {

        // Validate the request data 
        $validate = $request->validate([
            'firstName' => 'required|string|max:255',
            'lastName'  => 'required|string|max:255',
            'email'     => 'required|string|unique:doctors,email',
            'phone'     => 'required|string|max:15',
            'specialty' => 'required|string|max:25',
            'address'   => 'nullable|string|max:255',
        ]);

        // Update the doctor's information with the validate data
        $doctor->update($validated);

        // Redirect back to the doctors list with a success message 
        return redirect()->route('doctors.index')->with('success', 'Doctor updated successfully.');
    }

    /* Remove the specified doctor from storage */
    public function destroy(Doctor $doctor)
    {

        // Delete the doctor
        $doctor->delete();

        // Redirect back to the doctors list with a success massage
        return redirect()->route('doctors.index')->with('success','Doctor deleted successfull.');
    }
}