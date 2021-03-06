function GetServerInfoWork
{
    param([string]$computername)
    
    $disk = Get-WmiObject Win32_LogicalDisk -Filter "DriveType=3" -computer $computername | Where-Object { ($_.FreeSpace/$_.Size) -le .9} | Select-Object __SERVER, Name, FreeSpace
    Write-Output $disk
<#    
    foreach ($drive in $disk)
    {
    if ($disk.freespace/$disk.size -le .9)
    {
    $obj = New-Object -TypeName PSObject
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name ComputerName -Value $computername
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name DriveType  -Value ($disk.DriveType)
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name SysDriveFree -Value ($disk.freespace / 1MB -as [int])
    Write-Output $obj
    }
    }
#>
}

function Get-ServerInfo
{
    [CmdletBinding()]
    
    param
    (
        [Parameter(Mandatory=$True,ValueFromPipeline=$True,ValueFromPipelineByPropertyname=$True)]
        [Alias('host')]
        [string[]]$computername
    )
    BEGIN {}
    PROCESS
    {
        foreach ($computer in $computername)
        {
            GetServerInfoWork -computername $computer `
        }
    }
    END{}
}

Get-Content c:\names.txt | Get-ServerInfo
#Get-ServerInfo -computername localhost