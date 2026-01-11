//src/pages/admin/Messages.jsx

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Messages() {
    const [msgs, setMsgs] = useState([]);

    useEffect(() => {
        api.get("/admin/messages").then(res => setMsgs(res.data));
    }, []);

    return (
        <div className="container">
            <h3>Contact Messages</h3>

            <table className="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Message</th>
                    </tr>
                </thead>
                <tbody>
                    {msgs.map(msg => (
                        <tr key={msg.id}>
                            <td>{msg.name}</td>
                            <td>{msg.email}</td>
                            <td>{msg.message}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
