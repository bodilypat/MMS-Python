<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class requestAppointment extends Model
{
    protected $fillable = [
        'name',
        'email',
        'phone',
        'doctor',
        'message',
        'address',
        'stime'
    ];
}
