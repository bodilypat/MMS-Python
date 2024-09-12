<?php

namespace App\Http\Controllers;

use App\Models\Prescription;
use Illuminate\Http\Request;

class PrescriptionController extends Controllers
{
    public function store(Request $request)
    {
        $validate = $request->validate([
            'patient_id'        => 'required|exists:patient,id',
            'doctor_id'         => 'required|exists:doctors,id',
            'medical_record_id' => 'required|exists:medical_record,id',
            'medication_name'   => 'required|string',
            'dosage'            => 'required|string',
            'frequency'         => 'required|string',
            'instructions'      => 'nullable|string',
            'start_date'        => 'required|date',
            'end_date'          => 'nullable|date',
        ]);

        Prescription::create($validated);

        return redirect()->route('prescriptions.index')->with('success','Prescription created successfully.');
    }
}