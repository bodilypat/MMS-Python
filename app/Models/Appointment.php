<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Appointment extends Model
{
    use HasFactory;

    /* Define the fields that are mass-assignable to prevent mass assignment vulnerabilities */
    protected $fillable = [
        'patient-id',
        'doctor_id',
        'appointment_time',
        'status',
        'notes',
    ];
    /* Define the relationship with the Patient Model */
    public function patient() 
    {
        return $this->belongsTo(Patient::class);
    }

    /* Define the relationship with the doctor model */
    public function doctor()
    {
        return $this->belongsTo(Doctor::class);
    }
}