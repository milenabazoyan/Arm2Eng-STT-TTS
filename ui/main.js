let recorder;
let stream;
let timerInterval;
let audioContext;
let analyser;
let dataArray;
let animationId;

const MAX_RECORD_TIME = 30;

const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const timerDisplay = document.getElementById('timer');
const audioPlayer = document.getElementById('responseAudio');
const modelSelect = document.getElementById('modelSelect');
const canvas = document.getElementById('waveform');
const canvasCtx = canvas.getContext('2d');
const loadingInline = document.getElementById('loadingInline');

const speakerSelector = document.getElementById('speakerSelector');
const femaleBtn = document.getElementById('femaleBtn');
const maleBtn = document.getElementById('maleBtn');
let selectedGender = 'female';

modelSelect.addEventListener('change', () => {
  const selectedModel = modelSelect.value;
  if (selectedModel === 'bark') {
    speakerSelector.style.display = 'block';
    femaleBtn.classList.add('active');
    maleBtn.classList.remove('active');
    selectedGender = 'female';
  } else {
    speakerSelector.style.display = 'none';
    selectedGender = '';
  }
});

femaleBtn.addEventListener('click', () => {
  selectedGender = 'female';
  femaleBtn.classList.add('active');
  maleBtn.classList.remove('active');
});

maleBtn.addEventListener('click', () => {
  selectedGender = 'male';
  maleBtn.classList.add('active');
  femaleBtn.classList.remove('active');
});

startBtn.addEventListener('click', async () => {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    canvas.style.display = 'block';
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const source = audioContext.createMediaStreamSource(stream);
    analyser = audioContext.createAnalyser();
    analyser.fftSize = 2048;
    const bufferLength = analyser.fftSize;
    dataArray = new Uint8Array(bufferLength);
    source.connect(analyser);
    drawWaveform();

    recorder = RecordRTC(stream, {
      type: 'audio',
      mimeType: 'audio/wav',
      recorderType: StereoAudioRecorder,
      desiredSampRate: 16000,
      numberOfAudioChannels: 1
    });

    recorder.startRecording();

    startBtn.disabled = true;
    stopBtn.disabled = false;
    timerDisplay.style.display = 'block';

    let timeLeft = MAX_RECORD_TIME;
    timerDisplay.textContent = `${timeLeft}s`;

    timerInterval = setInterval(() => {
      timeLeft--;
      timerDisplay.textContent = `${timeLeft}s`;
      if (timeLeft <= 0) {
        stopRecordingAndSend();
      }
    }, 1000);
  } catch (err) {
    console.error('Error starting recording:', err);
    alert('Could not access microphone.');
  }
});

stopBtn.addEventListener('click', () => {
  stopRecordingAndSend();
});

function stopRecordingAndSend() {
  stopBtn.disabled = true;
  clearInterval(timerInterval);
  timerDisplay.style.display = 'none';
  canvas.style.display = 'none';
  cancelAnimationFrame(animationId);

  if (audioContext) {
    audioContext.close();
    audioContext = null;
  }

  if (!recorder) return;

  recorder.stopRecording(async () => {
    try {
      const blob = recorder.getBlob();
      stream.getTracks().forEach(track => track.stop());

      const formData = new FormData();
      formData.append('arm_speech', blob, 'recording.wav');

      const model = modelSelect.value;
      let url = `http://localhost:8080/translations/audio?model=${model}`;
      if (model === 'bark') {
        url += `&gender=${selectedGender}`;
      }

      loadingInline.style.display = 'flex';
      startBtn.disabled = true;
      stopBtn.disabled = true;

      const response = await fetch(url, {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        const audioBlob = await response.blob();
        audioPlayer.src = URL.createObjectURL(audioBlob);
      } else {
        console.error('Backend error:', response.status);
        const errMsg = await response.text();
        alert(`Failed to translate speech. ${errMsg}`);
      }

    } catch (err) {
      console.error('Error sending audio:', err);
      alert('Failed to send audio to backend.');
    } finally {
      loadingInline.style.display = 'none';
      startBtn.disabled = false;
    }
  });
}

function drawWaveform() {
  animationId = requestAnimationFrame(drawWaveform);

  analyser.getByteTimeDomainData(dataArray);

  canvasCtx.fillStyle = '#ffffff';
  canvasCtx.fillRect(0, 0, canvas.width, canvas.height);

  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = '#1e1e1e';

  canvasCtx.beginPath();

  const sliceWidth = canvas.width / 200;
  let x = 0;

  for (let i = 0; i < 200; i++) {
    const v = dataArray[i] / 128.0;
    const y = (v * canvas.height) / 2;

    if (i === 0) {
      canvasCtx.moveTo(x, y);
    } else {
      canvasCtx.lineTo(x, y);
    }

    x += sliceWidth;
  }

  canvasCtx.lineTo(canvas.width, canvas.height / 2);
  canvasCtx.stroke();
}

