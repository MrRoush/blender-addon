# Blender Google Classroom Add-on

A Blender 4.5 LTS add-on that integrates Google Classroom functionality directly into Blender, making it easy for students to access assignments, download .blend files, and submit completed work without leaving the 3D environment.

## Overview

This add-on is designed for computer animation classes that use Blender and Google Classroom. It streamlines the workflow for both students and teachers by:

- Viewing Google Classroom assignments directly in Blender
- Downloading starter .blend files attached to assignments
- Submitting completed assignments back to Google Classroom
- Tracking assignment status and due dates

## Quick Start

1. Install Python dependencies into Blender's Python environment
2. Install the add-on in Blender (Edit > Preferences > Add-ons)
3. Set up Google API credentials (see INSTALL_GUIDE.md)
4. Sign in with your Google account
5. Browse courses and assignments
6. Open and submit assignments

## Documentation

For detailed installation and setup instructions, see [INSTALL_GUIDE.md](INSTALL_GUIDE.md)

## Features

### For Students
- 📚 View all active courses
- 📝 Browse assignments with due dates
- 📥 Download .blend assignment files with one click
- 📤 Submit completed work directly from Blender
- ✅ Track submission status

### For Teachers
- Easy distribution of starter files
- Streamlined assignment collection
- Works with existing Google Classroom workflow
- No additional infrastructure needed

## Requirements

- Blender 4.5 LTS or later
- Google Classroom account
- Internet connection
- Google Cloud project with API credentials (see setup guide)

## Project Structure

```
google_classroom_addon/
├── __init__.py              # Add-on entry point
├── properties.py            # Blender property definitions
├── operators.py             # User action handlers
├── ui.py                    # UI panel definitions
├── api_client.py            # Google Classroom API client
├── requirements.txt         # Python dependencies
└── config/
    ├── credentials.json.template  # OAuth credentials template
    └── (credentials.json)         # Your OAuth credentials (not in repo)
```

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is provided as-is for educational purposes. Please ensure compliance with your institution's policies and Google's Terms of Service.

## Support

For detailed documentation, troubleshooting, and setup instructions, see [INSTALL_GUIDE.md](INSTALL_GUIDE.md)
