import pathlib
from setuptools import find_packages, setup
from whisper_live.__version__ import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(name="whisper-live",
      version=__version__,
      description="A nearly-live implementation of OpenAI's Whisper.",
      long_description=README,
      long_description_content_type="text/markdown",
      include_package_data=True,
      url="https://github.com/collabora/WhisperLive",
      author="Collabora Ltd",
      author_email="vineet.suryan@collabora.com",
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
      ],
      packages=find_packages(
        exclude=("examples",
                 "Audio-Transcription-Chrome",
                 "Audio-Transcription-Firefox",
                 "requirements",
                 "whisper-finetuning"
                )
      ),
      install_requires=[
        "PyAudio",
        "faster-whisper==0.6.0",
        "torch",
        "torchaudio",
        "websockets",
        "onnxruntime",
        "ffmpeg-python",
        "scipy",
        "websocket-client",
      ],
      python_requires='>=3.8, <4',  # Specify compatible Python versions
      platforms=['any']  # Include the Python version in wheel file names
)