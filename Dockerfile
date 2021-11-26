FROM huggingface/transformers-pytorch-cpu:latest

COPY outs/train model
COPY requirements.txt .
COPY src/inference.py inference.py

RUN pip3 install fire loguru

ENTRYPOINT ["python3", "inference.py", "model"]
