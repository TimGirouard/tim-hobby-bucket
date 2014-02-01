$computername = Read-Host
if ($computername -ne 'localhost')
{
try
{
    $ErrorActionPreference = "Stop"
    gwmi win32_operatingsystem -ComputerName $computername
}
catch
{
    "Caught a system exception, dude."
}
finally
{
    $ErrorActionPreference = "Continue"
}
} 