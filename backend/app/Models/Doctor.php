<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Doctor extends Model
{
    use HasFactory;

    // Define the table name explicitly (optional if it matches the model name in plural form)
    protected $table = 'doctors';

    // The primary key for the table
    protected $primaryKey = 'doctor_id';

    // Disable auto-incrementing for the primary key (if necessary)
    public $incrementing = true;

    // The attributes that are mass assignable
    protected $fillable = [
        'first_name',
        'last_name',
        'specialization',
        'email',
        'phone_number',
        'department',
        'birthdate',
        'address',
        'status',
        'notes'
    ];

    // Set the date format for the model
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    // Use custom date format if needed
    protected $casts = [
        'birthdate' => 'date',
    ];
}
