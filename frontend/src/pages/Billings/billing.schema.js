//src/pages/Billings/billing.schema.js 

import { Datatypes } from 'sequelize';
import sequelize from '../../config/database.js';
import Patient from '../Patients/patient.schema.js';
import Doctor from '../Doctors/doctor.schema.js';

const Billing = sequelize.define('Billing', {   
    billing_id: {
        type: Datatypes.INTEGER.UNSIGNED,
        autoIncrement: true,
        primaryKey: true
    },                  
    patient_id: {
        type: Datatypes.INTEGER.UNSIGNED,
        allowNull: false,
        references: {
            model: Patient,
            key: 'patient_id'
        }
    },
    doctor_id: {
        type: Datatypes.INTEGER.UNSIGNED,
        allowNull: false,
        references: {
            model: Doctor,
            key: 'doctor_id'
        }
    },      
    amount: {
        type: Datatypes.DECIMAL(10, 2),
        allowNull: false
    },  
    billing_date: {
        type: Datatypes.DATE,
        allowNull: false,
        defaultValue: Datatypes.NOW
    }   
}, {
    tableName: 'billings',
    timestamps: false
});         
