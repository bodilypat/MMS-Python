<?php

namespace App\Http\Controllers;

use App\Models\MidicalRecord;
use Illuminate\Http\Request;

class MedicalRecordController extends Controller
{
    public function store(Request $request)
    {
        $valdiated = $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'doctor_id' => 'nullable|exists:doctor,id',
            'dianosis' => 'required|string',
            'treatment' => 'nullable|string',
            'medications' => 'nullable|string',
            'notes' => 'nullable|string',
        ]);

        MedicalRecord::create($validated);

        return redirect()->route('medical-record.index')->with('success', 'Midical record created successfully.');
    }
    
}