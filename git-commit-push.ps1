param(
    [string]$Mensaje = "Actualización de materiales y archivos de clases"
)

$ErrorActionPreference = "Continue"

# --- Detectar git.exe en GitHub Desktop ---
$ghDesktopPaths = "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe"
$gitExe = Get-ChildItem $ghDesktopPaths -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending | Select-Object -First 1 -ExpandProperty FullName
if (-not $gitExe) { throw "No se encontró git.exe en GitHub Desktop" }

$repo = "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"

function git-cmd {
    param([string[]]$MyArgs)
    $o = & $gitExe -C $repo @MyArgs 2>&1 | ForEach-Object { "$_" }
    if ($LASTEXITCODE -ne 0) { throw "git falló: $($MyArgs -join ' ')" }
    return $o
}

# --- Verificar si hay cambios ---
$status = git-cmd @("status", "--porcelain")
if (-not $status) {
    Write-Output "No hay cambios para subir."
    return
}

# --- Mostrar cambios detectados ---
Write-Output "Cambios detectados:"
$status | ForEach-Object { Write-Output "  $_" }

# --- Preguntar antes de continuar ---
$r = Read-Host "`n¿Subir estos cambios a GitHub? (s/N)"
if ($r -notmatch '^[sS]') { Write-Output "Cancelado."; return }

# --- Add, commit, push ---
Write-Output "`nAgregando cambios..."
git-cmd @("add", "--sparse", "-A")

Write-Output "Committeando..."
git-cmd @("commit", "-m", $Mensaje)

Write-Output "Subiendo a GitHub..."
git-cmd @("push", "origin", "master")

Write-Output "`nListo. Cambios subidos exitosamente."
