<?php

wuse Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePrescriptionsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('prescriptions', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->foreignId('patient_id')->constrained()->onDelete('cascade'); // Foreign key to patients table
            $table->foreignId('doctor_id')->constrained()->onDelete('cascade'); // Foreign key to doctors table
            $table->string('medication_name'); // Name of the medication
            $table->text('dosage_instructions'); // Dosage instructions
            $table->date('prescription_date'); // Date the prescription was made
            $table->date('expiry_date')->nullable(); // Expiry date of the prescription (nullable)
            $table->text('notes')->nullable(); // Additional notes about the prescription
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
        Schema::dropIfExists('prescriptions');
    }
}
