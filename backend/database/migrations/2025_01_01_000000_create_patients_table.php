<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePatientsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('patients', function (Blueprint $table) {
            $table->id('patient_id'); // equivalent to 'patient_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->string('first_name', 100); // 'first_name VARCHAR(100) NOT NULL'
            $table->string('last_name', 100); // 'last_name VARCHAR(100) NOT NULL'
            $table->date('date_of_birth'); // 'date_of_birth DATE NOT NULL'
            $table->enum('gender', ['male', 'female', 'other']); // 'gender ENUM('male', 'female', 'other') NOT NULL'
            $table->string('email', 100)->unique()->nullable(); // 'email VARCHAR(100) UNIQUE'
            $table->string('phone_number', 20)->unique(); // 'phone_number VARCHAR(20) UNIQUE NOT NULL'
            $table->string('address', 255)->nullable(); // 'address VARCHAR(255)'
            $table->string('insurance_provider', 100)->nullable(); // 'insurance_provider VARCHAR(100)'
            $table->string('insurance_policy_number', 100)->nullable(); // 'insurance_policy_number VARCHAR(100)'
            $table->string('primary_care_physician', 100)->nullable(); // 'primary_care_physician VARCHAR(100)'
            $table->text('medical_history')->nullable(); // 'medical_history TEXT'
            $table->text('allergies')->nullable(); // 'allergies TEXT'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' & 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
            $table->enum('status', ['active', 'inactive', 'deceased'])->default('active'); // 'status ENUM('active', 'inactive', 'deceased') DEFAULT 'active'
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('patients');
    }
}