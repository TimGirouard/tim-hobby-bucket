# Best practice: avoid mistyped variable names
set-psdebug -strict

$datetime = Get-Date
$users = @(Get-Content "C:\userlist.txt")
$passwords = @(Get-Content "C:\passy\securestring.txt" | convertto-securestring)
$cred = new-object -typename System.Management.Automation.PSCredential `
         -argumentlist $users[0], $passwords[0]
         
#$Servers = Get-QADComputer -sizelimit 0 | where {$_.Name -like "*myserver*"} | select Name
$Servers = Get-Content "C:\Servers.txt"
$LogFile = "C:\BasicPCStats.txt"

new-variable -name CPULIMIT -value 50
new-variable -name MEMLIMIT -value 50
new-variable -name DISKLIMIT -value 80

#Write-Host "Test started at "+$datetime
"`r`n"+"`r`n"+"Test started at "+$datetime >> $LogFile

foreach($Server in ($Servers)){
    #CPU Info
    $cpu = Get-WmiObject Win32_processor -ComputerName $Server -Credential $cred
    # TODO: add error handler here in case $server is unavailable
    # Compare the wmi query result to the limit constant
    foreach($processor in $cpu){
    if($processor.LoadPercentage -le $CPULIMIT){
        # Write a formatted string that contains the server name and current CPU load
        #Write-Host $("Less than "+[string]$CPULIMIT+"% CPU Load on {0} ({1}%)" -f $server, $cpu.LoadPercentage) -ForegroundColor "Green"
        $("Less than "+[string]$CPULIMIT+"% CPU Load on {0} ({1}%)" -f $Server, $processor.LoadPercentage) >> $LogFile
    } else {
        # A warning message would be useful too
        #Write-Host $("More than "+[string]$CPULIMIT+"% CPU Load on {0} ({1}%)" -f $server, $cpu.LoadPercentage) -ForegroundColor "Red"
        $("More than "+[string]$CPULIMIT+"% CPU Load on {0} ({1}%)"+"`r`n" -f $Server, $processor.LoadPercentage) >> $LogFile
    }
    }
    #Memory Info 
    $memory = Get-WmiObject Win32_operatingsystem -ComputerName $Server -Credential $cred 
    $total = $memory.TotalVisibleMemorySize
    $free = $memory.FreePhysicalMemory
    if(($total-$free)*100/$total -le $MEMLIMIT){
        # Write a formatted string that contains the server name and current MEM load
        #Write-Host $("Less than "+[string]$MEMLIMIT+"% MEM Load on {0} ({1}%)" -f $server, [int]((($memory.TotalVisibleMemorySize - $memory.FreePhysicalMemory)*100)/ $memory.TotalVisibleMemorySize)) -ForegroundColor "Green"
        $("Less than "+[string]$MEMLIMIT+"% MEM Load on {0} ({1}%)" -f $server, [int]($total - $free)*100/ $total) >> $LogFile
    } else {
        # A warning message would be useful too
        #Write-Host $("More than "+[string]$MEMLIMIT+"% MEM Load on {0} ({1}%)" -f $server, [int]((($memory.TotalVisibleMemorySize - $memory.FreePhysicalMemory)*100)/ $memory.TotalVisibleMemorySize)) -ForegroundColor "Red"
        $("More than "+[string]$MEMLIMIT+"% MEM Load on {0} ({1}%)" -f $server, [int]($total - $free)*100/ $total) >> $LogFile 
    }
    #Disk Info 
    $disks = Get-WmiObject Win32_logicaldisk -ComputerName $Server -Credential $cred -Filter "DeviceID='C:'" | Select-Object Size,FreeSpace
    foreach($disk in $disks){
    [long]$freespace = $disk.FreeSpace
    [long]$disksize = $disk.size
    if(($freespace / $disksize)*100 -le $DISKLIMIT){
        # Write a formatted string that contains the server name and current disk space
        #Write-Host $("Less than "+[string]$DISKLIMIT+"% Hard Drive full on {0} ({1}%)" -f $server, [int](($freespace / $disksize)*100)) -ForegroundColor "Green"
        $("Less than "+[string]$DISKLIMIT+"% Hard Drive full on {0} ({1}%)" -f $server, [int](($FreeSpace / $disksize)*100)) >> $LogFile
    } else {
        # A warning message would be useful too
        #Write-Host $("More than "+[string]$DISKLIMIT+"% Hard Drive full on {0} ({1}%)" -f $server, [int](($FreeSpace / $disksize)*100)) -ForegroundColor "Red"
        $("More than "+[string]$DISKLIMIT+"% Hard Drive full on {0} ({1}%)" -f $server, [int](($FreeSpace / $disksize)*100)) >> $LogFile 
    }
    }

}
remove-variable -name CPULIMIT
remove-variable -name MEMLIMIT
remove-variable -name DISKLIMIT