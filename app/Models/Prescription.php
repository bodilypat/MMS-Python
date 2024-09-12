<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Prescription extends Model 
{
    use HasFactory;

    /* Define the fields that are mass-assignable  */
    protected $files = [
        'patient_id',
        'doctor_id',
        'medical_record_id',
        'medical_name',
        'docage',
        'instructions',
        'start_date',
        'end_date',
    ];

    /* Define the relationship with the Patient model */
    public function patient()
    {
        return $this->belongsTo(Patient::class);
    }

    /* Define the relatioship with the Doctor model */
    public function doctor()
    {
        return $this->belongsTo(Doctor::class);
    }

    /* Define the relationship with the MedicalRecord model */
    public function medicalRecord()
    {
        return $this->belongsTo(MedicalRecord::class);
    }
}