<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePaymentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('payments', function (Blueprint $table) {
            $table->id('billing_id'); // equivalent to 'billing_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->foreignId('patient_id')->constrained('patients')->onDelete('cascade')->onUpdate('cascade'); // 'patient_id INT NOT NULL' and foreign key reference to 'patients'
            $table->foreignId('appointment_id')->constrained('appointments')->onDelete('cascade')->onUpdate('cascade'); // 'appointment_id INT NOT NULL' and foreign key reference to 'appointments'
            $table->decimal('total_amount', 10, 2); // 'total_amount DECIMAL(10, 2) NOT NULL'
            $table->decimal('amount_paid', 10, 2)->default(0.00); // 'amount_paid DECIMAL(10, 2) NOT NULL DEFAULT 0.00'
            $table->decimal('balance_due', 10, 2)->default(0.00); // 'balance_due DECIMAL(10, 2) NOT NULL DEFAULT 0.00'
            $table->enum('payment_status', ['Paid', 'Pending', 'Partially Paid'])->default('Pending'); // 'payment_status ENUM('Paid', 'Pending', 'Partially Paid') DEFAULT 'Pending' NOT NULL'
            $table->timestamp('payment_date')->useCurrent(); // 'payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL'
            $table->decimal('insurance_claimed_amount', 10, 2)->nullable(); // 'insurance_claimed_amount DECIMAL(10, 2) DEFAULT NULL'
            $table->enum('insurance_status', ['Approved', 'Pending', 'Denied'])->nullable(); // 'insurance_status ENUM('Approved', 'Pending', 'Denied') DEFAULT NULL'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'

            // Adding Indexes
            $table->index('patient_id');
            $table->index('appointment_id');
            $table->index('payment_date');

            // Adding a unique constraint for (patient_id, appointment_id)
            $table->unique(['patient_id', 'appointment_id'], 'uc_patient_appointment');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('payments');
    }
}