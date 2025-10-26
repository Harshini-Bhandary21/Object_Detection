import { useState } from "react";

function App() {
  const [response, setResponse] = useState("");

  const handleLiveClick = async () => {
    try {
      const res = await fetch("http://localhost:5000/live");
      const data = await res.json();
      setResponse(data.message);
    } catch (error) {
      console.error("Error connecting to backend:", error);
      setResponse("Error connecting to backend");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🎥 Object Detection Dashboard</h1>
      <button
        onClick={handleLiveClick}
        style={{
          padding: "10px 20px",
          backgroundColor: "#007bff",
          color: "white",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          fontSize: "16px",
        }}
      >
        Go Live
      </button>
      <p style={{ marginTop: "20px" }}>{response}</p>
    </div>
  );
}

export default App;
