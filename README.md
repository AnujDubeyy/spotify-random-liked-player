# 🎧 Spotify Random Liked Songs Player

A Python script that opens a random song from your Spotify liked tracks in your browser.

## How it works

- Authenticates with Spotify using Spotipy (OAuth, `user-library-read` scope — read-only access to your library).
- Pages through all of your saved tracks (50 at a time) and collects their Spotify links.
- Picks one at random and opens it in your default browser.

## Setup

Prerequisites: Python 3 and pip, plus a Spotify app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) (to get a client ID/secret and set a redirect URI).

1. Clone this repo:

```bash
git clone https://github.com/AnujDubeyy/spotify-random-liked-player.git
cd spotify-random-liked-player
```

2. Install the dependencies used by `main.py` (this repo has no `requirements.txt`):

```bash
pip install spotipy python-dotenv
```

3. Create a `.env` file with your Spotify app credentials. The variable names must match exactly what `main.py` reads:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080
```

The redirect URI must also be registered in your Spotify app settings.

4. Run it:

```bash
python main.py
```

On first run, Spotipy opens a browser window for Spotify sign-in and permission approval, then opens a random liked song.

## Files

```
spotify-random-liked-player/
├── main.py      # Fetches saved tracks and opens a random one
└── README.md
```
