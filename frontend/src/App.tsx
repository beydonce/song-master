import { useEffect, useState } from "react";

interface ApiData {
  Name: string;
  Age: number;
  Date: string;
  Programming: string;
}

function App() {
  const [data, setData] = useState<ApiData | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/data")
      .then(res => res.json())
      .then((json: ApiData) => setData(json))
      .catch(console.error);
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>{data.Name}</h1>
      <p>Age: {data.Age}</p>
      <p>Date: {data.Date}</p>
      <p>Programming: {data.Programming}</p>
    </div>
  );
}

export default App;
