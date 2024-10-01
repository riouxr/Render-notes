# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Custom Notes and Frame Tools",
    "blender": (3, 6, 0),  # Adjust the Blender version if needed
    "category": "Output",
    "author": "Blender Bob",
    "description": "Adds custom note fields and tools for managing frame start and end values.",
    "version": (1, 0),
    "support": "COMMUNITY",
    "warning": "",
}

import bpy

class COPY_START_TO_FRAME_START(bpy.types.Operator):
    bl_idname = "scene.copy_start_to_frame_start"
    bl_label = "Copy to Start"
    bl_description = "Copy the value from Start to the frame start"

    def execute(self, context):
        scene = context.scene
        if scene.start:
            try:
                context.scene.frame_start = int(scene.start)
            except ValueError:
                self.report({'WARNING'}, "Invalid value for Start")
        return {'FINISHED'}

class COPY_END_TO_FRAME_END(bpy.types.Operator):
    bl_idname = "scene.copy_end_to_frame_end"
    bl_label = "Copy to End"
    bl_description = "Copy the value from End to the frame end"

    def execute(self, context):
        scene = context.scene
        if scene.end:
            try:
                context.scene.frame_end = int(scene.end)
            except ValueError:
                self.report({'WARNING'}, "Invalid value for End")
        return {'FINISHED'}

class OUTPUT_PT_custom_notes(bpy.types.Panel):
    bl_label = "Custom Notes"
    bl_idname = "OUTPUT_PT_custom_notes"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_order = 10  # Controls the order; higher numbers go later

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Add fields for Start and End
        row = layout.row()
        row.prop(scene, "start")
        row.operator("scene.copy_start_to_frame_start", text="Copy to Start")

        row = layout.row()
        row.prop(scene, "end")
        row.operator("scene.copy_end_to_frame_end", text="Copy to End")

        # Add the first larger text box for Notes with a label
        layout.label(text="Notes:")
        layout.prop(scene, "notes", text="")

        # Add additional text boxes for Notes without labels
        layout.prop(scene, "note_2", text="")
        layout.prop(scene, "note_3", text="")
        layout.prop(scene, "note_4", text="")
        layout.prop(scene, "note_5", text="")

def register():
    # Register new properties for Start, End, and multiple Notes
    bpy.types.Scene.start = bpy.props.StringProperty(
        name="Start",
        description="Custom Start field",
        default=""
    )
    bpy.types.Scene.end = bpy.props.StringProperty(
        name="End",
        description="Custom End field",
        default=""
    )
    bpy.types.Scene.notes = bpy.props.StringProperty(
        name="Notes",
        description="Custom Notes field for writing longer text",
        default=""
    )
    bpy.types.Scene.note_2 = bpy.props.StringProperty(
        name="Note 2",
        description="Custom Note 2 field",
        default=""
    )
    bpy.types.Scene.note_3 = bpy.props.StringProperty(
        name="Note 3",
        description="Custom Note 3 field",
        default=""
    )
    bpy.types.Scene.note_4 = bpy.props.StringProperty(
        name="Note 4",
        description="Custom Note 4 field",
        default=""
    )
    bpy.types.Scene.note_5 = bpy.props.StringProperty(
        name="Note 5",
        description="Custom Note 5 field",
        default=""
    )
    
    bpy.utils.register_class(COPY_START_TO_FRAME_START)
    bpy.utils.register_class(COPY_END_TO_FRAME_END)
    bpy.utils.register_class(OUTPUT_PT_custom_notes)

def unregister():
    # Unregister properties and panel
    del bpy.types.Scene.start
    del bpy.types.Scene.end
    del bpy.types.Scene.notes
    del bpy.types.Scene.note_2
    del bpy.types.Scene.note_3
    del bpy.types.Scene.note_4
    del bpy.types.Scene.note_5
    
    bpy.utils.unregister_class(COPY_START_TO_FRAME_START)
    bpy.utils.unregister_class(COPY_END_TO_FRAME_END)
    bpy.utils.unregister_class(OUTPUT_PT_custom_notes)

if __name__ == "__main__":
    register()
