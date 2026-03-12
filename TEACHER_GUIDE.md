# Teacher Guide — GitHub Classroom Blender Add-on

This guide helps teachers set up and use the GitHub Classroom Blender Add-on for animation and 3D art courses.

## Overview

The add-on allows:

**Students to:**
1. Pull their assignment .blend files from GitHub Classroom
2. Work on their projects in Blender
3. Automatically push changes back to GitHub when they save
4. No programming knowledge required

**Teachers to:**
1. Browse all student repositories in the classroom organization
2. Pull any student's .blend file to review their progress
3. Grade work by opening student files directly in Blender
4. Monitor progress throughout projects

## Initial Setup (One-Time)

### 1. Set Up GitHub Classroom

If you haven't already:
1. Go to [classroom.github.com](https://classroom.github.com/)
2. Create an organization for your class (or use an existing one)
3. Create assignments — GitHub Classroom will create a repo for each student

### 2. Prepare Assignment Repos

1. Create a **template repository** with a starter .blend file
2. In GitHub Classroom, create an assignment using that template
3. When students accept the assignment, they get their own copy of the repo

### 3. Create Your Personal Access Token

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Name it "Blender Classroom"
4. Select the **repo** scope
5. Click **Generate token** and copy it

### 4. Install the Add-on in Blender

1. Download or clone the repository
2. In Blender: **Edit → Preferences → Add-ons → Install**
3. Select the `github_classroom_addon` folder
4. Enable the add-on

**No Python dependencies to install!** The add-on uses only the standard library.

## Teaching Students to Use the Add-on

### First Day Setup (10-15 minutes)

1. **Install Add-on** (3 min)
   - Walk students through Edit → Preferences → Add-ons → Install
   - Enable the add-on

2. **Create GitHub Token** (5 min)
   - Guide students to github.com/settings/tokens
   - Help them create a token with the **repo** scope
   - **Important**: Tell them to save their token somewhere safe!

3. **First Sign-In** (3 min)
   - Press N → Classroom tab
   - Select "Student" role
   - Paste token and sign in
   - Enter the organization name

4. **Quick Demo** (4 min)
   - Click "Load My Assignments"
   - Open an assignment
   - Save (Ctrl+S) — show that it auto-pushes to GitHub

### Regular Student Workflow

1. Open Blender → Press `N` → **Classroom** tab
2. Sign in (if needed)
3. Click **Load My Assignments**
4. Select assignment → **Open Assignment**
5. Work on project
6. **Save (Ctrl+S)** — auto-pushes to GitHub!
7. Done!

## Reviewing Student Work

### Using the Add-on (Recommended)

1. Open Blender → Press `N` → **Classroom** tab
2. Select **Teacher** as your role
3. Sign in with your GitHub token
4. Enter your classroom organization name
5. Click **Load Student Repos**
6. Browse the list of student repositories
7. Select a student's repo → **Open for Review**
8. Review their work in Blender
9. Use **File → Save As** to keep a local copy if needed

### Using GitHub Directly

You can also review student work through GitHub:
1. Go to your GitHub Classroom organization
2. Browse student repos
3. Download .blend files directly
4. Open them in Blender

The add-on simply makes this process faster and keeps you in Blender.

## Troubleshooting Common Student Issues

### "No token provided"
- Student needs to create a Personal Access Token
- Guide them to github.com/settings/tokens
- Make sure they select the **repo** scope

### "Invalid token"
- Token may have expired or been revoked
- Have them create a new token

### No repositories found
- Check the organization name is correct
- Verify the student has accepted the assignment
- Make sure they're signed in with the right GitHub account

### "No .blend file found"
- The template repo may not have a .blend file
- Check the assignment template repository

### Auto-push not working
- Check that the student has auto-push enabled (checkbox in the UI)
- Verify they opened the file from the addon (not from File → Open)
- Make sure they have write access to the repo

## Monitoring Student Progress

Since each student pushes to their own repo:
1. **Check commit history** on GitHub to see when students saved
2. **Pull their latest file** through the addon to review progress
3. **Use GitHub's commit timestamps** to verify work was done on time

## Security Considerations

### Personal Access Tokens
- Each person uses their own token
- Tokens can be revoked at any time on GitHub
- Tokens are stored locally on each user's computer
- Never share tokens between users

### Student Privacy
- Students only see their own repos
- Teachers see all repos in the organization (as org owners)
- No data is sent to third parties

### Best Practices
- Have students revoke old tokens at the end of the semester
- Use separate organizations for different classes/semesters
- Don't store tokens in shared locations

## Tips for Success

1. **Test First**: Complete the entire workflow yourself before class
2. **Template Repos**: Always include a starter .blend file in the template
3. **Keep It Simple**: Students just need to know: Open, Work, Save
4. **Backup Plan**: Keep GitHub web access as a fallback
5. **Start Early**: Set up the first week and troubleshoot issues together
6. **Office Hours**: Offer extra help for students who struggle with setup

## Example Class Schedule

### Week 1
- Install add-on in class (10 min)
- Test with a simple assignment
- Troubleshoot any issues

### Week 2+
- Students use the add-on for all assignments
- Workflow becomes second nature
- More time for actual animation work!

## Questions?

1. Check [INSTALL_GUIDE.md](INSTALL_GUIDE.md) for detailed setup
2. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
3. Open an issue on [GitHub](https://github.com/MrRoush/blender-addon/issues)

Good luck with your animation course!
