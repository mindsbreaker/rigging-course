---
title: Attributes
---

Each node defines a series of [attributes](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-D53B9E3D-E6E3-4CC3-A38F-3AA3A09205E5) to accept input data and output the work product.  
These nodes can be connected together through their attributes, therefore constituting the dependency graph (DG).

The attributes defined by the node represent a kind of an interface for the node to the rest of the graph.  
Maya supports attributes of various types, such as simple numeric attributes for integers and floats.  
In addition, complex attributes are supported and can hold data such as string, numeric arrays, and geometry.  

To add [custom attributes](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-EC37B453-05D8-4A60-B6A9-57895363759E) (user) to objects, in the [Attribute Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED) select the menu **Attributes** -> **Add Attributes**,  
or select **Modify** -> **Add Attribute** from the main menu bar.  

Types of value for custom attributes:
- **Vector**: three floating point values.
- **Float**: a single floating point value.
- **Integer**: a single integer value.
- **Boolean**: an on/off switch.
- **String**: a text string.
- **Enum**: a list of choices.

___
### ChannelBox

The [Channel Box](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-4C954FB2-8B6A-4BBD-9695-DF432616D0D2) is the primary, fastest, and most streamlined tool for editing object attributes.  
It lets you quickly change [attribute values](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-6F862011-4578-40A0-9902-786CA2A44AE5), set keys on keyable attributes, lock or unlock attributes,  
and create **Expressions** & **Driven Key** on attributes.  

Use the [Channel Control](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-5636D755-8FA3-4E72-83AD-A67956727D55) to manage the keyable & locked states of attributes.  
In **Channel Box** select the menu **Edit** -> **Channel Control** or from main menu **Windows** -> **General Editors** -> **Channel Control**.  

The following colors represent the state of channels:

| *State* | *Color* |
|:--------- |:---------- |
| Locked | <i class="fa fa-square" style="color:#5C6874;"></i> - Dark Gray 
| Nonkeyable | <i class="fa fa-square" style="color:#949494;"></i> - Light Gray 
| Connected | <i class="fa fa-square" style="color:#F1F1A5;"></i> - Yellow 
| DrivenKey | <i class="fa fa-square" style="color:#5099DA;"></i> - Dark Blue 
| Constrained | <i class="fa fa-square" style="color:#A3CBF0;"></i> - Light Blue 
| Expression | <i class="fa fa-square" style="color:#CBA5F1;"></i> - Purple 
| Keyed On Frame | <i class="fa fa-square" style="color:#CD2729;"></i> - Red 
| Keyed Off Frame | <i class="fa fa-square" style="color:#DD727A;"></i> - Dark Pink 
| Key Altered | <i class="fa fa-square" style="color:#FEC9C6;"></i> - Light Pink 
| Anim Layer | <i class="fa fa-square" style="color:#50B4AD;"></i> - Dark Green 
| Blended | <i class="fa fa-square" style="color:#ACF1AC;"></i> - Light Green 
| Muted | <i class="fa fa-square" style="color:#BFA182;"></i> - Brown 

___
### Connections

To connect nodes use the [Connection Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2622D368-1DD5-45BA-9560-93626A5751FD) or the [Node Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-23277302-6665-465F-8579-9BC734228F69).  
In **Channel Box** select the menu **Edit** -> **Connection Editor** or from main menu **Windows** -> **General Editors** -> **Connection Editor**.  

#### Node Editor

!!!  In the **Node Editor** you can connect nodes by creating [**connection lines**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-C6E5588F-40A4-4B1E-9C02-A29DA9A4650F) or by [**dragging**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-591E9EB3-7B11-456D-92C2-0A6B470079FC) them.  

| *Desciption* | *Hotkey* |
|:---------------- |:------------ |
| Toggle Node Selected Pins | **`P`**  
| Show Connected Attrs | **`2`** (keypad)  
| Show All Attrs | **`3`** (keypad)  
| Show Custom Attrs | **`4`** (keypad)  
| Cut the connection link | **`Alt`** + **`Shift`** + **`LMB`** (drag)  
| Connect default output | **`MMB`** (drag)  
| Open the *Connection Editor* | **`Shift`** + **`MMB`** (drag)  