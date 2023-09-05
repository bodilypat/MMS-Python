<?php 

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class department extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'description',
        'photo_path',
        'block_id',
        'hod_id',
    ];

    public function rooms()
    {
        return $this->hasMany(rooms::class);
    }

    public function block(): belongTo
    {
        return $this->belongsTo(blocks::class);
    }
    
    public function hod(): HasOne
    {
        return $this->hasOne(hod::class);
    }
}