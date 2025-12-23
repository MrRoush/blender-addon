# Google Classroom Blender Add-on

A Blender add-on that integrates Google Classroom into Blender 4.5 LTS, allowing students and teachers to manage assignments directly from within Blender.

## Features

- **Authentication**: Sign in with your Google account
- **View Courses**: List all your active Google Classroom courses
- **View Assignments**: Browse assignments for each course
- **Download Files**: Automatically download .blend files attached to assignments
- **Submit Work**: Save and submit your completed assignments directly from Blender
- **Assignment Tracking**: View due dates and submission status

## Installation

### Step 1: Install Python Dependencies

The add-on requires several Google API libraries. Since Blender uses its own Python installation, you need to install these packages into Blender's Python environment.

#### On Windows:
```bash
# Navigate to Blender's Python directory (adjust version number as needed)
cd "C:\Program Files\Blender Foundation\Blender 4.5\4.5\python\bin"

# Install dependencies
.\python.exe -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

#### On macOS:
```bash
# Navigate to Blender's Python directory
cd /Applications/Blender.app/Contents/Resources/4.5/python/bin

# Install dependencies
./python3.11 -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

#### On Linux:
```bash
# Navigate to Blender's Python directory (adjust version and path as needed)
cd /usr/share/blender/4.5/python/bin

# Install dependencies
./python3.11 -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 2: Install the Add-on

1. Download or clone this repository
2. In Blender, go to **Edit > Preferences > Add-ons**
3. Click **Install** and navigate to the `google_classroom_addon` folder
4. Select the folder or zip it and select the zip file
5. Enable the add-on by checking the box next to "System: Google Classroom Integration"

### Step 3: Set Up Google API Credentials

To use this add-on, you need to set up a Google Cloud project and obtain OAuth 2.0 credentials:

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable Required APIs**:
   - In the Google Cloud Console, enable the following APIs:
     - Google Classroom API
     - Google Drive API

3. **Create OAuth 2.0 Credentials**:
   - Go to **APIs & Services > Credentials**
   - Click **Create Credentials > OAuth client ID**
   - Choose **Desktop app** as the application type
   - Download the credentials JSON file

4. **Add Credentials to Add-on**:
   - Rename the downloaded file to `credentials.json`
   - Place it in: `google_classroom_addon/config/credentials.json`
   - The full path should be: `<blender_config>/scripts/addons/google_classroom_addon/config/credentials.json`

## Usage

### First-Time Setup

1. Open Blender
2. In the 3D Viewport, press `N` to open the sidebar
3. Click on the **Google Classroom** tab
4. Click **Sign In with Google**
5. Your browser will open for authentication
6. Sign in with your Google account and grant permissions
7. Return to Blender - you're now authenticated!

### Viewing Courses and Assignments

1. After signing in, click **Refresh Courses** to load your courses
2. Expand the **Courses** section to see all your active courses
3. Click on a course name to select it
4. Click **Refresh Assignments** to load assignments for that course
5. Expand the **Assignments** section to see all assignments

### Opening an Assignment

1. Select an assignment from the list
2. If the assignment has a .blend file attached, you'll see it listed
3. Click **Open Assignment File** to download and open it in Blender
4. The file will open automatically in Blender

### Submitting an Assignment

1. After completing your work, **save your file** (File > Save or Ctrl+S)
2. Select the assignment you want to submit
3. Click **Submit Assignment**
4. The add-on will upload your .blend file and mark the assignment as turned in

### Status Messages

- **Green info boxes**: Show successful operations and current status
- **Red error boxes**: Display any errors that occur
- Watch for submission status indicators (e.g., "Already Submitted")

## Troubleshooting

### "Google API libraries not installed" Error
- Make sure you installed the dependencies into Blender's Python (see Step 1 above)
- Restart Blender after installing dependencies

### "Credentials file not found" Error
- Ensure `credentials.json` is in the correct location: `google_classroom_addon/config/credentials.json`
- Check that the file is not named `credentials.json.txt`

### Authentication Window Doesn't Open
- Check your firewall settings
- Try running Blender as administrator (Windows) or with sudo (Linux)
- Ensure port 8080 is not blocked

### "No courses found" or "No assignments found"
- Verify you're enrolled in courses on Google Classroom
- Check that the courses are active (not archived)
- Try refreshing the list

### Can't Submit Assignment
- Make sure you've saved your file first (File > Save)
- Check that you have permission to submit to the course
- Verify the assignment hasn't passed its due date

## For Teachers

### Setting Up for Your Class

1. Create a Google Cloud project for your class
2. Generate OAuth 2.0 credentials
3. Distribute the credentials.json file to your students (via secure method)
4. Provide students with installation instructions
5. Create assignments in Google Classroom and attach starter .blend files

### Best Practices

- Attach a template .blend file to each assignment
- Set clear due dates in Google Classroom
- Use assignment descriptions to provide detailed instructions
- Test the add-on yourself before deploying to students

## Privacy and Security

- Authentication tokens are stored locally in `google_classroom_addon/config/`
- The add-on only requests necessary permissions:
  - Read courses and assignments
  - Read and upload student submissions
  - Access Drive files attached to assignments
- No data is sent to third parties
- Students can revoke access at any time via Google Account settings

## System Requirements

- Blender 4.5 LTS or later
- Internet connection
- Google Classroom account (student or teacher)
- Python 3.11+ (included with Blender)

## Support

For issues, questions, or feature requests, please open an issue on the [GitHub repository](https://github.com/MrRoush/blender-addon).

## License

This add-on is provided as-is for educational purposes. Please ensure compliance with your institution's policies and Google's Terms of Service when using this add-on.

## Credits

Developed for computer animation classes using Blender and Google Classroom.
