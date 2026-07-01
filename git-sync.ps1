param(
    [string]$Mensaje = "Actualizacion de materiales y archivos de clases",
    [switch]$Auto,
    [switch]$Sparse,
    [switch]$Startup,
    [switch]$Forzar
)

$ErrorActionPreference = "Continue"
$repo = "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"
$logFile = "$repo\.git\auto-commit.log"
$sparseFile = "$repo\.git\info\sparse-checkout"

function Find-GitExe {
    $ghPaths = Get-ChildItem "$env:LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending
    if ($ghPaths) { return $ghPaths[0].FullName }
    $gwPaths = Get-ChildItem "${env:ProgramFiles}\Git\bin\git.exe", "${env:ProgramFiles(x86)}\Git\bin\git.exe" -ErrorAction SilentlyContinue
    if ($gwPaths) { return $gwPaths[0].FullName }
    $pathGit = (Get-Command git.exe -ErrorAction SilentlyContinue).Source
    if ($pathGit) { return $pathGit }
    throw "No se encontro git.exe"
}

function Invoke-Git {
    param($GitExe, [string[]]$GitArgs)
    $o = & $GitExe -C $repo @GitArgs 2>&1
    $exitCode = $LASTEXITCODE
    $o = $o | ForEach-Object { "$_" }
    if ($exitCode -ne 0) {
        throw "git fallo: $($GitArgs -join ' ')`n$($o -join "`n")"
    }
    return $o
}

function Get-DefaultBranch {
    param($GitExe)
    try {
        $remoteHead = Invoke-Git -GitExe $GitExe -GitArgs @("symbolic-ref", "refs/remotes/origin/HEAD")
        return $remoteHead.Trim() -replace '^refs/remotes/origin/', ''
    } catch {
        return "master"
    }
}

function Write-Log {
    param([string]$Text)
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - $Text"
    if ($Auto -or $Startup) { Add-Content -Path $logFile -Value $line -Encoding UTF8 }
    Write-Output $Text
}

$gitExe = Find-GitExe
$branch = Get-DefaultBranch -GitExe $gitExe

if ($Startup) {
    Start-Sleep -Seconds 30
    $timeout = 60
    $ok = $false
    while ($timeout -gt 0) {
        try {
            $req = [System.Net.WebRequest]::Create("https://github.com")
            $req.Timeout = 3000
            $req.GetResponse()
            $ok = $true
            break
        } catch {}
        Start-Sleep -Seconds 2
        $timeout -= 2
    }
    if (-not $ok) {
        Write-Log "Sin conexion a internet."
        return
    }
    & $PSCommandPath -Sparse -Auto -Forzar 2>&1 | ForEach-Object { "$_" } | Out-File "$env:USERPROFILE\.git-sync.log"
    return
}

if ($Sparse -or -not ($Auto -or $Startup)) {
    $carpetasEnDisco = Get-ChildItem -LiteralPath $repo -Directory |
        Where-Object { $_.Name -notmatch '^\.' } |
        Select-Object -ExpandProperty Name
    $archivosRaiz = & $gitExe -C $repo ls-files | Where-Object { $_ -notmatch '/' }
    $patronesEsperados = @()
    $carpetasEnDisco | ForEach-Object { $patronesEsperados += "$_/**" }
    $archivosRaiz | ForEach-Object { $patronesEsperados += $_ }
    $patronesExistentes = @()
    if (Test-Path $sparseFile) {
        $patronesExistentes = Get-Content $sparseFile
    }
    $carpetasEnSparse = $patronesExistentes | Where-Object { $_ -match '.+/\*\*' } | ForEach-Object { $_ -replace '/\*\*$' }
    $archivosEnSparse = $patronesExistentes | Where-Object { $_ -notmatch '.+/\*\*' -and $_ -notmatch '^/\*$' }
    $agregar = $carpetasEnDisco | Where-Object { $_ -notin $carpetasEnSparse }
    $quitar = $carpetasEnSparse | Where-Object { $_ -notin $carpetasEnDisco }
    $agregarArchivos = $archivosRaiz | Where-Object { $_ -notin $archivosEnSparse }
    $quitarArchivos = $archivosEnSparse | Where-Object { $_ -notin $archivosRaiz }
    if ($agregar -or $quitar -or $agregarArchivos -or $quitarArchivos) {
        Write-Output "`n--- Sparse-checkout ---"
        if ($agregar) { $agregar | ForEach-Object { Write-Output "  + $_/ (nueva carpeta)" } }
        if ($quitar) { $quitar | ForEach-Object { Write-Output "  - $_/ (ya no existe)" } }
        if ($agregarArchivos) { $agregarArchivos | ForEach-Object { Write-Output "  + $_ (nuevo archivo raiz)" } }
        if ($quitarArchivos) { $quitarArchivos | ForEach-Object { Write-Output "  - $_ (ya no existe)" } }
        if (-not $Forzar -and -not $Auto) {
            $r = Read-Host "`nActualizar sparse-checkout? (s/N)"
            if ($r -notmatch '^[sS]') { Write-Output "Cancelado."; return }
        }
        foreach ($c in $agregar) { Add-Content -Path $sparseFile -Value "$c/**" }
        foreach ($c in $agregarArchivos) { Add-Content -Path $sparseFile -Value $c }
        foreach ($c in $quitar + $quitarArchivos) {
            $contenido = Get-Content $sparseFile | Where-Object { $_ -ne "$c/**" -and $_ -ne $c }
            Set-Content -Path $sparseFile -Value $contenido
        }
        Invoke-Git -GitExe $gitExe -GitArgs @("read-tree", "-mu", "HEAD")
        if ($agregar) { Invoke-Git -GitExe $gitExe -GitArgs @("add", "--sparse", "--", $agregar) }
        Write-Output "Sparse-checkout actualizado."
    } else {
        Write-Output "Sparse-checkout sincronizado."
    }
}

$status = Invoke-Git -GitExe $gitExe -GitArgs @("status", "--porcelain")
if (-not $status) {
    Write-Log "Sin cambios - no se sube nada."
    exit 0
}

Write-Output "`n--- Cambios detectados ---"
$status | ForEach-Object { Write-Output "  $_" }

if (-not $Auto -and -not $Startup) {
    $r = Read-Host "`nSubir estos cambios a GitHub? (s/N)"
    if ($r -notmatch '^[sS]') { Write-Output "Cancelado."; return }
}

# Guardar cambios locales temporalmente para traer cambios remotos
try {
    Write-Output "`nTrayendo cambios remotos..."
    Invoke-Git -GitExe $gitExe -GitArgs @("stash")
    Invoke-Git -GitExe $gitExe -GitArgs @("pull", "--rebase", "origin", $branch)
    Invoke-Git -GitExe $gitExe -GitArgs @("stash", "pop")
} catch {
    Write-Output "Nota: No se pudo sincronizar con remoto, continuando..."
}

Invoke-Git -GitExe $gitExe -GitArgs @("add", "--sparse", "--all")
$msgFinal = if ($Auto) { "$Mensaje [auto $(Get-Date -Format 'yyyy-MM-dd HH:mm')]" } else { $Mensaje }

Write-Output "`nCommiteando..."
Invoke-Git -GitExe $gitExe -GitArgs @("commit", "-m", $msgFinal)

Write-Output "Subiendo a GitHub (rama $branch)..."
Invoke-Git -GitExe $gitExe -GitArgs @("push", "origin", $branch)

Write-Log "Listo. Cambios subidos exitosamente a rama '$branch'."
