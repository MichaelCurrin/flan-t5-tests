# FLAN-T5 tests
> Test how to run the FLAN-T5 transformer models locally with Python and on a webpage

[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")
[![OS - macOS](https://img.shields.io/badge/OS-macOS-blue?logo=apple&logoColor=white)](https://www.apple.com/macos/ "Go to Apple homepage")
[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/flan-t5-tests?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/flan-t5-tests/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

If you want to use Python to perform tasks like summarize or translate text, you don't have to setup an LLM and have it running as a server. You can simply use a transformer. FLAN-T5 is one of the popular ones.

This project is based on models listed on the [FLAN-T5](https://huggingface.co/docs/transformers/main/en/model_doc/flan-t5) model doc on HuggingFace and using the code samples for each.


## About the HuggingFace Inference API

For the case of `request.py`, that requests the HuggingFace Inference API instead of running against a local model.

If you use existing models rather than custom ones, you do not need to setup billing. It just works easily on the free tier. See the [Inference API doc](https://huggingface.co/docs/api-inference/index) on features.

The limits are vague on the Pricing page. But at least you can your usage - go to HuggingFace, Solutions, then Inference Endpoints.


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

For `request.py`, create a token on your HuggingFace account and add it to a local unversioned config as `.env`.

e.g.

```bash
TOKEN=hf_ABCD1234
```

## Usage

### CLI

Run a script in the [app](/app/) directory. The required model will be downloaded and used for inference.

```sh
$ cd app
$ python SCRIPT_PATH
```

For `request.py`, load the token in your environment first:

```sh
$ source .env
```

### Web app

Start a static HTTP server in the [docs](/docs/) directory. This is named as such to deploy it on GitHub Pages.

Then open the page in your browser.

Enter your details and submit. Note that the values are stored in localstorage so they can be persisted. For security, your token will **not** be logged or sent anywhere except to the HuggingFace API.

![sample image](/sample.png)

Note that on the small and even the large model, the results are not so good and can be sensitive, while the CLI options seemed more realistic. Some problems I found: giving English results when asking for German, getting a response to a question in German instead of translating the input, and changing the initial letter of the content to a lowercase where uppercase was useless in the response.

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
