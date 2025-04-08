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
            $table->id('record_id'); // equivalent to 'record_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->foreignId('patient_id')->constrained('patients')->onDelete('cascade')->onUpdate('cascade'); // 'patient_id INT NOT NULL' and foreign key reference to 'patients'
            $table->foreignId('appointment_id')->constrained('appointments')->onDelete('cascade')->onUpdate('cascade'); // 'appointment_id INT NOT NULL' and foreign key reference to 'appointments'
            $table->string('diagnosis', 500)->nullable(); // 'diagnosis VARCHAR(500)'
            $table->text('treatment_plan')->nullable(); // 'treatment_plan TEXT'
            $table->text('note')->nullable(); // 'note TEXT'
            $table->enum('status', ['Active', 'Archived', 'Inactive'])->default('Active'); // 'status ENUM('Active', 'Archived', 'Inactive') DEFAULT 'Active'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
            $table->integer('created_by')->nullable(); // 'created_by INT'
            $table->integer('updated_by')->nullable(); // 'updated_by INT'
            $table->string('attachments', 255)->nullable(); // 'attachments VARCHAR(255)'

            // Adding Indexes
            $table->index('patient_id');
            $table->index('appointment_id');

            // Adding check constraint for diagnosis length
            $table->check('CHAR_LENGTH(diagnosis) <= 500');
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