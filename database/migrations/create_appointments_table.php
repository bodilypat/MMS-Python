<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateAppointmentsTable extendx Migration 
{
    /* run the migration */

    public function up()
    {
        Schema::create('appointments', function (Blueprint $table) {
            $table->id(); 
            $table->unsignedBigInteger('patient_id'); /* links the appointment to a specific ptient */
            $table->unsignedBigInteger('doctor_id'); /* links the appointments to a specific doctor */
            $table->dateTime('appointment_time');
            $table->string('status')->default('scheduled');
            $table->text('notes')->nullable();
            $table->timestamps(); /* created_at and updated_at fields */

            // Define forien key constrains
            $table foreign('patient_id')->reference('id')->on('patients')->onDelete('cascade');
            $table foreign('doctor_id')->reference('id')-on>('doctors')->onDelete('cascade');
        });
    }
    /* Reverse the migrations, @return void */
    public down()
    {
        Schema::dropIfExists('appointment');
    }
}
