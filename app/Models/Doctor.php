<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Doctor extends Model 
{
    use HasFactory;

    /* Define the fields that are mass-assignable to prevent mass assignment valunerabilities */
    protected $fillable = [
        'firstName',
        'lastName',
        'email',
        'phone',
        'specialty',
        'address',
    ];

    /* optionally, define relationships with other models here */
    /* example: A doctor might have many appointment */
    public function appointments()
    {
        return $this->hasMany(Appointment::class);
    }

    public function patients()
    {
        return $this->belongsToMany(Patient::class);
    }
}