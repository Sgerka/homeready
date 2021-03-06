# -*- coding:utf-8 -*-

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
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110- 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Stephen Leger (s-leger)
#
# ----------------------------------------------------------
import bpy
from bpy.types import Operator, PropertyGroup, Mesh, Panel
from bpy.props import (
    FloatProperty, IntProperty, BoolProperty,
    CollectionProperty, EnumProperty
)
from .bmesh_utils import BmeshEdit as bmed
# from .materialutils import MaterialUtils
from mathutils import Vector, Matrix
from math import sin, cos, pi
from .archipack_manipulator import Manipulable
from .archipack_i18n import Archipacki18n
from .archipack_object import ArchipackCreateTool, ArchipackObject, ArchipackPanel


def update(self, context):
    self.update(context)


class archipack_truss(ArchipackObject, Manipulable, PropertyGroup):
    tabs: EnumProperty(
        options={'SKIP_SAVE'},
        description="Display settings",
        name='Ui tabs',
        items=(
            ('MAIN', 'Main', 'Display main settings', 'NONE', 0),
            ('MATERIALS', '', 'Display materials settings', 'MATERIAL', 1)
        ),
        default='MAIN',
    )
    truss_type: EnumProperty(
        name="Type",
        items=(
            ('1', 'Prolyte E20', 'Prolyte E20', 0),
            ('2', 'Prolyte X30', 'Prolyte X30', 1),
            ('3', 'Prolyte H30', 'Prolyte H30', 2),
            ('4', 'Prolyte H40', 'Prolyte H40', 3),
            ('5', 'OPTI Trilite 100', 'OPTI Trilite 100', 4),
            ('6', 'OPTI Trilite 200', 'OPTI Trilite 200', 5),
            ('7', 'User defined', 'User defined', 6)
        ),
        default='2',
        update=update
    )
    z: FloatProperty(
        name="Height",
        default=2.0, min=0.01, precision=5,
        unit='LENGTH', subtype='DISTANCE',
        update=update
    )
    segs: IntProperty(
        name="Segs",
        default=6, min=3,
        update=update
    )
    master_segs: IntProperty(
        name="Master Segs",
        default=1, min=1,
        update=update
    )
    master_count: IntProperty(
        name="Masters",
        default=3, min=2,
        update=update
    )
    entre_axe: FloatProperty(
        name="Distance",
        default=0.239, min=0.001, precision=5,
        unit='LENGTH', subtype='DISTANCE',
        update=update
    )
    master_radius: FloatProperty(
        name="Radius",
        default=0.02415, min=0.0001, precision=5,
        unit='LENGTH', subtype='DISTANCE',
        update=update
    )
    slaves_radius: FloatProperty(
        name="Subs radius",
        default=0.01, min=0.0001, precision=5,
        unit='LENGTH', subtype='DISTANCE',
        update=update
    )

    auto_update: BoolProperty(
            options={'SKIP_SAVE'},
            default=True,
            update=update
            )

    def setup_manipulators(self):
        if len(self.manipulators) < 1:
            s = self.manipulators.add()
            s.prop1_name = "z"
            s.type_key = 'SIZE'
            s.normal = Vector((0, 1, 0))

    def docylinder(self, faces, verts, radius, segs, tMt, tMb, tM, add=False):
        segs_step = 2 * pi / segs
        tmpverts = [0 for i in range(segs)]
        if add:
            cv = len(verts) - segs
        else:
            cv = len(verts)
        for seg in range(segs):
            seg_angle = pi / 4 + seg * segs_step
            tmpverts[seg] = radius * Vector((sin(seg_angle), -cos(seg_angle), 0))

        if not add:
            for seg in range(segs):
                verts.append(tM @ tMb @ tmpverts[seg])

        for seg in range(segs):
            verts.append(tM @ tMt @ tmpverts[seg])

        for seg in range(segs - 1):
            f = cv + seg
            faces.append((f + 1, f, f + segs, f + segs + 1))
        f = cv
        faces.append((f, f + segs - 1, f + 2 * segs - 1, f + segs))

    def update(self, context):

        o = self.find_in_selection(context, self.auto_update)

        if o is None:
            return

        self.setup_manipulators()

        if self.truss_type == '1':
            EntreAxe = 0.19
            master_radius = 0.016
            slaves_radius = 0.005
        elif self.truss_type == '2':
            EntreAxe = 0.239
            master_radius = 0.0255
            slaves_radius = 0.008
        elif self.truss_type == '3':
            EntreAxe = 0.239
            master_radius = 0.02415
            slaves_radius = 0.008
        elif self.truss_type == '4':
            EntreAxe = 0.339
            master_radius = 0.02415
            slaves_radius = 0.01
        elif self.truss_type == '5':
            EntreAxe = 0.15
            master_radius = 0.0127
            slaves_radius = 0.004
        elif self.truss_type == '6':
            EntreAxe = 0.200
            master_radius = 0.0254
            slaves_radius = 0.00635
        elif self.truss_type == '7':
            EntreAxe = self.entre_axe
            master_radius = min(0.5 * self.entre_axe, self.master_radius)
            slaves_radius = min(0.5 * self.entre_axe, self.master_radius, self.slaves_radius)

        master_sepang = (pi * (self.master_count - 2) / self.master_count) / 2
        radius = (EntreAxe / 2) / cos(master_sepang)
        master_step = pi * 2 / self.master_count

        verts = []
        faces = []

        if self.master_count == 4:
            master_rotation = pi / 4   # 45.0
        else:
            master_rotation = 0.0

        slaves_width = 2 * radius * sin(master_step / 2)
        slaves_count = int(self.z / slaves_width)
        slave_firstOffset = (self.z - slaves_count * slaves_width) / 2
        master_z = self.z / self.master_segs

        for master in range(self.master_count):

            master_angle = master_rotation + master * master_step

            tM = Matrix([
                [1, 0, 0, radius * sin(master_angle)],
                [0, 1, 0, radius * -cos(master_angle)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

            tMb = Matrix([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, self.z],
                [0, 0, 0, 1]])

            for n in range(1, self.master_segs + 1):
                tMt = Matrix([
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, self.z - n * master_z],
                    [0, 0, 0, 1]])
                self.docylinder(faces, verts, master_radius, self.segs, tMt, tMb, tM, add=(n > 1))

            if self.master_count < 3 and master == 1:
                continue

            ma = master_angle + master_sepang

            tM = Matrix([
                [cos(ma), sin(ma), 0, radius * sin(master_angle)],
                [sin(ma), -cos(ma), 0, radius * -cos(master_angle)],
                [0, 0, 1, slave_firstOffset],
                [0, 0, 0, 1]])

            if int(self.truss_type) < 5:
                tMb = Matrix([
                    [1, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1]])
                tMt = Matrix([
                    [1, 0, 0, 0],
                    [0, 0, 1, -slaves_width],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1]])
                self.docylinder(faces, verts, slaves_radius, self.segs, tMt, tMb, tM)

            tMb = Matrix([
                [1, 0, 0, 0],
                [0, 1.4142, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

            for n in range(1, slaves_count + 1):
                tMt = Matrix([
                    [1, 0, 0, 0],
                    [0, 1.4142, 0, -(n % 2) * slaves_width],
                    [0, 0, 1, n * slaves_width],
                    [0, 0, 0, 1]])
                self.docylinder(faces, verts, slaves_radius, self.segs, tMt, tMb, tM, add=(n > 1))

            if int(self.truss_type) < 5:
                tMb = Matrix([
                    [1, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 0, slaves_count * slaves_width],
                    [0, 0, 0, 1]])
                tMt = Matrix([
                    [1, 0, 0, 0],
                    [0, 0, 1, -slaves_width],
                    [0, 1, 0, slaves_count * slaves_width],
                    [0, 0, 0, 1]])
                self.docylinder(faces, verts, slaves_radius, self.segs, tMt, tMb, tM)

        bmed.buildmesh(o, verts, faces, weld=False)
        self.shade_smooth(context, o, 1.15)
        self.manipulators[0].set_pts([(0, 0, 0), (0, 0, self.z), (1, 0, 0)])

        self.restore_context(context)


class ARCHIPACK_PT_truss(ArchipackPanel, Archipacki18n, Panel):
    """Archipack Truss"""
    bl_idname = "ARCHIPACK_PT_truss"
    bl_label = "Truss"

    @classmethod
    def poll(cls, context):
        return archipack_truss.poll(context.active_object)

    def draw(self, context):
        o = context.active_object
        d = archipack_truss.datablock(o)

        if d is None:
            return

        layout = self.layout

        self.draw_common(context, layout)

        self.draw_prop(context, layout, layout, d, 'tabs', expand=True)

        box = layout.box()
        if d.tabs == 'MAIN':
            self.draw_prop(context, layout, box, d, 'truss_type')
            self.draw_prop(context, layout, box, d, 'z')
            self.draw_prop(context, layout, box, d, 'segs')
            self.draw_prop(context, layout, box, d, 'master_segs')
            self.draw_prop(context, layout, box, d, 'master_count')
            if d.truss_type == '7':
                self.draw_prop(context, layout, box, d, 'master_radius')
                self.draw_prop(context, layout, box, d, 'slaves_radius')
                self.draw_prop(context, layout, box, d, 'entre_axe')

        elif d.tabs == 'MATERIALS':
            if "archipack_material" in o:
                o.archipack_material[0].draw(context, box)


class ARCHIPACK_OT_truss(ArchipackCreateTool, Operator):
    bl_idname = "archipack.truss"
    bl_label = "Truss"
    bl_description = "Create Truss at cursor location"

    def create(self, context):
        m = bpy.data.meshes.new("Truss")
        o = bpy.data.objects.new("Truss", m)
        d = m.archipack_truss.add()
        # make manipulators selectable
        # d.manipulable_selectable = True
        # Link object into scene
        self.link_object_to_scene(context, o)
        o.color = (0, 1, 0, 1)

        # select and make active
        self.select_object(context, o, True)

        self.add_material(context, o, material="DEFAULT")
        self.load_preset(d)
        return o


    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if context.mode == "OBJECT":
            bpy.ops.object.select_all(action="DESELECT")
            o = self.create(context)
            o.location = self.get_cursor_location(context)
            # select and make active
            self.add_to_reference(context, o)
            self.select_object(context, o, True)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archipack: Option only valid in Object mode")
            return {'CANCELLED'}


def register():
    bpy.utils.register_class(archipack_truss)
    Mesh.archipack_truss = CollectionProperty(type=archipack_truss)
    bpy.utils.register_class(ARCHIPACK_PT_truss)
    bpy.utils.register_class(ARCHIPACK_OT_truss)


def unregister():
    bpy.utils.unregister_class(archipack_truss)
    del Mesh.archipack_truss
    bpy.utils.unregister_class(ARCHIPACK_PT_truss)
    bpy.utils.unregister_class(ARCHIPACK_OT_truss)
