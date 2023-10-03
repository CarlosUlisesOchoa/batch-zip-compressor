<div align="center">
  <h1>Python Batch ZIP Compressor</h1>
  <img src="https://img.shields.io/badge/python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</div>

---

## Overview

This Python script compresses and password-protects files in a given directory. It reads environment variables from a `.env` file to determine the input and output directories, as well as the password to use for encryption.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Prerequisites

- Python 3.6 or later
- pyminizip package (`pip install pyminizip`)

## Installation

1. Clone this repository.
2. Install the required package: `pip install pyminizip`.

## Configuration

Configure and rename .env.example to .env

- `INPUT_DIR`: The directory containing the files you want to compress.
- `OUTPUT_DIR`: The directory where the compressed files will be saved.
- `PASSWORD`: The password to use for encrypting the compressed files.

Example `.env` file:

```env
# .env.example
INPUT_DIR=input
OUTPUT_DIR=output
PASSWORD=1234
```

## Usage

Open a terminal and navigate to the directory containing the script and the `.env` file. Then, run the script:

```bash
python main.py
```

## Contributing

For contributing to this project, please feel free to [open an issue](https://github.com/CarlosUlisesOchoa/batch-zip-compressor/issues) or submit a pull request.

## Contact

- Website [carlos8a.com](https://carlos8a.com)
- GitHub [@CarlosUlisesOchoa](https://github.com/carlosulisesochoa)
- X [@Carlos8aDev](https://twitter.com/carlos8adev)
