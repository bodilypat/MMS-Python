<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Pharmacy extends Model
{
    use HasFactory;

    // The name of the table
    protected $table = 'pharmacies';

    // The primary key for the table
    protected $primaryKey = 'pharmacy_id';

    // Mass assignable fields
    protected $fillable = [
        'name',
        'address',
        'phone_number',
        'email',
    ];

    // Set up automatic handling of timestamps
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    public $timestamps = true;
}