<#

.Synopsis
Get_Builds finds all builds that exceed a certain number, $buildmin,
on a computer, $computername.

.Description
This information is gathered using the Win32_OperatingSystem WMI.

.Parameter computername
The computer name, or names, to query.  By default, it is 'localhost'.

.Parameter buildmin
The minimum buildnumber to be entered into the table of all builds.
By default, it is 7600.

.Example
Get_Builds -computer WIN2K8R2-PSTEST -build 7600

#>
param (
$computername = 'localhost',
$buildmin = 7600
)
Get-WmiObject -class win32_operatingsystem `
-ComputerName $computername | 
Where-Object { $_.BuildNumber -ge $buildmin } | 
Format-Table __SERVER,Caption,BuildNumber,ServicePackMajorVersion,
@{n='BIOSSerial';e={Get-WmiObject -class Win32_BIOS -ComputerName $_.__SERVER | Select-Object -ExpandProperty SerialNumber }}