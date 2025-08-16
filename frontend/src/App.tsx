
import { useState } from "react";
import Register from "./components/Register";

function App() {
  const [page, setPage] = useState<"home" | "register">("home");

  return (
    <div>
      {page === "home" && (
        <div>
          <h1>Welcome</h1>
          <button onClick={() => setPage("register")}>go to register</button>
        </div>
      )}

      {page === "register" && <Register/>}
    </div>
  )
}

export default App;
