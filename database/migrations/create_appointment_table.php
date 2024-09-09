<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateAppointmentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('appointments', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('doctor_id')->constrained()->onDelete('cascade'); // Foreign key to doctors table
            $table->foreignId('patient_id')->constrained()->onDelete('cascade'); // Foreign key to patients table
            $table->dateTime('appointment_date'); // Date and time of the appointment
            $table->string('status')->default('scheduled'); // Status of the appointment (e.g., scheduled, canceled, completed)
            $table->text('notes')->nullable(); // Additional notes or comments
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
        Schema::dropIfExists('appointments');
    }
}
