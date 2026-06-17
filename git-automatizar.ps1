param(
    [switch]$Sincronizar = $false,
    [switch]$Forzar = $false
)

$ErrorActionPreference = "Stop"

# --- Detectar git.exe en GitHub Desktop ---
$ghDesktopPaths = "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe"
$gitExe = Get-ChildItem $ghDesktopPaths -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending | Select-Object -First 1 -ExpandProperty FullName
if (-not $gitExe) { throw "No se encontró git.exe en GitHub Desktop" }

$repo = "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"
$sparseFile = "$repo\.git\info\sparse-checkout"

function git-cmd {
    param([string[]]$Args)
    $o = & $gitExe -C $repo @Args 2>&1 | ForEach-Object { "$_" }
    if ($LASTEXITCODE -ne 0) { throw "git falló: $($Args -join ' ')" }
    return $o
}

# --- Leer carpetas actuales en disco (excluir .git, archivos sueltos y el propio script) ---
$carpetasEnDisco = Get-ChildItem -LiteralPath $repo -Directory |
    Where-Object { $_.Name -notmatch '^\.' } |
    Select-Object -ExpandProperty Name

# --- Leer sparse-checkout actual ---
$patronesExistentes = @()
if (Test-Path $sparseFile) { $patronesExistentes = Get-Content $sparseFile | Where-Object { $_ -match '.+/\*\*' } }

# --- Extraer nombres de carpeta de los patrones ---
$carpetasEnSparse = $patronesExistentes | ForEach-Object { $_ -replace '/\*\*$' }

# --- Comparar ---
$agregar = $carpetasEnDisco | Where-Object { $_ -notin $carpetasEnSparse }
$quitar = $carpetasEnSparse | Where-Object { $_ -notin $carpetasEnDisco }

if (-not $agregar -and -not $quitar) {
    Write-Output "Todo sincronizado. No hay cambios."
    return
}

if ($agregar) {
    Write-Output "`nNUEVAS carpetas en PC (se subirán a GitHub):"
    $agregar | ForEach-Object { "  + $_" }
}
if ($quitar) {
    Write-Output "`nCARPETAS que ya no están en PC (se quitarán del sparse-checkout):"
    $quitar | ForEach-Object { "  - $_" }
}

if (-not $Forzar) {
    $r = Read-Host "`n¿Continuar? (s/N)"
    if ($r -notmatch '^[sS]') { Write-Output "Cancelado."; return }
}

# --- Agregar nuevas carpetas al sparse-checkout ---
foreach ($c in $agregar) {
    $linea = "$c/**"
    Add-Content -Path $sparseFile -Value $linea
    Write-Output "  -> Agregado al sparse-checkout: $linea"
}

# --- Quitar carpetas inexistentes del sparse-checkout ---
foreach ($c in $quitar) {
    $patron = "$c/**"
    $contenido = Get-Content $sparseFile | Where-Object { $_ -ne $patron }
    Set-Content -Path $sparseFile -Value $contenido
    Write-Output "  -> Quitado del sparse-checkout: $patron"
}

# --- Actualizar árbol de trabajo ---
git-cmd @("read-tree", "-mu", "HEAD")

# --- Agregar nuevas carpetas al index ---
if ($agregar) {
    git-cmd @("add", "--sparse", $agregar)
}

# --- Commit y push ---
if ($agregar -or $quitar) {
    $msgs = @()
    if ($agregar) { $msgs += "agregadas: $($agregar -join ', ')" }
    if ($quitar) { $msgs += "quitadas del sparse-checkout: $($quitar -join ', ')" }
    git-cmd @("commit", "-m", "Sincronizar carpetas: $($msgs -join '; ')")
    git-cmd @("push", "origin", "master")
    Write-Output "`nSincronización completada."
}
