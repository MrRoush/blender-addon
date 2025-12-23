# Quick Reference Card

Quick guide for using the Google Classroom Blender Add-on.

## First-Time Setup

1. Install dependencies: `python install_dependencies.py`
2. Open Blender → Edit → Preferences → Add-ons
3. Click Install → Select `google_classroom_addon` folder
4. Enable "System: Google Classroom Integration"
5. Add `credentials.json` to `config/` folder

## Daily Workflow

### Opening Blender
1. Press `N` to open sidebar
2. Click **Google Classroom** tab

### Sign In (First Time or After Timeout)
1. Click **Sign In with Google**
2. Browser opens → Sign in with your school Google account
3. Grant permissions
4. Return to Blender

### View Your Courses
1. Click **Refresh Courses**
2. Expand **Courses** section
3. Click on your course name

### View Assignments
1. Click **Refresh Assignments**
2. Expand **Assignments** section
3. Click on assignment to see details

### Start an Assignment
1. Select assignment with .blend file
2. Click **Open Assignment File**
3. File downloads and opens automatically

### Submit Your Work
1. Complete your work
2. Save file: **File → Save** (or Ctrl+S)
3. In Google Classroom panel, select the assignment
4. Click **Submit Assignment**
5. Wait for confirmation: "Assignment submitted successfully!"

## Keyboard Shortcuts

- `N` - Toggle sidebar (show/hide Google Classroom panel)
- `Ctrl+S` - Save file (required before submitting)

## Panel Sections

### Authentication (Top)
- Shows sign-in status
- Sign in/out buttons
- Your email when signed in

### Status Messages (Middle)
- 📘 Blue box = Info/status
- 🔴 Red box = Errors

### Courses Section
- List of your active courses
- Click to select
- Shows section and room info

### Assignments Section
- List of assignments in selected course
- Due dates and status
- Assignment descriptions
- Open/Submit buttons

## Assignment Status Icons

- 📄 **RADIOBUT_OFF** - Not selected
- 🔘 **RADIOBUT_ON** - Currently selected
- ⏰ **TIME** - Due date shown
- ⏸️ **PAUSE** - Not submitted
- ✅ **CHECKMARK** - Submitted
- 📁 **FILE_BLEND** - Has .blend file
- ℹ️ **INFO** - Information message
- 🔄 **FILE_REFRESH** - Refresh button
- 📂 **FILEBROWSER** - Open file button
- 📤 **EXPORT** - Submit button

## Common Actions

| Action | Steps |
|--------|-------|
| Refresh courses | Click "Refresh Courses" |
| Select course | Click course name in Courses list |
| Refresh assignments | Click "Refresh Assignments" |
| Select assignment | Click assignment title in Assignments list |
| Open assignment | Select assignment → "Open Assignment File" |
| Submit work | Save file → Select assignment → "Submit Assignment" |
| Sign out | Click "Sign Out" in authentication section |

## Important Rules

### Before Opening Assignment
- ✅ Must be signed in
- ✅ Must have refreshed courses
- ✅ Must have selected a course
- ✅ Must have refreshed assignments
- ✅ Assignment must have a .blend file

### Before Submitting
- ✅ Must be signed in
- ✅ Must have opened or created a .blend file
- ✅ **Must save file first** (Ctrl+S)
- ✅ Must select the assignment
- ✅ Cannot submit if already submitted

## Status Indicators

### Submission States
- **Not started** - No submission yet
- **Created** - Draft submission exists
- **Turned In** - Submitted (done!)
- **Returned** - Graded by teacher

### Connection States
- **Signed in** ✅ - Ready to use
- **Not signed in** ❌ - Click "Sign In with Google"
- **Loading...** ⏳ - Wait for operation to complete

## Tips & Tricks

✅ **Save often** - Use Ctrl+S frequently while working
✅ **Check due dates** - Shown next to each assignment
✅ **Watch status messages** - Blue box shows what's happening
✅ **Read error messages** - Red box explains problems
✅ **Refresh when needed** - After changes in Google Classroom
✅ **Internet required** - All operations need internet connection

## Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Can't sign in | Check credentials.json is in config folder |
| No courses | Click "Refresh Courses" |
| No assignments | Select a course first, then "Refresh Assignments" |
| Can't open file | Check internet connection |
| Can't submit | Save file first (Ctrl+S) |
| Already submitted | Assignment can only be submitted once |

## Getting Help

1. Check error messages in red boxes
2. See TROUBLESHOOTING.md for detailed help
3. Ask your teacher
4. Report issues on GitHub

## Remember

- 💾 **Save before submit** - Always!
- 🔄 **Refresh to see updates** - Changes in Google Classroom need refresh
- ⏰ **Watch deadlines** - Due dates are shown for each assignment
- ✅ **One submission** - Can't resubmit after turning in (without teacher help)

---

**Need more help?** See INSTALL_GUIDE.md for detailed instructions or TROUBLESHOOTING.md for common problems.
