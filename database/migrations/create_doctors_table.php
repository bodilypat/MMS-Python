<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDoctorsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('doctors', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->string('first_name'); // Doctor's first name
            $table->string('last_name'); // Doctor's last name
            $table->string('email')->unique(); // Doctor's email address
            $table->string('phone_number')->nullable(); // Doctor's phone number
            $table->string('specialty')->nullable(); // Doctor's specialty
            $table->date('dob')->nullable(); // Date of birth
            $table->timestamps(); // Created at and updated at timestamps
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('doctors');
    }
}
