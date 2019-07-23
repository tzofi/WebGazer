(function(window) {
    'use strict';

    window.webgazer = window.webgazer || {};
    webgazer.tracker = webgazer.tracker || {};
    webgazer.util = webgazer.util || {};
    webgazer.params = webgazer.params || {};

    /**
     * Constructor of Face-API.JS, Tiny YOLO Detector
     * Initialize detector with pre-trained weights.
     * @constructor
     */
    var TinyYolo = function() {
        //changeFaceDetector(TINY_FACE_DETECTOR); //SSD_MOBILENETV1);
        //faceapi.loadFaceLandmarkModel('../dependencies/faceapi-js');
        //faceapi.loadFaceLandmarkModel('/');
        loadModel();
        this.options = getFaceDetectorOptions();
        console.log(this.options);
        this.options._scoreThreshold = 0.25;
        //this.options.scoreThreshold = 0.25;
    };

    webgazer.tracker.TinyYolo = TinyYolo;

    /**
     *
     * @returns {Promise<any>}
     * */
    async function loadModel() {
        changeFaceDetector(TINY_FACE_DETECTOR); //SSD_MOBILENETV1);
        await faceapi.loadFaceLandmarkModel('/');
    }

    /**
     * Isolates the two patches that correspond to the user's eyes
     * @param  {Canvas} imageCanvas - canvas corresponding to the webcam stream
     * @param  {Number} width - of imageCanvas
     * @param  {Number} height - of imageCanvas
     * @return {Object} the two eye-patches, first left, then right eye
     */
    TinyYolo.prototype.getEyePatches = async function(imageCanvas, width, height) {
        //changeFaceDetector(TINY_FACE_DETECTOR); //SSD_MOBILENETV1);
        //await faceapi.loadFaceLandmarkModel('/');
        var workingImage = imageCanvas.getContext('2d').getImageData(0,0,width,height);
        var detection = await faceapi.detectAllFaces(imageCanvas, this.options).withFaceLandmarks();
        if(detection === undefined || detection.length == 0){
            return null;
        }
        //console.log(detection);
        var positions = detection[0].landmarks.positions;
        //console.log(positions);

        var leftEye = positions.slice(36,42);
        var rightEye = positions.slice(42,48);
        var allLeftX = [leftEye[0]._x, leftEye[1]._x, leftEye[2]._x,
                    leftEye[3]._x, leftEye[4]._x, leftEye[5]._x];
        var allLeftY = [leftEye[0]._y, leftEye[1]._y, leftEye[2]._y,
                    leftEye[3]._y, leftEye[4]._y, leftEye[5]._y];
        var allRightX = [rightEye[0]._x, rightEye[1]._x, rightEye[2]._x,
                     rightEye[3]._x, rightEye[4]._x, rightEye[5]._x];
        var allRightY = [rightEye[0]._y, rightEye[1]._y, rightEye[2]._y,
		     rightEye[3]._y, rightEye[4]._y, rightEye[5]._y];
        //console.log(allLeftX);
        //console.log(allLeftY);
        //console.log(allRightX);
        //console.log(allRightY);

        var leftOriginX = Math.round(Math.min(...allLeftX));
        var leftOriginY = Math.round(Math.min(...allLeftY));
        var leftWidth = Math.round(Math.max(...allLeftX) - leftOriginX);
        var leftHeight = Math.round(Math.max(...allLeftY) - leftOriginY);
        //console.log(leftOriginX);
        //console.log(leftOriginY);
        //console.log(leftWidth);
        //console.log(leftHeight);


        var rightOriginX = Math.round(Math.min(...allRightX));
        var rightOriginY = Math.round(Math.min(...allRightY));
        var rightWidth = Math.round(Math.max(...allRightX) - rightOriginX);
        var rightHeight = Math.round(Math.max(...allRightY) - rightOriginY);

        var eyeObjs = {};
        eyeObjs.positions = positions;

        //console.log([leftOriginX, leftOriginY, leftWidth, leftHeight]);
        var leftImageData = imageCanvas.getContext('2d').getImageData(leftOriginX, leftOriginY, leftWidth, leftHeight);
        eyeObjs.left = {
            patch: leftImageData,
            imagex: leftOriginX,
            imagey: leftOriginY,
            width: leftWidth,
            height: leftHeight
        };

        var rightImageData = imageCanvas.getContext('2d').getImageData(rightOriginX, rightOriginY, rightWidth, rightHeight);
        eyeObjs.right = {
            patch: rightImageData,
            imagex: rightOriginX,
            imagey: rightOriginY,
            width: rightWidth,
            height: rightHeight
        };
        
        //console.log(eyeObjs);
        return eyeObjs;
    }

    /**
     * Reset the tracker to default values
     */
    TinyYolo.prototype.reset = function(){
        console.log('To be implemented...')
    }

    /**
     * The tiny yolo object name
     * @type {string}
     */
    TinyYolo.prototype.name = 'tinyyolo';

}(window));
