$logdisk = gwmi win32_logicaldisk
foreach($disk in $logdisk)
{
    $disk.deviceid
    Switch ($disk.drivetype)
    {
        0
        {
            Write-Host 'Unknown Drive Type'
        }
        1
        {
            Write-Host 'No Root Directory'
        }
        2
        {
            Write-Host 'Removable Disk'
        }
        3
        {
            Write-Host 'Local Disk'
        }
        4
        {
            Write-Host 'Network Drive'
        }
        5
        {
            Write-Host 'Compact Disc'
        }
        6
        {
            Write-Host 'RAM Disk'
        }
        Default
        {
            Write-Host 'Unknown Drive Type'
        }
    }
}