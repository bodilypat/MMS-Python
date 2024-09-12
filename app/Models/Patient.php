<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Patient extends Model
{
    use HasFactory;

    /* Define which fields are mess-assignable to protect against mass assignment vulnerabilities */
    protected $fillable = [
        'firstName',
        'lastName',
        'email',
        'dob',
        'gender',
        'phone',
        'address',
    ];
    /* optionally, define relationships to other models here */
    /* a patient might have many appointments or medical records */
    public function appointment()
    {
        return $this->hasMany(Appointment::class);
    }

    public function medicalRecords()
    {
        return $this->hasMany(MedicalRecord::class);
    }
}