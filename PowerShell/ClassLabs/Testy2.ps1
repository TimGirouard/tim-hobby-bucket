function Get-Inventory
{
    PROCESS
    {
        try
        {
            $computername = $_
            $os = gwmi win32_operatingsystem -comp $computername -ea Stop
            $bios = gwmi win32_bios -comp $computername
            $obj= New-Object PSObject
            $obj | Add-Member -MemberType NoteProperty -Name ComputerName -Value $computername
            $obj | Add-Member -MemberType NoteProperty -Name OSBuild -Value ($os.buildnumber)
            $obj | Add-Member -MemberType NoteProperty -Name BIOSSerial -Value ($bios.serialnumber)
            Write-Output $obj
        }
        catch
        {
        
            "`nOops, couldn't find $computername"
        }
    }
}

"localhost","win2k8r2-pstest","local" | Get-Inventory