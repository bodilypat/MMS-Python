<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateInsuranceTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('insurance', function (Blueprint $table) {
            $table->id('insurance_id'); // equivalent to 'insurance_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->string('provider_name', 255); // 'provider_name VARCHAR(255) NOT NULL'
            $table->string('policy_number', 50)->unique(); // 'policy_number VARCHAR(50) NOT NULL UNIQUE'
            $table->enum('coverage_type', ['Full', 'Partial'])->default('Partial'); // 'coverage_type ENUM('Full', 'Partial') DEFAULT 'Partial''
            $table->decimal('coverage_amount', 10, 2)->default(0.00); // 'coverage_amount DECIMAL(10, 2) DEFAULT 0.00'
            $table->foreignId('patient_id')->constrained()->onDelete('cascade'); // 'patient_id INT NOT NULL' and 'FOREIGN KEY (patient_id) REFERENCES patients(patient_id)'
            $table->date('start_date'); // 'start_date DATE NOT NULL'
            $table->date('end_date'); // 'end_date DATE NOT NULL'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'

            // Adding a check constraint to ensure start_date <= end_date
            $table->check('start_date <= end_date'); // 'CONSTRAINT chk_dates CHECK (start_date <= end_date)'
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('insurance');
    }
}