//Define the structure of the response from the chat API
type ChatResponse = {
  reply: Record<string, unknown>;
};

//Function to send a message to the chat API and receive a response
export async function getChatResponse(message: string): Promise<string> {
  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error("The backend request failed.");
  }

  const data: ChatResponse = await response.json();

  return JSON.stringify(data.reply, null, 2);
}
