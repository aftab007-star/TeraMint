export async function fetchAIHealth() {
  try {
    const res = await fetch("http://127.0.0.1:8000/ai/health");  // 👈 changed
    if (!res.ok) throw new Error("Failed to reach backend");
    return await res.json();
  } catch (err) {
    console.error(err);
    return { ai_layer: "offline" };
  }
}

