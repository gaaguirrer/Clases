param(
    [Parameter(Mandatory, Position = 0, HelpMessage = "Nombre de la carpeta a agregar (ej: 'Gestión de Proyectos Tecnológicos')")]
    [string]$Carpeta,
    [Parameter(HelpMessage = "Mensaje para el commit")]
    [string]$Mensaje = "",
    [switch]$SubirTodo = $false
)

$ErrorActionPreference = "Stop"

# --- Detectar git.exe en GitHub Desktop ---
$ghDesktopPaths = @(
    "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe"
)
$gitExe = $null
foreach ($pat in $ghDesktopPaths) {
    $found = Get-ChildItem $pat -ErrorAction SilentlyContinue | Sort-Object FullName -Descending | Select-Object -First 1
    if ($found) { $gitExe = $found.FullName; break }
}
if (-not $gitExe) { throw "No se encontró git.exe en GitHub Desktop" }

$repo = "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"
$sparseFile = "$repo\.git\info\sparse-checkout"

# --- Función helper para ejecutar git ---
function git-cmd {
    param([string[]]$Args)
    & $gitExe -C $repo @Args 2>&1 | ForEach-Object { "$_" }
    if ($LASTEXITCODE -ne 0) { throw "git falló: $($Args -join ' ')" }
}

# --- Modo: subir todo (carpetas nuevas) ---
if ($SubirTodo) {
    # Buscar carpetas untracked en la raíz del repo
    $status = git-cmd @("status", "--porcelain")
    $nuevas = $status | Where-Object { $_ -match '^\?\? ' } | ForEach-Object { $_ -replace '^\?\? ' }
    if (-not $nuevas) { Write-Output "No hay carpetas nuevas para subir."; return }
    Write-Output "Carpetas nuevas detectadas:"
    $nuevas | ForEach-Object { "  - $_" }
    foreach ($c in $nuevas) {
        $linea = "$c/**"
        if (-not (Select-String -LiteralPath $sparseFile -Pattern "^$([regex]::Escape($linea))$" -Quiet)) {
            Add-Content -Path $sparseFile -Value $linea
            Write-Output "  -> Agregado al sparse-checkout: $linea"
        }
    }
    git-cmd @("read-tree", "-mu", "HEAD")
    git-cmd @("add", "--sparse", $nuevas)
    git-cmd @("commit", "-m", "Agregar carpetas: $($nuevas -join ', ')")
    git-cmd @("push", "origin", "master")
    Write-Output "Todo subido correctamente."
    return
}

# --- Modo: agregar una carpeta específica ---
if (-not $Carpeta) { throw "Debes especificar el nombre de la carpeta o usar -SubirTodo" }

$rutaCarpeta = "$repo\$Carpeta"
if (-not (Test-Path $rutaCarpeta)) { throw "La carpeta '$Carpeta' no existe en el repositorio local." }

$patron = "$Carpeta/**"
if (-not (Select-String -LiteralPath $sparseFile -Pattern "^$([regex]::Escape($patron))$" -Quiet)) {
    Add-Content -Path $sparseFile -Value $patron
    Write-Output "Agregado al sparse-checkout: $patron"
} else { Write-Output "El patrón ya existe en sparse-checkout." }

git-cmd @("read-tree", "-mu", "HEAD")
git-cmd @("add", "--sparse", $Carpeta)

if (-not $Mensaje) { $Mensaje = "Agregar carpeta: $Carpeta" }
git-cmd @("commit", "-m", $Mensaje)
git-cmd @("push", "origin", "master")
Write-Output "Carpeta '$Carpeta' subida exitosamente."
