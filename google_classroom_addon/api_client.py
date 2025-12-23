"""
Google Classroom API client module
Handles authentication and API calls to Google Classroom
"""

import os
import json
import pickle
from typing import Optional, List, Dict, Any
from datetime import datetime

# Google API imports - these will be installed separately
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
    import io
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False

# If modifying these scopes, delete the token.pickle file.
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.me',
    'https://www.googleapis.com/auth/classroom.student-submissions.me.readonly',
    'https://www.googleapis.com/auth/classroom.student-submissions.students.readonly',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file',
]

class GoogleClassroomClient:
    """Client for interacting with Google Classroom API"""
    
    def __init__(self):
        self.creds = None
        self.service = None
        self.drive_service = None
        self.config_dir = self._get_config_dir()
        self.token_file = os.path.join(self.config_dir, 'token.pickle')
        self.credentials_file = os.path.join(self.config_dir, 'credentials.json')
        
    def _get_config_dir(self) -> str:
        """Get configuration directory for storing credentials"""
        addon_dir = os.path.dirname(os.path.realpath(__file__))
        config_dir = os.path.join(addon_dir, 'config')
        os.makedirs(config_dir, exist_ok=True)
        return config_dir
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.creds is not None and self.creds.valid
    
    def authenticate(self) -> tuple[bool, str]:
        """
        Authenticate with Google Classroom
        Returns: (success, message)
        """
        if not GOOGLE_API_AVAILABLE:
            return False, "Google API libraries not installed. Please install google-auth, google-auth-oauthlib, google-auth-httplib2, and google-api-python-client"
        
        try:
            # Check if credentials file exists
            if not os.path.exists(self.credentials_file):
                return False, f"Credentials file not found at {self.credentials_file}. Please add your OAuth 2.0 credentials."
            
            # Load existing token if available
            if os.path.exists(self.token_file):
                with open(self.token_file, 'rb') as token:
                    self.creds = pickle.load(token)
            
            # If no valid credentials, authenticate
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, SCOPES)
                    self.creds = flow.run_local_server(port=0)
                
                # Save the credentials for next run
                with open(self.token_file, 'wb') as token:
                    pickle.dump(self.creds, token)
            
            # Build services
            self.service = build('classroom', 'v1', credentials=self.creds)
            self.drive_service = build('drive', 'v3', credentials=self.creds)
            
            return True, "Authentication successful"
            
        except Exception as e:
            return False, f"Authentication failed: {str(e)}"
    
    def logout(self):
        """Clear authentication and remove token file"""
        if os.path.exists(self.token_file):
            os.remove(self.token_file)
        self.creds = None
        self.service = None
        self.drive_service = None
    
    def get_user_email(self) -> Optional[str]:
        """Get email of authenticated user"""
        try:
            if self.creds and hasattr(self.creds, 'id_token'):
                return self.creds.id_token.get('email')
            return None
        except:
            return None
    
    def get_courses(self) -> tuple[bool, List[Dict[str, Any]], str]:
        """
        Get list of courses for the authenticated user
        Returns: (success, courses_list, error_message)
        """
        if not self.is_authenticated():
            return False, [], "Not authenticated"
        
        try:
            results = self.service.courses().list(
                pageSize=100,
                courseStates=['ACTIVE']
            ).execute()
            
            courses = results.get('courses', [])
            return True, courses, ""
            
        except HttpError as error:
            return False, [], f"API error: {error}"
        except Exception as e:
            return False, [], f"Error fetching courses: {str(e)}"
    
    def get_coursework(self, course_id: str) -> tuple[bool, List[Dict[str, Any]], str]:
        """
        Get list of coursework (assignments) for a course
        Returns: (success, coursework_list, error_message)
        """
        if not self.is_authenticated():
            return False, [], "Not authenticated"
        
        try:
            results = self.service.courses().courseWork().list(
                courseId=course_id,
                pageSize=100,
                orderBy='dueDate desc'
            ).execute()
            
            coursework = results.get('courseWork', [])
            return True, coursework, ""
            
        except HttpError as error:
            return False, [], f"API error: {error}"
        except Exception as e:
            return False, [], f"Error fetching coursework: {str(e)}"
    
    def get_student_submission(self, course_id: str, coursework_id: str) -> tuple[bool, Optional[Dict[str, Any]], str]:
        """
        Get student's submission for a coursework
        Returns: (success, submission, error_message)
        """
        if not self.is_authenticated():
            return False, None, "Not authenticated"
        
        try:
            results = self.service.courses().courseWork().studentSubmissions().list(
                courseId=course_id,
                courseWorkId=coursework_id,
                userId='me'
            ).execute()
            
            submissions = results.get('studentSubmissions', [])
            if submissions:
                return True, submissions[0], ""
            return True, None, "No submission found"
            
        except HttpError as error:
            return False, None, f"API error: {error}"
        except Exception as e:
            return False, None, f"Error fetching submission: {str(e)}"
    
    def download_drive_file(self, file_id: str, destination_path: str) -> tuple[bool, str]:
        """
        Download a file from Google Drive
        Returns: (success, error_message)
        """
        if not self.is_authenticated():
            return False, "Not authenticated"
        
        try:
            request = self.drive_service.files().get_media(fileId=file_id)
            
            with open(destination_path, 'wb') as fh:
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
            
            return True, ""
            
        except HttpError as error:
            return False, f"API error: {error}"
        except Exception as e:
            return False, f"Error downloading file: {str(e)}"
    
    def upload_submission_file(self, course_id: str, coursework_id: str, file_path: str) -> tuple[bool, str]:
        """
        Upload a file as part of an assignment submission
        Returns: (success, error_message)
        """
        if not self.is_authenticated():
            return False, "Not authenticated"
        
        try:
            # First, upload file to Google Drive
            file_metadata = {
                'name': os.path.basename(file_path),
            }
            media = MediaFileUpload(file_path, resumable=True)
            drive_file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            file_id = drive_file.get('id')
            
            # Get the submission
            success, submission, error = self.get_student_submission(course_id, coursework_id)
            if not success or not submission:
                return False, f"Could not get submission: {error}"
            
            submission_id = submission.get('id')
            
            # Add attachment to submission
            attachment = {
                'driveFile': {
                    'id': file_id,
                    'title': os.path.basename(file_path),
                }
            }
            
            self.service.courses().courseWork().studentSubmissions().modifyAttachments(
                courseId=course_id,
                courseWorkId=coursework_id,
                id=submission_id,
                body={'addAttachments': [attachment]}
            ).execute()
            
            return True, ""
            
        except HttpError as error:
            return False, f"API error: {error}"
        except Exception as e:
            return False, f"Error uploading file: {str(e)}"
    
    def submit_assignment(self, course_id: str, coursework_id: str) -> tuple[bool, str]:
        """
        Mark an assignment as turned in
        Returns: (success, error_message)
        """
        if not self.is_authenticated():
            return False, "Not authenticated"
        
        try:
            # Get the submission
            success, submission, error = self.get_student_submission(course_id, coursework_id)
            if not success or not submission:
                return False, f"Could not get submission: {error}"
            
            submission_id = submission.get('id')
            
            # Turn in the submission
            self.service.courses().courseWork().studentSubmissions().turnIn(
                courseId=course_id,
                courseWorkId=coursework_id,
                id=submission_id,
                body={}
            ).execute()
            
            return True, ""
            
        except HttpError as error:
            return False, f"API error: {error}"
        except Exception as e:
            return False, f"Error submitting assignment: {str(e)}"

# Global client instance
_client_instance = None

def get_client() -> GoogleClassroomClient:
    """Get or create the global client instance"""
    global _client_instance
    if _client_instance is None:
        _client_instance = GoogleClassroomClient()
    return _client_instance
