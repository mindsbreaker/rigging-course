---
title: Rigging
---


## *UI Management*

>:bulb: **Tip:** To avoid losing your settings & UI customization for the current Maya session ... 
YES Maya crash "sometimes" ! Use *'Save Preferences'* in the main menu *'File'*.

### Menus

With the keys **`F2`** >> **`F6`** you can switch between the default [menu sets](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129). (Mod / Rig / Anim / FX / Render)  
Customize your sets with the [Menu Set Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-AAAE82E6-CC81-4D50-A82B-E9A35C2F1D9F).


Useful & main [marking menus](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8BA1A3AA-4C44-4779-8B22-0AAE3627E8EB): 
| *Marking Menu*                  | *Hotkey*            
| --------------------  | --------------------
| Hotbox  | **`Spacebar`**  
| Translate / rotate / scale  | **`W`** / **`E`** / **`R`** and **`LMB`**  
| Global context  | **`RMB`**  
| Object context  | **`Shift`** and **`RMB`**  
| Component context  | **`Ctrl`** and **`RMB`**  
| Poly Brush  | **`O`** and **`LMB`**  
| Poly UV  | **`O`** and **`MMB`**  
| Keyframe  | **`Shift`** + **`S`** and **`LMB`**  

<br>

> :information_source: **Note:**  To toggle Maya's menu bars, use these shortcuts:
Main menu bar ::: **`Ctrl + M`**
Panel menu bar ::: **`Shift + M`**
Panel toolbar ::: **`Ctrl + Shift + M`**

<br>

### Shelves 

Fast create your custom [shelves](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-4A21F741-C9AC-4AE5-897E-B6F8C68ADF90):
- From a tool ::: on the tool icon in the [Tool Box](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-B345E162-0149-4E09-AC98-48DCFC227F33) click & drag with **`MMB`** to the shelf tab.  
- From a menu ::: presse the keys **`Ctrl`** + **`Shift`** and click **`LMB`** on the menu item.  
- From a command ::: select the command in the [Command Line](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-4981A0A5-9418-4274-918C-561E33B0102D) and click & drag with **`MMB`** to the shelf tab.  
- From a script ::: select the script lines in the [Script Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-7C861047-C7E0-4780-ACB5-752CD22AB02E) and click & drag with **`MMB`** to the shelf tab.  
- From a layout ::: in the [Panel Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-41817CDA-CA8D-43F5-AF22-747F8C7956A2) select a layout in the *'layout'* tab and click *'Add to Shelf'*
- From a set ::: with the [Quick Selection Set](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8F030BC7-8F4A-4C01-978B-DECBB807B5B0) tool, name the new set and click *'Add to Shelf'*

>:information_source: **Note:** Use the [Shelf Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-58C25080-5864-4709-BE3A-0543E9D1FCF2) to add double click command & popup menu to your shelves.


<br>

### Workspaces

Use [Workspaces](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-0384C282-3CA1-4587-9775-F7164D3F6980) to manage your tabbed panels & UI configuration.  
In the workspace [layout options](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-B69DF865-D749-43C6-9FD7-BC3E454C0311) you can link a *Menu Set*, a *Hotkey Set* and a *VP2.0 Preset*.  

>:bulb: **Tip:** To avoid bad UI manipulation you can freeze your current workspace.  
Use the lock icon in the upper right corner of Maya's main window.  

<br>

---

<br>

## *Scene Nodes*

Maya has many [types](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-21B83FF0-0435-4087-8C2E-23B420028B71) of nodes that serve any number of different functions.  


### DG Nodes

All nodes in Maya are considered DG nodes, is really at the heart of Maya.  
The relationship between these nodes is organized by the [Dependency Graph](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-51096BC4-32B7-4391-BE39-21641B374745) (DG),  
which describes the hierarchical relationship between connected nodes.  

> :information_source: **Note:**  The DG can be visualized in the *Node Editor* or the *Hypergraph* (Connections mode).

### DAG Nodes

DAG ([Directed Acyclic Graph](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-5029CF89-D420-4236-A7CF-884610828B70)) is essentially the object hierarchy and compose the [scene hierarchy](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-D71F6D34-FA77-43DC-9BF1-481123A682DC).  
It builds on top of DG and provides a way to describe the parent-child relationships.  

