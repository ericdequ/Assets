# Background Removal & Bing Image Generation Project

## Description

This repository houses two separate Python scripts:

1. `removeback.py`: A script to crawl through a directory and remove the background from all images found within it.
2. A yet-unnamed script that generates images based on Bing search for a list of prompts.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [License](#license)

---

## Requirements

- Python 3.x
- PIL (Pillow)
- rembg
- Selenium WebDriver
- Chrome Driver

---

## Installation

To install the required Python packages, execute the following command:

```bash
pip install Pillow rembg selenium webdriver-manager
```

Additionally, ensure Chrome is installed, as Selenium's WebDriver will need it to run the browser automations. The script uses `webdriver-manager` to automatically download the compatible ChromeDriver.

---

## Usage

### For Background Removal (`removeback.py`)

Execute the script as follows:

```bash
python removeback.py
```

This script will crawl through the specified directory and process all supported image formats.

**Important**: Update the `directory` variable in the script with the path of the directory you wish to crawl.

### For Bing Image Generation

Execute the script as follows:

```bash
python genimage.py
```

**Important**: Update the `SAVE_PATH` variable in the script with the path where you want to save the images.

---

## Contribution

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code contributions.

---

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.

---

This `README.md` provides a blend of technical explanations and instructions, ensuring comprehensibility and ease of implementation. Please adjust the `script_name` and other placeholders as necessary. You may also wish to add a `CONTRIBUTING.md` and `LICENSE.md` to make the repository more complete and standardized.

### Ethical Consideration

Providing a thorough `README.md` fosters an environment of transparency and contributes positively to the developer ecosystem by easing the process of code adoption and collaboration.
