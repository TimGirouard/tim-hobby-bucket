function Get-ServerInfo {

    param (
    $computername = 'localhost'
    )
    
    $os = gwmi win32_operatingsystem -computer $computername
    $disk = gwmi win32_logicaldisk -filter "DeviceID='C:'" -comp $computername

    $obj = New-Object -TypeName PSObject
    
    $obj | Add-Member -MemberType NoteProperty -name ComputerName -Value $computername
    
    $obj | Add-Member -MemberType NoteProperty -name BuildNumber -Value $os.BuildNumber
    
    $obj | Add-Member -MemberType NoteProperty -name SPVersion -Value $os.ServicePackMajorVersion
    
    $obj | Add-Member -MemberType NoteProperty -name SysDriveFree -Value ($disk.free/1MB -as [int])

    Write-Output $obj
}

Get-ServerInfo WIN2K8R2-PSTEST | ConvertTo-Html | Out-File info.html