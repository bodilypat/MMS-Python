<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;

// Define the routes for the user resource
Route::get('/users', [UserController::class, 'index']);  // Fetch all users
Route::get('/users/{user}', [UserController::class, 'show']);  // Fetch a single user
Route::post('/users', [UserController::class, 'store']);  // Add a new user
Route::put('/users/{user}', [UserController::class, 'update']);  // Update an existing user
Route::delete('/users/{user}', [UserController::class, 'destroy']);  // Delete a user

// Add other resources here like doctor, patient, etc., following the same structure.