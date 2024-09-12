<?php

namespace App\Models;

use Illuminate\Database\Eloquent\HasFactory;
use Illuminate\Database\Eloquent\Model;

class billings extends Model
{
    use HasFactory;

    /* Define the fields that are mass-assignable */
    protected $fileable = [
        'patient_id',
        'appointment_id',
        'amount',
        'paid_amount',
        'billing_date',
        'notes',
    ];

    /* Define the relationship with the Patient model */
    public function patient()
    {
        return $this->belongsTo(Patient::class);
    }

    /* Define the relationship with the appointment model */
    public function appointment()
    {
        return $this->belongsTo('Appointment::class');
    }
}