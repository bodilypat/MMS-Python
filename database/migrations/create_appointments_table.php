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
            $table->id('appointment_id'); // equivalent to 'appointment_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->foreignId('patient_id')->constrained('patients')->onDelete('cascade')->onUpdate('cascade'); // 'patient_id INT NOT NULL' and foreign key reference to 'patients'
            $table->foreignId('doctor_id')->constrained('doctors')->onDelete('cascade')->onUpdate('cascade'); // 'doctor_id INT NOT NULL' and foreign key reference to 'doctors'
            $table->dateTime('appointment_date'); // 'appointment_date DATETIME NOT NULL'
            $table->string('reason_for_visit', 255)->nullable(); // 'reason_for_visit VARCHAR(255)'
            $table->enum('status', ['Scheduled', 'Completed', 'Cancelled', 'No-Show'])->default('Scheduled'); // 'status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-Show') DEFAULT 'Scheduled'
            $table->integer('duration')->nullable(); // 'duration INT'
            $table->string('appointment_type', 100)->nullable(); // 'appointment_type VARCHAR(100)'
            $table->text('notes')->nullable(); // 'notes TEXT'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'

            // Adding Indexes
            $table->index('patient_id');
            $table->index('doctor_id');

            // Adding check constraint (to ensure appointment_date is not in the past)
            $table->check('appointment_date >= CURRENT_TIMESTAMP');
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