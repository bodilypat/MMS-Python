<?php

use Illuminate\Database\Migrations\Migration;
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
            $table->id('prescription_id'); // equivalent to 'prescription_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->foreignId('record_id')->constrained('medical_records')->onDelete('cascade')->onUpdate('cascade'); // 'record_id INT NOT NULL' and foreign key reference to 'medical_records'
            $table->string('medication_name', 255); // 'medication_name VARCHAR(255) NOT NULL'
            $table->string('dosage', 50); // 'dosage VARCHAR(50) NOT NULL'
            $table->string('frequency', 50); // 'frequency VARCHAR(50) NOT NULL'
            $table->date('start_date'); // 'start_date DATE NOT NULL'
            $table->date('end_date')->nullable(); // 'end_date DATE' and nullable
            $table->text('instructions')->nullable(); // 'instructions TEXT' and nullable
            $table->enum('status', ['Active', 'Completed', 'Expired', 'Cancelled'])->default('Active'); // 'status ENUM('Active', 'Completed', 'Expired', 'Cancelled') DEFAULT 'Active'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
            $table->integer('created_by')->nullable(); // 'created_by INT'
            $table->integer('updated_by')->nullable(); // 'updated_by INT'

            // Adding Indexes
            $table->index('record_id');
            $table->index('medication_name');

            // Adding check constraint for dosage length
            $table->check('CHAR_LENGTH(dosage) <= 50');
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