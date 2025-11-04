"use client";

import { useEffect, useState } from "react";
import { fetchAIHealth } from "../lib/api";

export default function Home() {
  const [aiStatus, setAiStatus] = useState<any>(null);

  useEffect(() => {
    fetchAIHealth().then(setAiStatus);
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-black text-white">
      <h1 className="text-3xl font-bold mb-6">TeraMint Dashboard</h1>

      {aiStatus ? (
        <div className="p-6 bg-gray-900 rounded-xl shadow-lg min-w-[320px] text-center">
          <p className="text-lg mb-2">
            <span className="font-semibold">AI Layer:</span>{" "}
            {aiStatus.ai_layer}
          </p>
          <p>
            <span className="font-semibold">Bots:</span>{" "}
            {aiStatus.bots_available?.join(", ") || "None"}
          </p>
          <p className="text-xs text-gray-400 mt-3">
            {aiStatus.timestamp}
          </p>
        </div>
      ) : (
        <p>Connecting to AI backend...</p>
      )}
    </main>
  );
}


