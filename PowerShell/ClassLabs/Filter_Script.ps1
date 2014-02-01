function Filter-Script
{
    param
    (
        [string]$computername
    )
    BEGIN {}
    PROCESS
    {
        $computername = $_
        
        if (test-connection $computername -ea silentlycontinue)
        {
            "$computername reachable"
        }
        else
        {
            "$computername not reachable"
        }
    }
    END {}
}

#Get-Content c:\names.txt | Filter-Script | Format-Table -auto
"localhost","localho","WIN2K8R2-PSTEST","WIN2R2-PSTEST" | Filter-Script | Format-Table -auto