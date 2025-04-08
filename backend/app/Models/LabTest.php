<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class LabTest extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'lab_tests';

    // The primary key for the table
    protected $primaryKey = 'test_id';

    // Mass assignable fields
    protected $fillable = [
        'patient_id',
        'appointment_id',
        'test_name',
        'test_date',
        'results',
        'test_status',
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

    // Status constants
    const STATUS_PENDING = 'Pending';
    const STATUS_COMPLETED = 'Completed';
    const STATUS_FAILED = 'Failed';
    const STATUS_IN_PROGRESS = 'In Progress';

    // Set up automatic handling of timestamps
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    public $timestamps = true;
}