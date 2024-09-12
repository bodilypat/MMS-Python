<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MedicalRecord extends Model
{
    use HasFactory;

    /* Protects against mass assignment vulnerabilities by specifying */
    protected $fillable = [
        'patient_id',
        'doctor_id',
        'diagnosis',
        'treatment',
        'medications',
        'notes',
    ];

    /* define the reletionship with the patient model */
    public function patient()
    {
        return $this->belongsTo(Patient::class);
    }

    /* define the relationship with the Doctor model */
    public function doctor()
    {
        return $this->belongsTo(Doctor::class);
    }
}