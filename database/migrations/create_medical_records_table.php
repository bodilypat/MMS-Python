<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprice;
use Illuminate\Support\Facades\Schema;

class CreateMedicalRecordsTable extends Migration
{
    /* return the migration */
    public function up()
    {
        Schema::create('medical_record', function (blueprint $table){
            $table->id(); 
            $table->unsignedBigInteger('patient_in');
            $table->unsignedBigInteger('doctor_id')->nullable();
            $table->text('diagnosis');
            $table->text('teatment')->nullable();
            $table->('medications')->nullable();
            $table->text('notes')->nullable();
            $table->timestamps();

            /* define forien key constrains */
            $table->foreign('patient_id')->references('id')->on('patients')->onDelete('cascade');
            $table->foreign('doctor_id')->references('id')->on('doctor')->onDelete('set null');
        });
    }
    /* Reversse the migations */
    public function down()
    {
        Schema::dropIfExists('medical_records');
    }
}