<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Insurance extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'insurance';

    // The primary key for the table
    protected $primaryKey = 'insurance_id';

    // Mass assignable fields
    protected $fillable = [
        'provider_name',
        'policy_number',
        'coverage_type',
        'coverage_amount',
        'patient_id',
        'start_date',
        'end_date',
    ];

    // Set up automatic handling of timestamps
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    public $timestamps = true;

    // Relationship with the patient
    public function patient()
    {
        return $this->belongsTo(Patient::class, 'patient_id');
    }
}