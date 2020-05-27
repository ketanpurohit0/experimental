<# This form was created using POSHGUI.com  a free online gui designer for PowerShell
.NAME
    ReleaseSQL
#>

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$RootLevel                       = New-Object system.Windows.Forms.Form
$RootLevel.ClientSize            = '948,769'
$RootLevel.text                  = "ETL SQL Deployment GUI"
$RootLevel.TopMost               = $false
$RootLevel.add_Load({ OnFormLoad $this $_ })

$Label1                          = New-Object system.Windows.Forms.Label
$Label1.text                     = "CHG Ticket"
$Label1.AutoSize                 = $true
$Label1.width                    = 25
$Label1.height                   = 10
$Label1.location                 = New-Object System.Drawing.Point(49,66)
$Label1.Font                     = 'Lucida Sans Typewriter,8'

$Label2                          = New-Object system.Windows.Forms.Label
$Label2.text                     = "Version List"
$Label2.AutoSize                 = $true
$Label2.width                    = 25
$Label2.height                   = 10
$Label2.location                 = New-Object System.Drawing.Point(254,66)
$Label2.Font                     = 'Lucida Sans Typewriter,8'

$Label2a                          = New-Object system.Windows.Forms.Label
$Label2a.text                     = "Enable"
$Label2a.AutoSize                 = $true
$Label2a.width                    = 25
$Label2a.height                   = 10
$Label2a.location                 = New-Object System.Drawing.Point(600,66)
$Label2a.Font                     = 'Lucida Sans Typewriter,8'

$Label3                          = New-Object system.Windows.Forms.Label
$Label3.text                     = "Deploy Version"
$Label3.AutoSize                 = $true
$Label3.width                    = 25
$Label3.height                   = 10
$Label3.location                 = New-Object System.Drawing.Point(656,66)
$Label3.Font                     = 'Lucida Sans Typewriter,8'

$L_Environment                   = New-Object system.Windows.Forms.Label
$L_Environment.text              = "Environment:".PadRight(240)
$L_Environment.AutoSize          = $true
$L_Environment.width             = 886
$L_Environment.height            = 10
$L_Environment.location          = New-Object System.Drawing.Point(10,17)
$L_Environment.Font              = 'Lucida Sans Typewriter,8'
$L_Environment.BackColor         = "LightBlue"  # Depending on Env value use DEV/SIT - LightGreen, UAT: LightBlue, PRE: Orange, PRD: Red

$L_CHGTicket                     = New-Object system.Windows.Forms.TextBox
$L_CHGTicket.multiline           = $false
$L_CHGTicket.width               = 146
$L_CHGTicket.height              = 20
$L_CHGTicket.location            = New-Object System.Drawing.Point(48,89)
$L_CHGTicket.Font                = 'Lucida Sans Typewriter,8'

$C_VersionList                   = New-Object system.Windows.Forms.ComboBox
$C_VersionList.text              = "Version"
$C_VersionList.width             = 342
$C_VersionList.height            = 20
@('Version_1','Version_Feb_2020') | ForEach-Object {[void] $C_VersionList.Items.Add($_)}
$C_VersionList.location          = New-Object System.Drawing.Point(253,88)
$C_VersionList.Font              = 'Lucida Sans Typewriter,8'

$CheckBox1                       = New-Object system.Windows.Forms.CheckBox
$CheckBox1.text                  = ""
$CheckBox1.AutoSize              = $false
$CheckBox1.width                 = 20
$CheckBox1.height                = 20
$CheckBox1.location              = New-Object System.Drawing.Point(600,89)
$CheckBox1.Font                  = 'Lucida Sans Typewriter,8'

$B_DeployVersion                 = New-Object system.Windows.Forms.Button
$B_DeployVersion.text            = "VersionNotYetSelected"
$B_DeployVersion.width           = 241
$B_DeployVersion.height          = 20
$B_DeployVersion.location        = New-Object System.Drawing.Point(654,89)
$B_DeployVersion.Font            = 'Lucida Sans Typewriter,8'

$Label4                          = New-Object system.Windows.Forms.Label
$Label4.text                     = "SQL Deploy Log"
$Label4.AutoSize                 = $true
$Label4.width                    = 25
$Label4.height                   = 10
$Label4.location                 = New-Object System.Drawing.Point(17,147)
$Label4.Font                     = 'Lucida Sans Typewriter,8'

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

$L_Message                   = New-Object system.Windows.Forms.Label
$L_Message.text              = "Message:".PadRight(240)
$L_Message.AutoSize          = $true
$L_Message.width             = 886
$L_Message.height            = 10
$L_Message.location          = New-Object System.Drawing.Point(10,700)
$L_Message.Font              = 'Lucida Sans Typewriter,8'
$L_Message.BackColor         = "LightBlue"

$TAB_Control 					= New-Object 'System.Windows.Forms.TabControl'
$TAB_Control.Alignment			= "Top"
$TAB_Control.SelectedIndex 		= 0
$TAB_Control.Size				= "928,749"


$TAB_Page_SQL 					= New-Object 'System.Windows.Forms.TabPage'
$TAB_Page_SQL.Text 				= "SQL Release TAB"
$TAB_Page_SQL.Size				= "928,749"

$TAB_Page_TBA 					= New-Object 'System.Windows.Forms.TabPage'
$TAB_Page_TBA.Text 				= "TBA"
$TAB_Page_TBA.Size				= "928,749"

$RootLevel.controls.Add($TAB_Control)
$TAB_Control.controls.AddRange(@($TAB_Page_SQL,$TAB_Page_TBA))
$TAB_Page_SQL.controls.AddRange(@($Label1,$Label2,$Label2a,$Label3,$L_Environment,$L_CHGTicket,$C_VersionList,$CheckBox1, $B_DeployVersion,$Label4,$DataGridView1,$L_Message))

$C_VersionList.Add_SelectedIndexChanged({ OnSelectedIndexChanged $this $_ })
$B_DeployVersion.Add_MouseClick({ OnDeployVersionMouseClick $this $_ })

function OnDeployVersionMouseClick ($sender,$event) {

    if ($B_DeployVersion.Text -cne "VersionNotYetSelected")
    {
        if ($CheckBox1.Checked -eq $true) { 
            $L_Message.text = "Message: Release $($B_DeployVersion.Text) now in progress..".PadRight(240)
        
            $now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $row = @("db", "sql", "status", $now)
            $DataGridView1.Rows.Add($row)

            $L_Message.text = "Message: Release $($B_DeployVersion.Text) now completed.".PadRight(240)

            
            #$DataGridView1.Rows[$DataGridView1.Rows.Count-1].Cells[1].Value = 'FooBar'
            #$DataGridView1.Rows[$DataGridView1.Rows.Count-1].Cells["Status"].Value = 'Completed'
        }
        else {
            $L_Message.text = "Message: Please Check The CheckBox".PadRight(240)
        }
    }
    else
    {
        $L_Message.text = "Message: No Version Currently Selected".PadRight(240)
    }
}


function OnSelectedIndexChanged ($sender,$event) { 
$B_DeployVersion.text = $sender.SelectedItem
}

function OnFormLoad ($sender, $event) {
Write-Host "OnStart"
}




#Write your logic code here

[void]$RootLevel.ShowDialog()