export async function getChatResponse(message: string): Promise<string> {
  // Simulate a small network delay.
  await new Promise((resolve) => setTimeout(resolve, 500));

  if (message.includes("SN-TEST-0001")) {
    return (
      "This is a mock response for SN-TEST-0001. " +
      "When the backend is connected, I will retrieve " +
      "the actual erasure record."
    );
  }

  if (message.toLowerCase().includes("failed")) {
    return (
      "This is a mock response about failed erasures. " +
      "The real backend will calculate the actual count."
    );
  }

  return (
    "I received your question: " +
    message +
    ". The real AI assistant will be connected later."
  );
}
