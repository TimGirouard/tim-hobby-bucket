$users = @(Get-Content "C:\userlist.txt","C:\passy\securestring.txt")
#$passwords = @(Get-Content "C:\passy\securestring.txt" | convertto-securestring)
$users[0]
$users[1]