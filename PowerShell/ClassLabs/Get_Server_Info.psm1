function GetServerInfoWork
{
    param([string]$computername,[string]$logfile)

    $os = Get-WmiObject Win32_OperatingSystem -computer $computername
    
    $disk = Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='C:'" -computer $computername
    
    # use $logfile to get the value from the 
    # -logfile parameter
    
    $obj = New-Object -TypeName PSObject
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name ComputerName -Value $computername
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name BuildNumber -Value ($os.BuildNumber)
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name SPVersion  -Value ($os.ServicePackMajorVersion)
    
    $obj | Add-Member -MemberType NoteProperty `
    -Name SysDriveFree -Value ($disk.free / 1MB -as [int])
    
    Write-Output $obj
}

function Get-ServerInfo
{
    [CmdletBinding()]
    
    param
    (
        [Parameter(Mandatory=$True,ValueFromPipeline=$True,ValueFromPipelineByPropertyname=$True)]
        [Alias('host')]
        [string[]]$computername,
        [string]$logfile
    )
    BEGIN {}
    PROCESS
    {
        foreach ($computer in $computername)
        {
            GetServerInfoWork -computername $computer `
            -logfile $logfile
        }
    }
    END{}
}