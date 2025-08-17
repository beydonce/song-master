import React, { useState } from "react";


function Register() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("")

    const handleRegister = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            const res = await fetch("http://localhost:5000/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify( {username, password}),
            });
            const data = await res.json();
            setMessage(data.message);
        }catch(err) {
            console.log(err);
            setMessage("something went wrong");
        }
    };

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            const res = await fetch("http://localhost:5000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify( {username, password}),
            });

            const data = await res.json();
            setMessage(data.message);

        }catch(err) {
            console.log(err);
            setMessage("something went wrong")
        }
    };
    


    return (
        <div>
            <h1>Auth Page</h1>
            <form>
                <input 
                    type="text"
                    placeholder="enter usernmae"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)} 
                />

                <input 
                    type="password"
                    placeholder="enter password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <div>
                    <button onClick={handleRegister}>Register</button>
                    <button onClick={handleLogin}>Login</button>
                </div>
            </form>
            {message && <p>{message}</p>}
        </div>
    )
}

export default Register