Most of the objects displayed in the Maya viewport are DAG nodes.  
These objects consists of a hierarchy in which the shape is a child of the transform.  

> :information_source: **Note:**  You can visualize the DAG in the [*Outliner*](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-4B9A9A3A-83C5-445A-95D5-64104BC47406) or *Hypergraph* (Hierarchy mode).  
This DAG relationship can be modified using the *'Parent'* (**`P`**) or *'Group'* (**`Ctrl + G`**) commands.  

>:bulb: **Tip:** You can traverse the DAG hierarchy using the arrow keys,  
*up-down* to navigate the parent-child relationship, and *left-right* to navigate the siblings.  

#### Transform Node
A transform node defines a transformation in space.  
The transformation can be modified by setting the values of `translation`, `rotation` and `scale` attributes.  
A transform node can have any number of children and at most a single parent.  

> :information_source: **Note:** You can set the *'Inherits Transform'* attribute to *OFF* to ignore the transformation of its ancestors in the hierarchy.  
This can be beneficial if the transforms are used for grouping purposes only.  

>:bulb: **Tip:** You can visualize the transform axis in the viewport by turning *ON* 
in the menu *Display* -> *Transform Display* -> *Local Rotation Axes*

#### Shape Node
Geometry data is stored in this node, such as mesh, nurbsCurve, locator, ...  
They don't contain parenting or transform informations.  
Shape nodes must have a transformation node as a parent to define where the geometry is located in space.  

### DAG Path

A DAG path is expressed in Maya as a string with the nodes in the path separated with the pipe **`|`** character.  
For example: `|pSphere1|pSphereShape1`  

Maya allows DAG nodes to have the same name as long as they are not direct siblings in the DAG hierarchy.  
Therefore a full DAG path provides a unique identifier for a specific DAG node.  

> :information_source: **Note:**  It's generally a good practice to make sure every node has a unique name across the entire scene.  

<br>

---

<br>

## *Transformations*

3D positions and transformations exist within coordinate systems called spaces.  
Transformations change an object’s [position, size, and orientation](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-9622730D-3D21-451C-8BEE-E01BCC979F91) without changing its shape.  

The transformations are relative to the pivot point of an object (or component)  
and are performed along or around the [world, object or local](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-A63AC5C8-8822-42AC-827E-164B5266DA03) axes.

### World vs Object or Local Space

The world space is the absolute position of an object or component in the whole scene.  
Every object in Maya has its own local coordinate system called object space.  
Local space is similar to object space, however it uses the origin and axes of the object’s parent node in the hierarchy of objects.  

### Absolute vs Relative

With **absolute** transform, objects or components are transformed with the scene's origin as the position reference.  
A **relative** transformation is set with the object's pivot as the position reference.  

