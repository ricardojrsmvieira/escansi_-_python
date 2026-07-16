# escansi
Python library to easily create ANSI escape codes and add them to your text.

[![Publish Python 🐍 distribution 📦 to PyPI and TestPyPI](https://github.com/ricardojrsmvieira/escansi_-_python/actions/workflows/publish.yml/badge.svg)](https://github.com/ricardojrsmvieira/escansi_-_python/actions/workflows/publish.yml)

<!-- 
uv run --exact ...

In contrast, uv run uses "inexact" syncing by default, ensuring that all required packages are installed but not removing extraneous packages. To enable exact syncing with uv run, use the --exact flag:
-->
<!-- The --no-dev flag can be used to exclude the dev group. -->
<!--
On-sync malware checking is in preview, and is subject to change until stabilized.
To enable malware checks, set UV_MALWARE_CHECK=1 in your environment.
-->
<!--
uv export --format requirements.txt --output-file requirements.txt
uv export --format pylock.toml --output-file pylock.toml
uv export --format cyclonedx1.5 --output-file sbom.json

In general, we recommend against using both a uv.lock and a requirements.txt file. The uv.lock format is more powerful and includes features that cannot be expressed in requirements.txt. If you find yourself exporting a uv.lock file, consider opening an issue to discuss your use case.

Support for exporting to CycloneDX is in preview, and may change in any future release.
 -->
<!--
 When publishing libraries, it is recommended to separately run tests with --resolution lowest or --resolution lowest-direct in continuous integration to ensure compatibility with the declared lower bounds.
 -->
