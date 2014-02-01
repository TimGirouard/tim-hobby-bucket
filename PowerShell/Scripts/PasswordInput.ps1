$userdoc = Get-Content "C:\userlist.txt"
read-host -assecurestring | convertfrom-securestring > C:\passy\securestring.txt
foreach($user in $userdoc)
{
read-host -assecurestring | convertfrom-securestring >> C:\passy\securestring.txt
}