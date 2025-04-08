<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Payment extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'payments';

    // The primary key for the table
    protected $primaryKey = 'billing_id';

    // Mass assignable fields
    protected $fillable = [
        'patient_id',
        'appointment_id',
        'total_amount',
        'amount_paid',
        'balance_due',
        'payment_status',
        'payment_date',
        'insurance_claimed_amount',
        'insurance_status',
        'created_at',
        'updated_at',
    ];

    // Relationships
    public function patient()
    {
        return $this->belongsTo(Patient::class, 'patient_id');
    }

    public function appointment()
    {
        return $this->belongsTo(Appointment::class, 'appointment_id');
    }

    // Set up automatic handling of timestamps
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    public $timestamps = true;
}