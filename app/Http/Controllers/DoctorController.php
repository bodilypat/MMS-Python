<?php

namespace App\Http\Controllers;

use App\Models\Doctor;
use Illuminate\Http\Request;

class DoctorController extends Controller
{
    /**
     * Display a listing of doctors.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $doctors = Doctor::all();
        return view('doctors.index', compact('doctors'));
    }

    /**
     * Show the form for creating a new doctor.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('doctors.create');
    }

    /**
     * Store a newly created doctor in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:doctors',
            'phone' => 'nullable|string|max:15',
            'specialization' => 'required|string|max:255',
        ]);

        Doctor::create($request->all());

        return redirect()->route('doctors.index')->with('success', 'Doctor added successfully.');
    }

    /**
     * Display the specified doctor.
     *
     * @param \App\Models\Doctor $doctor
     * @return \Illuminate\Http\Response
     */
    public function show(Doctor $doctor)
    {
        return view('doctors.show', compact('doctor'));
    }

    /**
     * Show the form for editing the specified doctor.
     *
     * @param \App\Models\Doctor $doctor
     * @return \Illuminate\Http\Response
     */
    public function edit(Doctor $doctor)
    {
        return view('doctors.edit', compact('doctor'));
    }

    /**
     * Update the specified doctor in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\Doctor $doctor
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Doctor $doctor)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:doctors,email,' . $doctor->id,
            'phone' => 'nullable|string|max:15',
            'specialization' => 'required|string|max:255',
        ]);

        $doctor->update($request->all());

        return redirect()->route('doctors.index')->with('success', 'Doctor updated successfully.');
    }

    /**
     * Remove the specified doctor from storage.
     *
     * @param \App\Models\Doctor $doctor
     * @return \Illuminate\Http\Response
     */
    public function destroy(Doctor $doctor)
    {
        $doctor->delete();

        return redirect()->route('doctors.index')->with('success', 'Doctor deleted successfully.');
    }
}
