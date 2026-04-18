// src/components/ChatPanel.jsx
import { useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { updateInteraction } from "../features/interaction/interactionSlice";

export default function ChatPanel() {
  const [message, setMessage] = useState("");
  const dispatch = useDispatch();

  const sendMessage = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat", {
      message,
    });
    dispatch(updateInteraction(res.data));
    setMessage("");
  };

  return (
    <div style={{ padding: "16px" }}>
      <h3>AI Assistant</h3>
      <textarea
        rows="4"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Describe your interaction..."
        style={{ width: "100%" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
