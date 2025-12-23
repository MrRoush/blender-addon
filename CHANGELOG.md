# Changelog

All notable changes to the Google Classroom Blender Add-on will be documented in this file.

## [1.0.0] - 2024-12-23

### Added
- Initial release of Google Classroom Blender Add-on
- OAuth2 authentication with Google Classroom
- View active Google Classroom courses
- Browse assignments for selected courses
- Download .blend files attached to assignments
- Submit completed assignments directly from Blender
- Track assignment due dates and submission status
- User-friendly UI in Blender's 3D Viewport sidebar
- Comprehensive documentation:
  - Installation guide (INSTALL_GUIDE.md)
  - Teacher setup guide (TEACHER_GUIDE.md)
  - README with quick start
- Dependency installation helper script
- OAuth credentials template

### Features
- **Authentication Panel**: Sign in/out with Google account
- **Courses Panel**: List and select from active courses
- **Assignments Panel**: View assignments with details
- **Status Tracking**: See submission status and due dates
- **File Operations**: Download and open .blend files
- **Submit Workflow**: Save and submit work in one step

### Security
- Local-only token storage
- OAuth2 secure authentication
- Minimal required API permissions
- Credentials kept in config directory

### Compatibility
- Blender 4.5 LTS
- Google Classroom API v1
- Google Drive API v3
- Python 3.11+

### Dependencies
- google-auth>=2.23.0
- google-auth-oauthlib>=1.1.0
- google-auth-httplib2>=0.1.1
- google-api-python-client>=2.100.0
