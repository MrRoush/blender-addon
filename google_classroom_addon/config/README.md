# Configuration Directory

This directory stores your OAuth credentials and authentication tokens.

## Required File

### credentials.json
Your OAuth 2.0 client credentials from Google Cloud Console.

**How to get this file:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable Google Classroom API and Drive API
3. Create OAuth 2.0 credentials (Desktop app type)
4. Download the JSON file
5. Rename it to `credentials.json`
6. Place it in this directory

**Template:** See `credentials.json.template` for the expected format.

## Generated Files

### token.pickle
Automatically created after first successful authentication. Contains your access and refresh tokens.

**Do not share this file** - it provides access to your Google account.

**To re-authenticate:** Delete this file and sign in again in Blender.

## Security Notes

- **Never commit credentials.json or token.pickle to version control**
- These files are listed in .gitignore
- Keep credentials.json secure but it can be shared with your class
- Each user's token.pickle is unique to their Google account
- Students can revoke access anytime via Google Account settings

## File Locations

When add-on is installed in Blender:
- Windows: `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\google_classroom_addon\config\`
- macOS: `~/Library/Application Support/Blender/4.5/scripts/addons/google_classroom_addon/config/`
- Linux: `~/.config/blender/4.5/scripts/addons/google_classroom_addon/config/`
