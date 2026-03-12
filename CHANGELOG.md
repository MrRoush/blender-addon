# Changelog

All notable changes to the GitHub Classroom Blender Add-on will be documented in this file.

## [2.0.0] - 2025-01-15

### Changed
- **Converted from Google Classroom to GitHub Classroom only**
- Renamed add-on from "Classroom Integration" to "GitHub Classroom"
- Renamed package from `google_classroom_addon` to `github_classroom_addon`
- Simplified UI for non-programmer students (art/animation students)
- Removed platform toggle (GitHub Classroom is now the only platform)

### Added
- **Student/Teacher role selector** for role-specific workflows
- **Auto-push on save**: Student work is automatically pushed to GitHub when saving (Ctrl+S)
- **Teacher repository browsing**: Teachers can see all student repos in the org for grading
- **Working file tracking**: Addon remembers which repo/file you're working on
- **Toggle auto-push**: Students can enable/disable auto-push from the UI
- **Disconnect button**: Students can disconnect from the current repo

### Removed
- Google Classroom integration (api_client.py)
- Google OAuth credentials template and setup
- Python dependency requirements (requirements.txt) — addon now uses only stdlib
- Dependency installation helper (install_dependencies.py)
- Platform selection toggle (Google/GitHub)
- Google Classroom courses and assignments panels

### Security
- Local-only token storage (GitHub Personal Access Token)
- Working file config stored locally
- No external Python dependencies required

### Compatibility
- Blender 4.5 LTS or later
- GitHub API v3
- Python 3.11+ (included with Blender)

## [1.0.0] - 2024-12-23

### Added
- Initial release with Google Classroom and GitHub Classroom support
