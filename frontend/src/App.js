import React, { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [probability, setProbability] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isOpened, setIsOpened] = useState(true);
  const handleInputChange = (event) => {
    setText(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    const response = await axios.post("http://localhost:8000/predict", { 'text' : text });
    setResult(response.data.result);
    setProbability(response.data.probability);
    setIsLoading(false); 
  };

  return (
    <div className="App">
      <h1>Text Polarity Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="text">Enter text:</label>
        <input
          type="text"
          id="text"
          name="text"
          required
          value={text}
          onChange={handleInputChange}
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Analyzing..." : "Analyze"}
        </button>
      </form>
      {result && (
        <div className="result">
          The polarity of the text is {result} with a probability of{" "}
          {probability ? `${probability.toFixed(2)}` : ""}.
          <div className={probability && result === "Positive" ? "positive" : "negative"}>
            {probability && (
              <>
                <p>{`${(probability * 100).toFixed(2)}%`}</p>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
