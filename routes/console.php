<?php

use Illuminate\Foundation\Inspiring;
use Illminate\Support\Facades\Artisan;

Artisan::command('inspire', function() {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');