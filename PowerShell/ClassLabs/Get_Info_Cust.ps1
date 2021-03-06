function Get-InfoCust
{
    param (
    $computername = 'localhost'
    )
    
    $os = gwmi win32_operatingsystem -computer $computername
    $bios = gwmi win32_bios -computer $computername
    $cs = gwmi win32_computersystem -computer $computername
    
    $computername
    $os.caption
    $cs.dnshostname
    $bios.serialnumber
    
    $obj = New-Object -TypeName PSObject
    
    $obj | Add-Member -MemberType NoteProperty -name ComputerName -value $computername
    
    $obj | Add-Member -MemberType NoteProperty -name OSVersion -value $os.caption
    
    $obj | Add-Member -MemberType NoteProperty -name DNS-Name -value $cs.dnshostname
    
    $obj | Add-Member -MemberType NoteProperty -name BIOS-SN -value $bios.serialnumber
    
    write-output $obj

}
Get-InfoCust |ft -auto