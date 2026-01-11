//src/pages/patient/Profile.jsx 

import { useEffect, useState } from "react";

export default function PatientProfile() {
    const [profile, setProfile] = useState({});
    
    useEffect(() => {
        api.get('/api/patient/profile').then(res => setProfile(res.data));
    }, []);

    return (
        <div className="container">
            <h1>Patient Profile</h1>
            <p>Name: {profile.name}</p>
            <p>Email: {profile.email}</p>
            <p>Phone: {profile.phone}</p>
        </div>
    )
}

