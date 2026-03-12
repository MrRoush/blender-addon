"""
GitHub Classroom Blender Add-on
Connect to GitHub Classroom to manage Blender assignments
"""

bl_info = {
    "name": "GitHub Classroom",
    "author": "Educational Technology",
    "version": (2, 0, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Classroom",
    "description": "Connect to GitHub Classroom to manage Blender assignments",
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
    # Property groups (must be registered before they are referenced)
    properties.GitHubRepoItem,
    properties.GitHubClassroomProperties,
    # Operators
    operators.GITHUB_OT_Authenticate,
    operators.GITHUB_OT_Logout,
    operators.GITHUB_OT_RefreshRepos,
    operators.GITHUB_OT_OpenFile,
    operators.GITHUB_OT_PushFile,
    operators.GITHUB_OT_ToggleAutoPush,
    operators.GITHUB_OT_Disconnect,
    operators.GITHUB_OT_SelectRepo,
    # Panels
    ui.GITHUB_PT_MainPanel,
    ui.GITHUB_PT_ReposPanel,
)

def register():
    """Register all classes, properties, and handlers"""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.github_classroom = bpy.props.PointerProperty(
        type=properties.GitHubClassroomProperties
    )

    # Register save handler for auto-push
    if operators.auto_push_on_save not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(operators.auto_push_on_save)

def unregister():
    """Unregister all classes, properties, and handlers"""
    # Remove save handler
    if operators.auto_push_on_save in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(operators.auto_push_on_save)

    del bpy.types.Scene.github_classroom

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
