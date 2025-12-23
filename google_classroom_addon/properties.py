"""
Property classes for Google Classroom add-on
"""

import bpy
from bpy.props import (
    StringProperty,
    IntProperty,
    BoolProperty,
    CollectionProperty,
    PointerProperty,
)
from bpy.types import PropertyGroup

class CourseItem(PropertyGroup):
    """Represents a Google Classroom course"""
    course_id: StringProperty(name="Course ID")
    name: StringProperty(name="Course Name")
    section: StringProperty(name="Section")
    description: StringProperty(name="Description")
    room: StringProperty(name="Room")

class AssignmentItem(PropertyGroup):
    """Represents a Google Classroom assignment"""
    assignment_id: StringProperty(name="Assignment ID")
    course_work_id: StringProperty(name="CourseWork ID")
    title: StringProperty(name="Title")
    description: StringProperty(name="Description")
    due_date: StringProperty(name="Due Date")
    state: StringProperty(name="State")
    has_blend_file: BoolProperty(name="Has Blend File", default=False)
    blend_file_id: StringProperty(name="Blend File ID")
    blend_file_name: StringProperty(name="Blend File Name")
    submission_id: StringProperty(name="Submission ID")
    submission_state: StringProperty(name="Submission State")

class GoogleClassroomProperties(PropertyGroup):
    """Main property group for Google Classroom integration"""
    
    # Authentication state
    is_authenticated: BoolProperty(
        name="Authenticated",
        description="Whether user is authenticated with Google",
        default=False
    )
    
    user_email: StringProperty(
        name="User Email",
        description="Email of authenticated user",
        default=""
    )
    
    # Courses
    courses: CollectionProperty(type=CourseItem)
    active_course_index: IntProperty(name="Active Course", default=-1)
    
    # Assignments
    assignments: CollectionProperty(type=AssignmentItem)
    active_assignment_index: IntProperty(name="Active Assignment", default=-1)
    
    # UI state
    show_courses: BoolProperty(
        name="Show Courses",
        description="Show courses list",
        default=False
    )
    
    show_assignments: BoolProperty(
        name="Show Assignments",
        description="Show assignments list",
        default=False
    )
    
    # Status messages
    status_message: StringProperty(
        name="Status",
        description="Current status message",
        default=""
    )
    
    error_message: StringProperty(
        name="Error",
        description="Current error message",
        default=""
    )
