"""
UI panel classes for Google Classroom add-on
"""

import bpy
from bpy.types import Panel

# Text wrapping configuration
MAX_LINE_LENGTH = 40

def wrap_text(text, layout, max_length=MAX_LINE_LENGTH):
    """
    Wrap long text into multiple lines for display in Blender UI
    
    Args:
        text: Text to wrap
        layout: Blender UI layout to add labels to
        max_length: Maximum characters per line
    """
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

class GCLASS_PT_MainPanel(Panel):
    """Main Google Classroom panel"""
    bl_label = "Google Classroom"
    bl_idname = "GCLASS_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Google Classroom'
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.google_classroom
        
        # Authentication section
        box = layout.box()
        box.label(text="Authentication", icon='USER')
        
        if props.is_authenticated:
            row = box.row()
            row.label(text=f"Signed in", icon='CHECKMARK')
            if props.user_email:
                box.label(text=f"{props.user_email}", icon='MAIL')
            box.operator("gclass.logout", icon='X')
        else:
            box.label(text="Not signed in", icon='ERROR')
            box.operator("gclass.authenticate", icon='CHECKBOX_HLT')
        
        # Status messages
        if props.status_message:
            box = layout.box()
            box.label(text=props.status_message, icon='INFO')
        
        if props.error_message:
            box = layout.box()
            box.label(text="Error:", icon='ERROR')
            wrap_text(props.error_message, box)
        
        # Info section
        if props.is_authenticated:
            layout.separator()
            box = layout.box()
            box.label(text="Quick Actions", icon='PRESET')
            box.operator("gclass.refresh_courses", icon='FILE_REFRESH')

class GCLASS_PT_CoursesPanel(Panel):
    """Courses list panel"""
    bl_label = "Courses"
    bl_idname = "GCLASS_PT_courses_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Google Classroom'
    bl_parent_id = "GCLASS_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        props = context.scene.google_classroom
        return props.is_authenticated and props.show_courses
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.google_classroom
        
        if len(props.courses) == 0:
            layout.label(text="No courses found", icon='INFO')
            return
        
        layout.label(text=f"{len(props.courses)} courses", icon='BOOKMARKS')
        
        for i, course in enumerate(props.courses):
            box = layout.box()
            
            # Course name as button
            row = box.row()
            icon = 'RADIOBUT_ON' if i == props.active_course_index else 'RADIOBUT_OFF'
            op = row.operator("gclass.select_course", text=course.name, icon=icon, emboss=False)
            op.course_index = i
            
            # Show details if selected
            if i == props.active_course_index:
                if course.section:
                    box.label(text=f"Section: {course.section}")
                if course.room:
                    box.label(text=f"Room: {course.room}")
                box.operator("gclass.refresh_assignments", icon='FILE_REFRESH')

class GCLASS_PT_AssignmentsPanel(Panel):
    """Assignments list panel"""
    bl_label = "Assignments"
    bl_idname = "GCLASS_PT_assignments_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Google Classroom'
    bl_parent_id = "GCLASS_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        props = context.scene.google_classroom
        return props.is_authenticated and props.show_assignments
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.google_classroom
        
        if len(props.assignments) == 0:
            layout.label(text="No assignments found", icon='INFO')
            return
        
        layout.label(text=f"{len(props.assignments)} assignments", icon='FILE_TEXT')
        
        for i, assignment in enumerate(props.assignments):
            box = layout.box()
            
            # Assignment title as button
            row = box.row()
            icon = 'RADIOBUT_ON' if i == props.active_assignment_index else 'RADIOBUT_OFF'
            op = row.operator("gclass.select_assignment", text=assignment.title, icon=icon, emboss=False)
            op.assignment_index = i
            
            # Show details if selected
            if i == props.active_assignment_index:
                # Due date
                if assignment.due_date:
                    box.label(text=f"Due: {assignment.due_date}", icon='TIME')
                
                # Submission state
                if assignment.submission_state:
                    state_text = assignment.submission_state.replace('_', ' ').title()
                    state_icon = 'CHECKMARK' if assignment.submission_state == 'TURNED_IN' else 'PAUSE'
                    box.label(text=f"Status: {state_text}", icon=state_icon)
                
                # .blend file indicator
                if assignment.has_blend_file:
                    box.label(text=f"File: {assignment.blend_file_name}", icon='FILE_BLEND')
                    row = box.row()
                    row.operator("gclass.open_assignment", icon='FILEBROWSER')
                else:
                    box.label(text="No .blend file", icon='INFO')
                
                # Description
                if assignment.description:
                    box.separator()
                    box.label(text="Description:", icon='TEXT')
                    # Split description into lines and show first 3
                    desc_lines = assignment.description.split('\n')
                    for line in desc_lines[:3]:
                        if len(line) > MAX_LINE_LENGTH:
                            wrap_text(line, box)
                        else:
                            box.label(text=line)
                    if len(desc_lines) > 3:
                        box.label(text="...")
                
                # Submit button
                box.separator()
                col = box.column()
                if assignment.submission_state == 'TURNED_IN':
                    col.enabled = False
                    col.label(text="Already submitted", icon='CHECKMARK')
                else:
                    col.operator("gclass.submit_assignment", icon='EXPORT')

# Helper operators for UI interactions
class GCLASS_OT_SelectCourse(bpy.types.Operator):
    """Select a course"""
    bl_idname = "gclass.select_course"
    bl_label = "Select Course"
    
    course_index: bpy.props.IntProperty()
    
    def execute(self, context):
        props = context.scene.google_classroom
        props.active_course_index = self.course_index
        props.assignments.clear()
        props.show_assignments = False
        return {'FINISHED'}

class GCLASS_OT_SelectAssignment(bpy.types.Operator):
    """Select an assignment"""
    bl_idname = "gclass.select_assignment"
    bl_label = "Select Assignment"
    
    assignment_index: bpy.props.IntProperty()
    
    def execute(self, context):
        props = context.scene.google_classroom
        props.active_assignment_index = self.assignment_index
        return {'FINISHED'}
