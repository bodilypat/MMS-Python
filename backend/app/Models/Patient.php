<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Patient extends Model
{
    use HasFactory;

    // Define the table name explicitly (optional if it matches the model name in plural form)
    protected $table = 'patients';

    // The primary key for the table
    protected $primaryKey = 'patient_id';

    // Disable auto-incrementing for the primary key (if necessary)
    public $incrementing = true;

    // The attributes that are mass assignable
    protected $fillable = [
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'email',
        'phone_number',
        'address',
        'insurance_provider',
        'insurance_policy_number',
        'primary_care_physician',
        'medical_history',
        'allergies',
        'status',
    ];

    // Set the date format for the model
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    // Use custom date format if needed
    protected $casts = [
        'date_of_birth' => 'date',
    ];
}
