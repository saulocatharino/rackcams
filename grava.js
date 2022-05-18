	var anc = document.querySelector(".download-anc")

	var data = [];
	  
	// In order record the screen with system audio
	var recording = navigator.mediaDevices.getDisplayMedia({
	    video: {
		mediaSource: 'screen',
	    },
	    audio: true,
	})

	    .then(async (e) => {

		// For recording the mic audio
		let audio = await navigator.mediaDevices.getUserMedia({ 
		    audio: true, video: false })


	  
		// Combine both video/audio stream with MediaStream object
		let combine = new MediaStream(
		    [...e.getTracks(), ...audio.getTracks()])

		/* Record the captured mediastream
		   with MediaRecorder constructor */
		let recorder = new MediaRecorder(combine);
	  
		recorder.start();


		data = []

		recorder.ondataavailable = (e) => {
			data.push(e.data);
		};
		alert("recording started")
	    });
