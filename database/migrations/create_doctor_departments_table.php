<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDoctorDepartmentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('doctor_departments', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('doctor_id')->constrained()->onDelete('cascade'); // Foreign key to doctors table
            $table->foreignId('department_id')->constrained()->onDelete('cascade'); // Foreign key to departments table
            $table->timestamps(); // Created at and updated at timestamps

            // Adding a composite unique key to ensure each doctor-department pair is unique
            $table->unique(['doctor_id', 'department_id']);
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('doctor_departments');
    }
}
