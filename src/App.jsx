import { useState } from "react";
import axios from "axios";
import "./App.css"; // Import CSS file

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleSubmit = async () => {
    if (!file) {
      alert("Please upload an MRI image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/predict", formData);
      setResult(response.data.result);
    } catch (error) {
      alert("Error processing the image.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">TumorCheck</h1>

      <div className="upload-box">
        <label className="upload-label">
          <input type="file" accept="image/*" onChange={handleFileChange} className="file-input" />
          <p className="upload-text">
            Drag & drop an image or <span className="browse-text">browse</span>
          </p>
        </label>

        {preview && (
          <img
            src={preview}
            alt="Uploaded MRI"
            className={`preview-image ${
              result === "No Tumor" ? "border-green" : result === "Have Tumor" ? "border-red" : ""
            }`}
          />
        )}

        <button onClick={handleSubmit} className="upload-button">
          {loading ? "Processing..." : "Check Tumor"}
        </button>

        {result && <div className="result-box"> {result}</div>}
      </div>
    </div>
  );
}

export default App;
