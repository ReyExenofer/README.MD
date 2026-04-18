// src/App.js
import ChatPanel from "./components/ChatPanel";
import SummaryPanel from "./components/SummaryPanel";

function App() {
  return <h1>Hello React 🚀</h1>;
}

export default App;
  return (
    <div style={{ display: "flex", height: "100vh", fontFamily: "Inter" }}>
      <div style={{ width: "50%" }}>
        <SummaryPanel />
      </div>
      <div style={{ width: "50%", borderLeft: "1px solid #ccc" }}>
        <ChatPanel />
      </div>
    </div>
  );
