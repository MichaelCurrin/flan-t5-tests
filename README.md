# FLAN-T5 tests
> Test how to run the FLAN-T5 transformer models locally

If you want to use Python to perform tasks like summarize or translate text, you don't have to setup an LLM and have it running as a server. You can simply use a transformer. FLAN-T5 is one of the popular ones.

This project is based on models listed on the [FLAN-T5](https://huggingface.co/docs/transformers/main/en/model_doc/flan-t5) model doc on HuggingFace and using the code samples for each.


## Installation

### Setup virtual environment

1. Install Python 3.
1. Create a virtual environment and activate it.
    ```sh
    $ python3 -m venv
    $ source venv/bin/activate
    ```
1. Install packages and also dev packages if you care about Mypy typechecking:
    ```sh
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    ```

Currently, `transformers` doesn't seem to have a typing package available so it is ignored in this project in the Mypy config.

### Setup dotenv file

For the case of `request.py`, that requests the HuggingFace Inference API. Create a token on your HuggingFace account and add to a local unversioned config as `.env`. e.g.

```bash
TOKEN=hf_ABCD1234
```

## Usage

Run a script. The required model will be downloaded and used for inference.

```sh
$ cd app
$ python SCRIPT_PATH
```

For the case of `request.py`, load the token in your environment first:

```sh
$ source .env
```


## Model notes

### Sizes

Regarding model sizes, the sizes aren't clear but the `.h5` file is half a GB for the small model, 3.4GB for the large model, and the XXL model has size of 41GB in its `.h5.json` config.

### Base model

Using "base" model fails with "bus error". And transformers docs say you wan't instantiate from base so maybe that's why.

### GPU options

Using the GPU script requires CUDA. See downloads.

https://developer.nvidia.com/cuda-downloads

Note CUDA is **not** available for macOS

https://developer.nvidia.com/nvidia-cuda-toolkit-developer-tools-mac-hosts

> NVIDIA CUDA Toolkit 12.6 no longer supports development or running applications on macOS.
