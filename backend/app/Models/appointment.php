<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Appointment extends Model
{
    use HasFactory;

    // Define the table name explicitly (optional if it matches the model name in plural form)
    protected $table = 'appointments';

    // The primary key for the table
    protected $primaryKey = 'appointment_id';

    // Disable auto-incrementing for the primary key (if necessary)
    public $incrementing = true;

    // The attributes that are mass assignable
    protected $fillable = [
        'patient_id',
        'doctor_id',
        'appointment_date',
        'reason_for_visit',
        'status',
        'duration',
        'appointment_type',
        'notes',
    ];

    // Set the date format for the model
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    // Define relationships
    public function patient()
    {
        return $this->belongsTo(Patient::class, 'patient_id');
    }

    public function doctor()
    {
        return $this->belongsTo(Doctor::class, 'doctor_id');
    }

    // Set the date format for the appointment date
    protected $casts = [
        'appointment_date' => 'datetime',
    ];
}