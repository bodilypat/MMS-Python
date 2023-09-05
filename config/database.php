<?php

use Illminate\Support\Str;
return [ 
     'default' => env('DB_CONNECTION', 'myssql'),
    'connection' => [
             'sqlite' => [
                      'driver' => 'sqlite',
                      'url' => env('DATABASE_URL'),
                      'database' => env('DB_DATABASE', database_path('database.sqlite')),
                      'prefix' => '',
                      'foreign_key_constraints' => env('DB_FOREIGN_KEYS', true),
                  ],
             'mysql' => [
                      'driver' => 'mysql',
                      'url' => env('DATABASE_URL'),
                  ],
  ],
  
