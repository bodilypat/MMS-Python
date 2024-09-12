<?php

namespace App\Http\Controllers;

use App\Models\Prescription;
use App\Models\Patient; // Assuming you have a Patient model
use App\Models\Doctor; // Assuming you have a Doctor model
use Illuminate\Http\Request;

class PrescriptionController extends Controller
{
    /**
     * Display a listing of the prescriptions.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $prescriptions = Prescription::with('patient', 'doctor')->get();
        return view('prescriptions.index', compact('prescriptions'));
    }

    /**
     * Show the form for creating a new prescription.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $patients = Patient::all();
        $doctors = Doctor::all();
        return view('prescriptions.create', compact('patients', 'doctors'));
    }

    /**
     * Store a newly created prescription in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'doctor_id' => 'required|exists:doctors,id',
            'medication' => 'required|string',
            'dosage' => 'required|string',
            'instructions' => 'nullable|string',
            'date' => 'required|date',
        ]);

        Prescription::create($request->all());

        return redirect()->route('prescriptions.index')->with('success', 'Prescription added successfully.');
    }

    /**
     * Display the specified prescription.
     *
     * @param \App\Models\Prescription $prescription
     * @return \Illuminate\Http\Response
     */
    public function show(Prescription $prescription)
    {
        return view('prescriptions.show', compact('prescription'));
    }

    /**
     * Show the form for editing the specified prescription.
     *
     * @param \App\Models\Prescription $prescription
     * @return \Illuminate\Http\Response
     */
    public function edit(Prescription $prescription)
    {
        $patients = Patient::all();
        $doctors = Doctor::all();
        return view('prescriptions.edit', compact('prescription', 'patients', 'doctors'));
    }

    /**
     * Update the specified prescription in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\Prescription $prescription
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Prescription $prescription)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'doctor_id' => 'required|exists:doctors,id',
            'medication' => 'required|string',
            'dosage' => 'required|string',
            'instructions' => 'nullable|string',
            'date' => 'required|date',
        ]);

        $prescription->update($request->all());

        return redirect()->route('prescriptions.index')->with('success', 'Prescription updated successfully.');
    }

    /**
     * Remove the specified prescription from storage.
     *
     * @param \App\Models\Prescription $prescription
     * @return \Illuminate\Http\Response
     */
    public function destroy(Prescription $prescription)
    {
        $prescription->delete();

        return redirect()->route('prescriptions.index')->with('success', 'Prescription deleted successfully.');
    }
}
