<# This form was created using POSHGUI.com  a free online gui designer for PowerShell
.NAME
    UTest-Tables
#>

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$Form                            = New-Object system.Windows.Forms.Form
$Form.ClientSize                 = '405,400'
$Form.text                       = "Form"
$Form.TopMost                    = $false

$DataGridView1                   = New-Object system.Windows.Forms.DataGridView
$DataGridView1.width             = 386
$DataGridView1.height            = 296
$DataGridView1Data = @(@("b"),@("c"))
$DataGridView1.ColumnCount = 4
$DataGridView1.ColumnHeadersVisible = $true
$DataGridView1.Columns[0].Name = "a"
foreach ($row in $DataGridView1Data){
          $DataGridView1.Rows.Add($row)
      }
$DataGridView1.location          = New-Object System.Drawing.Point(10,20)


$CheckBox1                       = New-Object system.Windows.Forms.CheckBox
$CheckBox1.text                  = "checkBox"
$CheckBox1.AutoSize              = $false
$CheckBox1.width                 = 95
$CheckBox1.height                = 20
$CheckBox1.location              = New-Object System.Drawing.Point(9,356)
$CheckBox1.Font                  = 'Microsoft Sans Serif,10'

$DataGridView1.controls.Add($CheckBox1)

$Form.controls.AddRange(@($DataGridView1))


[void]$Form.ShowDialog()