# Configuration Directory

This directory stores authentication and state files for the GitHub Classroom add-on.

## Files

### `github_token.json`
- Created automatically when you sign in with your GitHub Personal Access Token
- Contains your saved token so you don't need to sign in every time
- **Do not share this file** — it contains your authentication credentials

### `working_file.json`
- Created automatically when you open a .blend file from a repository
- Tracks which repository and file you're working on for auto-push
- Safe to delete if you want to disconnect from a repository

## Getting a GitHub Personal Access Token

1. Go to **GitHub.com** → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **Generate new token (classic)**
3. Give it a name like "Blender Classroom"
4. Select the **repo** scope (full control of repositories)
5. Click **Generate token**
6. **Copy the token** — you won't be able to see it again!
7. Paste the token into the add-on's "Token" field

## Security

- Token and working file data are stored locally on your computer
- These files are listed in `.gitignore` and will not be uploaded to GitHub
- If you suspect your token has been compromised, revoke it on GitHub and generate a new one
