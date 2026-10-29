<p align="center">
  <a href="https://holtdroid.github.io/holtdroid/"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/banner.png" alt="Holtdroid — a cozy holt for your test Androids"></a>
</p>

<p align="center">
  <a href="https://holtdroid.github.io/holtdroid/"><b>Documentation</b></a> ·
  <a href="https://holtdroid.github.io/holtdroid/start/introduction/">Introduction</a> ·
  <a href="https://holtdroid.github.io/holtdroid/start/installation/">Installation</a> ·
  <a href="https://holtdroid.github.io/holtdroid/concepts/architecture/">Architecture</a>
</p>

Holtdroid is a self-hosted, browser-based Android sandbox for testing APKs. Pick a build that
your CI or a sync job dropped into a folder or S3 bucket, launch an Android device on demand,
and get the device screen, Chrome DevTools for the app's WebViews, clipboard sync and a VPN
location switcher in one browser tab. It runs on Kubernetes, is infrastructure-agnostic and
Apache-2.0.

## Repositories

<table>
  <tr>
    <td width="88" align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-holtdroid.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/holtdroid"><b>holtdroid</b></a> — the portal<br>
      The api, the web UI, device providers (redroid containers and USB phones), the device agent, the SSH gateway, the <code>holtdroid</code> client and the Helm chart.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/start/introduction/">Docs</a> · Go, React</sub>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-holtdroid-redroid.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/holtdroid-redroid"><b>holtdroid-redroid</b></a> — Android images<br>
      redroid (Android in a container) prepared for sessions: one image per Android version, 11 to 15, with ARM64 translation.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/configuration/emulator/">Docs</a> · <code>ghcr.io/holtdroid/holtdroid-redroid</code></sub>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-holtdroid-sync.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/holtdroid-sync"><b>holtdroid-sync</b></a> — where builds come from<br>
      Jobs that copy APKs from Slack channels, S3 buckets and GitHub releases into Holtdroid's sources.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/sources/overview/">Docs</a> · <a href="https://holtdroid.github.io/holtdroid/sources/slack/">Slack</a> · <a href="https://holtdroid.github.io/holtdroid/sources/s3/">S3</a> · <a href="https://holtdroid.github.io/holtdroid/sources/github/">GitHub</a> · Go</sub>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-holtdroid-tunnel.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/holtdroid-tunnel"><b>holtdroid-tunnel</b></a> — network for real phones<br>
      A VpnService that sends all of a phone's traffic over USB to the host, so the session's VPN location applies. No root needed.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/configuration/phones/">Docs</a> · Kotlin</sub>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-holtdroid-webview.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/holtdroid-webview"><b>holtdroid-webview</b></a> — test browser<br>
      An Android WebView playground with DevTools unlocked, presets and adb control. Works without Holtdroid too.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/tools/webview/">Docs</a> · <a href="https://github.com/holtdroid/holtdroid-webview/releases">APK</a> · Kotlin</sub>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtdroid/.github/raw/main/profile/assets/icon-chromium-builds.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtdroid/chromium-builds"><b>chromium-builds</b></a> — browser versions on demand<br>
      Chromium and WebView for Android built from release tags with proprietary codecs, for x86_64 and arm64.<br>
      <sub><a href="https://holtdroid.github.io/holtdroid/sources/chromium/">Docs</a> · <a href="https://github.com/holtdroid/chromium-builds/releases">APKs</a></sub>
    </td>
  </tr>
</table>

<sub>Status: pre-alpha. Everything here changes freely until the first tagged release.</sub>

---

<p align="center">
  <img src="https://github.com/holtdroid/.github/raw/main/profile/assets/ai-disclaimer.png" alt="Disclaimer: fully AI-generated. Not a single line of code was written or reviewed by a human. Use at your own risk.">
</p>

> [!CAUTION]
> **Fully AI-generated.** Not a single line of this project was written or reviewed by a human: all of it was
> written by Claude through Claude Code. It's a Pandora's box, so use it at your own risk.
