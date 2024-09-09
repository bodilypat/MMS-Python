<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMedicalRecordsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('medical_records', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('patient_id')->constrained()->onDelete('cascade'); // Foreign key to patients table
            $table->foreignId('doctor_id')->constrained()->onDelete('cascade'); // Foreign key to doctors table
            $table->date('record_date'); // Date of the medical record
            $table->text('record_details'); // Details of the medical record
            $table->string('record_type'); // Type of the record (diagnosis, treatment, history)
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
        Schema::dropIfExists('medical_records');
    }
}
