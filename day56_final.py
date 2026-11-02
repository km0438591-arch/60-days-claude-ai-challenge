import { useState } from 'react';

function App() {
  const [isDemoReady, setIsDemoReady] = useState(true);

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      {/* Header - Portfolio Worthy */}
      <header className="max-w-5xl mx-auto text-center py-10">
        <h1 className="text-4xl font-bold">Your MVP Name</h1>
        <p className="text-gray-600 mt-2">Solving [Problem] in 10 seconds</p>
        <a href="#" className="inline-block mt-4 bg-black text-white px-6 py-2 rounded-full">
          Try Live Demo
        </a>
      </header>

      {/* Core MVP Feature */}
      <main className="max-w-5xl mx-auto bg-white rounded-2xl shadow p-6">
        <h2 className="font-semibold mb-4">Core Working Feature</h2>
        {/* Yaha apna main feature ka code daalo */}
        {isDemoReady ? <div>✅ MVP is Live & Working</div> : <div>Loading...</div>}
      </main>

      {/* For Submission */}
      <footer className="text-center mt-10 text-sm text-gray-400">
        Built for Day 56 Challenge - MVP Demo Ready
      </footer>
    </div>
  )
}
export default App;
