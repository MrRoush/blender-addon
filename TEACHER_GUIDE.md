# Quick Start Guide for Teachers

This guide helps teachers set up the Google Classroom Blender Add-on for their classes.

## Overview

The add-on allows students to:
1. View Google Classroom assignments in Blender
2. Download starter .blend files you attach to assignments
3. Submit completed work directly from Blender
4. Track assignment status and due dates

## Initial Setup (One-Time)

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "New Project" and give it a name (e.g., "Animation Class 2024")
3. Wait for the project to be created

### 2. Enable Required APIs

1. In your project, go to **APIs & Services > Library**
2. Search for and enable:
   - **Google Classroom API**
   - **Google Drive API**

### 3. Configure OAuth Consent Screen

1. Go to **APIs & Services > OAuth consent screen**
2. Choose **Internal** if using Google Workspace (recommended for schools)
   - Or **External** if using regular Gmail accounts
3. Fill in the required information:
   - App name: "Google Classroom Blender Integration"
   - User support email: Your email
   - Developer contact: Your email
4. Click **Save and Continue**
5. On the Scopes page, click **Save and Continue** (no need to add scopes manually)
6. Review and click **Back to Dashboard**

### 4. Create OAuth 2.0 Credentials

1. Go to **APIs & Services > Credentials**
2. Click **Create Credentials > OAuth client ID**
3. Choose **Desktop app** as the application type
4. Name it "Blender Add-on"
5. Click **Create**
6. **Download** the JSON file (click the download icon)
7. Rename it to `credentials.json`

### 5. Distribute to Students

You have two options:

#### Option A: Shared Credentials (Easier)
1. Share the `credentials.json` file with all students via:
   - Google Classroom attachment
   - School file server
   - Email (be aware this is less secure)
2. Each student will authenticate with their own Google account
3. Students place the file in: `google_classroom_addon/config/credentials.json`

#### Option B: Individual Setup (More Secure)
1. Share instructions for students to create their own Google Cloud projects
2. Each student creates their own OAuth credentials
3. More secure but requires more student technical knowledge

## Preparing Assignments

### Creating an Assignment with a Starter File

1. In Google Classroom, create a new assignment as usual
2. Click **Add** and choose **Google Drive**
3. Upload your starter .blend file
4. Set the file sharing to "Students can view file"
5. Add assignment details, due date, and instructions
6. Click **Assign**

### Best Practices

- **File Naming**: Use descriptive names like `assignment_01_character_modeling.blend`
- **Templates**: Include basic scene setup students need to start
- **Instructions**: Provide clear step-by-step instructions in the description
- **Due Dates**: Always set due dates so students can prioritize
- **Test First**: Test the workflow yourself before assigning to students

## Teaching Students to Use the Add-on

### First Day Setup (15-20 minutes)

1. **Install Dependencies** (5 min)
   - Walk through installing Python packages into Blender
   - Have students run `install_dependencies.py` or manually install

2. **Install Add-on** (3 min)
   - Show how to install via Edit > Preferences > Add-ons
   - Demonstrate enabling the add-on

3. **Add Credentials** (3 min)
   - Show where to place `credentials.json`
   - Verify the file location

4. **First Authentication** (5 min)
   - Guide students through signing in
   - Address any authentication issues
   - Show how to grant permissions

5. **Quick Demo** (4 min)
   - Demonstrate viewing courses
   - Show opening an assignment
   - Show submitting work

### Regular Workflow (Students)

1. Open Blender
2. Press `N` to open sidebar
3. Go to Google Classroom tab
4. (If needed) Sign in
5. Refresh courses and select their class
6. Refresh assignments
7. Select and open assignment
8. Complete work
9. Save file (Ctrl+S)
10. Submit assignment

## Troubleshooting Common Student Issues

### "Google API libraries not installed"
- Student needs to install dependencies
- Point them to `install_dependencies.py` or manual installation
- Have them restart Blender

### "Credentials file not found"
- Check file location and name
- Verify it's `credentials.json` not `credentials.json.txt`
- Make sure it's in the `config` folder

### "No courses found"
- Student might not be enrolled in your course
- Check they're signed in with correct account
- Verify course is Active (not Archived)

### Can't submit assignment
- File must be saved first
- Check assignment hasn't passed due date
- Verify student has submission permissions

## Monitoring Student Progress

- Use Google Classroom's normal interface to:
  - View submissions
  - Grade assignments
  - Provide feedback
  - Track late submissions

- The add-on doesn't change how you grade, it just makes submission easier for students

## Security Considerations

### OAuth Credentials
- OAuth credentials identify your application, not individual users
- Each student still authenticates with their own Google account
- Credentials can be safely shared with your class
- If credentials are compromised, you can revoke and create new ones

### Student Privacy
- Students authenticate with their own accounts
- Students can revoke access anytime via Google Account settings
- No student data is stored by the add-on beyond local authentication tokens

### Best Practices
- Don't post credentials publicly on the internet
- Share credentials only with enrolled students
- Consider creating new credentials each semester/year
- Inform students about what permissions they're granting

## Support Resources

### For Students
- Direct them to `INSTALL_GUIDE.md` for detailed setup instructions
- Create a FAQ document based on common issues in your class
- Consider creating a video tutorial specific to your setup

### For You
- GitHub Issues: Report bugs or request features
- Test everything before class starts
- Keep backup credentials in case of issues

## Tips for Success

1. **Do a Test Run**: Complete the entire workflow yourself before class
2. **Have Backup Plan**: Keep traditional submission method available initially
3. **Start Simple**: Use for one assignment first, then expand
4. **Get Feedback**: Ask students what works and what doesn't
5. **Document Issues**: Note common problems to improve setup for next semester

## Example Class Schedule

### Week 1
- Install add-on (in class)
- Test with a simple "hello world" assignment
- Troubleshoot issues

### Week 2+
- Use for all assignments
- Students become familiar with workflow
- Less time spent on submission logistics

## Questions?

If you have questions or issues:
1. Check `INSTALL_GUIDE.md` for detailed technical information
2. Review this guide for teaching-specific tips
3. Check GitHub Issues for similar problems
4. Create a new issue with your specific question

Good luck with your animation class!
