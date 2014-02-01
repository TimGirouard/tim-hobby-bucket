# Example of PowerShell Loop

$datetime = Get-Date
$Outputty = ""
$CredArray = @()
$users = @(Get-Content "C:\userlist.txt")
$passwords = @(Get-Content "C:\passy\securestring.txt" | convertto-securestring)
$NumArray = (0,1,2,3,4,5,6)
$Servers = Get-Content "C:\Servers.txt"
$LogFile = "C:\LoginLoopErrors.txt"

"`r`n"+"`r`n"+"Test started at "+$datetime >> $LogFile

Foreach ($num in $NumArray) {

$cred = new-object -typename System.Management.Automation.PSCredential `
         -argumentlist $users[$num], $passwords[$num]


Foreach($srvr in ($Servers)) {

try
{
$ErrorActionPreference = "Stop"
$s = New-PSSession -computerName $srvr -credential $cred
$users[$num]+" connected successfully on "+$srvr >> $LogFile
}
catch
 {
    "Caught a system exception using "+$users[$num]+" to log in to "+$srvr >> $LogFile
    "Exception Message: $($_.Exception.Message)" >> $LogFile
 }
finally
{
$ErrorActionPreference = "Continue"
}
Remove-PSSession $s

Start-Sleep -s 1

}
}
