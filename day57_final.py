// PolishedMVP.jsx - Day 57 Final
import { useState, useEffect } from 'react';

export default function PolishedMVP() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1200); // Simulate load
  }, []);

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center bg-white">
        <div className="animate-pulse text-center">
          <div className="w-12 h-12 border-4 border-black border-t-transparent rounded-full animate-spin mx-auto"></div>
          <p className="mt-4 text-sm">Polishing your experience...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#fafafa] text-black font-sans">
      {/* NAV */}
      <nav className="flex justify-between items-center max-w-6xl mx-auto p-6">
        <h1 className="font-bold text-xl">YourBrand.</h1>
        <button className="bg-black text-white px-5 py-2 rounded-full text-sm">Live Demo</button>
      </nav>

      {/* HERO - Portfolio Worthy */}
      <section className="max-w-6xl mx-auto text-center py-20 px-6">
        <span className="bg-white border px-3 py-1 rounded-full text-xs">✨ Day 57 - Portfolio Ready</span>
        <h2 className="text-5xl font-bold mt-6 leading-tight">We built the MVP.<br/>Now it shines.</h2>
        <p className="text-gray-500 mt-4 max-w-xl mx-auto">From functional to phenomenal. Refined UX, smooth animations, and production-grade UI.</p>
      </section>

      {/* CORE FEATURE CARD */}
      <section className="max-w-4xl mx-auto bg-white rounded-[24px] shadow-sm border p-8 mx-4">
        <div className="flex justify-between items-center">
          <h3 className="font-semibold">Core MVP Feature - Working</h3>
          <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
        </div>
        <div className="mt-6 h-48 bg-gray-50 rounded-xl flex items-center justify-center border border-dashed">
          {/* Yaha tumhara actual MVP feature aayega */}
          <p className="text-gray-400">Your Working Product UI Here</p>
        </div>
        <div className="mt-6 flex gap-3">
          <button className="flex-1 bg-black text-white py-3 rounded-xl">Try Now</button>
          <button className="flex-1 bg-gray-100 py-3 rounded-xl">View Code</button>
        </div>
      </section>

      {/* FOOTER */}
      <p className="text-center text-xs text-gray-400 py-10">Built with ❤️ for Day 57 Challenge | Portfolio Ready</p>
    </div>
  );
}
