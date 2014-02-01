
$serverList = "C:\Servers.txt" 


#$serverList = "test.txt" 


[System.Collections.ArrayList]$sysCollection = New-Object System.Collections.ArrayList($null) 


  


foreach ($server in (Get-Content $serverList))  


{  


    "Collecting information from $server" 


    [System.Collections.Specialized.OrderedDictionary]$si = @{}    # Blank hashtable for each iteration 


    $totCores=0 


  


    $si.Server=[string]$server; 


  


    try 


    { 


        [wmi]$sysInfo = Get-WmiObject Win32_ComputerSystem -Namespace "root\CIMV2" -ComputerName $server -ErrorAction Stop 


        [wmi]$bios = Get-WmiObject Win32_BIOS -Namespace "root\CIMV2" -computername $server 


        [wmi]$os = Get-WmiObject Win32_OperatingSystem -Namespace "root\CIMV2" -Computername $server 


        [array]$procs = Get-WmiObject Win32_Processor -Namespace "root\CIMV2" -Computername $server 


        [array]$mem = Get-WmiObject Win32_PhysicalMemory -Namespace "root\CIMV2" -ComputerName $server 


        [array]$nic = Get-WmiObject Win32_NetworkAdapterConfiguration -Namespace "root\CIMV2" -ComputerName $server | where{$_.IPEnabled -eq "True"} 


  


  


        $si.Manufacturer=[string]$sysInfo.Manufacturer; 


        $si.Model=[string]$sysInfo.Model; 


        $si.TotMem=[string]$sysInfo.TotalPhysicalMemory; 


        $si.BiosDesc=[string]$bios.Description; 


        $si.BiosVer=[string]$bios.SMBIOSBIOSVersion+"."+$bios.SMBIOSMajorVersion+"."+$bios.SMBIOSMinorVersion; 


        $si.BiosSerial=[string]$bios.SerialNumber; 


        $si.OSName=[string]$os.Name.Substring(0,$os.Name.IndexOf("|") -1); 


        $si.Arch=[string]$os.OSArchitecture; 


        $si.Processors=[string]@($procs).count; 


        $si.Cores=[string]$procs[0].NumberOfCores; 


        $iter=0 


        while ($iter -lt 12)   #Parse through each stick of memory (arbitrary 12 Memory stick columns) 


        { 


            if ($mem[$iter] -ne $null) { 


                $si."MemBank$iter" = [string]$mem[$iter].Capacity + "," + [string]$mem[$iter].BankLabel  


            } else { 


                $si."MemBank$iter" = "" 


            } 


            $iter++ 


        } 


        $iter=0 


        while ($iter -lt 4)    #Parse through each NIC (arbritrary 4 Network Card columns) 


        { 


            $si."DHCP$iter"=[string]$nic[$iter].DHCPEnabled; 


            $si."IPAddress$iter"=[string]$nic[$iter].IPAddress; 


            $si."Subnet$iter"=[string]$nic[$iter].IPSubnet; 


            $si."Gateway$iter"=[string]$nic[$iter].DefaultIPGateway; 


            $si."Mac$iter"=[string]$nic[$iter].MacAddress; 


            $iter++ 


        } 


    } 


    catch [Exception] 


    { 


        "Could not contact $server, skipping to next" 


        Continue 


    } 


    finally 


    { 


        [void]$sysCollection.Add((New-Object PSObject -Property $si))    #Add the dictionary list to the collection 


    } 


} 


  


$sysCollection | Export-CSV -path C:\ServerInventory.csv -NoTypeInformation    #Output the collection to a CSV file 
