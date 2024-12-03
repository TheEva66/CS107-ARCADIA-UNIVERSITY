import bpy
import bmesh

# Delete default objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a sphere for the body
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
body = bpy.context.object
body.name = "Body"

# Scale the body to be more oval
bpy.ops.object.mode_set(mode='EDIT')
bmesh_body = bmesh.from_edit_mesh(body.data)
bpy.ops.transform.resize(value=(1, 1, 1.5))
bpy.ops.object.mode_set(mode='OBJECT')

# Add a pink material for the body
mat = bpy.data.materials.new(name="BodyMaterial")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get("Principled BSDF")
bsdf.inputs['Base Color'].default_value = (1, 0.4, 0.6, 1)  # Pink
body.data.materials.append(mat)

# Add eyes
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(-0.2, 0.5, 1.2))
eye_left = bpy.context.object
eye_left.name = "EyeLeft"
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0.2, 0.5, 1.2))
eye_right = bpy.context.object
eye_right.name = "EyeRight"

# Add a white material for the eyes
eye_mat = bpy.data.materials.new(name="EyeMaterial")
eye_mat.use_nodes = True
eye_mat.node_tree.nodes["Principled BSDF"].inputs['Base Color'].default_value = (1, 1, 1, 1)
eye_left.data.materials.append(eye_mat)
eye_right.data.materials.append(eye_mat)

# Add pupils
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, location=(-0.2, 0.55, 1.25))
pupil_left = bpy.context.object
pupil_left
