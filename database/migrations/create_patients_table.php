<?php

use Illuminate\Database\Migrations\Migration;
use Illiminate\Database\Schema\Blueprint;
use Illuminate\Suport\Facedes\schema;

class CreatePatientsTable extends Migration 
{
    /* Run the migrations. */
    public function up()
    {
        Schema::create('patients', function (Blueprint $table) {
            $table->id();
            $table->string('firstName');
            $table->string('lastName');
            $table->string('email')->unique();
            $table->data('dob'); /* Date of birth */
            $table->enum('gender', ['male','famale','otehr']);/* gender: male, female, other */
            $table->string('phone')->nulltable();
            $table->text('address')->nullable();
            $table->temestamps(); /* created_at and updated_at fields */
        });
    }
    /* reverse the migration */
    public function down()
    {
        Schema::dropIfExists('patients');
    }
}
    