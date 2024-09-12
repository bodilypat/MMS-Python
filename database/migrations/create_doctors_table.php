<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDoctorsTable extends Migration
{
    /* run the migration */

    public functon up()
    {
        Schema::create('doctors', function(Blueprint $table){
            $table->id();
            $table->string('firstName');
            $table->string('lastName');
            $table->string('email')->unique();
            $table->string('phone')->nullable();
            $table->string('specialty'); /* Doctor's specialty */
            $table->text('address')->nullable();
            $table->timestamps(); /* created_at and update_at fields  */
        });
    }
    /*  reverse the migration */
}
public function down() 
{
    Schema::dropIfExists('doctors');
}