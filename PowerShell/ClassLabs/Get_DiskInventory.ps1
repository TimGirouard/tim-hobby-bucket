<#
.Synopsis
Get-DiskInventory takes a $computername and $drivetype parameter,
and then returns the device's drive letter, free space, total
size, and percentage of free space.

.Description
This information is gathered from the Win32_LogicalDisk WMI.

.Parameter computername
The computer name, or names, to query.  Default: localhost

.Parameter drivetyp
The drive type to query. 3 is a fixed disk, and is the default.

.Example
Get-DiskInventory -computername SERVER-R2 -drivetype 3
#>

param (
$computername = 'localhost',
$drivetype = 3
)
Get-WmiObject -class Win32_LogicalDisk `
-ComputerName $computername -filter "drivetype=$drivetype" |
sort-object -Property deviceid | Format-Table -property DeviceID,
@{n='FreeSpace(MB)';e={$_.FreeSpace / 1MB -as [int]}},
@{n='Size(GB)';e={$_.Size / 1GB -as [int]}},
@{n='%Free';e={$_.FreeSpace / $_.Size * 100 -as [int]}}