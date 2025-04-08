<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateLabTestsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('lab_tests', function (Blueprint $table) {
            $table->id('test_id'); // equivalent to 'test_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->foreignId('patient_id')->constrained('patients')->onDelete('cascade')->onUpdate('cascade'); // 'patient_id INT NOT NULL' and foreign key reference to 'patients'
            $table->foreignId('appointment_id')->constrained('appointments')->onDelete('cascade')->onUpdate('cascade'); // 'appointment_id INT NOT NULL' and foreign key reference to 'appointments'
            $table->string('test_name', 255); // 'test_name VARCHAR(255) NOT NULL'
            $table->date('test_date'); // 'test_date DATE NOT NULL'
            $table->text('results')->nullable(); // 'results TEXT' and nullable
            $table->enum('test_status', ['Pending', 'Completed', 'Failed', 'In Progress'])->default('Pending'); // 'test_status ENUM('Pending', 'Completed', 'Failed', 'In Progress') DEFAULT 'Pending'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'

            // Adding indexes for foreign keys
            $table->index('patient_id');
            $table->index('appointment_id');

            // Adding a unique constraint for (patient_id, appointment_id, test_name)
            $table->unique(['patient_id', 'appointment_id', 'test_name'], 'uc_patient_appointment');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('lab_tests');
    }
}
