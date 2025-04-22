!pip install nemo_toolkit['all'] --upgrade
!pip install numpy==1.24.3 --upgrade
!pip install --upgrade pytorch-lightning>=2.0.0
!pip install numba==0.61.0

# ---

import os

os.environ["NUMBA_CUDA_USE_NVIDIA_BINDING"] = "1"
os.environ["NUMBA_CUDA_DEFAULT_PTX_CC"] = "7.5"
os.environ["NUMBA_DEFAULT_PTX_VERSION"] = "8.4"
os.environ["HYDRA_FULL_ERROR"] = "1"

# ---

from google.colab import drive
drive.mount('/content/drive')

# ---

os.makedirs(
    "/content/NeMo/examples/asr/conf/conformer/hybrid_transducer_ctc/", exist_ok=True
)

!cp /content/drive/MyDrive/Capstone/configs/finetune_fastconformer.yaml \
    /content/NeMo/examples/asr/conf/conformer/hybrid_transducer_ctc/finetune_fastconformer.yaml

# ---

#Verify config was copied
!ls /content/NeMo/examples/asr/conf/conformer/hybrid_transducer_ctc

# ---

import subprocess

train_process = subprocess.Popen(
    [
        "python",
        "/content/NeMo/examples/asr/asr_hybrid_transducer_ctc/speech_to_text_hybrid_rnnt_ctc_bpe.py",
        "--config-path=/content/drive/MyDrive/Capstone/configs",
        "--config-name=finetune_fastconformer"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

for line in train_process.stdout:
    print(line, end="")