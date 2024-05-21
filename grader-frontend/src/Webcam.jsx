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
        () => {
            const image = webcamRef.current.getScreenshot();
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
        />
        <button onClick={capture}>Take photo</button>
    </>  
    );
     
}

export default WebcamComp;