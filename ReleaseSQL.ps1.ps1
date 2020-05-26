<# This form was created using POSHGUI.com  a free online gui designer for PowerShell
.NAME
    ReleaseSQL
#>

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$RootLevel                       = New-Object system.Windows.Forms.Form
$RootLevel.ClientSize            = '908,729'
$RootLevel.text                  = "ETL Deployment GUI"
$RootLevel.TopMost               = $false

$Label1                          = New-Object system.Windows.Forms.Label
$Label1.text                     = "CHG Ticket"
$Label1.AutoSize                 = $true
$Label1.width                    = 25
$Label1.height                   = 10
$Label1.location                 = New-Object System.Drawing.Point(49,66)
$Label1.Font                     = 'Microsoft Sans Serif,10'

$Label2                          = New-Object system.Windows.Forms.Label
$Label2.text                     = "Version List"
$Label2.AutoSize                 = $true
$Label2.width                    = 25
$Label2.height                   = 10
$Label2.location                 = New-Object System.Drawing.Point(254,66)
$Label2.Font                     = 'Microsoft Sans Serif,10'

$Label3                          = New-Object system.Windows.Forms.Label
$Label3.text                     = "Deploy Version"
$Label3.AutoSize                 = $true
$Label3.width                    = 25
$Label3.height                   = 10
$Label3.location                 = New-Object System.Drawing.Point(656,66)
$Label3.Font                     = 'Microsoft Sans Serif,10'

$L_Environment                   = New-Object system.Windows.Forms.Label
$L_Environment.text              = "Environment"
$L_Environment.AutoSize          = $true
$L_Environment.width             = 200
$L_Environment.height            = 10
$L_Environment.location          = New-Object System.Drawing.Point(10,17)
$L_Environment.Font              = 'Microsoft Sans Serif,10'

$L_CHGTicket                     = New-Object system.Windows.Forms.TextBox
$L_CHGTicket.multiline           = $false
$L_CHGTicket.width               = 146
$L_CHGTicket.height              = 20
$L_CHGTicket.location            = New-Object System.Drawing.Point(48,89)
$L_CHGTicket.Font                = 'Microsoft Sans Serif,10'

$C_VersionList                   = New-Object system.Windows.Forms.ComboBox
$C_VersionList.text              = "Version"
$C_VersionList.width             = 342
$C_VersionList.height            = 20
@('Version_1','Version_Feb_2020') | ForEach-Object {[void] $C_VersionList.Items.Add($_)}
$C_VersionList.location          = New-Object System.Drawing.Point(253,88)
$C_VersionList.Font              = 'Microsoft Sans Serif,10'

$B_DeployVersion                 = New-Object system.Windows.Forms.Button
$B_DeployVersion.text            = "VersionSelected"
$B_DeployVersion.width           = 241
$B_DeployVersion.height          = 20
$B_DeployVersion.location        = New-Object System.Drawing.Point(654,89)
$B_DeployVersion.Font            = 'Microsoft Sans Serif,10'

$Label4                          = New-Object system.Windows.Forms.Label
$Label4.text                     = "SQL Deploy Log"
$Label4.AutoSize                 = $true
$Label4.width                    = 25
$Label4.height                   = 10
$Label4.location                 = New-Object System.Drawing.Point(17,147)
$Label4.Font                     = 'Microsoft Sans Serif,10'

$DataGridView1                   = New-Object system.Windows.Forms.DataGridView
$DataGridView1.width             = 886
$DataGridView1.height            = 303
$DataGridView1.AllowUserToAddRows = $false
$DataGridView1.AllowUserToDeleteRows = $false
$DataGridView1Data = @(@("alm_out","Alter_Table_B1.sql","In Progress","2020-03-20 14:00:00 "),@("alm_udm","Create_Table_E1.sql","Succesfull","2020-03-20 15:15:30"))
$DataGridView1.ColumnCount = 4
$DataGridView1.ColumnHeadersVisible = $true
$DataGridView1.Columns[0].Name = "Database"
$DataGridView1.Columns[0].Width = 200
$DataGridView1.Columns[1].Name = "File"
$DataGridView1.Columns[1].Width = 300
$DataGridView1.Columns[2].Name = "Status"
$DataGridView1.Columns[2].Width = 200
$DataGridView1.Columns[3].Name = "Time"
$DataGridView1.Columns[3].Width = 143
foreach ($row in $DataGridView1Data){
          $DataGridView1.Rows.Add($row)
      }
$DataGridView1.location          = New-Object System.Drawing.Point(10,168)

$RootLevel.controls.AddRange(@($Label1,$Label2,$Label3,$L_Environment,$L_CHGTicket,$C_VersionList,$B_DeployVersion,$Label4,$DataGridView1))

$C_VersionList.Add_SelectedIndexChanged({ OnSelectedIndexChanged $this $_ })
$B_DeployVersion.Add_MouseClick({ OnDeployVersionMouseClick $this $_ })

function OnDeployVersionMouseClick ($sender,$event) { 
    $now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $row = @("db", "sql", "status", $now)
    $DataGridView1.Rows.Add($row)
}


function OnSelectedIndexChanged ($sender,$event) { 
$B_DeployVersion.text = $sender.SelectedItem
}




#Write your logic code here

[void]$RootLevel.ShowDialog()