$repoPath = "c:\Users\ingga\OneDrive\Documentos\Nueva carpeta\clases"
$intervalSeconds = 300  # Cada 5 minutos

Write-Host "[AUTO-PULL] Iniciando monitoreo del repositorio..."
Write-Host "[AUTO-PULL] Repositorio: $repoPath"
Write-Host "[AUTO-PULL] Intervalo: $($intervalSeconds/60) minutos"

while ($true) {
    try {
        Push-Location $repoPath

        # Verificar si hay actualizaciones disponibles
        git fetch origin

        # Obtener commits locales y remotos
        $localCommit = git rev-parse HEAD
        $remoteCommit = git rev-parse origin/master 2>$null

        if ($localCommit -ne $remoteCommit) {
            # Verificar si el remoto tiene cambios nuevos (no solo si estamos desfasados por commits locales sin push)
            $behindCount = git rev-list --left-right --count HEAD...origin/master | ForEach-Object { ($_ -split '\s+')[1] }

            if ([int]$behindCount -gt 0) {
                Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Cambios disponibles en el remoto. Ejecutando pull..."
                git pull
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Pull exitoso."
                } else {
                    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] ERROR: Pull fallo." -ForegroundColor Red
                }
            }
        }

        Pop-Location
    } catch {
        Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] ERROR: $_" -ForegroundColor Red
        Pop-Location
    }

    Start-Sleep -Seconds $intervalSeconds
}
