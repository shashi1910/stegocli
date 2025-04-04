# 🕵️‍♂️ StegoCLI - A Simple CLI Steganography Tool

**StegoCLI** is a lightweight command-line application for hiding secret messages inside PNG images using **Least Significant Bit (LSB) steganography**. It allows you to encode text into an image and decode it later — all from your terminal.

---

## 🚀 Features

- 🔐 Encode secret messages into PNG images
- 🧠 Decode messages hidden in images
- 🖼️ Works with lossless formats like PNG (no data corruption)
- 💻 Easy-to-use and scriptable via CLI
- ⚡ Fast and lightweight, with minimal dependencies

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shashi1910/stegocli
cd stegocli
```

### Install The tool on your machine
```bash
pip install -e .
```

### Encode Message
```bash
stegocli encode input.png output.png "This is a secret"
```
### Decode Message
```bash
stegocli decode output.png
```

