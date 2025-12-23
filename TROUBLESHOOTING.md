# Troubleshooting Guide

Common issues and solutions for the Google Classroom Blender Add-on.

## Installation Issues

### Problem: "Google API libraries not installed"

**Solution:**
1. Install dependencies into Blender's Python:
   ```bash
   # Run the helper script
   python install_dependencies.py
   
   # Or manually:
   <blender_python> -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
2. Restart Blender
3. Re-enable the add-on

**Note**: You must use Blender's Python, not your system Python!

### Problem: Can't find Blender's Python

**Locations by platform:**
- Windows: `C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin\python.exe`
- macOS: `/Applications/Blender.app/Contents/Resources/4.5/python/bin/python3.11`
- Linux: `/usr/share/blender/4.5/python/bin/python3.11`

### Problem: Add-on doesn't appear in preferences

**Solution:**
1. Make sure you installed the folder, not a single file
2. Check the folder name is `google_classroom_addon`
3. Look in System category
4. Restart Blender

## Authentication Issues

### Problem: "Credentials file not found"

**Solution:**
1. Ensure file is named exactly `credentials.json` (not `.txt` or `.json.json`)
2. Place in: `<addon_path>/google_classroom_addon/config/credentials.json`
3. Check file permissions (should be readable)
4. Verify JSON format is valid

### Problem: Browser doesn't open for authentication

**Solution:**
1. Check firewall settings
2. Ensure port 8080 is not blocked
3. Try running Blender as administrator/sudo temporarily
4. Look for the authentication URL in Blender's console
5. Copy URL manually to browser if needed

### Problem: "Authentication failed" error

**Causes:**
- Invalid credentials.json file
- OAuth consent screen not configured
- Required APIs not enabled
- Expired credentials

**Solution:**
1. Verify Google Cloud project has:
   - Classroom API enabled
   - Drive API enabled
   - OAuth consent screen configured
2. Re-download credentials.json
3. Delete `token.pickle` file and re-authenticate
4. Check credentials match your Google Cloud project

### Problem: "Access Denied" during OAuth

**Solution:**
1. Ensure OAuth consent screen is published
2. For school accounts: Must be "Internal" type
3. Check user is in allowed domain/organization
4. Verify app isn't blocked by administrator

## Usage Issues

### Problem: "No courses found"

**Solution:**
1. Verify you're enrolled in courses on Google Classroom
2. Check courses are Active (not Archived)
3. Try refreshing courses
4. Ensure correct Google account is authenticated
5. Check API permissions were granted during authentication

### Problem: "No assignments found"

**Solution:**
1. Verify course has assignments
2. Check assignment state (must not be deleted/draft)
3. Try refreshing assignments
4. Ensure you selected a course first

### Problem: Can't see .blend file in assignment

**Solution:**
1. File must be attached via Google Drive
2. File must have `.blend` extension
3. File must be accessible to you
4. Try refreshing assignments
5. Check file permissions in Google Drive

### Problem: Can't open assignment file

**Causes:**
- No internet connection
- File permissions issue
- Insufficient disk space

**Solution:**
1. Check internet connection
2. Verify you have permission to view the file
3. Check free disk space in temp directory
4. Try downloading file manually from Google Classroom first

### Problem: Can't submit assignment

**Common causes:**
- File not saved
- Assignment already submitted
- Past due date
- No submission permissions

**Solution:**
1. Save your file first (File > Save or Ctrl+S)
2. Check assignment hasn't already been submitted
3. Verify you're not past the due date
4. Ensure you're enrolled as a student (not teacher)
5. Check you selected the correct assignment

### Problem: "Upload failed" when submitting

**Solution:**
1. Check internet connection
2. Verify file size isn't too large (Google Drive limits)
3. Ensure Drive API permissions were granted
4. Try submitting through Google Classroom directly first
5. Check Google Drive storage quota

## Performance Issues

### Problem: Slow to load courses/assignments

**Solution:**
- This is normal for first load
- Subsequent loads should be faster
- Larger classes take longer
- Check your internet speed

### Problem: Blender freezes during operation

**Causes:**
- Large file download
- Slow network
- API timeout

**Solution:**
- Wait for operation to complete
- Check network connection
- Close and restart Blender if truly frozen

## Permission Issues

### Problem: "Insufficient permissions" error

**Solution:**
1. Sign out and sign in again
2. During authentication, make sure to grant all requested permissions
3. Delete `token.pickle` and re-authenticate
4. Check OAuth scopes in credentials.json

### Problem: Can't access teacher's files

**Solution:**
1. Verify file sharing settings in Google Classroom
2. File must be set to "Students can view"
3. Check you're enrolled in the course
4. Ask teacher to verify file permissions

## Network Issues

### Problem: "API error" messages

**Solution:**
1. Check internet connection
2. Verify Google services aren't blocked by firewall
3. Check if Google Classroom is experiencing outages
4. Try again in a few minutes

### Problem: Timeout errors

**Solution:**
1. Check your internet speed
2. Try on a different network
3. Large files take longer to download
4. Increase timeout if possible

## Data Issues

### Problem: Lost courses/assignments after restart

**Causes:**
- Authentication expired
- Token deleted

**Solution:**
- Click "Refresh Courses" to reload
- Sign in again if needed
- Data is fetched from Google each time

### Problem: Outdated assignment information

**Solution:**
- Click "Refresh Assignments" to update
- Information is cached until refresh
- Changes made in Google Classroom require refresh

## Advanced Troubleshooting

### Enable Blender's Python Console

1. Window > Toggle System Console (Windows)
2. Check console for error messages
3. Look for Python tracebacks

### Check Log Files

Look for errors in:
- Blender's system console
- Terminal where Blender was launched
- System logs

### Reset Add-on Completely

1. Sign out from add-on
2. Disable and remove add-on
3. Delete `google_classroom_addon` folder
4. Delete `token.pickle` file
5. Reinstall from scratch

### Verify API Status

Check Google's API status:
- [Google Workspace Status](https://www.google.com/appsstatus)
- Look for Classroom or Drive issues

### Check Quota Limits

Google APIs have usage quotas:
1. Go to Google Cloud Console
2. Check APIs & Services > Quotas
3. Look for Classroom API usage
4. Quota resets daily

## Still Having Issues?

If none of these solutions work:

1. **Check existing GitHub issues**: Someone may have had the same problem
2. **Create a new issue**: Include:
   - Blender version
   - Operating system
   - Error messages
   - Steps to reproduce
   - Screenshots if relevant
3. **Verify installation**: Try on a different computer to rule out local issues

## Getting Help

- GitHub Issues: [Report a bug](https://github.com/MrRoush/blender-addon/issues)
- Documentation: Check INSTALL_GUIDE.md and TEACHER_GUIDE.md
- Google Classroom Help: [Google Support](https://support.google.com/edu/classroom)
