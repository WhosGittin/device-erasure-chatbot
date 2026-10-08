import { useState } from "react";
import "./App.css";

type Message = {
  id: number;
  role: "user" | "assistant";
  content: string;
};

const examplePrompts = [
  "How many erasures failed?",
  "Why did SN-TEST-0001 fail?",
  "Show Northwind devices erased in March.",
];

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  function sendMessage(text: string) {
    const trimmedText = text.trim();

    if (!trimmedText) {
      return;
    }

    const userMessage: Message = {
      id: Date.now(),
      role: "user",
      content: trimmedText,
    };

    const assistantMessage: Message = {
      id: Date.now() + 1,
      role: "assistant",
      content:
        "This is a placeholder response. Once we connect the backend, I will be able to look up device erasure records.",
    };

    setMessages((previous) => [...previous, userMessage, assistantMessage]);

    setInput("");
  }

  return (
    <main className="app">
      <header className="header">
        <div>
          <h1>Erasure Assistant</h1>
        </div>
        <span className="status">Local demo</span>
      </header>

      <section className="chat">
        {messages.length === 0 ? (
          <div className="welcome">
            <div className="welcome-icon">✦</div>
            <h2>How can I help you today?</h2>
            <p>
              Ask questions about device erasure records. Choose an example to
              get started.
            </p>

            <div className="prompts">
              {examplePrompts.map((prompt) => (
                <button
                  className="prompt"
                  key={prompt}
                  onClick={() => sendMessage(prompt)}
                >
                  {prompt}
                  <span>↗</span>
                </button>
              ))}
            </div>
          </div>
        ) : (
          <div className="messages" aria-live="polite">
            {messages.map((message) => (
              <div key={message.id} className={`message ${message.role}`}>
                <span className="message-label">
                  {message.role === "user" ? "You" : "Assistant"}
                </span>
                <p>{message.content}</p>
              </div>
            ))}
          </div>
        )}
      </section>

      <form
        className="composer"
        onSubmit={(event) => {
          event.preventDefault();
          sendMessage(input);
        }}
      >
        <label className="visually-hidden" htmlFor="chat-input">
          Your message
        </label>
        <input
          id="chat-input"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="Ask about erasure records..."
        />
        <button type="submit" disabled={!input.trim()}>
          Send ↑
        </button>
      </form>

      <footer className="footer">
        Demo mode · Responses are not connected to real records
      </footer>
    </main>
  );
}

export default App;
