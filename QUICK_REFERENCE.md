# Quick Reference Card

Quick guide for using the GitHub Classroom Blender Add-on.

## First-Time Setup

1. Open Blender → Edit → Preferences → Add-ons
2. Click Install → Select `github_classroom_addon` folder
3. Enable "System: GitHub Classroom"
4. Create a token at github.com/settings/tokens (select **repo** scope)

## Daily Workflow (Students)

### Opening Blender
1. Press `N` to open sidebar
2. Click **Classroom** tab

### Sign In (First Time)
1. Select **Student** as your role
2. Paste your GitHub token
3. Click **Sign In**

### Load Your Assignments
1. Enter your classroom **Organization** name
2. Click **Load My Assignments**

### Start an Assignment
1. Select your assignment repository
2. Click **Open Assignment**
3. File downloads and opens automatically

### Save Your Work
1. Work on your project
2. Press **Ctrl+S** to save
3. Your work is **automatically pushed to GitHub**!
4. You can also click **Save & Push to GitHub** manually

## Daily Workflow (Teachers)

### Review Student Work
1. Select **Teacher** as your role
2. Sign in and enter organization name
3. Click **Load Student Repos**
4. Select a student's repo
5. Click **Open for Review**

## Keyboard Shortcuts

- `N` — Toggle sidebar (show/hide Classroom panel)
- `Ctrl+S` — Save file (auto-pushes to GitHub for students)

## Panel Sections

### Role & Authentication (Top)
- Student/Teacher toggle
- Sign in/out with GitHub token

### Classroom (Middle)
- Organization name
- Load assignments / Load student repos

### Current File (Students only)
- Shows connected repository and file
- Auto-push toggle (on/off)
- Manual push button
- Disconnect button

### Repositories (Bottom)
- List of assignment repos
- Open file button
- Save & Push button (students)

## Common Actions

| Action | Steps |
|--------|-------|
| Sign in | Enter token → Click "Sign In" |
| Load repos | Enter org → Click "Load My Assignments" |
| Open file | Select repo → "Open Assignment" |
| Save & push | Ctrl+S (auto) or click "Save & Push to GitHub" |
| Toggle auto-push | Click "Auto-Push on Save" checkbox |
| Sign out | Click "Sign Out" |

## Important Rules

### Before Opening an Assignment
- ✅ Must be signed in
- ✅ Must have entered organization name
- ✅ Must have loaded assignments
- ✅ Repository must have a .blend file

### Before Pushing
- ✅ Must be signed in
- ✅ Must have opened a file from the addon
- ✅ File must be saved (Ctrl+S)

## Tips & Tricks

✅ **Save often** — Ctrl+S auto-pushes your work to GitHub
✅ **Check status** — Blue box shows what's happening
✅ **Read errors** — Red box explains any problems
✅ **Internet required** — All operations need an internet connection
✅ **Auto-push** — Enabled by default; disable if you want manual control

## Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Can't sign in | Check your token is correct |
| No repos found | Verify organization name |
| Can't open file | Check internet connection |
| Auto-push failed | Check internet; try manual push |
| Token expired | Create new token on GitHub |

## Getting Help

1. Check error messages in red boxes
2. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed help
3. Ask your teacher
4. Report issues on [GitHub](https://github.com/MrRoush/blender-addon/issues)

## Remember

- 💾 **Ctrl+S saves AND pushes** — Your teacher can see your progress!
- 🔄 **Refresh to see updates** — Click "Load" buttons to refresh
- 🔐 **Keep your token safe** — Don't share it with anyone

---

**Need more help?** See [INSTALL_GUIDE.md](INSTALL_GUIDE.md) for detailed instructions or [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common problems.
