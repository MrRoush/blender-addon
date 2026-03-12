"""
UI panel classes for GitHub Classroom Blender add-on
Simplified interface for students (non-programmers) and teachers
"""

import bpy
from bpy.types import Panel
from .github_client import get_github_client

MAX_LINE_LENGTH = 40


def wrap_text(text, layout, max_length=MAX_LINE_LENGTH):
    """Wrap long text into multiple lines for Blender UI"""
    words = text.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 < max_length:
            line += word + " "
        else:
            if line:
                layout.label(text=line)
            line = word + " "
    if line:
        layout.label(text=line)


class GITHUB_PT_MainPanel(Panel):
    """Main GitHub Classroom panel in the 3D Viewport sidebar"""
    bl_label = "GitHub Classroom"
    bl_idname = "GITHUB_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Classroom'

    def draw(self, context):
        layout = self.layout
        props = context.scene.github_classroom
        client = get_github_client()

        # Role selector
        box = layout.box()
        box.label(text="I am a:", icon='USER')
        row = box.row(align=True)
        row.prop(props, "role", expand=True)

        # Authentication
        box = layout.box()
        if client.is_authenticated():
            row = box.row()
            row.label(
                text=f"Signed in as @{client.username}", icon='CHECKMARK'
            )
            box.operator("github_class.logout", icon='X')
        else:
            box.label(text="Sign In", icon='LOCKED')
            box.prop(props, "github_token", text="Token")
            box.operator("github_class.authenticate", icon='CHECKBOX_HLT')

        # Classroom Organization
        if client.is_authenticated():
            box = layout.box()
            box.label(text="Classroom", icon='COMMUNITY')
            box.prop(props, "github_org", text="Organization")
            if props.role == 'TEACHER':
                box.operator(
                    "github_class.refresh_repos",
                    text="Load Student Repos", icon='FILE_REFRESH'
                )
            else:
                box.operator(
                    "github_class.refresh_repos",
                    text="Load My Assignments", icon='FILE_REFRESH'
                )

        # Working file status (for students with auto-push)
        if props.role == 'STUDENT' and client.is_authenticated():
            working = client.get_working_file()
            if working:
                box = layout.box()
                box.label(text="Current File", icon='FILE_BLEND')
                box.label(text=f"Repo: {working['repo_name']}")
                box.label(text=f"File: {working['file_path']}")

                # Auto-push toggle
                row = box.row()
                if client.auto_push:
                    icon = 'CHECKBOX_HLT'
                else:
                    icon = 'CHECKBOX_DEHLT'
                row.operator(
                    "github_class.toggle_auto_push",
                    text="Auto-Push on Save", icon=icon
                )

                # Manual push button
                box.operator("github_class.push_file", icon='EXPORT')

                # Disconnect
                box.operator("github_class.disconnect", icon='X')

        # Status messages
        if props.status_message:
            box = layout.box()
            box.label(text=props.status_message, icon='INFO')

        if props.error_message:
            box = layout.box()
            box.label(text="Error:", icon='ERROR')
            wrap_text(props.error_message, box)


class GITHUB_PT_ReposPanel(Panel):
    """Assignment repositories panel"""
    bl_label = "Repositories"
    bl_idname = "GITHUB_PT_repos_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Classroom'
    bl_parent_id = "GITHUB_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        props = context.scene.github_classroom
        client = get_github_client()
        return client.is_authenticated() and props.show_repos

    def draw(self, context):
        layout = self.layout
        props = context.scene.github_classroom

        if len(props.github_repos) == 0:
            layout.label(text="No repositories found", icon='INFO')
            return

        count = len(props.github_repos)
        if props.role == 'TEACHER':
            layout.label(
                text=f"{count} student repos", icon='FILE_FOLDER'
            )
        else:
            layout.label(
                text=f"{count} assignments", icon='FILE_FOLDER'
            )

        for i, repo in enumerate(props.github_repos):
            box = layout.box()

            # Repo name as selection button
            row = box.row()
            if i == props.active_repo_index:
                icon = 'RADIOBUT_ON'
            else:
                icon = 'RADIOBUT_OFF'
            op = row.operator(
                "github_class.select_repo",
                text=repo.repo_name, icon=icon, emboss=False
            )
            op.repo_index = i

            # Show details if selected
            if i == props.active_repo_index:
                if repo.description:
                    box.label(text=repo.description, icon='TEXT')

                if repo.updated_at:
                    box.label(
                        text=f"Updated: {repo.updated_at}", icon='TIME'
                    )

                # .blend file indicator
                if repo.has_blend_file:
                    box.label(
                        text=f"File: {repo.blend_file_name}",
                        icon='FILE_BLEND'
                    )
                    row = box.row()
                    if props.role == 'TEACHER':
                        row.operator(
                            "github_class.open_file",
                            text="Open for Review", icon='FILEBROWSER'
                        )
                    else:
                        row.operator(
                            "github_class.open_file",
                            text="Open Assignment", icon='FILEBROWSER'
                        )
                else:
                    box.label(text="No .blend file found", icon='INFO')

                # Push button (students only)
                if props.role == 'STUDENT':
                    box.separator()
                    col = box.column()
                    if repo.submitted:
                        col.label(text="Submitted", icon='CHECKMARK')
                        col.operator(
                            "github_class.push_file",
                            text="Resubmit", icon='EXPORT'
                        )
                    else:
                        col.operator(
                            "github_class.push_file",
                            text="Save & Push", icon='EXPORT'
                        )
