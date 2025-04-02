import React, { useState, useEffect } from "react";

function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // Check if form is valid (both fields have content)
  const isFormValid = title.trim() !== "" && content.trim() !== "";

  // ... rest of your fetch notes and useEffect code ...

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isFormValid) return; // Extra validation check

    setError("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:5001/api/notes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, content }),
      });

      if (!response.ok) throw new Error("Failed to add note");

      const newNote = await response.json();
      setNotes([...notes, newNote]);
      setTitle("");
      setContent("");
    } catch (err) {
      setError("Failed to add note. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Notes App</h1>

      {error && (
        <div className="error-message">
          {error}
          <button onClick={() => setError("")}>✕</button>
        </div>
      )}

      <form onSubmit={handleSubmit} className="note-form">
        <input
          type="text"
          placeholder="Note Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea
          placeholder="Note Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
        <button
          type="submit"
          disabled={loading || !isFormValid}
          style={{
            backgroundColor: !isFormValid
              ? "#ccc"
              : loading
              ? "#666"
              : "#007bff",
            cursor: !isFormValid ? "not-allowed" : loading ? "wait" : "pointer",
          }}
        >
          {loading ? "Adding..." : "Add Note"}
        </button>
      </form>

      {/* ... rest of your notes list code ... */}
    </div>
  );
}

export default App;
