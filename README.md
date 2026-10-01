# Download Manager

GDM Downloader is a Python-based command-line tool that lets you download video and music from supported media URLs using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

* **Video downloads:** Select from the resolutions available for the provided URL.
* **Music downloads:** Download audio in M4A format.
* **Automatic quality detection:** Displays the video resolutions detected for the URL.
* **Metadata and thumbnails:** Attempts to add metadata and embed thumbnails using FFmpeg.
* **Cross-platform script:** Designed to run on Windows, Android, and iPhone with a compatible Python environment.

## Requirements

* Python 3.10 or later recommended.
* yt-dlp.
* FFmpeg and FFprobe for video/audio merging and post-processing.
* An internet connection.

## 1. Windows Installation

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation, enable **Add Python to PATH** if the installer offers that option.

### Step 2: Install yt-dlp

Open PowerShell or the VS Code terminal and run:

```powershell
py -m pip install -U yt-dlp
```

### Step 3: Install FFmpeg

Download FFmpeg from:

https://ffmpeg.org/download.html

Install a Windows build and add its `bin` directory to your system's PATH.

Verify the installation:

```powershell
ffmpeg -version
ffprobe -version
```

### Step 4: Download the script

Download `gdm.py` from this repository and open a terminal in the folder containing the file.

### Step 5: Run GDM

```powershell
py gdm.py
```

Follow the on-screen instructions to enter a URL, choose video or music, and select a video resolution when prompted.

---

## 2. Android Installation

GDM can be run on Android using **Termux**, which provides a terminal environment for Python and other command-line tools.

### Step 1: Install Termux

Install Termux using its official project:

https://github.com/termux/termux-app

### Step 2: Install the required packages

Open Termux and run:

```bash
pkg update && pkg upgrade
pkg install python ffmpeg
python -m pip install -U yt-dlp
```

### Step 3: Allow storage access

```bash
termux-setup-storage
```

Grant the requested storage permission.

### Step 4: Get the script

Download `gdm.py` from the **Code → Download ZIP** option on this repository, extract it, and place the file somewhere accessible to Termux.

Alternatively, if you have Git installed:

```bash
pkg install git
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 5: Run the script

Navigate to the folder containing `gdm.py` and run:

```bash
python gdm.py
```

Your downloads will normally be saved in Termux's current working directory unless the download configuration or environment changes the output location.

---

## 3. iPhone Installation

On iPhone, you can try running GDM through **[a-Shell](https://apps.apple.com/app/a-shell/id1473805438)**, an iOS terminal app.

iOS has additional restrictions on software installation and file access, so compatibility may vary.

### Step 1: Install a-Shell

Install a-Shell from the App Store and open it.

### Step 2: Get the script

Download `gdm.py` from this repository using Safari or the GitHub website.

Save the file to the Files app in a location that a-Shell can access.

### Step 3: Install yt-dlp

In a-Shell, try:

```bash
python3 -m pip install -U yt-dlp
```

If this command is unavailable, check the Python and package-installation instructions for your installed a-Shell version.

### Step 4: Check FFmpeg support

The script uses FFmpeg post-processors to merge media, add metadata, and embed thumbnails. Check whether your a-Shell environment provides compatible FFmpeg and FFprobe executables.

Some iOS environments may not support all required dependencies or post-processing features.

### Step 5: Run GDM

Navigate to the directory containing `gdm.py` and run:

```bash
python3 gdm.py
```

If Python, yt-dlp, and the required FFmpeg tools are supported, follow the on-screen prompts to download media.

**Note:** iPhone support is dependent on the capabilities of a-Shell and the installed dependencies. Successful execution is not guaranteed on every iOS version.

---

## How to Use

1. Start the script.
2. Enter a complete media URL beginning with `http://` or `https://`.
3. Choose video (`v`) or music (`m`).
4. If downloading video, choose one of the displayed resolutions.
5. Wait for the download to finish.
6. Enter `y` to download another file or `n` to exit.

## Troubleshooting

| Problem                                         | What to check                                                                                 |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'yt_dlp'` | Install yt-dlp in the same Python environment used to run the script.                         |
| `ffmpeg not found`                              | Install FFmpeg and ensure it is accessible through PATH or the terminal environment.          |
| No video qualities detected                     | Check the URL, internet connection, and whether the media source is supported.                |
| Download fails                                  | Update yt-dlp and check whether the media source requires authentication or restricts access. |
| Thumbnail or metadata processing fails          | Verify that compatible FFmpeg tools are installed and accessible.                             |
| iPhone installation fails                       | Check a-Shell's supported Python packages and command-line tools.                             |

## Important Notice

Use this tool only for media you own, have permission to download, or are otherwise legally permitted to access and download. Respect copyright laws, platform terms, and the rights of content creators.

GDM Downloader is provided for educational and informational purposes. Users are responsible for how they use the software.

## Dependencies

* [Python](https://www.python.org/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [FFmpeg](https://ffmpeg.org/)

## License

Add a `LICENSE` file to this repository if you intend to distribute the project under a specific open-source license.
