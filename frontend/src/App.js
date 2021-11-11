import React, { useState } from "react";
import HomePage from "./components/HomePage";
import ResultPage from "./components/ResultPage";

function App() {
  const [result, setResult] = useState(null);
  return (
    <div>
      {result === null ? (
        <HomePage setResult={setResult} />
      ) : (
        <ResultPage result={result} setResult={setResult} />
      )}
    </div>
  );
}

export default App;
