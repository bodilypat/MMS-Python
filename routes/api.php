<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::midleware('auth:api')->get('/user', function (Request $request){
    return $request->user();
});