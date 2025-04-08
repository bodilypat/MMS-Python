<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Prescription extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'prescriptions';

    // The primary key for the table
    protected $primaryKey = 'prescription_id';

    // Mass assignable fields
    protected $fillable = [
        'record_id',
        'medication_name',
        'dosage',
        'frequency',
        'start_date',
        'end_date',
        'instructions',
        'status',
        'created_by',
        'updated_by',
    ];

    // Relationships
    public function medicalRecord()
    {
        return $this->belongsTo(MedicalRecord::class, 'record_id');
    }

    // Define status options
    const STATUS_ACTIVE = 'Active';
    const STATUS_COMPLETED = 'Completed';
    const STATUS_EXPIRED = 'Expired';
    const STATUS_CANCELLED = 'Cancelled';

    // Set up automatic handling of timestamps
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    public $timestamps = true;
}