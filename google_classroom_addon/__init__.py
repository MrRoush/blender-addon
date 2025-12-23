"""
Google Classroom Blender Add-on
Integrates Google Classroom with Blender to manage assignments
"""

bl_info = {
    "name": "Google Classroom Integration",
    "author": "Educational Technology",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Google Classroom",
    "description": "Connect to Google Classroom to view and submit assignments",
    "category": "System",
    "doc_url": "https://github.com/MrRoush/blender-addon",
}

import bpy
import sys
import os

# Add the addon directory to the path to import modules
addon_dir = os.path.dirname(os.path.realpath(__file__))
if addon_dir not in sys.path:
    sys.path.append(addon_dir)

from . import properties
from . import operators
from . import ui

classes = (
    properties.GoogleClassroomProperties,
    properties.CourseItem,
    properties.AssignmentItem,
    operators.GCLASS_OT_Authenticate,
    operators.GCLASS_OT_RefreshCourses,
    operators.GCLASS_OT_RefreshAssignments,
    operators.GCLASS_OT_OpenAssignment,
    operators.GCLASS_OT_SubmitAssignment,
    operators.GCLASS_OT_Logout,
    ui.GCLASS_OT_SelectCourse,
    ui.GCLASS_OT_SelectAssignment,
    ui.GCLASS_PT_MainPanel,
    ui.GCLASS_PT_CoursesPanel,
    ui.GCLASS_PT_AssignmentsPanel,
)

def register():
    """Register all classes and properties"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.google_classroom = bpy.props.PointerProperty(
        type=properties.GoogleClassroomProperties
    )

def unregister():
    """Unregister all classes and properties"""
    del bpy.types.Scene.google_classroom
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
