# API for AM->EN speech-to-text, text-to-speech pipeline
The backend part of this project is used to create the pipeline of the flow.
In our backend system we have a single API endpoint which accepts POST request of type form data.

## Pipeline
The pipeline consists of 3 phases:
1) **speech-to-text**: this phase is responsible for converting the wav audio file which contains Armenian speech to a text in Armenian, by using *FastConformer-Hybrid model from NVIDIA Nemo*.
2) **text-to-text (translation)**: this phase is responsible for translating the Armenian text in English by using *Amazon Translate* which is a third party service by Amazon Web Service (AWS) providing APIs translation.
3) **text-to-speech**: this phase is responsible for converting the translated English text into speech, i.e. a wav audio file, by using one of the following 3 models: *NVIDIA Nemo’s FastPitch* model to generate mel spectrograms and *HiFi-GAN* as the vocoder to synthesize natural-sounding English speech, or *YourTTS* model to return the translated speech with the user's sound, or *Bark* model to select between male or female sounds which are a bit realistic than others but its slow.

![flow pipeline](resources/pipeline_diagram.png "Pipeline Diagram")

## How to run the backend
First of all you need to have python version 3.10.13 and AWS account set up in your local CLI (if you do not have any account please check the **AWS Guide** section down below).
1) `python -m venv my_venv`
2) `source my_venv/bin/activate`
3) `install_required_packages.sh` (requirements.txt file is not used to avoid package version conflicts such as `ERROR: Cannot install -r requirements.txt (line 67) and networkx==3.3 because these package versions have conflicting dependencies.`)
4) `python run.py`
NOTE: to close venv please type `deactivate` in your command line

To test you can send the following test example:

<audio controls>
  <source src="https://github.com/milenabazoyan/Arm2Eng-STT-TTS/blob/main/api/resources/test/common_voice_hy-AM_41864771.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

```sh
curl -X POST "http://localhost:8080/translations/audio?model=fast_pitch" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "arm_speech=@resources/test/common_voice_hy-AM_41864771.wav;type=audio/wav"; open output.wav
```
This is the expected output of **Fast Pitch** model

<audio controls>
  <source src="./resources/test/fast_pitch_output.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

```sh
curl -X POST "http://localhost:8080/translations/audio?model=your_tts" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "arm_speech=@resources/test/common_voice_hy-AM_41864771.wav;type=audio/wav"; open output.wav
```
This is the expected output of **Your TTS** model

<audio controls>
  <source src="./resources/test/your_tts_output.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

```sh
curl -X POST "http://localhost:8080/translations/audio?model=bark&gender=male" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "arm_speech=@resources/test/common_voice_hy-AM_41864771.wav;type=audio/wav"; open output.wav
```
This is the expected output of **Bark** model using *female* sound

<audio controls>
  <source src="./resources/test/bark_male.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

```sh
curl -X POST "http://localhost:8080/translations/audio?model=bark&gender=female" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "arm_speech=@resources/test/common_voice_hy-AM_41864771.wav;type=audio/wav"; open output.wav
```
This is the expected output of **Bark** model using *male* sound

<audio controls>
  <source src="./resources/test/bark_female.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

## AWS Guide
-   Sign up or log in at [https://aws.amazon.com (https://aws.amazon.com).   
-   Navigate to **IAM (Identity and Access Management)** and create a user with programmatic access.
-   Attach the policy: `AmazonTranslateFullAccess`.
- Create a file at `~/.aws/credentials` (Linux/macOS) or `C:\Users\USERNAME\.aws\credentials` (Windows):
> [default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1
