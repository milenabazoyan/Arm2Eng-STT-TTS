# Arm2Eng-STT-TTS

This project represents a pipeline for End-to-End Acoustic and Semantic Modeling For Armenian-to-English Speech and Text Systems. The project itself is divided in 3 submodules:

* the fine-tuned model for Armenian ASR and demo scripts for English TTS model (represented in `models` directory)
* the backend system, for providing an API to use the pipeline (represented in `api` directory)
* the frontend for demonstrating in a user friendly way the pipeline by using the API provided by the backend (represented in ui directory).

## Pipeline

The pipeline consists of three phases: Armenian speech to text -> Armenian text to English text translation -> English text to Armenian speech. For the last phase there are 3 models that we can choose to run, here is an example:

For the following speech as input

[input_speech_example_for_readme.webm](https://github.com/user-attachments/assets/6968a6e6-bc74-4f14-b5d1-395de7defb6e)

if we choose English text to speech model as Fast Pitch we get

[fast_pitch_output.webm](https://github.com/user-attachments/assets/192e82fe-6cd1-4cec-ae0a-42d8062223d4)

if we choose English text to speech model as Your TTS we get

[your_tts_output.webm](https://github.com/user-attachments/assets/ff1a2a2f-e0c8-4eb8-9b02-0d2a89d10ff7)

if we choose English text to speech model as Bark using female sound we get

[bark_female_output.webm](https://github.com/user-attachments/assets/1497a306-9f33-433e-8724-1bc106cca038)

if we choose English text to speech model as Bark using male sound we get

[bark_male_output.webm](https://github.com/user-attachments/assets/eeeb8bb7-692b-4406-8678-9b16481cbab6)

## How To Run Locally
First of all you need to have python version 3.10.13 and AWS account set up in your local CLI (if you do not have any account please check the **AWS Guide** section down below).

If you have set up AWS account locally which supports translate you can skip this part
- Sign up or log in at [https://aws.amazon.com (https://aws.amazon.com).
- Navigate to **IAM (Identity and Access Management)** and create a user with programmatic access.
- Attach the policy: AmazonTranslateFullAccess.
- Create a file at ~/.aws/credentials (Linux/macOS) or C:\Users\USERNAME\.aws\credentials (Windows):
> [default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1

Now since you have Python version 3.10.13 and AWS account set up you need to
1) cd api
2) python -m venv my_venv
3) source my_venv/bin/activate
4) install_required_packages.sh (requirements.txt file is not used to avoid package version conflicts such as `ERROR: Cannot install -r requirements.txt (line 67) and networkx==3.3 because these package versions have conflicting dependencies.`)
5) python run.py
6) cd ../ui
7) open index.html
NOTE: to close venv please type deactivate in your command line

## For More Information
Each module's directory has its own README.md file which you can read one by one:

See README in asr model
See README in tts model
See README in api
See README in ui
