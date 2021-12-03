---
title: Transformations
---

3D positions and transformations exist within coordinate systems called spaces.  
Transformations change an object’s [position, size, and orientation](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-9622730D-3D21-451C-8BEE-E01BCC979F91) without changing its shape.  

The transformations are relative to the pivot point of an object (or component)  
and are performed along or around the [world, object or local](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-A63AC5C8-8822-42AC-827E-164B5266DA03) axes.

___
### World vs Object / Local Space

The world space is the absolute position of an object or component in the whole scene.  
Every object in Maya has its own local coordinate system called object space.  
Local space is similar to object space, however it uses the origin and axes of the object’s parent node in the hierarchy of objects.  

___
### Absolute vs Relative

With **absolute** transform, objects or components are transformed with the scene's origin as the position reference.  
A **relative** transformation is set with the object's pivot as the position reference.  

To set precise values to objects or components, use the input box at the right end of the [Status Line](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-86E5CEDA-4100-40AE-8F95-346206CF8456#WS17956D7ADBC6E73662C853C8117AE30BF5B-7FFE) toolbar,  
and choose between *Absolute* or *Relative* transform.

___
### Reset and Freeze

Use the menu [*Modify*](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-378D7FF6-492F-4DA4-A468-507E6ABF8B58) -> *Reset Transformations* to sets the transformations on the selected objects back to zero.  
To force zero values on transformations and keep object's current position use the the menu *Modify* -> *Freeze Transformations*.

! The reset & freeze operations will affect all descendants. Don't reset & freeze everything everytime, it's not the clean way.  

___
### Pivot Point

The [pivot point](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-150B390E-840B-4FE3-B8E9-8DEBCE7CEC97) defines the position around which objects or components are rotated and scaled.  
To activate custom pivot [editing](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-6BCE41D8-07CB-4A99-99CD-1D3986896157) mode, press / hold **`D`** key or press **`Insert`** on the keyboard.  
You can reset the selected object's [pivot to center](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-7F4D1D6F-C2CE-4E31-B82E-FDFA9D492219) with the menu *Modify* -> *Center Pivot*.  

To keep your custom pivot placement in a clean way, use the menu  *Modify* -> *Bake Pivot*.  
The translation & orientation values of the transform node will be updated with the pivot's local offset.  

!!! You can change the pivot / manipulator size by pressing **+** or **-** on the keyboard. Use the [snapping](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-E6E866EE-EEE8-4974-A3E7-9AD6ADBB9BCD) mode to help customize pivot placement.