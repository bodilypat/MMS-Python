<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Patient extends Model
{
    use HasFactory;

    // The table associated with the model
    protected $table = 'patients';

    // The attributes that are mass assignable
    protected $fillable = [
        'name',
        'email',
        'phone',
        'address',
        'medical_history'
    ];

    // The attributes that should be hidden for arrays
    protected $hidden = [
        'created_at',
        'updated_at',
    ];

    // The attributes that should be cast to native types
    protected $casts = [
        'created_at' => 'datetime',
        'updated_at' => 'datetime',
    ];

    // Define relationships here
    public function appointments()
    {
        return $this->hasMany(Appointment::class);
    }
}