To set precise values to objects or components, use the input box at the right end of the [Status Line](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-86E5CEDA-4100-40AE-8F95-346206CF8456#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFE) toolbar,  
and choose between *Absolute* or *Relative* transform.

### Reset and Freeze

Use the menu [*Modify*](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-378D7FF6-492F-4DA4-A468-507E6ABF8B58) -> *Reset Transformations* to sets the transformations on the selected objects back to zero.  
To force zero values on transformations and keep object's current position use the the menu *Modify* -> *Freeze Transformations*.

> :warning: **Warn:**  The reset & freeze operations will affect all descendants.
> Don't reset & freeze everything everytime, it's not the clean way.  

### Pivot Point

The [pivot point](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-150B390E-840B-4FE3-B8E9-8DEBCE7CEC97) defines the position around which objects or components are rotated and scaled.  
To activate custom pivot [editing](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-6BCE41D8-07CB-4A99-99CD-1D3986896157) mode, press / hold **`D`** key or press **`Insert`** on the keyboard.  
You can reset the selected object's [pivot to center](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-7F4D1D6F-C2CE-4E31-B82E-FDFA9D492219) with the menu *Modify* -> *Center Pivot*.  

To keep your custom pivot placement in a clean way, use the menu  *Modify* -> *Bake Pivot*.  
The translation & orientation values of the transform node will be updated with the pivot's local offset.  

>:bulb: **Tip:** You can change the pivot / manipulator size by pressing **+** or **-** on the keyboard.  
Use the [snapping](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-E6E866EE-EEE8-4974-A3E7-9AD6ADBB9BCD) mode to help customize pivot placement.

---

<br>

## *Constraints*

With [constraints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-FA047B7D-41AD-4643-9D10-BB1F3B397B4D), you can drive the position, orientation, and scale of one object with the transformations of another object.  
The object that is driven is called the **`Constrained`** or **`Child`** object, and the driver object is called the **`Target`** or **`Parent`** object.  
When a constraint relationship has more than one target object, weights attributes are used to determine the amount of influence.  

An object with a parent constraint does not behave the same as an object with a point and orient constraint.  
When a [Parent](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-29785337-D109-48C5-AFC4-8A7A1D0C246F) constraint is used, rotating the target object(s) affects the constrained object’s rotation along the **world** axis.  
When a [Point](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-79F8E9DC-72B9-4465-8D77-8A69F61D313A) and [Orient](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-ABED0435-54C5-44BE-9E1B-9A2975133695) constraint are used, rotating the target object(s) affects the constrained object’s rotation along its **local** axis.  

> :information_source: **Note:**  To keep offset in the world between constrained & target objects,  
> check the *Maintain Offset* parameter in the constraint option box. (checked by default)  
> ![Maintain Offset](resources/images/maintain_offset.png)

> :warning: **Warn:**  An object can't be constrained to one of it's children, otherwise you'd get a cycle.  
> ![Cycle warning](resources/images/cycle_warning.jpg)

---

<br>

## *Attributes*

Each node defines a series of [attributes](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-D53B9E3D-E6E3-4CC3-A38F-3AA3A09205E5) to accept input data and output the work product.  
These nodes can be connected together through their attributes, therefore constituting the dependency graph (DG).

The attributes defined by the node represent a kind of an interface for the node to the rest of the graph.  
Maya supports attributes of various types, such as simple numeric attributes for integers and floats.  
In addition, complex attributes are supported and can hold data such as string, numeric arrays, and geometry.  

To add [custom attributes](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-EC37B453-05D8-4A60-B6A9-57895363759E) (user) to objects, in the [Attribute Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED) select the menu *Attributes* -> *Add Attributes*,  
or select *Modify* -> *Add Attribute* from the main menu bar.  

Types of value for custom attributes:
- **Vector**: three floating point values.
- **Float**: a single floating point value.
- **Integer**: a single integer value.
- **Boolean**: an on/off switch.
- **String**: a text string.
- **Enum**: a list of choices.

### ChannelBox

The [Channel Box](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-4C954FB2-8B6A-4BBD-9695-DF432616D0D2) is the primary, fastest, and most streamlined tool for editing object attributes.  
It lets you quickly change [attribute values](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-6F862011-4578-40A0-9902-786CA2A44AE5), set keys on keyable attributes, lock or unlock attributes,  
and create *Expressions* & *Driven Key* on attributes.  

Use the [Channel Control](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-5636D755-8FA3-4E72-83AD-A67956727D55) to manage the [keyable & locked](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-5636D755-8FA3-4E72-83AD-A67956727D55) states of attributes.  
In *Channel Box* select the menu *Edit* -> *Channel Control* or from main menu *Windows* -> *General Editors* -> *Channel Control*.  

The following colors represent the state of channels:

| *State*  | *Color*  
| -------  | -------  
| Locked  | ![#5C6874](https://via.placeholder.com/15/5C6874/000000?text=+) - Dark Gray  
| Nonkeyable  | ![#949494](https://via.placeholder.com/15/949494/000000?text=+) - Light Gray  
| Connected  | ![#F1F1A5](https://via.placeholder.com/15/F1F1A5/000000?text=+) - Yellow  
| DrivenKey  | ![#5099DA](https://via.placeholder.com/15/5099DA/000000?text=+) - Dark Blue  
| Constrained  | ![#A3CBF0](https://via.placeholder.com/15/A3CBF0/000000?text=+) - Light Blue  
| Expression  | ![#CBA5F1](https://via.placeholder.com/15/CBA5F1/000000?text=+) - Purple  
| Keyed On Frame  | ![#CD2729](https://via.placeholder.com/15/CD2729/000000?text=+) - Red  
| Keyed Off Frame  | ![#DD727A](https://via.placeholder.com/15/DD727A/000000?text=+) - Dark Pink  
| Key Altered  | ![#FEC9C6](https://via.placeholder.com/15/FEC9C6/000000?text=+) - Light Pink  
| Anim Layer  | ![#50B4AD](https://via.placeholder.com/15/50B4AD/000000?text=+) - Dark Green  
| Blended  | ![#ACF1AC](https://via.placeholder.com/15/ACF1AC/000000?text=+) - Light Green  
| Muted  | ![#BFA182](https://via.placeholder.com/15/BFA182/000000?text=+) - Brown  

### Connections

To connect nodes use the [Connection Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2622D368-1DD5-45BA-9560-93626A5751FD) or the [Node Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-23277302-6665-465F-8579-9BC734228F69).  
In *Channel Box* select the menu *Edit* -> *Connection Editor* or from main menu *Windows* -> *General Editors* -> *Connection Editor*.  

#### Node Editor

>:bulb: **Tip:**  In the *Node Editor* you can connect nodes by creating [connection lines](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-C6E5588F-40A4-4B1E-9C02-A29DA9A4650F) or by [dragging](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-591E9EB3-7B11-456D-92C2-0A6B470079FC) them.  

| *Desciption*  | *Hotkey*  
| ------------  | --------  
| Toggle Node Selected Pins  | **`P`**  
| Show Connected Attrs  | **`2`** (keypad)  
| Show All Attrs  | **`3`** (keypad)  
| Show Custom Attrs  | **`4`** (keypad)  
| Cut the connection link  | **`Alt`** + **`Shift`** + **`LMB`** (drag)  
| Connect default output  | **`MMB`** (drag)  
| Open the *Connection Editor*  | **`Shift`** + **`MMB`** (drag)  

---

<br>

## *Skeleton*

Building a [skeleton](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-906B71D3-C153-4880-A8EF-F9A6D1AE4AD5) is the process of placing and orienting joints to create a system with which you can pose a deformable object.  
If you are creating a skeleton for a human biped, you would place joints at all the major points of articulation in its model.  
(shoulders, knees, elbows, spine and so on)
The [skeleton hierarchy](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-DC88B9A7-593B-427E-9BED-4D7822B0E0B6) is composed of a series of joints and joints chains with hierarchical relationships.  

### Joints and bones

[Joints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-1B59334F-2605-44C3-B584-A55B239A2CBE) are the building blocks of skeletons and their points of articulation.  
Each joint can have one or more bone attached to it, and more than one child joint.  
Bones are only visual cues that illustrate the relationships between joints.  

> :information_source: **Note:**  Joints are specific nodes without shape, they can't be rendered but are displayed in the viewport by  the bones.  

A [joint chain](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-267B988F-4E21-4963-BF6A-478E5F6FEF81) is any group of joints and their bones connected in a series.  
The joint chain begins at the highest joint in the chain’s hierarchy, and its bones are drawn pointing down the chain.  


> :warning: **Warn:**  You can't create a mirrored duplicate of a joint chain with a scale of -1. Use *Skeleton -> Mirror Joint* instead.  

---

<br>

## *Deformations*

### Skinning

[Skinning](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-EFE68C08-9ADA-4355-8203-5D1D109DCC82) is the process of binding a modeled surface to a skeleton.  
You can bind any model to its skeleton using a [skinCluster](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E292C8A-388A-4E77-B42D-165F1C9E1E5F) node.  
And the model will follow or react to the transformations of the skeleton’s joints and bones.  

### Smooth Skinning

Smooth deformations are provided by enabling several joints to influence the same deformable object points.  
The smoothing effects around joints are automatically set up when you [bind skin](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8DBA9E62-3854-4348-A0AD-1F981ECEA54F).  
Maya offers three [methods](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-630C335C-B63E-4F2E-A4A4-AEA1DD00B0D6) to smooth skin a model:  

- Classic Linear
- Dual Quaternion
- Weight Blended (blend of both methods).


> :information_source: **Note:**  The *Dual Quaternion* method has better deformation and keep model's volume.  

### Edit Weights

You can directly modify the values of individual skin point weights using the [Component Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-B698CC5D-2771-488E-98E8-2D4E31DB3B2D).  
The *Component Editor* lets you easily set specific skin point weights to particular values.

If you want to shape the deformation directly and are not concerned with specific values,  
you can instead paint weights with the [Paint Skin Weights Tool](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-99189E9D-237F-471E-A02C-BE6593B4828B).

---

<br>