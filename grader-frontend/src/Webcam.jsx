import React, { useRef, useState } from "react";
import Webcam from "react-webcam";

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: 'environment'
};

const WebcamComp = () => {
  const webcamRef = useRef(null);
  const [extractedText, setExtractedText] = useState('');

  const capture = React.useCallback(
    async () => {
      if (webcamRef.current) {
        const imageSrc = webcamRef.current.getScreenshot();

        if (imageSrc) {
          const convertedImage = await fetch(imageSrc).then((res) => res.blob());
          const formData = new FormData();
          formData.append('image', convertedImage, 'captured.jpg');

          const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            body: formData
          });

          if (response.ok) {
            const data = await response.json();
            setExtractedText(data.extracted_text);
          } else {
            console.error('Error in response:', response.statusText);
          }
        }
      }
    },
    [webcamRef]
  );

  return (
    <>
      <h1>Kumon Homework Grader</h1>
      <Webcam
        audio={false}
        height={720}
        screenshotFormat="image/jpeg"
        width={1280}
        videoConstraints={videoConstraints}
        ref={webcamRef}
      />
      <button onClick={capture}>Take Photo</button>
      {extractedText && (
        <div>
          <h2>Extracted Text:</h2>
          <pre>{extractedText}</pre>
        </div>
      )}
    </>
  );
}

export default WebcamComp;