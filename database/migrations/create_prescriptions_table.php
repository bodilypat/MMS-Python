<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePrescriptionsTable extends Migration 
{
    /* Run the Migration */

    public function up()
    {
        Schema::create('prescriptions', function(Blueprint $table){
            $table->id();
            $table->unsignedBigInteger('patient_id');
            $table->unsignedBigInteger('doct_id');
            $table->unsignedBigInteger('medical_record_id')->nullable();
            $table->string('medication_name');
            $table->string('docage');
            $table->string('frequency');
            $table->text('instructions')->nullable();
            $table->date('start_date');
            $table->date('end_date')->nullable();
            $table->timestamps();

            /* Define foreign key constrains */
            $table->foreign('patient_id')->reference('id')->on('patients')->onDelete(cascade);
            $table->foreign('doctor_id')->reference('id')->on('doctor')->onDelete('cascad');
            $table->foreign('medical_record_id')->reference('id')->on('medical_records')->onDelete('set null');
        });
    }
    /* Reverse the migration. */
    public function down()
    {
        Schema:dropIfExists('prescription');
    }
}