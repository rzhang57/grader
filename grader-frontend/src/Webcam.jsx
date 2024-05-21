import React, { useRef } from "react"
import Webcam from "react-webcam"

const videoConstraints = {
    width: 1280,
    height: 720,
    facingMode: 'environment'
};

const WebcamComp = (/*props */) => {
    const webcamRef = useRef(null);
    const capture = React.useCallback(
        async () => {
            const image = webcamRef.current.getScreenshot();

            const convertedImage = await fetch(image).then((res) => res.blob());

            await fetch('http://localhost:5000/analyze', {
                method: 'POST',
                body: convertedImage
            });
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
    </>  
    );
     
}

export default WebcamComp;