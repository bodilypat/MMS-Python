<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePatientsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('patients', function (Blueprint $table) {
            $table->id(); // Automatically creates an auto-incrementing unsigned BIGINT (11) primary key
            $table->string('first_name');
            $table->string('last_name');
            $table->date('date_of_birth');
            $table->char('gender', 1); // Use CHAR(1) for gender representation
            $table->string('address');
            $table->string('phone_number');
            $table->string('email')->unique(); // Ensure email is unique
            $table->timestamps(); // Adds created_at and updated_at columns
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('patients');
    }
}
