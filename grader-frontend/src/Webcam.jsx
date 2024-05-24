import React, { useRef, useState } from "react"
import Webcam from "react-webcam"
import ProcessedImage from "./ProcessedImage.jsx"

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: 'environment'
};

const WebcamComp = (/*props */) => {
    
    const webcamRef = useRef(null);
    const [imageSrc, setImageSrc] = useState('');

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
        
                    const processedImage = await response.blob();
                    const imageUrl = URL.createObjectURL(processedImage);
                    setImageSrc(imageUrl);
                }
            }
        },
        [webcamRef]
    );
    return (
    <>
        <h1>Kumon homework grader</h1>
        <Webcam
        audio={false}
        height={720}
        screenshotFormat="image/jpeg"
        width={1280}
        videoConstraints={videoConstraints}
        ref={webcamRef}
        />
        <button onClick={capture}>Take photo</button>
        {imageSrc && <ProcessedImage imageSrc={imageSrc}/>}
    </>  
    );
     
}

export default WebcamComp;