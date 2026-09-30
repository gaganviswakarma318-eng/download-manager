import yt_dlp
from urllib.parse import urlparse


# ============================================================
# URL VALIDATION
# ============================================================

def get_valid_url():
    """Prompt until the user enters a valid HTTP(S) URL."""
    while True:
        url = input("\nEnter the URL to download: ").strip()
        parsed_url = urlparse(url)

        if parsed_url.scheme in {"http", "https"} and parsed_url.netloc:
            return url

        print("Invalid URL.")
        print("Please enter a complete http:// or https:// URL.")


# ============================================================
# VIDEO QUALITY DETECTION
# ============================================================

def get_available_video_qualities(url):
    """
    Extract the available video resolutions from the URL.

    Returns:
        list[int]: Available video heights, sorted from lowest to highest.
    """

    print("\nFetching available video qualities...")

    options = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            info = downloader.extract_info(url, download=False)

        formats = info.get("formats", [])

        # Collect unique video resolutions.
        heights = {
            fmt.get("height")
            for fmt in formats
            if fmt.get("vcodec") != "none"
            and fmt.get("height") is not None
        }

        # Remove invalid values and sort.
        heights = sorted(
            height
            for height in heights
            if isinstance(height, int) and height > 0
        )

        return heights

    except yt_dlp.utils.DownloadError as error:
        print(f"\nCould not fetch video information:")
        print(error)
        return []


def get_video_quality(url):
    """
    Show only the video qualities actually available
    and ask the user to choose one.
    """

    heights = get_available_video_qualities(url)

    if not heights:
        print("\nNo video qualities could be detected.")
        return None

    print("\nAvailable video qualities:")

    for index, height in enumerate(heights, start=1):
        print(f"{index}. {height}p")

    while True:
        choice = input("\nChoose video quality: ").strip()

        try:
            choice = int(choice)

            if 1 <= choice <= len(heights):
                selected_quality = heights[choice - 1]

                print(f"Selected quality: {selected_quality}p")

                return selected_quality

        except ValueError:
            pass

        print(
            f"Invalid choice. Please enter a number "
            f"between 1 and {len(heights)}."
        )


# ============================================================
# DOWNLOAD OPTIONS
# ============================================================

def get_download_options(url):
    """Ask whether the user wants video or music."""

    while True:
        choice = input(
            "\nDownload video or music? [v/m]: "
        ).strip().lower()

        # ----------------------------------------------------
        # VIDEO
        # ----------------------------------------------------

        if choice in {"v", "video"}:

            quality = get_video_quality(url)

            if quality is None:
                print("Unable to determine video quality.")
                return None

            return {
                # Best video stream up to selected resolution
                # + best available audio stream.
                "format": (
                    f"bestvideo[height<={quality}]+bestaudio/"
                    f"best[height<={quality}]"
                ),

                # Merge video + audio into MP4.
                "merge_output_format": "mp4",

                # Download thumbnail.
                "writethumbnail": True,

                # Add metadata and embed thumbnail.
                "postprocessors": [
                    {
                        "key": "FFmpegMetadata"
                    },
                    {
                        "key": "EmbedThumbnail"
                    },
                ],
            }

        # ----------------------------------------------------
        # MUSIC
        # ----------------------------------------------------

        if choice in {"m", "music", "audio"}:

            return {
                # Prefer the original M4A stream.
                # Fall back to the best available audio.
                "format": "bestaudio[ext=m4a]/bestaudio",

                "writethumbnail": True,

                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "m4a",
                        "preferredquality": "0",
                    },
                    {
                        "key": "FFmpegMetadata"
                    },
                    {
                        "key": "EmbedThumbnail"
                    },
                ],
            }

        print("\nInvalid choice.")
        print("Enter 'v' for video or 'm' for music.")


# ============================================================
# DOWNLOAD
# ============================================================

def download_media(url, options):
    """Download the media using yt-dlp."""

    if options is None:
        return

    try:
        print("\nStarting download...\n")

        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])

        print("\nDownload completed successfully.")

    except yt_dlp.utils.DownloadError as error:
        print("\nDownload failed:")
        print(error)

    except KeyboardInterrupt:
        print("\nDownload cancelled by user.")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 50)
    print("                 GDM Downloader")
    print("=" * 50)

    while True:

        # Get URL.
        url = get_valid_url()

        # Get download options.
        options = get_download_options(url)

        # Download.
        download_media(url, options)

        # Ask whether the user wants another download.
        while True:
            again = input(
                "\nDownload another file? [y/n]: "
            ).strip().lower()

            if again in {"y", "yes"}:
                break

            if again in {"n", "no"}:
                print("\nExiting GDM.")
                return

            print("Please enter 'y' or 'n'.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

