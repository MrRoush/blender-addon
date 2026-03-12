# Blender GitHub Classroom Add-on

A Blender 4.5 LTS add-on that integrates **GitHub Classroom** directly into Blender, making it easy for students to pull assignment .blend files, work on them, and push their changes back — all without leaving the 3D environment. Teachers can also use the add-on to pull student files for review and grading.

## Overview

This add-on is designed for animation and 3D art courses that use Blender. It connects to **GitHub Classroom** using a simple Personal Access Token — no complex setup or cloud admin access required.

### For Students
- 📥 **Pull** your assignment .blend file from your GitHub Classroom repository
- 🎨 Work on your project in Blender as usual
- 📤 **Auto-push** your changes to GitHub every time you save (or push manually)
- No programming knowledge required — just enter your token and go!

### For Teachers
- 📂 **Browse** all student repositories in your GitHub Classroom organization
- 📥 **Pull** any student's .blend file to review their progress
- Grade work by opening student files directly in Blender
- Monitor student progress throughout projects

## Quick Start

### Students

1. Install the add-on in Blender (Edit → Preferences → Add-ons → Install)
2. Open the **Classroom** sidebar panel (press N in the 3D Viewport → Classroom tab)
3. Select **Student** as your role
4. Create a [GitHub Personal Access Token](https://github.com/settings/tokens) with the **repo** scope
5. Enter your token and click **Sign In**
6. Enter your classroom organization name and click **Load My Assignments**
7. Select a repository and click **Open Assignment** to download and open your .blend file
8. Work on your project — your changes are **automatically pushed to GitHub when you save**!

### Teachers

1. Install the add-on in Blender (Edit → Preferences → Add-ons → Install)
2. Open the **Classroom** sidebar panel (press N in the 3D Viewport → Classroom tab)
3. Select **Teacher** as your role
4. Sign in with your GitHub Personal Access Token
5. Enter your classroom organization name and click **Load Student Repos**
6. Select a student's repository and click **Open for Review**

## Requirements

- Blender 4.5 LTS or later
- Internet connection
- A GitHub account and [Personal Access Token](https://github.com/settings/tokens) with the **repo** scope
- **No external Python dependencies required** — uses only Python standard library

## Documentation

- [INSTALL_GUIDE.md](INSTALL_GUIDE.md) — Detailed installation instructions
- [TEACHER_GUIDE.md](TEACHER_GUIDE.md) — Teacher setup and grading workflow
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) — Daily usage quick reference
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — Common issues and solutions

## Project Structure

```
github_classroom_addon/
├── __init__.py          # Add-on entry point and registration
├── properties.py        # Blender property definitions
├── operators.py         # User action handlers and save handler
├── ui.py                # UI panel definitions
├── github_client.py     # GitHub API client (stdlib only)
└── config/
    └── README.md        # Configuration guide
```

## How It Works

1. **Authentication**: Students and teachers sign in with a GitHub Personal Access Token
2. **Repository Listing**: Students see their own assignment repos; teachers see all repos in the organization
3. **File Operations**: .blend files are downloaded from GitHub and opened in Blender
4. **Auto-Push**: When students save their work (Ctrl+S), changes are automatically pushed back to their GitHub repository
5. **Teacher Review**: Teachers can pull any student's file to review progress and grade work

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is provided as-is for educational purposes. Please ensure compliance with your institution's policies and GitHub's Terms of Service.
