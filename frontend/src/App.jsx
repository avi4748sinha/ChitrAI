import { useState } from "react";

function App() {
  // User ka prompt store karta hai
  const [prompt, setPrompt] = useState("");

  // Backend se aane wali generated image
  const [image, setImage] = useState(null);

  // Image generate ho rahi hai ya nahi
  const [loading, setLoading] = useState(false);

  // Agar API error aaye to yahan store hoga
  const [error, setError] = useState("");

  // Generate button click hone par API call hogi
  const generateImage = async () => {
    setLoading(true);
    setError("");

    try {
      // FastAPI backend ko prompt bhej rahe hain
      const response = await fetch(
        "http://127.0.0.1:8000/generate-image",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: prompt,
          }),
        }
      );

      // Backend error check
      if (!response.ok) {
        throw new Error("Image generation failed");
      }

      // Backend ka JSON response
      const data = await response.json();

      // Base64 ko browser ke image URL mein convert kar rahe hain
      setImage(
        `data:${data.mime_type};base64,${data.image_base64}`
      );

    } catch (err) {
      setError(err.message);
    } finally {
      // API call complete hone ke baad loading false
      setLoading(false);
    }
  };

const downloadImage = () => {
  if (!image) return;

  const link = document.createElement("a");
  link.href = image;
  link.download = "chitrai-image.png";

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};




  return (
    <div className="app">

      {/* Header */}
      <header className="header">

        {/* Existing ChitrAI logo */}
        <img
          src="/chitrai-logo.png"
          alt="ChitrAI Logo"
          className="logo"
        />

        <p>Generative AI Image Studio</p>
      </header>


      <main className="container">

        {/* Prompt section */}
        <section className="generator">

          <h2>Create an Image</h2>

          {/* User yahan image ka description likhega */}
          <textarea
            placeholder="Describe the image you want to generate..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />

          {/* Button API call start karega */}
          <button
            onClick={generateImage}
            disabled={!prompt.trim() || loading}
          >
            {loading ? "Generating..." : "Generate Image"}
          </button>

        </section>


        {/* Generated image section */}
        <section className="preview">

          <h2>Generated Image</h2>

          <div className="image-box">

            {/* Image generate ho rahi hai */}
            {/* Generated image + Download button */}
{!loading && !error && image && (
  <>
    <img
      src={image}
      alt="AI Generated"
    />

    <button
      type="button"
      onClick={downloadImage}
      className="download-button"
    >
      Download Image
    </button>
  </>
)}
            

            {/* Starting state */}
            {!loading && !error && !image && (
              <p>Your generated image will appear here</p>
            )}

          </div>
          
          

        </section>
        

      </main>
    </div>
  );
}

export default App;