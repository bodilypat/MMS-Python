
<?php

namespace App\Http\Controllers;

use App\Models\MedicalRecord;
use App\Models\Patient; // Assuming you have a Patient model
use Illuminate\Http\Request;

class MedicalRecordsController extends Controller
{
    /**
     * Display a listing of medical records.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $medicalRecords = MedicalRecord::with('patient')->get(); // Assuming you have a relationship
        return view('medical-records.index', compact('medicalRecords'));
    }

    /**
     * Show the form for creating a new medical record.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $patients = Patient::all(); // Fetch patients for dropdown
        return view('medical-records.create', compact('patients'));
    }

    /**
     * Store a newly created medical record in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'date' => 'required|date',
            'diagnosis' => 'required|string',
            'treatment' => 'nullable|string',
            'notes' => 'nullable|string',
        ]);

        MedicalRecord::create($request->all());

        return redirect()->route('medical-records.index')->with('success', 'Medical record added successfully.');
    }

    /**
     * Display the specified medical record.
     *
     * @param \App\Models\MedicalRecord $medicalRecord
     * @return \Illuminate\Http\Response
     */
    public function show(MedicalRecord $medicalRecord)
    {
        return view('medical-records.show', compact('medicalRecord'));
    }

    /**
     * Show the form for editing the specified medical record.
     *
     * @param \App\Models\MedicalRecord $medicalRecord
     * @return \Illuminate\Http\Response
     */
    public function edit(MedicalRecord $medicalRecord)
    {
        $patients = Patient::all(); // Fetch patients for dropdown
        return view('medical-records.edit', compact('medicalRecord', 'patients'));
    }

    /**
     * Update the specified medical record in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\MedicalRecord $medicalRecord
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, MedicalRecord $medicalRecord)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'date' => 'required|date',
            'diagnosis' => 'required|string',
            'treatment' => 'nullable|string',
            'notes' => 'nullable|string',
        ]);

        $medicalRecord->update($request->all());

        return redirect()->route('medical-records.index')->with('success', 'Medical record updated successfully.');
    }

    /**
     * Remove the specified medical record from storage.
     *
     * @param \App\Models\MedicalRecord $medicalRecord
     * @return \Illuminate\Http\Response
     */
    public function destroy(MedicalRecord $medicalRecord)
    {
        $medicalRecord->delete();

        return redirect()->route('medical-records.index')->with('success', 'Medical record deleted successfully.');
    }
}
