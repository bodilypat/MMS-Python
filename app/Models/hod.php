<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class had extends Model
{
    use HasFactory;

    protected $fillable = [
        'doctor_id',
    ];
    public function department(): BelongsTo
    {
        return $this->belongsTo(department::class);
    }
}