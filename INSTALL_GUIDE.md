# GitHub Classroom Blender Add-on — Installation Guide

A Blender add-on that integrates GitHub Classroom into Blender 4.5 LTS, allowing students and teachers to manage animation assignments directly from within Blender.

## Features

- **Simple Sign-In**: Authenticate with a GitHub Personal Access Token (no complex setup)
- **Student/Teacher Roles**: Role-based interface for students and teachers
- **Pull Assignments**: Download .blend files from your GitHub Classroom repository
- **Auto-Push on Save**: Student work is automatically pushed to GitHub when saving
- **Teacher Review**: Teachers can browse and pull any student's work for grading
- **No External Dependencies**: Uses only Python standard library

## Installation

### Step 1: Install the Add-on

No Python dependencies need to be installed! The add-on uses only the standard library.

1. Download or clone this repository
2. In Blender, go to **Edit → Preferences → Add-ons**
3. Click **Install** and navigate to the `github_classroom_addon` folder
4. Select the folder (or zip it first and select the zip file)
5. Enable the add-on by checking the box next to **"System: GitHub Classroom"**

### Step 2: Create a GitHub Personal Access Token

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Give it a name like **"Blender Classroom"**
4. Select the **repo** scope (full control of private repositories)
5. Click **Generate token**
6. **Copy the token** — you won't be able to see it again!

> **Tip for teachers**: You can walk students through this process in class. It takes about 2 minutes.

## Usage

### For Students

#### First-Time Setup

1. Open Blender
2. Press `N` to open the sidebar in the 3D Viewport
3. Click the **Classroom** tab
4. Select **Student** as your role
5. Paste your GitHub token and click **Sign In**
6. Enter your classroom organization name (your teacher will provide this)
7. Click **Load My Assignments**

#### Daily Workflow

1. Open Blender → Press `N` → **Classroom** tab
2. (If needed) Sign in with your token
3. Click **Load My Assignments** to see your repos
4. Select an assignment and click **Open Assignment**
5. Work on your project as usual
6. **Save your file (Ctrl+S)** — changes are automatically pushed to GitHub!
7. You can also manually click **Save & Push to GitHub** at any time

### For Teachers

#### Setup

1. Open Blender → Press `N` → **Classroom** tab
2. Select **Teacher** as your role
3. Sign in with your GitHub token
4. Enter your GitHub Classroom organization name
5. Click **Load Student Repos** to see all student repositories

#### Reviewing Student Work

1. Browse the list of student repositories
2. Select a student's repo
3. Click **Open for Review** to download and open their .blend file
4. Review their work in Blender
5. Use **File → Save As** to save a local copy if needed

### Status Messages

- **Blue info boxes**: Show successful operations and current status
- **Red error boxes**: Display any errors that occur

## Privacy and Security

- Authentication tokens are stored locally in `github_classroom_addon/config/`
- The add-on only requires the **repo** scope on GitHub
- No data is sent to third parties
- Students and teachers can revoke their token at any time on GitHub

## System Requirements

- Blender 4.5 LTS or later
- Internet connection
- A GitHub account and Personal Access Token with the **repo** scope

## Support

For issues, questions, or feature requests, please open an issue on the [GitHub repository](https://github.com/MrRoush/blender-addon).

## License

This add-on is provided as-is for educational purposes. Please ensure compliance with your institution's policies and GitHub's Terms of Service.
