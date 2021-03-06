<#
.Synopsis
Get-OSInfo takes a $computername and $logfile parameter,
and then returns the device's name, OS build number, BIOS Serial Number,
and last boot-up time.

.Description
This information is gathered from the Win32_Operating System and
Win32_Bios WMIs.

.Parameter computername
The computer name, or names, to query.  Default: localhost

.Parameter logfile
A place to store devices that were not reachable during Get-OSInfo query.

.Example
Get-OSInfo

.Example
Get-OSInfo -computername SERVER-R2 -logfile c:\log.txt
#>

function Get-OSInfoWork
{
    param($computername,$logfile)
    try
    {
        $os = gwmi win32_operatingsystem -ComputerName $computername -ea Stop
        $bios = gwmi win32_bios -ComputerName $computername
        $obj = New-Object -TypeName PSObject
        $obj | Add-Member -MemberType NoteProperty `
        -Name ComputerName -Value $computername
        $obj | Add-Member -MemberType NoteProperty `
        -Name OSBuild -Value ($os.buildnumber)
        $obj | Add-Member -MemberType NoteProperty `
        -Name BIOSSerial -Value ($bios.serialnumber)
        $obj | Add-Member -MemberType NoteProperty `
        -Name LastBoot -Value ($os.ConvertToDateTime($os.lastbootuptime))
    }
    catch
    {
        $computername >> $logfile
    }
    Write-Output $obj
}

function Get-OSInfo
{
        [CmdletBinding()]
    
    param
    (
        [Parameter(Mandatory=$False,ValueFromPipeline=$True,ValueFromPipelineByPropertyname=$True)]
        [Alias('host')]
        [string[]]$computername,
        [string]$logfile
    )
    BEGIN
    {
        if ($logfile)
        {
            Remove-Item -ea SilentlyContinue $logfile
        }
    }
    PROCESS
    {
        if(-not $computername)
        {
            $computername = "localhost"
        }
        foreach($computer in $computername)
        {
            Get-OSInfoWork -computername $computer `
            -logfile $logfile
        }
    }
    END{}
}

#Get-OSInfo localhost,WIN2K8R2-PSTEST,localho c:\log.txt
#Get-OSInfo