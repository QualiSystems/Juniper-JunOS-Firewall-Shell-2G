

[![Build status](https://travis-ci.org/QualiSystems/Juniper-JunOS-Firewall-Shell-2G.svg?branch=dev)](https://travis-ci.org/QualiSystems/Juniper-JunOS-Firewall-Shell-2G)
[![Coverage Status](https://coveralls.io/repos/github/QualiSystems/Juniper-JunOS-Firewall-Shell-2G/badge.svg)](https://coveralls.io/github/QualiSystems/Juniper-JunOS-Firewall-Shell-2G)
[![PyPI version](https://badge.fury.io/py/Juniper-JunOS-Firewall-Shell-2G.svg)](https://badge.fury.io/py/Juniper-JunOS-Firewall-Shell-2G)
[![Dependency Status](https://dependencyci.com/github/QualiSystems/Juniper-JunOS-Firewall-Shell-2G/badge)](https://dependencyci.com/github/QualiSystems/Juniper-JunOS-Firewall-Shell-2G)
[![Stories in Ready](https://badge.waffle.io/QualiSystems/Juniper-JunOS-Firewall-Shell-2G.svg?label=ready&title=Ready)](http://waffle.io/QualiSystems/Juniper-JunOS-Firewall-Shell-2G)

![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/cloudshell_logo.png)

# **Juniper JunOS Firewall 2G Shell**  

Release date: April 2017

Shell version: 1.0.0

Document version: 1.0.0

# In This Guide

* [Overview](#overview)
* [Downloading the Shell](#downloading-the-shell)
* [Importing and Configuring the Shell](#importing-and-configuring-the-shell)
* [Updating Python Dependencies for Shells](#updating-python-dependencies-for-shells)
* [Typical Workflows](#typical-workflows)
* [References](#references)


# Overview
A shell integrates a device model, application or other technology with CloudShell. A shell consists of a data model that defines how the device and its properties are modeled in CloudShell, along with automation that enables interaction with the device via CloudShell.

### Networking Shells
CloudShell's networking shells provide L2 or L3 connectivity between resources and/or Apps.

### **Juniper JunOS Firewall 2G Shell**
The **Juniper JunOS Firewall 2G** shell provides you with connectivity and management capabilities such as device structure discovery and power management for the **Juniper JunOS Firewall**. 

For more information on the **Juniper JunOS Firewall**, see the official **Juniper** product documentation.

### Standard version
**Juniper JunOS Firewall 2G Shell 1.0.0** is based on the Firewall Shell Standard version **3.0.0**.

For detailed information about the shell’s structure and attributes, see the [Firewall Shell Standard](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/firewall_standard.md) in GitHub.

### Supported OS

▪ JunOS


### Requirements

Release: **Juniper JunOS Firewall 2G Shell 1.0.0**

▪ CloudShell version: 8.0 and above

▪ Certified models: Juniper SRX220

### Data Model

The shell's data model includes all shell metadata, families, and attributes.

#### **Juniper JunOS Firewall Families and Models**

The Juniper JunOS Firewall families and models are listed in the following table:

|Family|Model|Description|
|:---|:---|:---|
|CS_ Firewall|Juniper JunOS Firewall 2G|Generic Juniper JunOS Firewall 2 Generation|
|CS_Chassis|Generic Chassis|Default Firewall chassis|
|CS_Module|Generic Module|Modules located on the chassis|
|CS_SubModule|Generic Sub Module|Sub modules|
|CS_Port|Generic Port|Interface|
|CS_PortChannel|Generic Port Channel|Group of interfaces|
|CS_PowerPort|Generic Power Port|Power Supply module|


#### **Juniper JunOS Firewall 2G Shell Attributes**

The attribute names and types are listed in the following section of the Firewall Shell Standard:

https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/firewall_standard.md#attributes

### Automation
This section describes the automation (drivers) associated with the data model. The shell’s driver is provided as part of the shell package. There are two types of automation processes, Autoload and Resource.  Autoload is executed when creating the resource in the **Inventory** dashboard, while resource commands are run in the sandbox.

The following commands are associated with the Juniper JunOS Firewall shell:

|Command|Description|
|:-----|:-----|
|Autoload|Discovers the chassis, its hierarchy and attributes when creating the resource. The command can be rerun in the Inventory dashboard and not in the sandbox, as for other commands.|
|Health Check|Checks if the device is powered-on and connectable.|
|Run Custom Command|Executes a custom command on the device.<br>Command Input:</br><li>**Command** (Mandatory): The command to run. Commands requiring a response are not supported.</br>|
|Save|Creates a configuration file and saves it to the provided destination.<br>Command Inputs:</br><li>**Folder Path** (Optional): Path where the configuration file will be saved. This field is optional. If empty, the value will be taken from the **Backup Location** attribute on the root resource. The path should include the protocol type, for TFTP use *tftp://server_address/folder1*, for FTP use *ftp://username:password@server_address/folder1*.</br><li>**Configuration Type**: Specify whether the file should update the **Startup** or **Running** config.<br>- **Startup**: Configuration that is loaded when the device boots or powers up. <br>- **Running**: Current configuration in the device. It may have been modified since the last boot. If left empty, the **Running** default configuration type will be used.<br><li>**VRF Management Name** (Optional): Virtual routing and forwarding is used to share the same/overlapping sub-net on the same core. If left empty, the value of the **VRF Management Name** attribute on the root model, will be used.| 
|Restore|Restores a configuration from the saved file.<br>Command Inputs:</br><li>**Path**: Full path from which the configuration file will be restored. The path should include the protocol type, for TFTP use *tftp://asdf*, for FTP use *ftp://username:password@server_address/folder1/file1.bin*.</br><li>**Configuration Type**: Specify whether the file should update the **Startup** or **Running** config.<br>- **Startup**: Configuration that is loaded when the device boots or powers up. Startup configuration is not supported on all switches.<br>- **Running**: Current configuration in the device. It may have been modified since the last boot.<br><li>**Restore Method**: Determines whether the restore should **Append** or **Override** the current configuration. <br>If left empty, restore will **Override** the current configuration.<br><li>**VRF Management Name** (Optional):  Virtual routing and forwarding is used to share same/overlapping sub-net on the same core. If left empty, the value of the **VRF Management Name** attribute on the root model, will be used.|
|Load Firmware|Uploads and updates the firmware on the resource. <br>Command Inputs:</br><li>**Path**: Path to tftp://server where the firmware file is stored. The path should include the protocol type, for TFTP, use *tftp://server_address/folder1/file1.bin*, for FTP use *ftp://username:password@server_address/folder1/file1.bin*."<br><li>**VRF Management Name** (Optional): Virtual routing and forwarding is used to share same/overlapping sub-net on the same core. If left empty, the value of the **VRF Managament Name** attribute on the root model will be used.|

# Downloading the Shell
The **Juniper JunOS Firewall 2G** shell is available from the [Quali Community Integrations](https://community.quali.com/integrations) page. 

Download the files into a temporary location on your local machine. 

The shell comprises:

|File name|Description|
|:---|:---|
|JuniperJunosFirewallShell2G.zip|Juniper JunOS Firewall 2G shell package|
|cloudshell-firewall-juniper-junos-2-gen-dependencies-package-1.0.X.zip|Shell Python dependencies (for offline deployments only)|

# Importing and Configuring the Shell
This section describes how to import the **Juniper JunOS Firewall 2G 1.0.0** shell and configure and modify the shell’s devices.

### Importing the shell into CloudShell

**To import the shell into CloudShell:**
  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  
  2. In CloudShell Portal, as Global administrator, open the **Manage – Shells** page.
  
  3. Click **Import**.
  
  4. In the dialog box, navigate to the shell's zip package, select it and click **Open**.

The shell is displayed in the **Shells** page and can be used by domain administrators in all CloudShell domains to create new inventory resources, as explained in [Adding Inventory Resources](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Add-Rsrc-Tmplt.htm?Highlight=adding%20inventory%20resources). 

### Offline installation of a shell

**Note:** Offline installation instructions are relevant only if CloudShell Execution Server has no access to PyPi. You can skip this section if your execution server has access to PyPi. For additional information, see the online help topic on offline dependencies.

In offline mode, import the shell into CloudShell and place any dependencies in the appropriate dependencies folder. The dependencies folder may differ, depending on the CloudShell version you are using:

* For CloudShell version 8.3 and above, see [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository).

* For CloudShell version 8.2, perform the appropriate procedure: [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository) or [Setting the python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

* For CloudShell versions prior to 8.2, see [Setting the python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

### Adding shell and script packages to the local PyPi Server repository
If your Quali Server and/or execution servers work offline, you will need to copy all required Python packages, including the out-of-the-box ones, to the PyPi Server's repository on the Quali Server computer (by default *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository*).

For more information, see [Configuring CloudShell to Execute Python Commands in Offline Mode](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=Configuring%20CloudShell%20to%20Execute%20Python%20Commands%20in%20Offline%20Mode).

**To add Python packages to the local PyPi Server repository:**
  1. If you haven't created and configured the local PyPi Server repository to work with the execution server, perform the steps in [Add Python packages to the local PyPi Server repository (offline mode)](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=offline%20dependencies#Add). 
  
  2. For each shell or script you add into CloudShell, do one of the following (from an online computer):
      * Connect to the Internet and download each dependency specified in the *requirements.txt* file with the following command: 
`pip download -r requirements.txt`. 
     The shell or script's requirements are downloaded as zip files.

      * In the [Quali Community's Integrations](https://community.quali.com/integrations) page, locate the shell and click the shell's **Download** link. In the page that is displayed, from the Downloads area, extract the dependencies package zip file.

3. Place these zip files in the local PyPi Server repository.
 
### Setting the python PythonOfflineRepositoryPath configuration key
Before PyPi Server was introduced as CloudShell’s python package management mechanism, the `PythonOfflineRepositoryPath` key was used to set the default offline package repository on the Quali Server machine, and could be used on specific Execution Server machines to set a different folder. 

**To set the offline python repository:**
1. Download the *cloudshell-firewall-juniper-junos-2-gen-dependencies-package-1.0.X.zip* file, see [Downloading the Shell](#downloading-the-shell).

2. Unzip it to a local repository. Make sure the execution server has access to this folder. 

3.  On the Quali Server machine, in the *~\CloudShell\Server\customer.config* file, add the following key to specify the path to the default python package folder (for all Execution Servers):  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

4. If you want to override the default folder for a specific Execution Server, on the Execution Server machine, in the *~TestShell\Execution Server\customer.config* file, add the following key:  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

5. Restart the Execution Server.

### Configuring a new resource
This section explains how to create a new resource from the shell.

In CloudShell, the component that models the device is called a resource. It is based on the shell that models the device and allows the CloudShell user and API to remotely control the device from CloudShell.

You can also modify existing resources, see [Managing Resources in the Inventory](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Mng-Rsrc-in-Invnt.htm?Highlight=managing%20resources).

**To create a resource for the device:**
  1. In the CloudShell Portal, in the **Inventory** dashboard, click **Add New**. 
     ![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/create_a_resource_device.png)
     
  2. From the list, select **Juniper JunOS Firewall 2G**.
  
  3. Enter the **Name** and **IP address** of the **Juniper JunOS Firewall**.
  
  4. Click **Create**.
  
  5. In the **Resource** dialog box, enter the device's settings, see [Juniper JunOS Firewall 2G Shell Attributes](#juniper-junos-firewall-2g-shell-attributes). Make sure to fill in the device's SNMP version and credentials.
  
  6. Click **Continue**.

CloudShell validates the device’s settings and updates the new resource with the device’s structure.

# Updating Python Dependencies for Shells
This section explains how to update your Python dependencies folder. This is required when you upgrade a shell that uses new/updated dependencies. It applies to both online and offline dependencies.

### Updating offline Python dependencies
**To update offline Python dependencies:**
1. Download the latest Python dependencies package zip file locally.

2. Extract the zip file to the suitable offline package folder(s). 

3. Restart any execution server that has a live instance of the relevant driver or script. This requires running the Execution Server's configuration wizard, as explained in the [Configure the Execution Server](http://help.quali.com/doc/9.0/CS-Install/content/ig/configure%20cloudshell%20products/cfg-ts-exec-srver.htm?Highlight=configure%20the%20execution%20server) topic of the CloudShell Suite Installation guide. 

### Updating online Python dependencies
In online mode, the execution server automatically downloads and extracts the appropriate dependencies file to the online Python dependencies repository every time a new instance of the driver or script is created.

**To update online Python dependencies:**
* If there is a live instance of the shell's driver or script, restart the execution server, as explained above. If an instance does not exist, the execution server will download the Python dependencies the next time a command of the driver or script runs.

# Typical Workflows 

#### **Workflow 1** - *Save configuration* 
1. In CloudShell Portal, reserve the **Juniper JunOS** resource.

2. Run the **Save** resource command.

3. In the command inputs field, enter the following information:
	* **Folder Path**: For example, *tftp://ipaddress/shared folder*.
	* **Configuration Type**: **Startup** or **Running**.
	* **VRF Management Name**: Provide the VRF Management name, if relevant.
	
4. Click **Run**.

The **Startup** or **Running** configuration is saved to a file named *<ResourceName>-<startup/running-config>-<timestamp>*, which will be stored in the folder path you entered above.

#### **Workflow 2** - *Restore configuration* 
1. In CloudShell Portal, reserve the **Juniper JunOS** resource.

2. Run the **Restore** resource command.

3. In the command inputs field, enter the following information:
	* **Path**: (Mandatory) Enter the full path of the configuration file. 
	* **Restore Method**: (Optional) Possible values are **Override** or **Append**. If left empty, the **Override** method is used. 
	* **Configuration Type**: (Mandatory) Possible values are **Startup** or **Running**.
	* **VRF Management Name**: (Optional) Provide the VRF Management name, if relevant.
	
4. Click **Run**.

#### **Workflow 3** - *Load firmware* 
1. In CloudShell portal, reserve the **Juniper JunOS** resource.

2. Run the **Load Firmware** resource command. 

3. In the command inputs field, enter the following information:
	* **Remote Host** (Mandatory). Enter the full path to the firmware file on the remote host, for example: tftp://10.1.1.1/ios12.SE1-smp-k8.bin.
	* **File Path** (Mandatory). Enter the destination filename on the device itself, for example: *bootflash:/ios12.SE1-smp-k8.bin*.
	
4. Click **Run**.

# References
To download and share integrations, see [Quali Community's Integrations](https://community.quali.com/integrations). 

For instructional training and documentation, see [Quali University](https://www.quali.com/university/).

To suggest an idea for the product, see [Quali's Idea box](https://community.quali.com/ideabox). 

To connect with Quali users and experts from around the world, ask questions and discuss issues, see [Quali's Community forums](https://community.quali.com/forums). 
 
