// src/components/SummaryPanel.jsx
import { useSelector } from "react-redux";

export default function SummaryPanel() {
  const interaction = useSelector((state) => state.interaction);

  return (
    <div style={{ padding: "16px", background: "#f4f4f4", height: "100%" }}>
      <h3>Interaction Summary</h3>
      <p><strong>HCP:</strong> {interaction.hcp_name}</p>
      <p><strong>Date:</strong> {interaction.date}</p>
      <p><strong>Time:</strong> {interaction.time}</p>
      <p><strong>Attendees:</strong> {interaction.attendees.join(", ")}</p>
      <p><strong>Topics:</strong> {interaction.topics.join(", ")}</p>
      <p><strong>Summary:</strong> {interaction.summary}</p>
    </div>
  );
}
