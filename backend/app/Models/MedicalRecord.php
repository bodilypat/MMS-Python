<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MedicalRecord extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'medical_records';

    // The primary key for the table
    protected $primaryKey = 'record_id';

    // Mass assignable fields
    protected $fillable = [
        'patient_id',
        'appointment_id',
        'diagnosis',
        'treatment_plan',
        'note',
        'status',
        'created_by',
        'updated_by',
        'attachments',
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

    // Define status options
    const STATUS_ACTIVE = 'Active';
    const STATUS_ARCHIVED = 'Archived';
    const STATUS_INACTIVE = 'Inactive';

    // Define created and updated at fields
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    // Set up automatic handling of timestamps
    public $timestamps = true;
}