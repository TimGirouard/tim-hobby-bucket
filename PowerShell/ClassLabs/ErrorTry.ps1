function Get-Stuff
{
    BEGIN
    {
        del c:\retry.txt -ea SilentlyContinue
        del c:\errors.txt -ea SilentlyContinue
    }
    PROCESS
    {
        try
        {
            $computername = $_
            gwmi win32_bios -comp $computername -ea Stop -ev WmiError
        }
        catch
        {
            $computername | Out-File c:\retry.txt -append
            $WmiError | Out-File C:\errors.txt -Append       
        }
<#
        finally
        {
            Write-Host "Command executed"
        }
#>
    }
}
'WIN2K8R2-PSTEST','Notonline','localhost' | Get-Stuff